import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

class Tweets(object):

    def __init__(self, handle):
        self.handle = handle
        self._tweets = self._your_turn()

    def _your_turn(self):
        pass # code ...
