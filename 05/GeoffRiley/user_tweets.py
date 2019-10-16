from datetime import datetime
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
    """TODOs:
    - create a tweepy api interface
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory
    - implement len() an getitem() magic (dunder) methods"""

    def __init__(self, handle, max_id=None):
        self._handle = handle
        self._save_file = f'{DEST_DIR}/{handle}.{EXT}'
        self._max_id = max_id
        self._auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self._auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self._api = tweepy.API(self._auth)
        self.read_tweets()
        self.save()

    def read_tweets(self):
        twitterings = self._api.user_timeline(screen_name=self._handle, max_id=self._max_id, count=NUM_TWEETS)
        self._twitterings = [Tweet(x.id_str, x.created_at, x.text) for x in twitterings]

    def save(self):
        if not os.path.exists(DEST_DIR):
            os.makedirs(DEST_DIR)
        if os.path.exists(self._save_file):
            os.remove(self._save_file)
        with open(self._save_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(Tweet._fields)
            writer.writerows([(x.id_str, x.created_at, x.text) for x in self._twitterings])

    def __len__(self):
        return len(self._twitterings)

    def __getitem__(self, item):
        return self._twitterings[item]

    @property
    def output_file(self):
        return self._save_file


if __name__ == "__main__":

    for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()