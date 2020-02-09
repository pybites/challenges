from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAGS_HTML = re.compile(r"<category>([^<]+)</category>")


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    file = open(RSS_FEED, "r").read()
    tags = re.findall(TAGS_HTML, file)
    return tags


def get_top_tags(tags):
    c = Counter(tags)
    return c.most_common(10)


def get_similarities(tags):
    similars = []
    for i in range(0, len(tags) - 1):
        for j in range(i + 1, len(tags)):
            if IDENTICAL > SequenceMatcher(None,tags[i], tags[j]).ratio() > SIMILAR:
                similars.append([tags[i],tags[j]])
    return similars
    
print(SequenceMatcher('aabb', "aab").ratio())

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
