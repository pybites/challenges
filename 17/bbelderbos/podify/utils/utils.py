import logging
import os
import re
import sys
from urllib.request import urlretrieve


def get_db_name(feed):
    return re.sub(r'https?://(\S+?)\..*', r'\1', feed)


def get_test_feed():
    if not os.path.isfile(RSS):
        logging.debug('RSS file not found, downloading it')
        try:
            urlretrieve(FEED, RSS)
        except Exception as exc:
            logging.error('Cannot get rss, error: {}'.format(exc))
            sys.exit(1)

    with open(RSS) as f:
        return f.read()
