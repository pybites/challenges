from hashlib import md5  # needed for API auth
from urllib import request
from pathlib import Path
import json  # use dumps and loads
import os
from time import sleep, time  # between API pagination calls
from exception_handling import handle_exceptions

import settings
# import requests  # call Marvel API

# get from marvel developer account:
PUBLIC_KEY = os.environ['PUBLIC_KEY']
PRIVATE_KEY = os.environ['PRIVATE_KEY']
CACHE_DIR = os.environ['CACHE_DIR']

# https://developer.marvel.com/docs
MARVEL_OBJECTS = 'characters comics creators events series stories'.split()

def get_api_endpoint(endpoint):
    """generate valid endpoint url based on
    https://developer.marvel.com/documentation"""

    # if id != -1:
    #     endpoint += f'/{id}'
    #     if extra:
    #         endpoint += f'/{extra}'

    # calculate endpoint based on optional parameters
    # endpoint = f'{endpoint}/{id}/{extra}'
    time_stamp = round(time())
    hash_data = f'{time_stamp}{PRIVATE_KEY}{PUBLIC_KEY}'.encode('utf-8')
    hash_ = md5(hash_data).hexdigest()
    return f'https://gateway.marvel.com:443/v1/public/' \
           f'{endpoint}?ts={time_stamp}' \
           f'&apikey={PUBLIC_KEY}&hash={hash_}'

@handle_exceptions
def get_cache_marvel_data(endpoint):
    """Helper function to cache Marvel API JSON data to file"""
    if endpoint not in MARVEL_OBJECTS:
        raise ValueError('Invalid value for endpoint or extra')
    # if extra:
    #     if extra not in MARVEL_OBJECTS:
    #         raise ValueError('Invalid value for endpoint or extra')

    data = None
    cache_filename = Path(CACHE_DIR, f'cache_{endpoint}')
    if cache_filename.exists():
        with open(cache_filename) as cache_file:
            data = cache_file.read()
        return json.loads(data)

    endpoint = get_api_endpoint(endpoint)
    with request.urlopen(endpoint) as f:
        data = json.loads(f.read())
    
    with open(cache_filename, 'w') as f:
        json.dump(data, f)
    return data

if __name__ == '__main__':
    # 1. cache API data
    # 2. load JSON file(s) and build awesome graphs
    data = get_cache_marvel_data('comics')
