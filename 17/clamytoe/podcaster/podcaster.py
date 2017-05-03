import os
import random
import sqlite3
import feedparser
from collections import OrderedDict
from sys import exit


class Podcast(object):

    def __init__(self, rss):
        """Constructor requires the url to the rss feed"""
        self.rss = rss
        self.episodes = self._update()

    def _update(self):
        """Internal method for retrieving the rss feed"""
        response = feedparser.parse(self.rss)

        if response.status == 200:
            self.title = response.feed.title
            self.subtitle = response.feed.subtitle
            self.link = response.feed.link
            self.author = response.feed.author_detail.name
            self.email = response.feed.author_detail.email

            data = response.entries
            casts = {}
            for i, entry in enumerate(data):
                casts[len(data) - i] = {
                    'title': entry.title,
                    'published': entry.published,
                    'published_parsed': entry.published_parsed,
                    'file': entry.id,
                    'duration': entry.itunes_duration,
                    'summary': entry.summary
                }

            for cast in casts:
                print(casts[cast]['title'])
            episodes = OrderedDict(sorted(casts.items(), key=lambda n: n[0]))

            return episodes
        else:
            print('There was a error retrieving the rss feed')
            exit(1)

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
        return f'Podcast "{self.title}" with {len(self.episodes)} episodes>'
