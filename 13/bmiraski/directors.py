from collections import defaultdict
from collections import namedtuple
import csv
import sqlite3
from statistics import mean
import unicodedata

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

db = sqlite3.connect('movies.db')

Movie = namedtuple('Movie', 'title year score')


def pop_movie_datebase():
    """Extract movies from csv and populate relevant data in db."""
    if db.execute("SELECT * from movies").fetchone() is None:
        with open(MOVIE_DATA, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            movies = [[row['director_name'], row['movie_title'],
                       row['title_year'], row['imdb_score']] for row in reader]
        for movie in movies:
            db.execute("""INSERT into movies
                       (director, movie_title, year, score)
                       VALUES (?, ?, ?, ?)""",
                       (movie[0], unicodedata.normalize("NFKD",
                        movie[1]).rstrip(),
                        movie[2], movie[3])
                       )
        db.commit()
    # head = list(db.execute("""SELECT * from movies""").fetchall())
    # print(head[0:5])
    # print(len(head))


def get_average_scores():
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    movies = list(db.execute("""SELECT * from movies""").fetchall())
    dir_count = defaultdict()
    for movie in movies:
        if movie[1] != '':
            if movie[1] not in dir_count:
                dir_count[movie[1]] = 1
            else:
                dir_count[movie[1]] += 1
    filter_movie = [movie for movie in movies if
                    movie[1] in dir_count and dir_count[movie[1]] > 3]

    filter_dir = [dir for dir in dir_count.keys() if dir_count[dir] > 3]

    dir_avg = defaultdict()

    for dir in filter_dir:
        davg = _calc_mean([movie for movie in filter_movie if movie[1] == dir])
        dir_avg[dir] = davg

    print(dir_avg['James Cameron'])
    print(dir_avg['Sam Mendes'])

def _calc_mean(movies):
    """Helper method to calculate mean of list of Movie namedtuples"""
    return mean([movie[4] for movie in movies])


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    # directors = get_movies_by_director()
    # directors = get_average_scores(directors)
    # print_results(directors)
    pop_movie_datebase()
    get_average_scores()


if __name__ == '__main__':
    main()
