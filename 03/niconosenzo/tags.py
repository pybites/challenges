from xml.etree import ElementTree
from collections import Counter
import difflib
import operator

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tag_list = []
    with open('rss.xml','rt') as f:
        tree = ElementTree.parse(f)

    # list all the category tags and append them to tag_list
    for tag in tree.iter('category'):
        tag_list.append(tag.text)

    # now we go through the tag_list and remove the dashes 
    for i in range(len(tag_list)):
        if tag_list[i].count('-') != 0:
            tag_list[i] = tag_list[i].replace('-',' ')

    return tag_list


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    # Create a dictonary with tag:ocurrence
    tag_dict = Counter(tags)
    # lets sort the dictonary
    sorted_tags = sorted(tag_dict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_tags[0:TOP_NUMBER]


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    # create a list of unique tags
    unique_tags_dict = Counter(tags)
    unique_tags_list = []
    for i in unique_tags_dict.items():
        unique_tags_list.append(i[0])
    
    similarities = []
    for i in unique_tags_list:
        if not i.endswith('s'):
            similarities.append(difflib.get_close_matches(i, unique_tags_list, n=2, cutoff=0.87))

    # check which have similarities and create a new list with those that have
    onlysim = []
    for i in range(len(similarities)):
        if len(similarities[i]) == 2:
            onlysim.append(similarities[i])

    # remove duplicates
    for x,y in onlysim:
        if [y,x] in onlysim:
            onlysim.remove([y,x])

    return onlysim


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
