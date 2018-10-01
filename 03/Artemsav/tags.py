from collections import Counter
from difflib import SequenceMatcher
from itertools import combinations
import re
import xml.etree.ElementTree as etree
import difflib

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    tree = etree.parse(RSS_FEED)
    root = tree.getroot()
    all_tags = [node.text for node in root.findall('.//category')]
    return all_tags


def get_top_tags(tags):
    return Counter(get_tags()).most_common(TOP_NUMBER)


def get_similarities(tags):
    tags = set(get_tags())
    need_merge = []
    for strings in combinations(tags, 2):
        if difflib.SequenceMatcher(lambda x: x not in '-', *strings).ratio() > SIMILAR:
            need_merge.append(strings)
    return need_merge


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