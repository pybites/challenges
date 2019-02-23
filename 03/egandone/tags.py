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
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED) as rss_feed:
        tags = [tag.replace('-', ' ').lower() for tag in TAG_HTML.findall(rss_feed.read())]
    return tags

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    counter = Counter(tags)
    return counter.most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    similiar_tags = [] 
    tag_set = set(tags)
    reduced_set = tag_set.copy()   
    for tag1 in tag_set:
        reduced_set.remove(tag1)
        for tag2 in reduced_set:
            match_ratio = SequenceMatcher(a = tag1, b = tag2).ratio()
            if match_ratio > SIMILAR:
                if len(tag2) < len(tag1):
                    s = (tag2, tag1)
                else:
                    s = (tag1, tag2)
                similiar_tags.append(s)
    return similiar_tags

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
