TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87

from bs4 import BeautifulSoup
def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open(RSS_FEED) as f: 
        soup = BeautifulSoup(f, 'html.parser')
        tags=[tags.text for tags in soup.find_all('category')]
    return sorted(tags)

import collections
def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    counter=collections.Counter(tags)
    return counter.most_common(TOP_NUMBER)

from difflib import SequenceMatcher
import itertools
def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    similar_pairs=[]
    for s1, s2 in itertools.combinations(sorted(list(set(tags))), 2):
        ratio=SequenceMatcher(a=s1,b=s2).ratio()
        if SIMILAR<ratio:
            similar_pairs.append((s1,s2))
    return similar_pairs


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
