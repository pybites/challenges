import csv
import datetime
import os
import unittest
from unittest.mock import patch

from usertweets import UserTweets, NUM_TWEETS, Tweet, DEST_DIR, EXT
from nose.tools import assert_is_not_none

DT = ''
HANDLE = 'pybites'
MAX_ID = '819831370113351680'
TWEETS = ()


def get_tweet_list():
    global DT, TWEETS
    fname = os.path.join(DEST_DIR, 'pybites_tweets' + '.' + EXT)
    csv_tweets = read_csv(fname)
    tweets = [Tweet(tw[0], tw[1], tw[2]) for tw in csv_tweets]
    DT = tweets[0].created_at
    TWEETS = (tweets[0].text, tweets[-1].text)
    return tweets


def read_csv(fname):
    with open(fname) as f:
        has_header = csv.Sniffer().has_header(f.readline())
        f.seek(0)
        r = csv.reader(f)
        if has_header:
            next(r, None)  # skip the headers
        return list(r)


class TestUserTweets(unittest.TestCase):
    def setUp(self):
        super().setUp()
        with patch('usertweets.UserTweets.tweets_list') as mock_tweets_list:
            mock_tweets_list.return_value = get_tweet_list()
            self.user = UserTweets(HANDLE, max_id=MAX_ID)

    def tearDown(self):
        self.user = None
        super().tearDown()

    def test_num_tweets(self):
        self.assertEqual(len(self.user), NUM_TWEETS)

    def test_first_tweet_returned_by_api(self):
        self.assertEqual(self.user[0].id_str, MAX_ID)
        self.assertEqual(self.user[0].created_at, DT)
        self.assertEqual(self.user[0].text, TWEETS[0])

    def test_read_back_from_cached_csv(self):
        csv_tweets = read_csv(self.user.output_file)
        self.assertEqual(len(csv_tweets), NUM_TWEETS)
        self.assertEqual(csv_tweets[0][0], MAX_ID)
        self.assertEqual(csv_tweets[0][1], str(DT))
        self.assertEqual(csv_tweets[0][2], TWEETS[0])
        self.assertEqual(csv_tweets[-1][2], TWEETS[1])


if __name__ == "__main__":
    unittest.main()
