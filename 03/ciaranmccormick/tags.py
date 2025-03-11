from itertools import combinations
from collections import Counter
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher as SM

TOP_NUMBER = 10
RSS_FEED = "rss.xml"
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tree = ET.parse(RSS_FEED)
    root = tree.getroot()

    return [cat.text.lower().replace("-", " ") for cat in root.iter("category")]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    counter = Counter(tags)
    return counter.most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    tags = sorted(tags)
    similars = [
        pair
        for pair in combinations(set(tags), 2)
        if SM(None, *pair).ratio() >= SIMILAR
    ]
    return similars


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print("* Top {} tags:".format(TOP_NUMBER))
    for tag, count in top_tags:
        print("{:<20} {}".format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print("* Similar tags:")
    for singular, plural in similar_tags.items():
        print("{:<20} {}".format(singular, plural))
