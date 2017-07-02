from collections import namedtuple
from functools import wraps
import re
import shelve

CACHE = 'items.shelve'
DEFAULT_OVERWRITE = True

Item = namedtuple('Item', 'id kind title genres overview poster')


def _get_title(item):
    # movies API uses 'title', series API uses 'name'
    title = item.get('title')

    if not title:
        title = item.get('name')

    return title


def _store(kind, resp, overwrite=DEFAULT_OVERWRITE):
    with shelve.open(CACHE) as sh:
        for item in resp:
            key = str(item['id'])

            if overwrite and key in sh:
                del sh[key]

            title = _get_title(item)
            if not title:
                continue

            item = Item(id=item['id'],
                        kind=kind,
                        title=title,
                        genres=item['genre_ids'],
                        overview=item['overview'],
                        poster=item['poster_path'])

            sh[key] = item


def store_results(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        func_name = str(args[1]).lower()
        kind = re.sub(r'.*bound.*?\.(\S+) of.*', r'\1', func_name)
        print(kind)
        resp = f(*args, **kwargs)
        _store(kind, resp)
        print(len(resp))
        return resp
    return wrapped
