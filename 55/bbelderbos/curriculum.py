from collections import namedtuple, OrderedDict
from itertools import islice
import json
from math import ceil
import sys

import requests

BOOK_URL = "http://pbreadinglist.herokuapp.com/books/{}"
BOOK_API_URL = "http://pbreadinglist.herokuapp.com/api/books/{}"
NUMBER_DAYS_CHALLENGE = 100
CHALLENGE_HASHTAG = '#100DaysOfData'
VERSION = 0.1
GITHUB_REPO = "https://github.com/bbelderbos/100DaysOfData"

Book = namedtuple('Book', 'title pages')


def get_book(bookid):
    book = requests.get(BOOK_API_URL.format(bookid)).json()
    return Book(book['title'], int(book['pages']))


def _calc_pages_per_day(books):
    total_pages = sum(book.pages for book in books)
    return ceil(total_pages / NUMBER_DAYS_CHALLENGE)


def _gen_book_pages(books):
    for book in books:
        for page in range(1, book.pages + 1):
            yield (book.title, page)


def create_activities(books):
    pages_per_day = _calc_pages_per_day(books)
    pages = _gen_book_pages(books)
    for day in range(1, 101):
        update = (f'Day {str(day).zfill(2)}: {CHALLENGE_HASHTAG} '
                  'progress: today I ')

        chunk = list(islice(pages, pages_per_day))
        if chunk:
            first_book, first_page = chunk[0]
            last_book, last_page = chunk[-1]

            finished = ''
            if last_book != first_book:
                finished = f'finished 📗 {first_book} and '

            update += f'{finished}read 📘 {last_book} till p.{last_page}'
        else:
            # no chunk means I have 1 or 2 leeway days
            update += (f'completed the {CHALLENGE_HASHTAG} challenge reading'
                       f' {len(books)} books on the subject! #milestone')

        update += ' (logged via @pybites CodeChalleng.es)'
        yield update


def generate_response(activities):
    ret = {
        "title": CHALLENGE_HASHTAG,
        "version": VERSION,
        "github_repo": GITHUB_REPO,
        "tasks": [OrderedDict(day=day,
                              activity=activity,
                              done=False)
                  for day, activity in enumerate(activities, 1)]
    }
    return json.dumps(ret)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print((f'Usage: python {sys.argv[0]} bookid_1 bookid_2 '
              'bookid_n (in order of reading)'))
        sys.exit(1)

    bookids = sys.argv[1:]
    books = [get_book(bookid) for bookid in bookids]
    activities = create_activities(books)
    print(generate_response(activities))
