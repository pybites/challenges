import hashlib
import json
import os
from time import sleep
from pathlib import Path

import requests

public_key = os.environ['PUBLIC_KEY']
private_key = os.environ['PRIVATE_KEY']

output_dir = Path('data')
Path.mkdir(output_dir, exist_ok=True)

endpoints = 'characters comics creators events series stories'.split()


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


def get_data(endpoints=endpoints):
    """Helper function to loop over the endpoints saving the data
       in  output_dir, you probably want to use json.dump
    """
    pass


if __name__ == '__main__':
    get_data()
