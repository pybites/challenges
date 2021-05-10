import requests
import requests_cache

requests_cache.install_cache('book_cache', backend='sqlite', expire_after=86400)

BASE_URL = 'https://www.googleapis.com/books/v1/volumes'
SEARCH_URL = BASE_URL + '?q={}'
BOOK_URL = BASE_URL + '/{}'


def get_book_info(book_id):
    return requests.get(BOOK_URL.format(book_id)).json()


def search_books(term):
    return requests.get(SEARCH_URL.format(term)).json()


if __name__ == '__main__':
    from pprint import pprint as pp
    #pp(get_book_info('PvwDFlJUYHcC'))
    term = 'python for finance'
    pp(search_books(term))
