"""
tags
Created January 31, 2022 by Jennifer Baughman

Description: CodeChallenge 03: Given our RSS feed what tags does PyBites
mostly use and which tags should be merged (based on similarity)?
"""

import xml.etree.ElementTree as ETree
from collections import Counter
from pprint import pprint
from difflib import get_close_matches

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags(feed=RSS_FEED):
    """Returns a list of tags from the RSS feed passed in.
    
    Args:
        feed: XML document path. Defaults to constant.

    Returns: list of strings

    """
    tree = ETree.parse(feed)
    root = tree.getroot()
    return [t.text for t in root.iter('category')]


def get_top_tags(tags, top_number=TOP_NUMBER):
    """Get the most common tags in the list of tags
    
    Args:
        tags: list of tags
        top_number: number of most common tags returned

    Returns: list of tuples containing the tag and count

    """
    tag_count = Counter(tags)
    return tag_count.most_common(10)


def _cleanup_tags(tags):
    t = set(tags)
    return sorted(list(t))


def get_similarities(tags, similar=SIMILAR):
    tags = _cleanup_tags(tags)
    similar_tags = {}
    for tag in tags:
        match = get_close_matches(tag, tags, cutoff=similar)
        if len(match) == 1:
            continue
        match.sort()
        if match[1] != similar_tags.get(tag):
            similar_tags[match[0]] = match[1]
    return similar_tags


def main():
    t = get_tags()
    print("* Top 10 tags:")
    for top in get_top_tags(t):
        print(f"{top[0]:20}{top[1]}")
    print("\n* Similar tags:")
    for k, v in get_similarities(t).items():
        print(f"{k:20}{v}")



if __name__ == "__main__":
    main()
