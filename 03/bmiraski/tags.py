"""Process tag items on PyBites."""

from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.

    Replace dash with whitespace.
    Hint: use TAG_HTML.findall
    """
    with open(RSS_FEED) as rss:
        tags = TAG_HTML.findall(rss.read())
    clean_tags = []
    for tag in tags:
        if '-' in tag:
            new_tag = ""
            for c in tag:
                if c != '-':
                    new_tag += c
                else:
                    new_tag += ' '
            tag = new_tag
        clean_tags.append(tag.lower())
    return clean_tags


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tagsself.

    Hint: use most_common method of Counter (already imported)
    """
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR.

    Hint 1: compare each tag, use product from itertools (already imported).

    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    """
    unique_tags = []
    for tag in tags:
        if tag not in unique_tags:
            unique_tags.append(tag)
    compare_group = product(unique_tags, repeat=2)
    similar_tags = []
    for pair in compare_group:
        if pair[0][0] != pair[1][0]:
            continue
        else:
            sim = SequenceMatcher(None, pair[0], pair[1])
            if sim.ratio() >= SIMILAR and sim.ratio() != IDENTICAL:
                similar_tags.append(pair)
    us_tags = []
    for pair in similar_tags:
        if (pair[1], pair[0]) not in us_tags and pair[0] < pair[1]:
            us_tags.append(pair)
    return us_tags


if __name__ == "__main__":
    tags = get_tags()
    print(len(tags))
    print(set(tags))
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
