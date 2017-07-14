import requests
import os
import argparse
import datetime


class MovieError(Exception):

    def __init__(self, reason, response=None):
        self.reason = reason
        self.response = response
        Exception.__init__(self, reason)

    def __str__(self):
        return self.reason


class Movie:

    def __init__(self):
        self.id = None
        self.original_title = None
        self.title = None
        self.popularity = None
        self.release_date = None

    def __repr__(self):
        return f"{self.original_title} ({self.release_date})"


def map_movie(movie_resource=None):

    if movie_resource is None:
        raise MovieError('invalid movie resource')

    movie = Movie()
    movie.id = movie_resource['id']
    movie.original_title = movie_resource['original_title']
    movie.title = movie_resource['title']
    movie.popularity = movie_resource['popularity']
    movie.release_date = movie_resource['release_date']
    return movie


class Api(object):

    def __init__(self, api_key=None):

        if api_key is None:
            raise MovieError('api key is mandatory')

        self.key = api_key

    def _url(self, path):
        return 'https://api.themoviedb.org/3/' + path

    def get_movies(self, year=None, genre=None, voteaverage=None):
        upcoming_movies_url = self._url('discover/movie')

        query_params = {
            'api_key': self.key,
            'page': 1
        }

        if year:
            query_params['year'] = year

        if genre:
            query_params['with_genres'] = genre

        if voteaverage:
            query_params['vote_average.gte'] = voteaverage

        movies_resp = requests.get(upcoming_movies_url, params=query_params)

        if movies_resp.status_code != 200:
            raise MovieError(reason=movies_resp.reason, response=movies_resp)

        json = movies_resp.json()
        movies = [map_movie(m) for m in json['results']]

        if json['total_pages'] > 1:

            for x in range(2, json['total_pages'] + 1):
                query_params['page'] = x
                movies_resp = requests.get(upcoming_movies_url, params=query_params)
                json = movies_resp.json()
                movies += [map_movie(m) for m in json['results']]

        return movies


def send_email(api_key, domain_name, from_email, to_email, movies):

    html_body = "<html><body><h1>Upcoming Movies</h1><ul>"
    html_body += "".join([f"<li>{repr(m)}</li>" for m in movies])
    html_body += "</ul></body></html>"

    requests.post(
        f"https://api.mailgun.net/v3/{domain_name}/messages",
        auth=("api", api_key),
        data={"from": f"Mailgun Sandbox <{from_email}>",
              "to": to_email,
              "subject": "Upcoming movies",
              "html": html_body})


# Movies api key
key = os.getenv("MOVIEDB_KEY")
# ------

# MailGun configuration
mailgun_key = os.getenv("MAILGUN_KEY")
to_email = "abcd12345@mailinator.com"
domain_name = os.getenv("MAILGUN_DOMAIN")
from_email = f"postmaster@{domain_name}"
# ------

# Configuring available inputs
parser = argparse.ArgumentParser()
parser.add_argument("--genre",
                    help="""A coma separated list of the genre ids, 
                    examples: 28-Action, 27-Horror, 14-Fantasy, etc""")
parser.add_argument("--year",
                    help="""A filter to limit the results to a specific year 
                    (looking at all release dates). Default is current year""")
parser.add_argument("--voteaverage",
                    help="""Filter and only include movies that have a rating 
                    that is greater or equal to the specified value.""")
args = parser.parse_args()

if not args.year:
    args.year = datetime.datetime.now().year

api = Api(key)
movies = api.get_movies(args.year, args.genre, args.voteaverage)

send_email(mailgun_key, domain_name, from_email, to_email, movies)
