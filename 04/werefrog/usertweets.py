import csv

from pathlib import Path

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET


DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100


class UserTweets(object):
    """
    - create a tweepy api interface
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory
    - implement len() an getitem() magic (dunder) methods"""

    _statuses = []

    def __init__(self, handle, max_id=None):
        self.handle = handle
        self.max_id = max_id
        self.output_file = Path(DEST_DIR, f"{self.handle}.{EXT}")
        self.authenticate()
        self.get_statuses()
        self.write_csv()

    def authenticate(self):
        self._auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self._auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self._api = tweepy.API(self._auth)

    def get_statuses(self):
        try:
            self._statuses = self._api.user_timeline(screen_name=self.handle, max_id=self.max_id, count=NUM_TWEETS)
        except tweepy.error.TweepError:
            self._statuses = []

    def write_csv(self):
        self.output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id_str', 'created_at', 'status'])
            writer.writerows([status.id_str.strip(), status.created_at, status.text.strip()] for status in self._statuses)

    def __len__(self):
        """Get number of statuses."""
        return len(self._statuses)

    def __getitem__(self, key):
        """Retrieve the statuses by index."""
        return self._statuses[key]


if __name__ == "__main__":

    for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
