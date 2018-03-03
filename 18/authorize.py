import os
import pickle

from rauth.service import OAuth1Service, OAuth1Session

CONSUMER_KEY = os.environ.get('GR_KEY')
CONSUMER_SECRET = os.environ.get('GR_SECRET')
SESSION = 'session' 

def authorize():
    goodreads = OAuth1Service(
	consumer_key=CONSUMER_KEY,
	consumer_secret=CONSUMER_SECRET,
	name='goodreads',
	request_token_url='http://www.goodreads.com/oauth/request_token',
	authorize_url='http://www.goodreads.com/oauth/authorize',
	access_token_url='http://www.goodreads.com/oauth/access_token',
	base_url='http://www.goodreads.com/'
	)

    request_token, request_token_secret = goodreads.get_request_token(header_auth=True)

    authorize_url = goodreads.get_authorize_url(request_token)
    print('Visit this URL in your browser: ' + authorize_url)
    accepted = 'n'
    while accepted.lower() == 'n':
        # you need to access the authorize_link via a browser,
        # and proceed to manually authorize the consumer
        accepted = input('Have you authorized me? (y/n) ')

    session = goodreads.get_auth_session(request_token, request_token_secret)
    pickle.dump(session, open(SESSION, "wb"))
    return session

