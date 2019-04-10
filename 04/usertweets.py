from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100


class UserTweets(object):

    def create_api(self):
        # Create api object
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)
        return api
    
    def tweets_per_handle(self, handle):
        # create a list of statuses (tweets), but only using id, timestamp and text for each
        statuses = [[x.id_str,x.created_at.strftime("%Y-%m-%d %H:%M:%S"),x.text] for x in tweepy.Cursor(self.api.user_timeline, id=handle).items(NUM_TWEETS)]
        # write the tweets on a csv file 
        with open(DEST_DIR + "/" + handle + "." + EXT, 'w') as myfile:
            writer = csv.writer(myfile)
            for status in statuses:
                writer.writerow(status)
        return statuses

    
    def __init__(self, handle, max_id=100):
        self.handle = handle
        self.api = self.create_api()
        self.tweets = self.tweets_per_handle(handle)

    def __getitem__(self, position):
        return self.tweets[position]


if __name__ == "__main__":

    for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
