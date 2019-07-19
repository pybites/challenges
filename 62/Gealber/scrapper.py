import urllib.request
from urllib.request import urlsplit
import sys
import concurrent.futures
from bs4 import BeautifulSoup
import codecs
import gender_guesser.detector as gender

URLS_ES = [
    'https://2018.es.pycon.org/#schedule',
    'https://2017.es.pycon.org/es/schedule/',
    'http://2016.es.pycon.org/es/schedule/',
    'http://2015.es.pycon.org/es/schedule/',
    'http://2014.es.pycon.org/talks',
    'http://2013.es.pycon.org/#agenda',
]


class Scrapper:
    def __init__(self):
        pass

    @staticmethod
    def connect(url: str) -> tuple:
        """
        Connect to the given url and extract the html.\n
        :param url:
        """
        year = urlsplit(url).netloc.split('.')[0]
        try:
            headers = dict()
            headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 " \
                                    "(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                page = codecs.decode(response.read())
            return page, int(year)
        except urllib.request.URLError as e:
            print(f"The following error had raise while trying to connect to {url}\n")
            print(e)
            sys.exit()

    @staticmethod
    def scrapper_es(html, year: int) -> list:
        """
        Scrape th page given from connect(). Return the list with all
        the speakers in a list.
        :param html:
        :param year:
        :return speakers: List of speakers' full name.
        """
        soup = BeautifulSoup(html, "lxml")
        speakers = []
        years_common = [2015, 2016, 2017]
        if year == 2018:
            items = soup.select("div.schedule__talk--speaker > div > p")
            for i, link in enumerate(items):
                s = str(link)
                start_content = s.find('<p>')
                end_content = s.find('</p>', start_content + 1)
                speaker = str(s[start_content + 3: end_content]).replace(' y', ',').split(', ')
                speakers = speakers + speaker
            return speakers

        elif year in years_common:
            items = soup.select("div.slot-inner > p > strong")
            for i, link in enumerate(items):
                s = str(link)
                start_content = s.find('<strong>')
                end_content = s.find('</strong>', start_content + 1)
                speaker = str(s[start_content + 8: end_content]).replace(' y', ',').split(', ')
                speakers = speakers + speaker
            return speakers
        elif year == 2014:
            items = soup.select("h1.text-center")
            for i, link in enumerate(items):
                s = str(link)
                start_content = s.find('ter">')
                end_content = s.find('</h1>', start_content + 1)
                speaker = str(s[start_content + 5: end_content]).replace(' y', ',').split(', ')
                speakers = speakers + speaker
            return speakers
        elif year == 2013:
            items = soup.select('li > div > a[target="_blank"]')
            for i, link in enumerate(items):
                s = str(link)
                start_content = s.find('">')
                end_content = s.find('</a>', start_content + 1)
                speaker = str(s[start_content + 2: end_content]).replace(' y', ',').split(', ')
                speakers = speakers + speaker
            return speakers

    def do_classify_in_threads(self) -> dict:
        """
        Open the the URLS and scrape the info related to the speakers.
        After that store the info in a dictionary to be classify by gender.
        Return a dictionary with the following form {'2016': [1, 0, 0, 1], '2018': [0, 1, 0]}
        where 1 represent a female and 0 a male.
        :return:
        """
        speakers_in_year_es = {}

        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            future_to_url = {executor.submit(self.connect, url): url for url in URLS_ES}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    page = future.result()[0]
                    year = future.result()[1]
                    speakers_in_year_es[str(year)] = self.scrapper_es(page, year)
                except Exception as exc:
                    print(f"{url} generated the following exception: \n{exc}")

        # With the next loops we get a dictionary
        # of this form {'2016': ['female', 'male', 'female']}
        # and then we replace 'female' by 1 and other cases by 0.
        d = gender.Detector()
        for year in speakers_in_year_es:
            for i, name in enumerate(speakers_in_year_es[year]):
                speakers_in_year_es[year][i] = 1 if d.get_gender(name.split()[0]) == 'female' else 0

        return speakers_in_year_es


def main():
    import matplotlib.pyplot as plt
    import numpy as np

    scrapper = Scrapper()
    data = scrapper.do_classify_in_threads()

    v = [2013, 2019, 0, 10]
    plt.axis(v)
    for year in data:
        height = np.array(data[year]).sum()
        plt.bar(int(year), height=height)


if __name__ == '__main__':
    main()
