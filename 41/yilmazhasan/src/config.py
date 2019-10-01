import ssl

# TWITTER API KEYS - Get these keys from your twitter app
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
databasename = "tipdatabase.db"


LOCAL_CSV = 'daily-python-tip.csv'  # for testing
REMOTE_CSV = 'https://t.co/oARrOmrin7'
FIELDS = 'time code name email admin1 admin2 published'.split()
CONTEXT = ssl._create_unverified_context()
TEST = False


