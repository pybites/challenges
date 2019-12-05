# Challenge 13
# - Parse the CSV using csv.DictReader
# - Grab director, title, year, and imdb score
# - Only consider directors with a minimum of four movies
# - Take movies where year >= 1960
# - Print top 20 highest rated directors w/ movies in desc order by rating

import csv
from statistics import mean
from collections import defaultdict, namedtuple

DATASET = 'movie_metadata.csv'
TOP_DIRS = 20
MOVIE_COUNT = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys = directors, and values = a list of movies (named tuples)'''
    storage = defaultdict(list)
    with open(DATASET) as data:
        extract = csv.DictReader(data)
        for row in extract:
            try:
                if int(row['title_year']) >= MIN_YEAR:
                    storage[row['director_name']].append(
                        Movie(title=row['movie_title'],
                              year=row['title_year'],
                              score=float(row['imdb_score'])))
            except ValueError:
                continue
        reduced_d = {k: v for k, v in storage.items() if len(v) >= MOVIE_COUNT}
    return reduced_d


def get_average_scores(directors):
    '''Reformat data, returning avg score of movies per director'''
    return {
        (director,  _calc_mean(movies)): movies
        for director, movies in directors.items()
    }


def _calc_mean(movies):
    '''Get average of movie scores for a given set'''
    return round(mean([movie.score for movie in movies]), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    counter = 0
    for (director_info, movies) in sorted(directors.items(), key=lambda key: key[0][1], reverse=True)[:TOP_DIRS]:
        name, avg_score = director_info
        counter += 1
        fmt_director_entry = '{counter}. {director:<52} {avg}'
        fmt_movie_entry = '{year}] {title:<50} {score}'
        sep_line = '-' * 60
        print(fmt_director_entry.format(counter=counter, director=name,
              avg=avg_score))
        print(sep_line)
        for movie in sorted(movies, key=lambda movie: movie.score,
                            reverse=True):
            print(fmt_movie_entry.format(year=movie.year, title=movie.title,
                                         score=movie.score))
        print("")


directors = get_movies_by_director()
directors = get_average_scores(directors)
print_results(directors)
