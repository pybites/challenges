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

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
API = tweepy.API(auth)


class UserTweets(object):

    def __init__(self, handle, max_id=None):
        self._handle = handle
        self._max_id = max_id
        self._count = NUM_TWEETS
        self.output_file = os.path.join(DEST_DIR, self._handle + EXT)
        self._tweets = list(self._get_tweets())
        self._save_tweets()

    def _get_tweets(self):
        user_timeline = API.user_timeline(id=self._handle, max_id=self._max_id, count=self._count)
        user_tweets = (Tweet(tweets.id_str, tweets.created_at, tweets.text.replace('\n', ''))
                       for tweets in user_timeline)

        return user_tweets

    def _save_tweets(self):
        with open(self.output_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(Tweet._fields)
            writer.writerows(self._tweets)

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, pos):
        return self._tweets[pos]


if __name__ == "__main__":

    for handle in ('pybites', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        
        for tw in user[:5]:
            print(tw)
        print()
