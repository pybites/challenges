from collections  import Counter
from difflib import get_close_matches
import re

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open(RSS_FEED) as f:
        content = f.read().lower()
    
    listTags = re.findall('<category>.*?</category>', content)

    for i, tag in enumerate(listTags):
        if '-' in tag:
            listTags[i] = tag.replace('-', ' ')

    strTags = ''
    return re.sub('<category>', '',
                  strTags.join(listTags).rstrip('</category>'))\
                  .split('</category>')


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(get_tags()).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    tagsLst = list(set(get_tags()))
    tagsLst.sort()
    tagsLstCpy = tagsLst.copy()
    similar = []

    for tag in tagsLst:
        match = get_close_matches(tag, tagsLstCpy, cutoff=SIMILAR)
        if len(match) == 2:
            similar.append((tag, match[1]))
            tagsLstCpy.remove(tag)

    return similar


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
