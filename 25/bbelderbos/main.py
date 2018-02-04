from collections import defaultdict
from datetime import datetime
import shelve

from themoviedb import Movies, Tv, CACHE
from notifications import generate_mail_msg, mail_msg

SENT_CACHE = 'sent.shelve'

language = 'en'
num_pages = 3


def update_store():
    mo = Movies()
    mo.get_now_playing()
    mo.get_upcoming()
    tv = Tv()
    tv.get_on_the_air()
    tv.get_popular()


def load_store():
    items = defaultdict(lambda: defaultdict(list))

    with shelve.open(CACHE) as sh, shelve.open(SENT_CACHE) as ca:
        for key in sh:

            if key in ca:
                continue
            ca[key] = datetime.utcnow()

            entry = sh[key]
            items[entry.kind][entry.listing].append(
                entry)

        return items


if __name__ == '__main__':
    update_store()
    items = load_store()
    content = generate_mail_msg(items)
    mail_msg(content)
