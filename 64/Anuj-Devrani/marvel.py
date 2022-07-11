import asyncio
import hashlib  # needed for API auth
import json  # use dumps and loads
from typing import IO
import os
from time import sleep  # between API pagination calls

import requests
import json
import pathlib
import sys
import argparse

# Async calls
import aiohttp
import aiofiles
from aiohttp import ClientSession


# get from marvel developer account:
PUBLIC_KEY = os.environ['PUBLIC_KEY']
PRIVATE_KEY = os.environ['PRIVATE_KEY']

# https://developer.marvel.com/documentation/authorization
# "Authentication for Server-Side Applications" section
ENDPOINT = ('https://gateway.marvel.com:443/v1/public/{endpoint}?ts=1&'
            'apikey={public_key}&hash={hash_}')

# https://developer.marvel.com/docs
MARVEL_OBJECTS = 'characters comics creators events series stories'.split()


def get_api_endpoint(endpoint: str) -> str:
    """Helper function to form a valid API endpoint (use ENDPOINT)"""
    time_stamp = '1'
    secret = time_stamp + PRIVATE_KEY + PUBLIC_KEY
    result = hashlib.md5(secret.encode('utf-8'))
    digest = result.hexdigest()

    return ENDPOINT.format(endpoint=endpoint, public_key=PUBLIC_KEY, 
                            hash_=digest)


def initial_call_to_marvel(filename: str, endpoint:str) -> (list):
    """This function performs the initial call to marvel to get the total no of results and the paginated urls"""
    # Get list of comics
    ENDPOINT = get_api_endpoint(endpoint)
    offset = 0
    ENDPOINT = ENDPOINT + '&' + 'limit=10'
    response = requests.get(url=ENDPOINT.format(endpoint=endpoint))

    url_list = []
    if response.ok:
        res = response.json()
        with open(filename, 'w') as file:
            json.dump(res['data'], file)
            file.write('\n')
        # Collect all the results
        TOTAL_RESULTS = res['data']['total']
        TOTAL_PAGES = round(TOTAL_RESULTS/10)

        for page in range(1, TOTAL_PAGES):
            offset = page * 10
            url = ENDPOINT + '&offset=' + str(offset)
            url_list.append(url)
        return url_list
    else:
        print('Error Contacting Marvel Base')
        raise Exception


async def fetch_data(url: str, session: ClientSession, **kwargs) -> str:
    """GET request wrapper to fetch page HTML.

    kwargs are passed to `session.request()`.
    """

    resp = await session.request(method="GET", url=url, **kwargs)
    resp.raise_for_status()
    print("Got response for URL: %s", url)
    res = await resp.json()
    res = res['data']
    return json.dumps(res)


async def write_one(file: IO, url: str, **kwargs) -> None:
    """Write the found HREFs from `url` to `file`."""
    res = await fetch_data(url=url, **kwargs)
    if not res:
        return None
    async with aiofiles.open(file, "a") as f:
        res = res + '\n'
        await f.write(res)
        print("Wrote results URL: %s", url)


async def bulk_crawl_and_write(file: IO, urls: list, **kwargs) -> None:
    """Crawl & write concurrently to `file` for multiple `urls`."""
    semaphore = asyncio.Semaphore(15)
    async with semaphore:
        async with ClientSession() as session:
            tasks = []
            for url in urls:
                tasks.append(
                    write_one(file=file, url=url, session=session, **kwargs)
                )
            await asyncio.gather(*tasks)


if __name__ == '__main__':
    # 1. cache API data
    # 2. load JSON file(s) and build awesome graphs

    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    here = pathlib.Path(__file__).parent

    # To run the file pass the desired enpoint
    # choices are -> 'characters comics creators events series stories'
    # >>> python marvel.py -endpoint=<choice>
    parser = argparse.ArgumentParser()
    parser.add_argument('-endpoint', action='store', dest='endpoint', help='pass the selected enpoint')
    arguments = parser.parse_args()
    endpoint = arguments.endpoint

    filepath = here.joinpath("{}.json".format(endpoint))

    urls_list = initial_call_to_marvel(filepath, endpoint)
    asyncio.run(bulk_crawl_and_write(file=filepath, urls=urls_list))

