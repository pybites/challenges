from collections import namedtuple
from functools import wraps
import shelve

CACHE = 'items.shelve'

Item = namedtuple('Item', 'id title genres overview poster')


def _store(resp, overwrite=False):
    sh = shelve.open(CACHE)
    for item in resp:
        key = str(item['id'])

        if key in sh:
            continue

        if overwrite:
            del sh[key]

        item = Item(id=item['id'],
                    title=item['title'],
                    genres=item['genre_ids'],
                    overview=item['overview'],
                    poster=item['poster_path'])

        sh[key] = item
    sh.close()


def store_results(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        resp = f(*args, **kwargs)
        _store(resp)
        return resp
    return wrapped
