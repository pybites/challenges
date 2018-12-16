from collections import namedtuple
import csv
import os
import sys
import time

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 200

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
API = tweepy.API(auth)

Tweet = namedtuple('Tweet', 'id_str created_at text')


class UserTweets(object):

    def __init__(self, handle, max_id=None):
        self.handle = handle
        self.max_id = max_id
        self.output_file = '{}.{}'.format(os.path.join(DEST_DIR, self.handle), EXT)
        self._tweets = list(self._get_tweets())
        self._save_tweets()

    def _get_tweets(self):
        tweets = API.user_timeline(self.handle, count=NUM_TWEETS, max_id=self.max_id)
        return (Tweet(s.id_str, s.created_at, s.text.replace('\n', '')) for s in tweets)

    def _save_tweets(self):
        with open(self.output_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(Tweet._fields)
            writer.writerows(self._tweets)

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, pos):
        return self._tweets[pos]


if __name__ == "__main__":

    handles = """pybites importpython lifehacker Schwarzenegger github gvanrossum""".split()

    for handle in handles:
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
        time.sleep(1)
