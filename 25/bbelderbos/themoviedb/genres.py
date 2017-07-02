import os
import pickle

from .tmdb_init import tmdb

CACHE = 'genres.pkl'


def cache_genres():
    gen = tmdb.Genres()
    genres = gen.list()

    genres = {g['id']: g['name'] for g in genres['genres']}

    with open(CACHE, 'wb') as f:
        pickle.dump(genres, f)


def get_genres_cache():
    if not os.path.isfile(CACHE):
        print('Cache file not found, generating one')
        cache_genres()

    with open(CACHE, 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    if os.path.isfile(CACHE):
        os.remove(CACHE)

    genres = get_genres_cache()

    from pprint import pprint as pp
    pp(genres)
