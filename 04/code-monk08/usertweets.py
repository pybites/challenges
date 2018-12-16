from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = '.csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', 'id_str created_at text')


class UserTweets(object):

    def __init__(self, handle, max_id=None):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(self.auth)
        self.handle = handle
        self.max_id = max_id
        self.output_file = os.path.join(
            DEST_DIR, "{}{}".format(self.handle, EXT))
        self._tweets = list(self._get_tweets())
        self._save_tweets()

    def _get_tweets(self):
        user_timeline = self.api.user_timeline(
            id=self.handle, max_id=self.max_id, count=NUM_TWEETS)
        for tweet in user_timeline:
            yield tweet

    def _save_tweets(self):
        if not os.path.exists(DEST_DIR):
            os.mkdir(DEST_DIR)
        with open(self.output_file, 'w') as f:
            writer_obj = csv.writer(f)
            writer_obj.writerow(Tweet._fields)
            writer_obj.writerows(
                [(tweet.id_str, tweet.created_at, tweet.text.replace('\n', ' ')) for tweet in self._tweets])

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, pos):
        return self._tweets[pos]


if __name__ == "__main__":
    handles = ('pybites', 'codemonk08_')
    for handle in handles:
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
