from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    return TAG_HTML.findall(open(RSS_FEED).read())


def get_top_tags(tags):
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    result = {}
    for x, y in product(tags, tags):
        if x == y or x[0] != y[0]:
            continue
        else:
            if SequenceMatcher(None, x, y).ratio() >= SIMILAR and y not in result:
                result[x] = y
    return result


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
