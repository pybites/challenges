# http://pybit.es/codechallenge17.html
from collections import namedtuple
from datetime import datetime, timedelta
import os
import platform
from pprint import pprint as pp
import sqlite3
import sys
import time
import urllib.request

import feedparser
import schedule

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.sql.expression import func

FEED = 'http://noahkagan.libsyn.com/rss'
LOCAL = platform.system() == 'Darwin'
RSS = 'rss'

Episode = namedtuple('Episode', 'id title link published')

Base = declarative_base()

class Podcast(Base):
    __tablename__ = 'podcasts'
    id = Column('id', String(), primary_key=True)
    title = Column('title', String(), index=True)
    link = Column('link', String())
    published = Column('published', DateTime())
    done = Column('done', Boolean(), default=False)
    created_on = Column('created_on', DateTime(), default=datetime.now)
    updated_on = Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "<Podcast(id='%s', title='%s', link='%s', published='%s', done='%s')>" \
               % (self.id, self.title, self.link, self.published, self.done)


engine = create_engine('sqlite:///podcast.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


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
            print('RSS file not found, downloading it')
            try:
                urllib.request.urlretrieve(FEED, RSS)
            except Exception as exc:
                print('Cannot get rss, error: {}'.format(exc))
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
    print('Subject: {}'.format(subject))
    print('Message: {}'.format(msg))


def _get_stats():
    status = dict(session.query(Podcast.done, func.count(Podcast.done)).group_by(Podcast.done).all())
    done = status.get(True)
    total = sum(status.values())
    perc = done/total * 100
    return 'Podcast consumption stats: {:.1f}% done [{} of {}]'.format(perc, done, total)


def cron():
    #schedule.every(10).minutes.do(job)
    #schedule.every().hour.do(job)
    #while True:
    #    schedule.run_pending()
    #    time.sleep(6)
    pass


def main():
    feed = parse_feed()
    ids_in_db = get_episodes_from_db()
    new_episodes = dict((k, feed[k]) for k in feed.keys() if k not in ids_in_db)
    print('adding {} new episodes'.format(len(new_episodes)))
    add_new_episodes_to_db(new_episodes)
    ep = get_random_episode()
    mark_episode_done(ep)
    mail_episode(ep)
    cron()


if __name__ == '__main__':
    main()
