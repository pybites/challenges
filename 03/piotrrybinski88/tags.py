from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re
from typing import List

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags() -> List:
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED) as file:
        data = file.read().replace('-', ' ').lower()
    return re.findall(TAG_HTML, data)


def get_top_tags(tags: List) -> List:
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags: List) -> List:
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    product_of_words = list(product(tags, repeat=2))
    similar_words = []
    for word_one, word_two in product_of_words:
        if word_two[0] == word_one[0] and word_two != word_one:
            if SequenceMatcher(None, word_one, word_two).ratio() > SIMILAR:
                list_of_similar_words = [word_one, word_two]
                list_of_similar_words.sort()

                if list_of_similar_words not in similar_words:
                    similar_words.append(list_of_similar_words)
        else:
            continue

    return similar_words

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
