import re
from collections import Counter
from difflib import SequenceMatcher
from itertools import product

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAGS = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open('rss.xml', 'r') as fp:
        lines = fp.read()
    return [tag.replace('-', ' ') for tag in TAGS.findall(lines)]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(10)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    similar_tags = []
    for first, second in product(tags, tags):
        if first == second or first[0] != second[0]:
            continue
        if SequenceMatcher(None, first, second).ratio() >= SIMILAR:
            similar_tags.append(sorted((first, second)))
    return similar_tags


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    get_similarities(tags)
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
