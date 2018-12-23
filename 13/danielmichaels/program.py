"""
Challenge 13:

- parse movie_metadata.csv
- get 20 highest paid directors based on mean movie ratings
- director must have >= 4 titles
- all movies >= 1960
- run tests before commit
"""

import csv
from collections import namedtuple, defaultdict
from statistics import mean

Movie = namedtuple('Movie', 'title year score')

FILE = 'movie_metadata.csv'
DIRECTORS = 20
YEAR = 1960
MOVIES = 4


def main():
    directors = movies_by_director()
    updated = average_scores(directors)
    print(updated)


def movies_by_director():
    """Extracts all movies and directors from CSV.

    :return: data structure containing all movie info for each director."""

    movie_data = defaultdict(list)
    with open(FILE, 'r') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            try:
                director = row['director_name']
                if int(row['title_year']) >= YEAR:
                    title = row['movie_title'].strip()
                    score = float(row['imdb_score'])
                    year = int(row['title_year'])
                    movie_data[director].append(Movie(title=title,
                                                      score=score,
                                                      year=year))
            except ValueError:
                continue

    return movie_data


def average_scores(director):
    """Take each movies average score from csv.

    :param director: data struct containing all movies from each directo.
    :return: returns directors that meet criteria.
    """


def calc_mean(movies):
    """Given a list of movies from the same director calculate their mean
    rating.

    :arg movies: average scores from all movies.
    :return: directors mean rating from all movies.
    """


if __name__ == '__main__':
    main()
