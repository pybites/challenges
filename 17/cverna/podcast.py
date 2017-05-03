# http://pybit.es/codechallenge17.html
# quick template (instructions converted into methods)
# could use class as well
# use as needed (not required of course)
#
import os
import sqlite3
from time import sleep
from collections import namedtuple
from random import randint
# this module might save you time parsing feeds
import feedparser

INTERVAL = 24 * 60 * 60  # change if you don't want every day
FEED = 'https://www.podcastinit.com/feed/mp3/'

conn = sqlite3.connect('podcast.sqlite')
db = conn.cursor()
Episode = namedtuple('Episode', 'title url')


# Feed parsing
def parse_feed(feed=FEED):
    items = []
    feed = feedparser.parse(feed)
    for entry in feed['entries']:
        for link in entry['links']:
            if link['type'] == 'audio/mpeg':
                ep_data = Episode(title=entry['title'], url=link['href'])
                items.append(ep_data)
    return items


# Keep cache of feed in SQLite

def get_episodes_from_db(unplayed=False):
    if unplayed:
        db.execute("SELECT * FROM podcast WHERE played=0")
    else:
        db.execute("SELECT title FROM podcast")
    rows = db.fetchall()
    return rows


def add_new_episodes_to_db(episodes):
    old_episode = get_episodes_from_db()
    for episode in episodes:
        if (episode.title,) not in old_episode:
            db.execute("INSERT INTO podcast (title, url, played) VALUES ('{}', '{}', 0)".
                       format(episode.title, episode.url))
            conn.commit()


# Send out new episode and mark as complete

def get_random_episode():
    unplayed = get_episodes_from_db(unplayed=True)
    if len(unplayed) > 0:
        episode = randint(0, len(unplayed)-1)
        mark_episode_done(unplayed[episode])
        return unplayed[episode]


def mark_episode_done(episode):
    db.execute("UPDATE podcast SET played=1 WHERE title='{}'".format(episode[0]))
    conn.commit()


def mail_episode(episode):
    # could use os.environ to retrieve credentials


def main():
    db.execute(
        'CREATE TABLE IF NOT EXISTS podcast (title TEXT PRIMARY_KEY, url TEXT, played INTEGER)')
    while True:
        feed = parse_feed()
        add_new_episodes_to_db(feed)
        episode = get_random_episode()
        print(episode)
        sleep(20)  # or use system cron / sched / pypi


if __name__ == '__main__':
    main()
    conn.close()
