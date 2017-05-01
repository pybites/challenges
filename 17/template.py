# http://pybit.es/codechallenge17.html
# quick template (instructions converted into methods)
# could use class as well
# use as needed (not required of course)
#
import os
import random
import sqlite3
from time import sleep

# this module might save you time parsing feeds
import feedparser

INTERVAL = 24 * 60 * 60  # change if you don't want every day
FEED = 'your_feed'


# Feed parsing

def parse_feed(feed=FEED):
    items = []
    # ...
    return items


# Keep cache of feed in SQLite

def get_episodes_from_db():
    pass


def add_new_episodes_to_db(episodes):
    pass


# Send out new episode and mark as complete

def get_random_episode():
    pass


def mark_episode_done(episode):
    pass


def mail_episode(episode):
    # could use os.environ to retrieve credentials
    pass


def main():
    while True:
        feed = parse_feed()
        for episode in feed:
            pass
        # ...
        # etc
        # ...
        sleep(INTERVAL)  # or use system cron / sched / pypi


if __name__ == '__main__':
    main()
