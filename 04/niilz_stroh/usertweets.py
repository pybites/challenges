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

Tweet = namedtuple('Tweet', ['id_str', 'created_at', 'text'])

class UserTweets:
    def __init__(self, handle, max_id=None):
        self.handle = handle
        self.max_id = max_id
        self.time_line = api.user_timeline(self.handle, max_id=max_id, count=100)
        self.tweets = []
        self.output_file = f'data/{self.handle}.csv'

        for status in self.time_line:
            self.tweets.append(
                Tweet(status.id_str, status.created_at, status.text)
                )

        with open(self.output_file, 'w', newline='') as csvfile:

            twitter_data = csv.writer(csvfile)
            twitter_data.writerow(['id_str', 'created_at', 'text'])
            for tw in self.tweets:
                twitter_data.writerow(tw)

    def __len__(self):
        return len(self.tweets)
    
    def __getitem__(self, idx):
        return self.tweets[idx]


if __name__ == "__main__":

    for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        print()
