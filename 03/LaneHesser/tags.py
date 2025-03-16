import collections
import itertools
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher


TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def main():
    tags = get_tags()
    top_tags = get_top_tags(tags)

    print(top_tags)
    print('* Top {} tags:'.format(TOP_NUMBER))

    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))

    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')

    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""

    tree = ET.parse(source=RSS_FEED)
    root = tree.getroot()

    return [
        child.text.replace('-', ' ').lower()
        for child in root.iter('category')
    ]

    # with open(RSS_FEED) as f:
    #     f = f.read().replace('-', ' ')
    #     return TAG_HTML.findall(f)


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return collections.Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    possibilities = set(itertools.product(tags, repeat=2))
    similarities = set()

    for pair in possibilities:
        if pair[0] == pair[1] or ((pair[1], pair[0]) in similarities):
            continue

        ratio = SequenceMatcher(a=pair[0], b=pair[1]).ratio()
        if ratio > SIMILAR:
            similarities.add(pair)

    return similarities


if __name__ == "__main__":
    main()
