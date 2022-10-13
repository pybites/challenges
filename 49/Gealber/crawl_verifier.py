import concurrent.futures
import threading
from urllib.request import Request, urlopen, URLError
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import sqlite3
import feedparser
from datetime import date
import queue
import time
import logging

conn = sqlite3.connect('urls.db')
c = conn.cursor()
c.execute('CREATE TABLE Urls (urls VARCHAR)')
links_to_crawl = queue.Queue(maxsize=10)


class Crawl:
    base_url = ''
    error_links = set()
    crawled_links = set()
    headers = {}

    def __init__(self, headers, base_url):
        Crawl.headers = headers
        Crawl.base_url = base_url

    @staticmethod
    def crawl(thread_name, url, links_to_crawl):
        """
        This method connect to the given url and put it in the corresponding set() or queue.
        If there's an error when parsing the url is added to error_links set.
        Otherwise extract the links of the page with BeautifulSoup and pass this links to the method
        enqueue_links() to well ....be enqueued.
        :param thread_name: Current thread name
        :param url: url to connect
        :param links_to_crawl: queue with the links extracted.
        """
        try:
            if urlparse(url).netloc == 'planetpython.org' and url not in Crawl.error_links:
                req = Request(url, headers=Crawl.headers)
                response = urlopen(req)
                Crawl.crawled_links.add(url)
                logging.info(f"{thread_name}")
                if response.getcode() == '200':
                    logging.info("Connected successfully")
                    d = feedparser.parse(f"{url}/rss20.xml")
                    date_updated = d.feed.parse.published_parsed
                    date_updated = date(date_updated[0], date_updated[1], date_updated[2])
                    difference = date.today() - date_updated
                    if difference.days > 365:
                        print(f"Feed {url}/rss20.xml is Out of date")
                        logging.warning(f"Feed {url}/rss20.xml is Out of date")
                        Crawl.error_links.add(url)
                print(f"Url {url} Crawled with status: {response.getcode()}")
                print(f" {len(Crawl.crawled_links)} Crawled in total")
                logging.info(f"Url {url} Crawled with status: {response.getcode()}")
                logging.info(f" {len(Crawl.crawled_links)} Crawled in total")
                soup = BeautifulSoup(str(response.read(), 'utf-8'), 'lxml')
                Crawl.enqueue_links(soup.find_all('a'), links_to_crawl)
        except URLError as err:
            print(f"Url {url} threw this error {err.reason}")
            logging.error(f"Url {url} threw this error {err.reason}")
            Crawl.error_links.add(url)

    @staticmethod
    def enqueue_links(links, links_to_crawl):
        """
        Enqueue the links if not in the set() crawled_links and not in links_to_crawl.
        :param links:
        :param links_to_crawl: queue that contain the links to be crawled.
        """
        for link in links:
            if urljoin(Crawl.base_url, link.get('href')) not in Crawl.crawled_links:
                if urljoin(Crawl.base_url, link.get('href')) not in links_to_crawl:
                    links_to_crawl.put(link)
                    logging.info(f"Link {link} just added to the queue links_to_crawl")


class Inspection:
    def __init__(self, headers):
        self.headers = headers

    @staticmethod
    def read_config(config_file) -> list:
        """
        Extract urls from config.ini.
        :param config_file:
        """
        urls = []
        with open(config_file, 'w') as file:
            for line in file.readlines():
                urls.append(line)
        return urls

    def links_start_page(self, timeout) -> list:
        """
        Extract links to examine from the start page.
        :param timeout: a timeout to connect.
        :return links: a list with the urls of the home page.
        """
        req = Request('https://planetpython.org/', headers=self.headers)
        with urlopen(req, timeout=timeout) as resp:
            page = str(resp.read(), 'utf-8')

        soup = BeautifulSoup(page, 'lxml')
        children = soup.select("ul.level-one > li")
        extract_sections = []
        for child in children:
            extract_sections.append(child)
        links = []
        for i in range(1, 4):
            soup_link = extract_sections[i]
            items = soup_link.select("li > a")
            for item in items:
                s = str(item)
                start_link = s.find('href="')
                end_link = s.find('">', start_link + 1)
                link = s[start_link + 6: end_link]
                links.append(link)
        return links


def run(url):
    """
    Well...........
    :param url:
    """
    try:
        Crawl.crawl(threading.current_thread(), url, links_to_crawl)
        logging.info(f"Starting to crawl {url} in thread {threading.current_thread()}")
        print("Wasiting 5 secs...")
        logging.info("Waiting 5 secs....")
        time.sleep(5)
    except:
        print(f"Exception thrown with {url}")
        logging.exception(f"Exception thrown with {url}")
    links_to_crawl.task_done()


def main():
    logging.basicConfig(filename='crawler.log', format='%(levelname)s:%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logging.info('Started...')
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 '
                      '(KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
        'Accept_Language': 'en-US, en, q=0.8',
        'Accept': 'text/html,application/xhtml+xml,application/xml'
    }
    url = 'http://planetpython.org'
    Crawl(headers=headers, base_url=url)
    links_to_crawl.put(url)
    inspection = Inspection(headers=headers)
    urls_to_inspection = [url for url in inspection.read_config('config.ini')]
    urls_to_inspection.append(inspection.links_start_page(timeout=60))
    for link in urls_to_inspection:
        links_to_crawl.put(link)
    while not links_to_crawl.empty():
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            url = links_to_crawl.get()
            logging.info(f"Url {url} just pull out of the queue links_to_crawl")
            futures = []
            if url is not None:
                future = executor.submit(run, url)
                futures.append(future)

            for future in concurrent.futures.as_completed(futures):
                try:
                    if future.result() is not None:
                        c.execute('INSERT INTO Urls (urls,) VALUE (?,)', (future.result(),))
                        logging.info(f"{future.result} added to the database")
                except:
                    print(future.exception())
                    logging.exception(f"The following exception threw: {future.exception()}")

    logging.info('...Finished')


conn.commit()
conn.close()
print(f"Total links Crawled {len(Crawl.crawled_links)}")
print(f"Total errors {len(Crawl.error_links)}")

if __name__ == '__main__':
    main()
