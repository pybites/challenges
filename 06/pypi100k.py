from datetime import datetime
import logging
import os
from time import mktime
import sys

import bs4
import feedparser
import requests

NUM_PACKS_TO_REACH = 100000
NOW = datetime.utcnow()
PYPI = 'https://pypi.python.org/pypi'
PYPI_OUT = 'pypi.html'
RSS = 'https://pypi.python.org/pypi?%3Aaction=packages_rss'
RSS_OUT = 'feed.rss'
LOGFILE = 'pypi.log'
REFRESH = True


logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)  # ignore imported module's debug messages

fileHandler = logging.FileHandler(LOGFILE)
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)


def get_feed(rss, fname):
    r = requests.get(rss)
    if r.status_code != 200:
        sys.exit('cannot get feed')
    with open(fname, 'w') as f:
        f.write(r.text)


def get_current_num_packages():
    if not os.path.isfile(PYPI_OUT) or REFRESH:
        get_feed(PYPI, PYPI_OUT)
    with open(PYPI_OUT) as f:
        soup = bs4.BeautifulSoup(f.read(), "lxml")
        div = soup.find('div', {"class":"section"})
        try:
            return int(div.find('strong').text)
        except:
            sys.exit('Cannot scrape number of package')


def main():
    if not os.path.isfile(RSS_OUT) or REFRESH:
        get_feed(RSS, RSS_OUT)

    num_packages = get_current_num_packages()
    logging.info('Now there are {} packages'.format(num_packages))

    with open(RSS_OUT) as f:
        html = f.read()
        items = feedparser.parse(html)
        dates = [datetime.fromtimestamp(mktime(item['published_parsed'])) for item in items['entries']]
        maxdate = max(dates) 
        mindate = min(dates)
        logging.info('RSS new packages: min date = {} / max date = {}'.format(mindate, maxdate))
        avg_addtime = (maxdate - mindate) / len(dates)
        logging.info('Avg time between additions: {}'.format(avg_addtime))
        packages_to_be_added = NUM_PACKS_TO_REACH - num_packages
        logging.info('Packages to be added: {}'.format(packages_to_be_added))
        time_till_reach = avg_addtime * packages_to_be_added
        logging.info('Time till reach = {}'.format(time_till_reach))
        endresult = NOW + time_till_reach
        logging.info('Result (NOW + time till reach): {}'.format(endresult))

if __name__ == "__main__":
    main()
