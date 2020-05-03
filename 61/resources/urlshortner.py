from flask_restful import Resource, request

import backoff
import json
import logging
import requests
import sys

from models.url import UrlModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UrlShortner(Resource):

    @classmethod
    def get(cls):
        data = request.get_json()
        long_url = data.get('url', None)
        url = UrlModel.get_item_by_url(long_url)
        if url:
            return {"url": url.to_json()}, 200
        else:
            return {"message": "{} not found".format(long_url)}, 404  # Url not found

    @classmethod
    def post(cls):
        data = request.get_json()
        long_url = data.get('url', None)
        url = UrlModel.get_item_by_url(long_url)
        if url:
            return {"url": url.to_json()}, 400 # url already existing
        else:
            if long_url and len(long_url.strip()):
                bitlyapi = BitlyApi(access_token='395fd04d700718f8a3fbbd3d5c67f9ed1b1ad3d4')
                shorten_url = bitlyapi.get_shortend_url(long_url)
                data = UrlModel(long_url, shorten_url['link'])
                try:
                    data.save_to_db()
                except Exception as e:
                    return {"message": "An error occured while inserting".format(e)}, 500 # Intenral Error
                return {"url": "shorturl {}".format(shorten_url.get('link'))}, 200
            else:
                return {"message": "URL cannot be spaces, empty"}, 201


class BitlyApi():
    def __init__(self, access_token):

        self.ACCESS_TOKEN = access_token

    @backoff.on_exception(backoff.expo, requests.exceptions.ConnectionError, max_time=10)
    @backoff.on_exception(backoff.expo, requests.exceptions.ConnectTimeout, max_tries=5, factor=5)
    @backoff.on_exception(backoff.expo, requests.exceptions.HTTPError, max_tries=5, factor=5)
    def get_shortend_url(self, long_url):

        endpoint = 'https://api-ssl.bitly.com/v4/shorten'
        headers = {'Authorization': 'Bearer {}'.format(self.ACCESS_TOKEN), 'Content-Type': 'application/json'}

        data = {"domain": "bit.ly", "long_url": long_url}
        response = requests.post(url=endpoint, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            logging.error(response.status_code)
            logging.error(json.loads(response.content.decode('utf-8')))
            sys.exit()
