from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re
import string

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    tags = None
    with open(RSS_FEED) as fp:
        for line in fp:
            tags = TAG_HTML.findall(line.lower())
    return [tag.translate(string.maketrans('-', ' ')) for tag in tags if tag]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    if tags:
        return Counter(tags).most_common(10)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    tag_pairs = product(tags, tags)
    all_tag_pairs = [sorted(tag) for tag in list(tag_pairs)]
    for tag_pair in all_tag_pairs:
        if tag_pair[0] != tag_pair[1]:
            match_ratio = SequenceMatcher(a=tag_pair[0], b=tag_pair[1]).ratio()
            if match_ratio > SIMILAR and match_ratio < IDENTICAL:
                yield tag_pair



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
