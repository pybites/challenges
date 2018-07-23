import feedparser
from itertools import count
from collections import Counter
from difflib import SequenceMatcher
from itertools import product

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    d = feedparser.parse(RSS_FEED)
    tag_list = []

    # parse the feed using feedparser
    for i,entry in enumerate(d.entries):
        for j,tag in enumerate(d.entries[i].tags):
            tag_list.append(d.entries[i].tags[j].term)
    
    # Some cleaning up, replace hyphens with spaces
    clean_tag_list = []
    for tag in tag_list:
        clean_tag_list.append(tag.replace('-',' ')) 
    
    return clean_tag_list


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    
    # Cartesian (cross) product
    cross_product = list(product(tags, repeat=2))
    similar_tags = {el:0 for el in cross_product}

    for key in similar_tags.keys():
        seq = SequenceMatcher(None, key[0],key[1])
        similarity = seq.ratio()
        similar_tags[key] = similarity

    most_similar = dict((k,v) for k,v in similar_tags.items() if v >= 0.87 and v<1)

    # remove redundant tuples like (a,b) and (b,a)
    unique_most_similar = {}
    for k,v in most_similar.items():
        if not((k[1],k[0]) in unique_most_similar.keys()):
            unique_most_similar[k] = v

    return unique_most_similar.keys()


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))

