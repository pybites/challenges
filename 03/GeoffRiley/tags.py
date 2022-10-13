import re
from collections import Counter
from difflib import SequenceMatcher
from itertools import permutations

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87

TAG_REGEX = re.compile(r'<category>([^<]+?)</category>')


def get_tags() -> list:
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open(RSS_FEED) as f:
        return [t.replace('-', ' ').lower() for t in TAG_REGEX.findall(f.read())]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return list(Counter(tags).most_common(TOP_NUMBER))


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    return ((t, s) if t < s else (s, t) for t, s in permutations(set(tags), 2) if
            t[0] == s[0] and SequenceMatcher(None, t, s).ratio() > SIMILAR)


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
