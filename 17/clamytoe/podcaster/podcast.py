import os
import random
import sqlite3
import feedparser
from collections import OrderedDict


class Podcast(object):

    def __init__(self, rss):
        """Constructor requires the url to the rss feed"""
        self.rss = rss

    def _info(self):
        """Internal method for retrieving the rss feed"""
        response = feedparser.parse(self.rss)
        return response

    def _detail(self, feed):
        """Populates detailed information about the podcast"""
        response = feed
        self.title = response['title']
        self.subtitle = response['subtitle']
        self.link = response['link']
        self.author = response['author_detail']['name']
        self.email = response['author_detail']['email']
        self.content = response['content']

    def parse_feed(self):
        """Parsed the information received from the rss feed"""
        self._detail(self._info()['feed'])  # populate podcast detail into object
        data = self._info()['entries']
        casts = {}
        for entry in data:
            cast_id = int(entry['title'].split()[0][1:])
            casts[cast_id] = {
                'title': entry['title'],
                'published': entry['published'],
                'file': entry['id'],
                'duration': entry['itunes_duration'],
                'summary': entry['summary']
            }

        episodes = OrderedDict(sorted(casts.items(), key=lambda n: n[0]))

        return episodes

    # Keep cache of feed in SQLite

    def get_episodes_from_db(self):
        pass

    def add_new_episodes_to_db(self, episodes):
        pass

    def get_random_episode(self):
        pass

    def mark_episode_done(self, episode):
        pass

    def mail_episode(self, episode):
        # could use os.environ to retrieve credentials
        pass

    def __repr__(self):
        pass
