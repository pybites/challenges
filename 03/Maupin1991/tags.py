import re
import difflib

import itertools

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open(RSS_FEED) as f:
        r = f.read()
        all_tags = re.findall(r'<category>(.+?)</category>', r)
        return [m.replace("-", " ").lower() for m in all_tags]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    d = {i: tags.count(i) for i in tags if tags.count(i)}
    return ((k, d[k]) for k in sorted(d, key=d.get, reverse=True)[:TOP_NUMBER])


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    return [(a, b)
            for (a, b) in itertools.permutations(tags, 2)
            if difflib.SequenceMatcher(a=a.lower(), b=b.lower()).ratio() > SIMILAR
            and a != b
            and b.endswith('s')]


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
