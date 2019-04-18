from collections import Counter
from difflib import SequenceMatcher
from itertools import product,combinations
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
TRANS_TABLE = str.maketrans('-',' ')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED,mode='r') as f:
        tags = re.findall(TAG_HTML,f.read().lower())
    return [tag.translate(TRANS_TABLE) for tag in tags]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    
    # Build all tags
    result = list()
    for t in combinations(tags,2):
        t = tuple(sorted(t))
        s = SequenceMatcher(None,a=t[0],b=t[1])
        if SIMILAR < s.ratio() < IDENTICAL:
            result.append(t)
    return result


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    # _similar_tags = get_similarities(tags)
    # print(_similar_tags)
    similar_tags = dict(get_similarities(tags))
    #print(similar_tags)
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
