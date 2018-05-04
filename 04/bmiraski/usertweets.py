from collections import namedtuple
import csv
import os
import requests

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
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)
        self.handle = handle
        self.max_id = max_id
        self.output_file = 'data/' + str(self.handle) + '.csv'
        self._tweets = list(self._get_tweets(api))
        self._save_tweets()

    def _get_tweets(self, api):
        """Hint: use the user_timeline() method on the api you defined in init.
        See tweepy API reference: http://docs.tweepy.org/en/v3.5.0/api.html
        Use a list comprehension / generator to filter out fields
        id_str created_at text (optionally use namedtuple)"""
        tweets = api.user_timeline(self.handle, None, self.max_id, NUM_TWEETS)
        for tweet in tweets:
            yield Tweet(tweet.id_str, tweet.created_at, tweet.text)


    def _save_tweets(self):
        """Use the csv module (csv.writer) to write out the tweets.
        If you use a namedtuple get the column names with Tweet._fields.
        Otherwise define them as: id_str created_at text
        You can use writerow for the header, writerows for the rows"""
        with open(self.output_file, 'w', newline='') as csvfile:
            tweet_writer = csv.writer(csvfile)
            tweet_writer.writerow(Tweet._fields)
            tweet_writer.writerows(self._tweets)

    def __len__(self):
        """See http://pybit.es/python-data-model.html"""
        return len(self._tweets)

    def __getitem__(self, pos):
        """See http://pybit.es/python-data-model.html"""
        return self._tweets[pos]



if __name__ == "__main__":

    for handle in ('pybites', 'mkennedy', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
