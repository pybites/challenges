import csv
from collections import defaultdict, namedtuple
from statistics import mean
from operator import itemgetter
MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(MOVIE_DATA, encoding='utf-8') as f:
        for row in csv.DictReader(f):
            try:
                if int(row['title_year']) >= MIN_YEAR:
                   directors[row['director_name']].append(
                        Movie(
                            title=row['movie_title'].replace("\xa0", ""),
                            year=int(row['title_year']),
                            score=float(row['imdb_score'])
                        )
                    )
            except ValueError:
                continue
    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate average score'''
    return {
        (director,  _calc_mean(movies)): movies
        for director, movies in directors.items()
        if len(movies) >= MIN_MOVIES
    }


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(mean([movie.score for movie in movies]),1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    counter = 0
    for (dirplusavg, movies) in sorted(directors.items(), key=itemgetter(1), reverse=True)[:NUM_TOP_DIRECTORS]:
        director, avg = dirplusavg
        counter += 1
        fmt_director_entry = '{counter}. {director:<52} {avg}'
        fmt_movie_entry = '{year}] {title:<50} {score}'
        sep_line = '-' * 60
        print(fmt_director_entry.format(counter=counter, director=director, avg=avg))
        print(sep_line)
        for movie in sorted(movies, key=lambda movie: movie.score, reverse=True):
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
        print("")

def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    pass

print_results(get_average_scores(get_movies_by_director()))
