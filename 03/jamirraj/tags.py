from collections import Counter
from difflib import SequenceMatcher
from itertools import product

import re
from xml.etree import ElementTree as ET

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED."""

    feed = ET.parse(RSS_FEED)
    tags = [tag.text.replace('-', ' ').lower() for tag in feed.findall('.//category')]

    return tags


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""

    top_tags = {letter: count for letter, count in Counter(tags).most_common(TOP_NUMBER)}
    return top_tags


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    tags_pairs = {}
    for tag in tags:
        for t in tags:
            if tag[0] == t[0] and tag != t and tag not in tags_pairs and t not in tags_pairs:
                seq = SequenceMatcher(None, tag, t)
                if seq.ratio() > SIMILAR:
                    if len(tag) < len(t):
                        tags_pairs[tag] = t
                    else:
                        tags_pairs[t] = tag
            else:
                continue

    return tags_pairs


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags.items():
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
