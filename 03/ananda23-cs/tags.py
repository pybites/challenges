from collections import Counter
from difflib import SequenceMatcher
from itertools import product
from xml.etree import cElementTree as ET

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tree = ET.parse(RSS_FEED)
    root = tree.getroot()
    categories = [cat.text.replace('-', ' ').lower() for cat in root.findall('./channel/item/category')]
    return categories


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    for tag1, tag2 in product(tags, tags):
        if tag1 == tag2 or tag1[0] != tag2[0]:
            continue
        else:
            sm = SequenceMatcher(None, tag1, tag2)
            if sm.ratio() > SIMILAR:
                yield tuple(sorted([tag1, tag2]))

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
