import os
import pickle
from pprint import pprint as pp
import sys
import xml.dom.minidom
import xmltodict

from goodreads import client

from authorize import authorize

CONSUMER_KEY = os.environ.get('GR_KEY')
CONSUMER_SECRET = os.environ.get('GR_SECRET')
SESSION = 'session' 

try:
    session = pickle.load(open(SESSION, "rb"))
except FileNotFoundError:
    session = authorize()

ACCESS_TOKEN = session.access_token
ACCESS_TOKEN_SECRET = session.access_token_secret

gc = client.GoodreadsClient(CONSUMER_KEY, CONSUMER_SECRET)
gc.authenticate(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

resp = session.get("/updates/friends.xml")
#xml_out = xml.dom.minidom.parseString(resp.content)
d = xmltodict.parse(resp.content)
pp(d)
