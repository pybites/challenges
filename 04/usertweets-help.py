from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', 'id_str created_at text')


class UserTweets(object):

    def __init__(self, handle, max_id=None):
        """Get handle and optional max_id.
        Use tweepy.OAuthHandler, set_access_token and tweepy.API
        to create api interface.
        Use _get_tweets() helper to get a list of tweets.
        Save the tweets as data/<handle>.csv"""
        # ...
        self._tweets = list(self._get_tweets())
        self._save_tweets()

    def _get_tweets(self):
        return self.api.user_timeline(
            screen_name=self.user_name, count=count
        )

    def _save_tweets(self):
        headers = ['id_str', 'created_at', 'text']
        prepared_datas = self.prepare_data_csv(self._tweets)
        self._save_in_csv('test', headers, prepared_datas)

    def save_in_csv(self, filename, headers, datas):
        with open('{}/{}/{}'.format(DEST_DIR, filename, EXT), 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(headers)
            for data in datas:
                writer.writerow(data)

    def __len__(self):
        """See http://pybit.es/python-data-model.html"""
        pass

    def __getitem__(self, pos):
        """See http://pybit.es/python-data-model.html"""
        pass


if __name__ == "__main__":

    for handle in ('pybites', 'techmoneykids', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
