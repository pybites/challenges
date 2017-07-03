from collections import namedtuple
from functools import wraps
import re
import shelve

CACHE = 'items.shelve'
DEFAULT_OVERWRITE = False

Item = namedtuple('Item', 'id kind listing title genres overview release_date poster')  # noqa E501


def _get_title(item):
    # movies API uses 'title', series API uses 'name'
    title = item.get('title')

    if not title:
        title = item.get('name')

    return title


def _get_release_date(item):
    # movies API uses 'release_date', series API uses 'first_air_date'
    release_date = item.get('release_date')

    if not release_date:
        release_date = item.get('first_air_date')

    return release_date


def _store(kind, listing, resp, overwrite=DEFAULT_OVERWRITE):
    with shelve.open(CACHE) as sh:
        for item in resp:
            key = str(item['id'])

            if overwrite and key in sh:
                del sh[key]

            title = _get_title(item)
            if not title:
                continue

            release_date = _get_release_date(item)
            if not release_date:
                continue

            item = Item(id=item['id'],
                        kind=kind,
                        listing=listing,
                        title=title,
                        genres=item['genre_ids'],
                        overview=item['overview'],
                        release_date=release_date,
                        poster=item['poster_path'])

            sh[key] = item


def store_results(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        class_name = str(args[0]).lower()
        kind = re.sub(r'.*\.(\S+)\sobject.*', r'\1', class_name)
        print(kind)
        func_name = str(args[1]).lower()
        listing = re.sub(r'.*bound.*?\.(\S+) of.*', r'\1', func_name)
        print(listing)
        resp = f(*args, **kwargs)
        _store(kind, listing, resp)
        print(len(resp))
        return resp
    return wrapped
