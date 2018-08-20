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
    - implement len() an getitem() magic (dunder) methods"""

    def __init__(self, screen_name, max_id=None):
        self._user = screen_name
        self._tweets = 0
        self._max_id = max_id
        self.output_file = "{}/{}_tweets.{}".format(DEST_DIR, self._user, EXT)
        try:
            self._auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            self._auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
            self._api = tweepy.API(self._auth)
        except Exception:
            print("Problem Authenticating")

        tweets = self._api.user_timeline(screen_name=self._user,
                                         max_id=self._max_id,
                                         count=NUM_TWEETS)

        self._tweets = [Tweet(tw.id_str, tw.created_at, tw.text) for tw in tweets]
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        self.save()

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, position):
        return self._tweets[position]

    def save(self):
        if len(self._tweets) == 0:
            print("No tweets to save")
            return
        if not os.path.exists(DEST_DIR):
            os.makedirs(DEST_DIR)
        with open(self.output_file, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(Tweet._fields)
            writer.writerows([(tweet.id_str, tweet.created_at, tweet.text) for tweet in self._tweets])


if __name__ == "__main__":

    # for handle in ('pybites', 'techmoneykids', 'bbelderbos'):
    for handle in ('pybites', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
