from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', 'id_str, created_at, text')


class UserTweets(object):

    def __init__(self, handle, max_id=None):
        """
        Get user tweets from tweepy API. Writes output to
        a csv in the data directory specified.
        :param handle: username
        :param max_id: (optional) maximum number of tweets to return
        """

        # setting up
        self._auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self._auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self._handle = handle
        self._api = tweepy.API(self._auth)
        self._max_id = max_id

        # get user tweets
        self._tweets = list(self._get_tweets())

        # save the csv file
        self.output_file = os.path.join(DEST_DIR, self._handle + '.' + EXT)
        self._save_tweets()

    def _get_tweets(self):
        """Returns list of Tweet namedtuples from the user timeline"""
        return [Tweet(id_str=j.id_str,
                      text=j.text,
                      created_at=j.created_at)
                for j in self._api.user_timeline(id=self._handle,
                                                 max_id=self._max_id)]

    def _save_tweets(self):
        """Writes all the tweets fetched by the get_tweets method in a csv file"""
        with open(self.output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(Tweet._fields)
            for t in self._tweets:
                writer.writerow(list(t.__getattribute__(f)
                                     for f in Tweet._fields))
            return

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, pos):
        return self._tweets[pos]


if __name__ == "__main__":

    for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
