import hashlib  # needed for API auth
import json  # use dumps and loads
import os
from time import sleep  # between API pagination calls

import requests  # call Marvel API

# get from marvel developer account:
PUBLIC_KEY = os.environ['PUBLIC_KEY']
PRIVATE_KEY = os.environ['PRIVATE_KEY']

# https://developer.marvel.com/documentation/authorization
# "Authentication for Server-Side Applications" section
ENDPOINT = ('https://gateway.marvel.com:443/v1/public/{endpoint}?ts=1&'
            'apikey={public_key}&hash={hash_}')

# https://developer.marvel.com/docs
MARVEL_OBJECTS = 'characters comics creators events series stories'.split()


def get_api_endpoint():
    """Helper function to form a valid API endpoint (use ENDPOINT)"""
    pass


def cache_marvel_data():
    """Helper function to cache Marvel API JSON data to file"""
    pass


if __name__ == '__main__':
    # 1. cache API data
    # 2. load JSON file(s) and build awesome graphs
    pass
