import requests
import random
# You'll need to create a file named config.py containing a line like: apikey="<your_api_key>"
from config import apikey

# Random OMDB title picker.


def generate_random_imdb_id():
    # This is the highest IMDB title id at time of writing. This stinks. Wish I had a better way to
    # dynamically set this!
    max_imdb_title_number = 9916754
    random.seed()
    random_id = int(random.random() * max_imdb_title_number)
    return f"tt{random_id}"


def make_omdb_request(imdb_title_id):
    movie_params = {'apikey': apikey, 'i': imdb_title_id}
    return requests.get("http://www.omdbapi.com", movie_params)


def get_random_movie() -> dict:
    usable_movie = False
    movie_json = {}

    while True:
        random_imdb_title_id = generate_random_imdb_id()
        req = make_omdb_request(random_imdb_title_id)
        movie_json: dict = req.json()
        if movie_json['Response'] == "True":
            break
    return movie_json


if __name__ == "__main__":
    movie_json = get_random_movie()

    for field in movie_json.keys():
        if movie_json[field] != "N/A":
            print(f"{field}: {movie_json[field]}")
