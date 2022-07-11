import ssl
import os

# TWITTER API KEYS - Get these keys from your twitter app
consumer_key = os.environ.get("consumer_key") or ""
consumer_secret = os.environ.get("consumer_secret") or ""
access_token = os.environ.get("access_token") or ""
access_token_secret = os.environ.get("access_token_secret") or ""

databasename = "tipdatabase.db"


LOCAL_CSV = 'daily-python-tip.csv'  # for testing
REMOTE_CSV = 'https://t.co/oARrOmrin7'
FIELDS = 'time code name email admin1 admin2 published'.split()
CONTEXT = ssl._create_unverified_context()
TEST = False


