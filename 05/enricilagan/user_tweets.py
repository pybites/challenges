from collections import namedtuple
import csv

import tweepy

from config import TWITTER_KEY, TWITTER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

EXT = 'csv'
NUM_TWEETS = 200

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

Tweet = namedtuple('Tweet', 'id created text')


class UserTweets(object):
    def __init__(self, user_handle, max_id=None):
        """ TODO 1: create a tweepy api interface
        TODO 3: optionally get up until 'max_id' tweet id"""
        self.api = tweepy.API(auth)
        self.handle = user_handle
        self.max_id = max_id
        # self._file = f'{user_handle}.{EXT}'

        self._tweets = list(self._get_tweets())
        # self._save_tweets()

    def _get_tweets(self):
        """TODO 2: get all tweets for passed in handle"""
        tweets = self.api.user_timeline(screen_name=self.handle, max_id=self.max_id,
                                        count=NUM_TWEETS)

        for tweet in tweets:
            yield Tweet(tweet.id, tweet.created_at, tweet.text)

    def _save_tweets(self):
        """TODO 4: save tweets to csv file in data/ subdirectory"""
        with open(self._file, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=Tweet._fields)
            writer.writeheader()
            writer.writerows([tweet._asdict() for tweet in self._tweets])

    def __len__(self):
        """TODO 5: implement len() an getitem() magic (dunder) methods"""
        """See http://pybit.es/python-data-model.html"""
        return len(self._tweets)

    def __getitem__(self, pos):
        return self._tweets[pos]


if __name__ == "__main__":
    # noinspection SpellCheckingInspection
    handle = 'creingalain'
    print('--- {} ---'.format(handle))
    user = UserTweets(handle)
    for tw in user[:5]:
        print(tw)
    print()
