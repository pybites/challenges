from collections import Counter
from difflib import get_close_matches
import feedparser


TOP_NUMBER = 10
RSS_FEED = "rss.xml"
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    return dict(
        Counter(
            [
                str(tag["term"]).replace("-", " ")
                for entry in feedparser.parse(RSS_FEED)["entries"]
                for tag in entry["tags"]
            ]
        )
    )


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return dict(Counter(tags).most_common(TOP_NUMBER))


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    sim = set()
    for tag in tags:
        close = get_close_matches(tag, tags, cutoff=SIMILAR)
        if len(close) > 1:
            sim.add(tuple(sorted(close)))
    return sim


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print("* Top {} tags:".format(TOP_NUMBER))
    for tag, count in top_tags.items():
        print("{:<20} {}".format(tag, count))
    similar_tags = get_similarities(tags)
    print()
    print("* Similar tags:")
    for singular, plural in similar_tags:
        print("{:<20} {}".format(singular, plural))
