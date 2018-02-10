from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100


def get_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)


header = ['id_str', 'created_at', 'text']
Tweet = namedtuple('Tweet', header)


class UserTweets(object):
    """TODOs:
    - create a tweepy api interface
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory
    - implement len() and getitem() magic (dunder) methods"""
    api = get_api()

    def __init__(self, handle, max_id=None):
        self.id = handle
        self.max_id = max_id
        self.output_file = os.path.join(DEST_DIR, handle + '.' + EXT)
        self._tweets = [Tweet(tw.id_str, tw.created_at, tw.text) for tw in self._get_tweets()]
        self._2csv()

    def _get_tweets(self, n=NUM_TWEETS):
        data = []
        try:
            if self.max_id:
                data = tweepy.Cursor(self.api.user_timeline, id=self.id, max_id=self.max_id).items(limit=n)
            else:
                data = tweepy.Cursor(self.api.user_timeline, id=self.id).items(limit=n)
        except Exception as e:
            print('Failed with Cursor: {}'.format(e))
        return data

    def _2csv(self):
        with open(self.output_file, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, dialect='excel')
            try:
                spamwriter.writerow(header)
                for tw in self._tweets:
                    spamwriter.writerow(tw)
            except Exception as e:
                print('Failed: {}'.format(e))

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, item):
        return self._tweets[item]


if __name__ == "__main__":

    for handle in ('pybites', 'techmoneykids', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        try:
            user = UserTweets(handle)
        except Exception as e:
            print('Failed: {}'.format(e))
        else:
            for tw in user[:5]:
                print(tw)
        print()
