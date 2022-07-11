import xml.etree.ElementTree as ET
from collections import Counter
from difflib import SequenceMatcher

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tag_list = []
    tree = ET.parse(RSS_FEED)
    root = tree.getroot()
    for item in root.findall("channel/item/category"):
        tag_list.append(item.text.replace("-", " ").lower())
    return tag_list


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    tag_counter = Counter(tags)
    return tag_counter.most_common(10)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    similar_tag_set = set()
    for idx, tag1 in enumerate(tags, start=1):
        for tag2 in tags[idx:]:
            if SIMILAR < SequenceMatcher(None, tag1, tag2).ratio() < 1:
                if len(tag1) < len(tag2):
                    similar_tag_set.add((tag1, tag2))
                else:
                    similar_tag_set.add((tag2, tag1))
    return similar_tag_set


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
