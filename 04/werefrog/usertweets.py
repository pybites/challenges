import argparse
import csv
import logging
import os

from collections import namedtuple
from operator import attrgetter
from pathlib import Path
from types import SimpleNamespace

import tweepy


# ======================================================================
# Settings
# ======================================================================

try:
    import config as settings
except ModuleNotFoundError:
    # No config module, read environment variables
    settings = SimpleNamespace()
    settings.CONSUMER_KEY = os.getenv("TWITTER_API_KEY")
    settings.CONSUMER_SECRET = os.getenv("TWITTER_API_SECRET")
    settings.ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    settings.ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")


settings.LOG_FORMAT = '%(asctime)s %(levelname)s - %(name)s - %(message)s'
settings.LOG_PATH = Path(__file__).parent.joinpath("logs", "logs.log")
settings.LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

settings.DEFAULT_HANDLES = ('pybites', '_juliansequeira', 'bbelderbos')


# ======================================================================
# Loggers
# ======================================================================

logging.basicConfig(
    handlers=[
        logging.FileHandler(filename=settings.LOG_PATH, encoding='utf8', mode='a')
    ],
    format=settings.LOG_FORMAT,
    level=logging.DEBUG
)


# ======================================================================
# Definitions
# ======================================================================

CSV_DIR = Path('data')
CSV_DIR.mkdir(parents=True, exist_ok=True)

NUM_TWEETS = 100


Tweet = namedtuple('Tweet', ['id_str', 'created_at', 'text'])


class UserTweets:
    """
    - create a tweepy api interface
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory
    - implement len() an getitem() magic (dunder) methods"""

    def __init__(self, handle, max_id=None):
        self.tweets = []
        self.handle = handle
        self.max_id = max_id
        self.output_file = CSV_DIR.joinpath(f"{self.handle}.csv")
        self.refresh()
        self.write_csv()

    def __repr__(self):
        return f"<{type(self).__name__} handle='{self.handle}'>"

    def __len__(self):
        """Get number of tweets."""
        return len(self.tweets)

    def __getitem__(self, key):
        """Retrieve the tweets by index."""
        return self.tweets[key]

    def refresh(self):
        """Use API to get user's timeline and update self.tweets."""
        auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
        auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
        api = tweepy.API(auth)

        kwargs = {
            'screen_name': self.handle,
            'max_id': self.max_id,
            'count': NUM_TWEETS
        }
        try:
            self.tweets = [
                Tweet(*attrgetter(*Tweet._fields)(status))
                for status in api.user_timeline(**kwargs)
            ]
        except tweepy.error.TweepError:
            logging.warning(f"{self}: Refreshing user's timeline... FAILED")

    def write_csv(self):
        with self.output_file.open('w', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(Tweet._fields)
            writer.writerows(self.tweets)


# ======================================================================
# Main
# ======================================================================

def main(handle):
    user = UserTweets(handle)

    title = f"( {handle} )"
    print(f"\n{title:=^80}")

    for status in user[:5]:
        print(status)


# ======================================================================
# Standalone
# ======================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--users', nargs='+', help='<Optional> Users')
    args = parser.parse_args()

    handles = args.users if args.users else settings.DEFAULT_HANDLES

    for handle in handles:
        main(handle)
