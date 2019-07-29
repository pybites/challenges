import requests
import random
import pprint


def get_random_movie() -> dict:
    usable_movie = False
    movie_json = {}

    random.seed()
    while usable_movie is not True:
        random_id = int(random.random() * 9916754)
        random_imdb_title_id = f"tt{random_id}"
        print(f"random IMDB title ID: {random_imdb_title_id}")
        movie_params = {'apikey': '16bf123d', 'i': random_imdb_title_id}

        req = requests.get("http://www.omdbapi.com", movie_params)

        movie_json: dict = req.json()

        # Filter out obscure titles for which no info is known.
        if ("Type" not in movie_json) or (movie_json['Type'] is not "movie"):
            continue

    return movie_json


if __name__ == "__main__":
    mj = get_random_movie()
    print(f"Title: {mj['Title']}")
    pprint.pprint(mj)
