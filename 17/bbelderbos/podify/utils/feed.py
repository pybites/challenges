from collections import namedtuple
from datetime import datetime
import time

import feedparser

Episode = namedtuple('Episode', 'id title link published')


def parse_feed(feed):
    output = feedparser.parse(feed)

    d = {}
    for e in output['entries']:
        id = e.get('id')
        title = e.get('title')
        link = e.get('link')
        published = _to_dt(e.get('published_parsed'))
        d[id] = Episode(id, title, link, published)
    return d


def _to_dt(struct):
    return datetime.fromtimestamp(time.mktime(struct))
