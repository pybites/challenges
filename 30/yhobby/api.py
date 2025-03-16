'''
docstring
'''
from pprint import pprint
import collections

import requests


def search(keyword: str) -> tuple:
    '''docstring'''
    Episode = collections.namedtuple('Episode', ['category', 'id', 'url', 'title', 'description'])
    url = 'https://search.talkpython.fm/api/search?q={keyword}'
    response = requests.get(url)
    data = response.json()
    output = list(map(Episode._make, (episode.values() for episode in data['results'])))
    return tuple(output)


if __name__ == '__main__':
    pprint(search('test'))