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
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    #print("get_tags method here")

    temp = []
    file = open(RSS_FEED, "r")
    for rss in file:
        #print("rss:", rss)
        temp = re.findall(TAG_HTML,rss)
        #print("temp:", temp)

    #print("temp size:", len(temp))

    new_temp = []
    for i in temp:
        replace_dash = i.replace("-", " ")
        replace_dash = replace_dash.lower()
        new_temp.append(replace_dash)

    #print("New Temp:", new_temp)
    #print("Size of New Temp:", len(new_temp))
    #print("Updated set New Temp size:", len(set(new_temp)))

    file.close()

    return(new_temp)

    pass


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""

    #print("get_top_tags method call here")
    #print("tags:", tags)

    tag_list = Counter(tags).most_common(TOP_NUMBER)

    #print("tag_list:", tag_list)

    return tag_list
    pass


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    print("get_similarities method call here")

    #print("tags:", tags)
    ret_list = []
    for x in tags:
        for y in tags:
            temp = SequenceMatcher(None, x, y)
            d = temp.ratio()
            if d > SIMILAR:
                if d < IDENTICAL:
                    temp = x,y
                    temp = sorted(temp)
                    ret_list.append(temp)

    print("ret_list:", ret_list)

    return ret_list
    pass


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
