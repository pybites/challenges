"""
tags
Created January 31, 2022 by Jennifer Baughman

Description: CodeChallenge 03: Given our RSS feed what tags does PyBites
mostly use and which tags should be merged (based on similarity)?
"""

import xml.etree.ElementTree as ETree
from collections import Counter

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
    tag_count = Counter(tags)
    return tag_count.most_common(10)


def get_similarities(similar=SIMILAR):
    pass


def main():
    t = get_tags()
    print(get_top_tags(t))



if __name__ == "__main__":
    main()
