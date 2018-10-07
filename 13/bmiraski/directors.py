from collections import defaultdict
import csv
import sqlite3
from statistics import mean
import unicodedata

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

db = sqlite3.connect('movies.db')


def pop_movie_datebase():
    """Extract movies from csv and populate relevant data in db."""
    if db.execute("SELECT * from movies").fetchone() is None:
        with open(MOVIE_DATA, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            movies = [[row['director_name'], row['movie_title'],
                       row['title_year'], row['imdb_score']] for row in reader]
        for movie in movies:
            if movie[2] != '' and movie[0] != '':
                if int(movie[2]) >= MIN_YEAR:
                    if db.execute("""SELECT director, movie_title from movies
                                  WHERE director = ? AND movie_title = ?""",
                                  (movie[0], unicodedata.normalize("NFKD",
                                   movie[1]).rstrip())).fetchone() is None:
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

    db.execute("DROP TABLE IF EXISTS diravg")
    db.execute("""CREATE TABLE diravg (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        director TEXT NOT NULL,
        avg FLOAT NOT NULL
    )""")
    db.commit()

    for dir in dir_avg:
        db.execute("""INSERT INTO diravg (director, avg) VALUES (?, ?)""",
                   (dir, dir_avg[dir]))
        db.commit()

    # check = db.execute("SELECT * from diravg")
    # print(list(check)[0:5])


def _calc_mean(movies):
    """Helper method to calculate mean of list of Movie namedtuples"""
    return mean([movie[4] for movie in movies])


def print_results():
    """Print directors ordered by highest average rating.

    For each director print his/her movies also ordered by highest rated movie.
    """
    fmt_director_entry = '{counter}. {director:<53} {avg:.1f}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60

    directors = list(db.execute("""SELECT * FROM diravg ORDER BY avg DESC"""
                                ).fetchall())

    directors = directors[0:20]

    counter = 0
    for director in directors:
        counter += 1
        print(fmt_director_entry.format(counter=counter, director=director[1],
                                        avg=director[2]))
        print(sep_line)
        movies = list(db.execute("""SELECT * from movies WHERE director = ?
                            ORDER BY score DESC""", (director[1], )).fetchall())
        for movie in movies:
            print(fmt_movie_entry.format(year=movie[3], title=movie[2],
                                         score=movie[4]))
        print('\n')


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    # directors = get_movies_by_director()
    # directors = get_average_scores(directors)
    # print_results(directors)
    pop_movie_datebase()
    get_average_scores()
    print_results()

if __name__ == '__main__':
    main()
