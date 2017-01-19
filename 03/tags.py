from collections import Counter
import re

from test import parse_tags_html

FROM_TO = str.maketrans('-', ' ')
MSG = '{}, {} not in test set'
NUM_ITEMS = 10
RSS_FEED = 'all.rss.xml'
TAG = re.compile(r'<category>([^<]+)</category>')


def _normalize(words):
    """Make words lowercase and replace characters"""
    return [w.translate(FROM_TO) for w in words]


def _read_rss():
    """Reads the RSS feed in"""
    with open(RSS_FEED) as f:
        return f.read().lower()


def count_tags():
    """Count the number of tags in our RSS feed"""
    xml = _read_rss()
    tags = TAG.findall(xml)
    tags_normalized = _normalize(tags)
    counter = Counter(tags_normalized)
    return(counter.most_common(NUM_ITEMS))


if __name__ == "__main__":
    tests = list(parse_tags_html())
    counts = count_tags()
    for tag, count in counts:
        assert (tag, count) in tests, MSG.format(tag, count)
        print('{:<20} {}'.format(tag,count))
