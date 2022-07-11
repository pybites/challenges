import re
from collections import Counter
from difflib import SequenceMatcher
from typing import List, Tuple

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags() -> List[str]:
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED) as f:
        tags = TAG_HTML.findall(f.read().lower())
    return [tag.replace("_", "").lower() for tag in tags]


def get_top_tags(tags: List[str]) -> List[Tuple[str, int]]:
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags: List[str]) -> Tuple[str, str]:
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    for tag1 in tags:
        for tag2 in tags:
            if tag1 == tag2 or tag1[0] != tag2[0]: continue

            similarity_ratio = SequenceMatcher(None, tag1, tag2).ratio()
            if SIMILAR < similarity_ratio:
                yield tuple(sorted([tag1, tag2]))


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
