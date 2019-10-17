import feedparser
from difflib import get_close_matches
from collections import Counter
from operator import itemgetter

TOP_NUMBER = 10
RSS_FEED = 'https://pybit.es/feeds/all.rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    feed_data = feedparser.parse(RSS_FEED)
    tag_groups = [channel.get('tags') for channel in feed_data.entries]
    return [tags['term'] for tag_list in tag_groups for tags in tag_list]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    counted = Counter(tags)
    return sorted(counted.items(), key=itemgetter(1),
                  reverse=True)[:TOP_NUMBER]


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    # remove duplicates
    deduped = set(tags)
    # make it indexable
    tags = list(deduped)
    similarities = []
    for index, word in enumerate(tags):
        # if not last index
        last_index = len(tags) - 1
        if index != last_index:
            similar = get_close_matches(word,
                                        tags[index + 1:],
                                        n=1,
                                        cutoff=SIMILAR)
            if len(similar) == 1:
                similarities.append((word, similar[0]))
    return similarities


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
