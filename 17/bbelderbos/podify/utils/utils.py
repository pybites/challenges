import logging
import os
import re
import sys
from urllib.request import urlretrieve

TEST_FEED = 'http://noahkagan.libsyn.com/rss'
RSS = os.path.basename(TEST_FEED)

def get_db_name(feed):
    return re.sub(r'https?://(\S+?)\..*', r'\1', feed)


def get_test_feed(rss=RSS, feed=TEST_FEED):
    if not os.path.isfile(rss):
        logging.debug('RSS file not found, downloading it')
        try:
            urlretrieve(feed, rss)
        except Exception as exc:
            logging.error('Cannot get rss, error: {}'.format(exc))
            sys.exit(1)

    with open(rss) as f:
        return f.read()


if __name__ == '__main__':
    assert get_db_name(TEST_FEED) == 'noahkagan'
    get_test_feed()
    assert os.path.isfile(RSS)
