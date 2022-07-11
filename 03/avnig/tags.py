TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
import re
from collections import Counter
from difflib import SequenceMatcher
from itertools import product

tags_re_tags_html = re.compile('\s+<li><a href="http:\/\/.*?\/tag\/.*?\.html">(.*?)<\/a>')
tags_re_rss = re.compile(r'<category>(.*?)<\/category>')


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""

    with open('rss.xml') as xml_file:
        return [tags_re_rss.findall(line.lower().replace('-', ' ')) for line in xml_file][1]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    result = {}
    for x, y in product(tags, tags):
        if x == y or x[0] != y[0]:
            continue
        else:
            if SIMILAR <= SequenceMatcher(None, x, y).ratio() and y not in result:
                result[x] = y
    return result


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
