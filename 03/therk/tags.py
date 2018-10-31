#!/usr/bin/env python3

from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = '../rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED."""

    with open(RSS_FEED) as file:
        tags = TAG_HTML.findall(file.read())
    return [tag.replace('-', ' ').lower() for tag in tags]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    stags = []
    for tag1, tag2 in product(tags, tags):
        if tag1 == tag2 or tag1[0] != tag2[0]:
            continue
        if SequenceMatcher(None, tag1, tag2).ratio() > SIMILAR:
            stags.append(sorted((tag1, tag2)))
    return stags


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
