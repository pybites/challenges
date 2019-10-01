import ssl

# TWITTER API KEYS - Get these keys from your twitter app
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
consumer_key = "3yRNSjK2EvlDPa91URqvx2UXh"
consumer_secret = "tTwbTLxkW4ee2hQPPJrN12IFZr4QKk9cxSG8pty5APAzwvwqTN"
access_token = "476723317-tAVQDJIgnyI92GPd0T9kwyUAimzHbbZccUX8doCC"
access_token_secret = "5CVyrH386j9psmckgwbzhMrHSta18vnL0wntjx7FGCxb1"
databasename = "tipdatabase.db"


LOCAL_CSV = 'daily-python-tip.csv'  # for testing
REMOTE_CSV = 'https://t.co/oARrOmrin7'
FIELDS = 'time code name email admin1 admin2 published'.split()
CONTEXT = ssl._create_unverified_context()
TEST = False


