from collections import namedtuple
import csv
import unittest
from unittest.mock import patch


from tweets import TWEETS  # mock data
from usertweets import UserTweets, NUM_TWEETS

HANDLE = 'pybites'
MAX_ID = '819831370113351680'

Tweet = namedtuple('Tweet', ['id_str', 'created_at', 'text'])


def read_csv(fname):
    with open(fname) as f:
        has_header = csv.Sniffer().has_header(f.readline())
        f.seek(0)
        r = csv.reader(f)
        if has_header:
            next(r, None)  # skip the header
        return [Tweet(*tw) for tw in r]  # list(r)


class TestUserTweets(unittest.TestCase):
    def setUp(self):
        super().setUp()
        with patch('tweepy.API.user_timeline') as mock_timeline:
            mock_timeline.return_value = TWEETS
            self.user = UserTweets(HANDLE, max_id=MAX_ID)

    def tearDown(self):
        self.user = None
        super().tearDown()

    def test_num_tweets(self):
        self.assertEqual(len(self.user), NUM_TWEETS)

    def test_first_tweet_returned_by_api(self):
        tw_n = 0
        self.assertEqual(self.user[tw_n].id_str, MAX_ID)
        self.assertEqual(self.user[tw_n].created_at, TWEETS[tw_n].created_at)
        self.assertEqual(self.user[tw_n].text, TWEETS[tw_n].text)

    def test_read_back_from_cached_csv(self):
        csv_tweets = read_csv(self.user.output_file)
        self.assertEqual(len(csv_tweets), NUM_TWEETS)
        tw_n = 0  # first
        self.assertEqual(csv_tweets[tw_n].id_str, MAX_ID)
        self.assertEqual(csv_tweets[tw_n].created_at,
                         str(TWEETS[tw_n].created_at))
        self.assertEqual(csv_tweets[tw_n].text, TWEETS[tw_n].text)
        tw_n = -1  # last
        self.assertEqual(csv_tweets[tw_n].text, TWEETS[tw_n].text)


if __name__ == "__main__":
    unittest.main()
