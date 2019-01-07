#!/usr/bin/env python3
"""
Challenge 13:

- parse movie_metadata.csv
- get 20 highest rated directors based on mean movie ratings
- director must have >= 4 titles
- all movies >= 1960
"""

import csv
from collections import namedtuple, defaultdict
from statistics import mean

Movie = namedtuple('Movie', 'title year score')
Directors = namedtuple('Directors', 'info avg')

FILE = 'movie_metadata.csv'
DIRECTORS = 21
YEAR = 1960
MOVIES = 4


def main():
    directors = get_movies_by_director()
    updated = get_average_scores(directors)
    printer(updated)


def get_movies_by_director():
    """Extracts all movies and directors from CSV.

    :return movie_data: data structure containing all movie info for each
    director.
    """

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


def get_average_scores(directors):
    """Take each movies average score from csv.

    :param directors: data struct containing all movies from each director.
    :return updated_directors: returns directors that meet criteria.
    """
    updated_directors = defaultdict(list)
    for key, movies in directors.items():
        if len(movies) >= 4:
            avg = _calc_mean(movies)
            updated_directors[key].append(Directors(info=movies, avg=avg))
    return updated_directors


def _calc_mean(movies):
    """Given a list of movies from the same director calculate their mean
    rating.

    :arg movies: average scores from all movies.
    :return avg: directors mean rating from all movies.
    """
    avg = mean([movie.score for movie in movies])
    return avg


def printer(updated_directors):
    """Prints out top 20 directors according to their average IMDB score,
    including all their movies, by year and score for that movie.

    :param updated_directors: defaultdict
    """
    fmt_director_entry = '{counter}. {director:<52} {avg:.1f}'
    fmt_movie_entry = '[{year}] {title:<50} {score}'
    sep_line = '-' * 60
    counter = 1
    for director, info in sorted(updated_directors.items(),
                                 key=lambda x: x[1][0].avg, reverse=True):
        if counter < DIRECTORS:
            print(fmt_director_entry.format(counter=counter, director=director,
                                            avg=info[0].avg))
            print(sep_line)
            for movie in info:
                for item in movie[0]:
                    print(fmt_movie_entry.format(year=item.year,
                                                 title=item.title,
                                                 score=item.score))
            counter += 1
            print(sep_line)


if __name__ == '__main__':
    main()
