import hashlib  # needed for API auth
import json
import os
from time import sleep  # between API pagination calls

import requests

# get from marvel developer account:
public_key = os.environ['PUBLIC_KEY']
private_key = os.environ['PRIVATE_KEY']

ENDPOINTS = 'characters comics creators events series stories'.split()


# recommended prep work

def get_data_from_marvel_api_endpoint(endpoint):
    """Helper function to get data from the Marvel API:

       https://gateway.marvel.com:443/v1/public/{endpoint}

       See: https://developer.marvel.com/documentation/authorization
       "Authentication for Server-Side Applications" section
       -> you will need to hash ts, public and private key, use hashlib

       Endpoints: https://developer.marvel.com/docs

       Return the response json object.
    """
    ts = 1


if __name__ == '__main__':
    your_endpoint = ''  # one of ENDPOINTS
    get_data_from_marvel_api_endpoint(your_endpoint)
