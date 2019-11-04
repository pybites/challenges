from collections import Counter
from difflib import SequenceMatcher
from itertools import combinations

import re


TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
CATEGORY_PATTERN = r"(?<=<category>).+?(?=</category>)"


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    pattern = re.compile(CATEGORY_PATTERN)
    with open(RSS_FEED, 'r') as f:
        rss = f.read()
    return [tag.replace("-", " ") for tag in pattern.findall(rss.lower())]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    return [sorted([a, b]) for (a, b) in combinations(set(tags), 2)
            if SIMILAR <= SequenceMatcher(None, a, b).ratio()]


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
