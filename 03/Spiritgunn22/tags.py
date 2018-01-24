import re
from collections import Counter
from difflib import SequenceMatcher
from itertools import combinations


TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
tag_locator = re.compile(r'<category>(\w+)</category>')


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open(RSS_FEED, 'r') as xml_data:
        result = tag_locator.findall(xml_data.read())
    return result


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    unique_tags = list(Counter(tags).keys())
    combos = list(combinations(unique_tags, 2))
    similar = {c[0]:c[1] for c in combos if SequenceMatcher(None, c[0], c[1]).ratio() >= SIMILAR}
    return similar



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
