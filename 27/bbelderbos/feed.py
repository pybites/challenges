from collections import namedtuple
from datetime import datetime, timedelta
import re
from time import mktime

import feedparser

DEFAULT_FEED = 'https://pybit.es/feeds/all.rss.xml'
DEFAULT_LOOK_DAYS_BACK = datetime.now() - timedelta(days=1)

Post = namedtuple('Post', 'title url summary')


def get_latest_feed_entry(url_match, feed=DEFAULT_FEED,
                          go_back_dt=DEFAULT_LOOK_DAYS_BACK):
    '''Returns most recent feed entry matching url_match regex'''
    for entry in feedparser.parse(feed)['entries']:
        title = 'PyBites ' + entry['title']

        url = entry['link']

        summary_html = entry.get('summary', 'No summary available')
        summary_text = re.sub('<[^<]+?>', '', summary_html)

        published = entry['published_parsed']
        dt = datetime.fromtimestamp(mktime(published))

        if dt < go_back_dt:
            continue

        if not url_match.match(url):
            continue

        return Post(title=title,
                    url=url,
                    summary=summary_text)

    return None
