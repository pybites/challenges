import os

import requests
import toolz


OMDB_API_KEY = os.environ.get('OMDB_API_KEY', '')


def main():
    query = input('Enter keyword: ')
    params = {
        'apikey': OMDB_API_KEY,
        's': query,
    }
    url = 'http://www.omdbapi.com/'
    response = requests.get(url, params=params)

    data = response.json()
    search_results = data.get('Search')
    print('Total:', data.get('totalResults'))
    print('-----')
    for each in search_results:
        print('Title:', toolz.get_in(['Title'], each))
        print('Year:', toolz.get_in(['Year'], each))
        print('imdbID:', toolz.get_in(['imdbID'], each))
        print('Type:', toolz.get_in(['Type'], each))
        print('Poster:', toolz.get_in(['Poster'], each))
        print('-----')


if __name__ == '__main__':
    main()
