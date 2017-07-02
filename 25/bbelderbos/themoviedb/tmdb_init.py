import os
import sys

import tmdbsimple as tmdb

key = os.environ.get('THE_MOVIE_DB_API_KEY')

if not key:
    print('Set themoviedb API_KEY in your env')
    print('export THE_MOVIE_DB_API_KEY=xyz')
    sys.exit(1)

tmdb.API_KEY = key
