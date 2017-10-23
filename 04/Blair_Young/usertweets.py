from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100
Tweet = namedtuple('Tweet', 'id_str created_at text')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

class UserTweets(object):
    '''Setup Twitter API interface'''
    def __init__(self, handle, max_id=None):
        self.output_file = os.path.join(DEST_DIR, handle+'.csv')
        self.timeline_tweets = api.user_timeline(handle, max_id = max_id, count = 100)
        self._tweets = list(self._get_tweets())
        self._save_tweets()
        
    def _get_tweets(self):
        '''grabs tweets from user'''
        for tweet in self.timeline_tweets:
            yield Tweet(tweet.id_str, tweet.created_at, tweet.text)

    def _save_tweets(self):
        '''saves tweets to output dir as .csv'''
        with open(self.output_file, 'w') as f:
            w = csv.writer(f)
            w.writerow(Tweet._fields)
            w.writerows([(tweet.id_str, tweet.created_at, tweet.text) for tweet in self._tweets])

    def __len__(self):
        '''get len'''
        return len(self._tweets)

    def __getitem__(self, pos):
        '''iteratable'''
        return self._tweets[pos]


if __name__ == "__main__":

    for handle in ('pybites', 'techmoneykids', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
        