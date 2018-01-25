from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
data_dir = os.path.join(os.getcwd(), 'data')
TWEET = namedtuple('Tweet', 'Text Created_At ID_Str')

class UserTweets(object):
    """TODOs:
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory"""
    def __init__(self, handle):
        self.handle = handle
        self.filename = os.path.join(data_dir, '{}_tweets.csv'.format(handle))
        self._tweets = list(self.get_tweets())
        self.save_tweets()

    def get_tweets(self):
        public_tweets = api.user_timeline(id=self.handle, count=5)
        for tweet in public_tweets:
            yield TWEET(tweet.text, tweet.created_at, tweet.id_str)

    def save_tweets(self):
        with open(self.filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(TWEET._fields)
            writer.writerows([[tweet.Text, tweet.Created_At, tweet.ID_Str] for tweet in self._tweets])

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, item):
        return self._tweets[item]


if __name__ == "__main__":

    for handle in ('pybites', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        print(len(user))
        for tw in user[:5]:
            print(tw)
