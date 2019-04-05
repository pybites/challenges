import re
from difflib import SequenceMatcher as sm

TOP_NUMBER = 10
RSS_FEED = '../rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open(RSS_FEED) as feed:
        feed_lines = feed.read().lower()

        tags = re.findall(
                r'\<category\>([\w\s\-\_]+)\<\/category\>',
                feed_lines)

        tags_dict = {}
        for tag in tags:
            if "-" in tag:
                tag = tag.replace("-", " ")
            if tag not in tags_dict:
                tags_dict[tag] = 1
            else:
                tags_dict[tag] += 1
        return tags_dict


def get_top_tags(tags):
    sorted_tags = sorted(tags.items(),
                        key=lambda tag: tag[1],
                        reverse=True)

    return sorted_tags[0:10]


def get_similarities(tags):
    similars = []
    for tag1 in tags:
        for tag2 in tags:
            seq = sm(None, tag1, tag2)
            ratio = seq.ratio()
            if ratio >= SIMILAR and tag1 != tag2:
                similars.append(sorted((tag1, tag2),
                                key=lambda t: len(t)))
    return similars


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print(f'* Top {TOP_NUMBER} tags:')
    for tag, count in top_tags:
        print(f'{tag:<20} {count}')
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print(f'{singular:<20} {plural}')
