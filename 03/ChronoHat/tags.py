TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87

import xml.etree.ElementTree as e_tree
from operator import itemgetter
from difflib import get_close_matches

def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    feed = e_tree.parse(RSS_FEED)
    return [tag.text.replace('-',' ').lower() for tag in feed.findall('.//category')]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return sorted(list({(x, tags.count(x)) for x in tags}), key = itemgetter(1), reverse = True)[:TOP_NUMBER]


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    tag_set = set(tags)
    tag_pairs = []
    for word in tag_set:
        for match in get_close_matches(word, tag_set, len(tag_set), SIMILAR):
            if [match, word] not in tag_pairs and word != match:
                tag_pairs.append([word, match])
    return tag_pairs


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
