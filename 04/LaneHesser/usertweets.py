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


class UserTweets:
    # - save tweets to csv file in data/ subdirectory
    def __init__(self, handle, max_id=None):
        self.handle = handle
        self.max_id = max_id

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        self.api = tweepy.API(auth)
        self._tweets = self._get_tweets()
        self._save_tweets()

    def _get_tweets(self):
        tweets = self.api.user_timeline(id=self.handle,
                                        max_id=self.max_id,
                                        count=NUM_TWEETS)

        return [
                Tweet(tweet.id_str, tweet.created_at, tweet.text)
                for tweet in tweets
            ]

    def _save_tweets(self):
        try:
            os.mkdir(DEST_DIR)
        except FileExistsError:
            print("Directory already exists. Skipping directory creation.")

        path = f'{DEST_DIR}/{self.handle}.{EXT}'
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['id_str', 'created_at', 'text'])
            writer.writerows(self._tweets)

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, tweet):
        return self._tweets[tweet]


def main():
    for handle in ('pybites', 'juliansequeira', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()


if __name__ == "__main__":
    main()
