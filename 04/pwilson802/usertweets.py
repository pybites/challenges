from collections import namedtuple
import csv
import os
from pathlib import Path

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', 'id_str created_at text')


class UserTweets(object):

    def __init__(self, handle, max_id=None):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)
        self.handle = handle
        self.max_id = max_id

        self._tweets = list(self._get_tweets())
        self._save_tweets()

    def _get_tweets(self):
        for tw in self.api.user_timeline(self.handle, count=100, max_id=self.max_id):
            id_str = tw.id_str
            created_at = tw.created_at
            text = tw.text
            yield Tweet(id_str, created_at, text)

    def _save_tweets(self):
        file = Path(f'data/{self.handle}.csv')
        with open(file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self._tweets[0]._fields)
            writer.writerows(self._tweets)


    def __len__(self):
        """See http://pybit.es/python-data-model.html"""
        return len(self._tweets)

    def __getitem__(self, pos):
        """See http://pybit.es/python-data-model.html"""
        return self._tweets[pos]


if __name__ == "__main__":

    for handle in ('pybites', 'juliansequeira', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
