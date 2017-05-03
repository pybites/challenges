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
            self.image = response.feed.image.href
            # TODO: Clean up the summary by removing whitespace and line returns
            self.summary = response.feed.summary
            self.author = response.feed.author_detail.name
            self.email = response.feed.author_detail.email

            data = response.entries
            # TODO: Put into a database istead of an OrderedDict
            casts = {}
            for i, entry in enumerate(data):
                # remove extra parameters from file link if they exist
                file_link = self._format_link(entry.links[1].href)
                duration_time = self._format_duration(entry.itunes_duration)

                casts[len(data) - i] = {
                    'title': entry.title,
                    'file': file_link,
                    'duration': duration_time,
                    'published': entry.published,
                    # TODO: Clean up summary by removing html tags and line returns
                    'summary': entry.summary
                }

            for cast in casts:
                print(casts[cast]['title'])
            episodes = OrderedDict(sorted(casts.items(), key=lambda n: n[0]))

            return episodes
        else:
            # TODO: Handle other return codes from server
            print('There was a error retrieving the rss feed')
            exit(1)

    @staticmethod
    def _format_link(link):
        """Removes extra parameters from file link if they exist"""
        if '?' in link:
            return link.split('?')[0]
        else:
            return link

    @staticmethod
    def _format_duration(seconds):
        """Converts seconds into hh:mm:ss format"""
        if ':' in seconds:
            return seconds
        else:
            m, s = divmod(int(seconds), 60)
            h, m = divmod(m, 60)
            return f'{h:02}:{m:02}:{s:02}'

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
