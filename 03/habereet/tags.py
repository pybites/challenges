from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')

def get_similarity():
    return float(input("Pick a decimal that you want to use as your similarity ratio: "))

def get_tags():
    with open(RSS_FEED) as RSS_File:
        regex = TAG_HTML
        for line in RSS_File:
            tags = regex.findall(line)
    for idx, tag in enumerate(tags):
        tags[idx]= tag.replace("-"," ")
        tags[idx] = tags[idx].lower()
    return tags


def get_top_tags(tags):
    c = Counter()
    for tag in tags:
        c.update({tag: 1})
    return c.most_common(TOP_NUMBER)


def get_similarities(tags):
    for word_pair in product(tags, tags):
        if word_pair[0][0] == word_pair[1][0]:
            word_pair = tuple(sorted(word_pair))  # set needs hashable type
            similarity = SequenceMatcher(None, *word_pair).ratio()
            if SIMILAR < similarity < IDENTICAL:
                yield word_pair


if __name__ == "__main__":
    #get_user_similarity = get_similarity()
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(list(tags)))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
