import nltk
import itertools
import xml.etree.ElementTree as etree
from collections import Counter, OrderedDict
from difflib import SequenceMatcher

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""

    tree = etree.parse(RSS_FEED)
    root = tree.getroot()
    tags = [node.text for node in root.findall('.//category')]
    return [tag.replace('-', ' ').lower() for tag in tags]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""

    for pair in itertools.combinations(set(tags), 2):
        if pair[0][0] != pair[1][0]:
            continue

        if SequenceMatcher(None, *pair).ratio() > SIMILAR:
            yield tuple(sorted(pair))


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    # print('* Top {} tags:'.format(TOP_NUMBER))
    # for tag, count in top_tags:
    #     print('{:<20} {}'.format(tag, count))
    # similar_tags = dict(get_similarities(tags))
    # print()
    # print('* Similar tags:')
    # for singular, plural in similar_tags.items():
        # print('{:<20} {}'.format(singular, plural))
    # get_tags()
