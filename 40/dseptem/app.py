import json

from flask import Flask, send_from_directory
from flask_restful import reqparse, Resource, Api
from flask_cors import CORS
import requests
from apscheduler.schedulers.background import BackgroundScheduler

from scraper import retrieve_tweets

es_base_url = 'http://localhost:9200/tweets/tw'
api_base_url = '/api'

app = Flask(__name__)
CORS(app)  # required for Cross-origin Request Sharing
api = Api(app)

parser = reqparse.RequestParser()


@app.route('/')
def default():
    return send_from_directory('frontend', 'index.html')


@app.route('/<path:path>')
def serve_index(path):
    return send_from_directory('frontend', path)


class Tweet(Resource):
    def get(self, t_id):
        # the base URL for a "beers" object in Elasticsearch, e.g.
        # http://localhost:9200/tweets/tw/<t_id>
        url = es_base_url + '/' + t_id
        # query Elasticsearch
        resp = requests.get(url)
        data = resp.json()
        # Return the full Elasticsearch object as a result
        beer = data['_source']
        return beer

    def delete(self, t_id):
        # same as above
        url = es_base_url + '/' + t_id
        # Query Elasticsearch
        resp = requests.delete(url)
        # return the response
        data = resp.json()
        return data

# The API URLs all start with /api/v1, in case we need to implement different versions later
api.add_resource(Tweet, api_base_url + '/tweets/<t_id>')


class TweetList(Resource):
    def get(self):
        # same as above
        url = es_base_url + '/_search'
        # we retrieve all the beers (well, at least the first 100)
        # Limitation: pagination to be implemented
        query = {
            "query": {
                "match_all": {}
            },
            "size": 100
        }
        # query Elasticsearch
        resp = requests.post(url, data=json.dumps(query))
        data = resp.json()
        # build an array of results and return it
        tweets = []
        for hit in data['hits']['hits']:
            tweet = hit['_source']
            tweet['id'] = hit['_id']
            tweets.append(tweet)
        return tweets


api.add_resource(TweetList, api_base_url + '/tweets')


class Search(Resource):
    def get(self):
        # parse the query: ?q=[something]
        parser.add_argument('q')
        query_string = parser.parse_args()
        # base search URL
        url = es_base_url + '/_search'
        # Query Elasticsearch
        query = {
            "query": {
                "multi_match": {
                    "fields": ["text", "date", "tags"],
                    "query": query_string['q'],
                    "type": "cross_fields",
                    "use_dis_max": False
                }
            },
            "size": 100
        }
        resp = requests.post(url, data=json.dumps(query))
        data = resp.json()
        # Build an array of results
        tweets = []
        for hit in data['hits']['hits']:
            tweet = hit['_source']
            tweet['id'] = hit['_id']
            tweets.append(tweet)
        return tweets


api.add_resource(Search, api_base_url + '/search')

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(retrieve_tweets, 'cron', hour='4,20')
    scheduler.start()
    app.run(debug=True, use_reloader=False)
