import collections
import tweepy
import csv
import os


DATA_DIR = 'data'
NUM_TWEETS = 100
FIELD_NAMES = 'id_str created_at text'.split()

try:
    os.mkdir(DATA_DIR)
except FileExistsError:
    pass

Tweet = collections.namedtuple('Tweet', FIELD_NAMES)


class UserTweets:
    CONSUMER_KEY = os.environ['cs_key']
    CONSUMER_SECRET = os.environ['cs_secret']
    ACCESS_TOKEN = os.environ['acc_token']
    ACCESS_TOKEN_SECRET = os.environ['acc_secret']

    AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    API = tweepy.API(AUTH)

    def __init__(self, user, **kwargs):
        _cursor = tweepy.Cursor(
            self.API.user_timeline,
            tweet_mode='extended',
            id=user,
            **kwargs
        )

        self.tweets = []
        try:
            self.tweets = [
                Tweet(id_str=item.id_str, created_at=item.created_at, text=item.full_text)
                for item in list(_cursor.items(NUM_TWEETS))
            ]

            csv_file = f"{user}.csv"
            csv_file = os.path.join(DATA_DIR, csv_file)

            with open(csv_file, "w", newline='') as f:
                fieldnames = FIELD_NAMES
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(tweet._asdict() for tweet in self.tweets)
        except tweepy.TweepError as e:
            print(f"Error: {e}")

    def __len__(self):
        return len(self.tweets)

    def __getitem__(self, index):
        return self.tweets[index]







