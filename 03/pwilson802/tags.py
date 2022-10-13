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
    """Find all tags (TAG_HTML) in RSS_FEED."""
    tags = []
    with open(RSS_FEED) as file:
        for line in file.readlines():
            for tag in TAG_HTML.findall(line):
                tags.append(tag.replace('-', ' ').lower())
    return tags

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    tag_count = Counter(tags)
    return tag_count.most_common(10)



def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    similar_tags = []
    s_tags = set(tags)
    for tag in s_tags:
        for compare_tag in s_tags:
            if tag == compare_tag:
                continue
            else:
                compare = SequenceMatcher(None, tag, compare_tag).ratio()
                if compare > SIMILAR:
                    if (compare_tag, tag) not in similar_tags:
                        if len(tag) < len(compare_tag):
                            similar_tags.append((tag, compare_tag))
                        else:
                            similar_tags.append((compare_tag, tag))
    return similar_tags
                
            

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
