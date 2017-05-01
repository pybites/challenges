# http://pybit.es/codechallenge17.html
from collections import namedtuple
from datetime import datetime
import logging
import os
import platform
from pprint import pprint as pp
import sqlite3
import sys
import time
import urllib.request

import feedparser
import schedule
from sqlalchemy.sql.expression import func

from model import session, Podcast

FEED = 'http://noahkagan.libsyn.com/rss'
LOCAL = platform.system() == 'Darwin'
RSS = 'rss'

FORMAT = '%(asctime)-15s :: %(message)s'
logging.basicConfig(filename='podcast.log', level=logging.DEBUG, format=FORMAT)

Episode = namedtuple('Episode', 'id title link published')


def convert_time_struct_to_dt(struct):
    return datetime.fromtimestamp(time.mktime(struct))


def parse_feed():
    d = {}
    output = feedparser.parse(_get_feed())
    for e in output['entries']:
        id = e.get('id')
        title = e.get('title')
        link = e.get('link')
        published = convert_time_struct_to_dt(e.get('published_parsed'))
        d[id] = Episode(id, title, link, published)
    return d


def _get_feed():
    if LOCAL:
        if not os.path.isfile(RSS):
            logging.debug('RSS file not found, downloading it')
            try:
                urllib.request.urlretrieve(FEED, RSS)
            except Exception as exc:
                logging.error('Cannot get rss, error: {}'.format(exc))
                sys.exit(1)
        with open(RSS) as f:
            return f.read()
    else:
        return FEED


def get_episodes_from_db():
    return [row.id for row in session.query(Podcast.id).all()]


def add_new_episodes_to_db(new_episodes):
    records = [Podcast(id=ep.id, title=ep.title, link=ep.link, published=ep.published) 
               for ep in new_episodes.values()]
    session.add_all(records)
    session.commit()


def get_random_episode():
    # http://stackoverflow.com/questions/60805/getting-random-row-through-sqlalchemy
    return session.query(Podcast).filter(Podcast.done==False).order_by(func.random()).first()


def mark_episode_done(episode):
    episode.done = True
    session.commit()


def mail_episode(ep):
    # could use os.environ to retrieve credentials
    subject = 'Podcast for today: {}'.format(ep.title)
    msg = '{}\n\n{}'.format(ep.link, _get_stats())
    logging.debug('Subject: {}'.format(subject))
    logging.debug('Message: {}'.format(msg))


def _get_stats():
    status = dict(session.query(Podcast.done, func.count(Podcast.done)).group_by(Podcast.done).all())
    done = status.get(True, 0)
    total = sum(status.values())
    perc = done/total * 100
    return 'Podcast consumption stats: {:.1f}% done [{} of {}]'.format(perc, done, total)


def main():
    feed = parse_feed()
    ids_in_db = get_episodes_from_db()
    new_episodes = dict((k, feed[k]) for k in feed.keys() if k not in ids_in_db)

    logging.debug('adding {} new episodes'.format(len(new_episodes)))
    add_new_episodes_to_db(new_episodes)

    ep = get_random_episode()
    if not ep:
        logging.debug('no unplayed episode, no email')
    else:
        mail_episode(ep)
        mark_episode_done(ep)


if __name__ == '__main__':
    main()
