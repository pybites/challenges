from collections import Counter
from difflib import SequenceMatcher
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')

def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace and make all tags lowercase.
    """
    with open(RSS_FEED) as rss_feed:
        tags = [tag.replace('-', ' ').lower() for tag in TAG_HTML.findall(rss_feed.read())]
    return tags

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    """
    counter = Counter(tags)
    return counter.most_common(TOP_NUMBER)

def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
   """
    similiar_tags = [] 
    # Use a set to get all the unique tags
    tag_set = set(tags)
    # Copy of the original set of tags that is reduced by the current
    # tag on each iteration.  Since we only need to consider each 
    # tag combination once 
    reduced_set = tag_set.copy()   
    for tag1 in tag_set:
        reduced_set.remove(tag1)
        # Compare the current tag with only those to which
        # it hasn't already been compared.
        for tag2 in reduced_set:
            match_ratio = SequenceMatcher(a = tag1, b = tag2).ratio()
            if match_ratio > SIMILAR:
                # Need to sort the tags so the shorter one is first
                # ... probably not really necessary but it is required
                #     to get the tests to pass ...
                similiar_tags.append(sorted([tag1, tag2]))
    return similiar_tags

if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print(f'* Top {TOP_NUMBER} tags:')
    for tag, count in top_tags:
        print(f'{tag:<20} {count}')
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print(f'{singular:<20} {plural}')
