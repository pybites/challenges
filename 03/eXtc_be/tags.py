# tags.py - PyBites Blog Tag Analysis
# https://pybit.es/articles/codechallenge03/


import xml.etree.ElementTree as ET
from collections import Counter
import difflib

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tags = []

    tree = ET.parse(RSS_FEED)
    root = tree.getroot()

    for item in root[0].iter('item'):  # root[0] = channel
        for cat in item.iter('category'):
            tags.append(cat.text.replace('-', ' '))

    return tags


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    c = Counter(tags)
    return c.most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    matches = []
    for tag in sorted(set(tags)):
        hits = difflib.get_close_matches(tag, set(tags), 3, SIMILAR)
        for hit in hits:
            if hit != tag and hit not in [mm for m in matches for mm in m]:
                matches.append((tag, hit))

    return matches


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
