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
Tweet = namedtuple('Tweet', ['id_str', 'created_at', 'text'])


class UserTweets(object):
    """TODOs:
    - create a tweepy api interface
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory
    - implement len() an getitem() magic (dunder) methods
    """

    def __init__(self, handle, max_id=None):
        """"""
        self._handle = handle
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self._time_line = tweepy.API(auth).user_timeline(handle=self._handle, count=NUM_TWEETS, max_id=max_id)
        self._tweets = self._get_tweets()
        self.output_file = os.path.join(DEST_DIR, f'{self._handle}.csv')
        self._save_tweets()

    def _get_tweets(self):
        """"""
        return [Tweet(tweet.id_str, tweet.created_at, tweet.text) for tweet in self._time_line]

    def _save_tweets(self):
        """"""
        with open(self.output_file, 'w') as fp:
            writer = csv.writer(fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['id_str', 'created_at', 'text'])
            for tweet in self._get_tweets():
                writer.writerow([tweet.id_str, tweet.created_at, tweet.text.encode('ascii', 'replace').decode()])

    def __len__(self):
        """"""
        return len(self._tweets)

    def __getitem__(self, item):
        """"""
        return self._tweets[item]


if __name__ == "__main__":

    for handle in ['pybites', '_juliansequeira', 'bbelderbos']:
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
