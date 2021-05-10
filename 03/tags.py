from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

REPLACE_CHARS = str.maketrans('-', ' ')
IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace (REPLACE_CHARS)"""
    with open(RSS_FEED) as f:
        tags = TAG_HTML.findall(f.read().lower())
    return [tag.translate(REPLACE_CHARS) for tag in tags]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    for pair in product(tags, tags):
        # performance enhancements 1.992s -> 0.144s
        if pair[0][0] != pair[1][0]:
            continue
        pair = tuple(sorted(pair))  # set needs hashable type
        similarity = SequenceMatcher(None, *pair).ratio()
        if SIMILAR < similarity < IDENTICAL:
            yield pair


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
