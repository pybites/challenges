from collections import namedtuple
from tweets import TWEETS
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'ryanh153/data'
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
        self._max_id = int(max_id)
        self.output_file = f'{DEST_DIR}/myData.{EXT}'
        self._tweets = list(self._get_tweets())
        self._save_tweets()

    def _get_tweets(self):
        """Hint: use the user_timeline() method on the api you defined in init.
        See tweepy API reference: http://docs.tweepy.org/en/v3.5.0/api.html
        Use a list comprehension / generator to filter out fields
        id_str created_at text (optionally use namedtuple)"""

        if self._max_id:
            generator = (tweet for tweet in TWEETS if int(tweet.id_str) <= self._max_id)
        else:
            generator = (tweet for tweet in TWEETS)
        return generator

    def _save_tweets(self):
        """Use the csv module (csv.writer) to write out the tweets.
        If you use a namedtuple get the column names with Tweet._fields.
        Otherwise define them as: id_str created_at text
        You can use writerow for the header, writerows for the rows"""

        with open(self.output_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Date", "Tweet"])
            for tweet in self._tweets:
                writer.writerow([tweet.id_str, tweet.created_at, tweet.text])

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, pos):
        return self._tweets[pos]


if __name__ == "__main__":

    for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle, '100000000000000000000000000000000000000')
        for tw in user[:5]:
            print(tw)
        print()
