
import copy
from collections import Counter
from difflib import SequenceMatcher
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import feedparser

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    tags = list()
    feed = feedparser.parse(RSS_FEED)
    for _item in feed.entries:
        for _tags in _item.tags:
            print(_tags['term'])
            tags.append(_tags['term'].replace('-', ' '))
    return tags


def get_tags_v2():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tags = list()
    tree = ET.ElementTree(file=RSS_FEED)
    for node in tree.iter():
        if node.tag == 'category':
            tags.append(node.text.replace('-', ' '))
    return tags


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    c = Counter(tags)
    return c.most_common(TOP_NUMBER)


def get_top_tags_v2(tags):

    def filter_out(_tags, tag):
        filter_tags = list(filter(lambda x: x != tag, _tags))
        return filter_tags

    def tags_max(_tags):
        c = dict()
        for item in _tags:
            c[item] = c.get(item, 0) + 1
        return max(c, key=c.get)

    def tag_count(_tags, tag):
        count = 0
        for elt in _tags:
            if elt == tag:
                count += 1
        return count

    top_tags = list()
    tags_copy = copy.deepcopy(tags)
    top = '-1'
    for n in range(0, TOP_NUMBER):
        top = tags_max(tags)
        tags = filter_out(tags, top)
        top_tags.append((top, tag_count(tags_copy, top)))

    return top_tags


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""

    def already_in(seq, val):
        for s, p in seq:
            if val in [s, p]:
                return True
        return False

    unique_tags = sorted(set(tags))
    similarities = list()
    for tag in unique_tags:
        for _tag in unique_tags:
            if _tag != tag:
                ratio = SequenceMatcher(None, tag, _tag).ratio()
                if ratio > 0.87:
                    if not already_in(similarities, tag):
                        similarities.append((tag, _tag))
    return similarities


if __name__ == "__main__":
    tags = get_tags()
    print(tags)
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
