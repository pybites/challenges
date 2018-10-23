#!/usr/bin/env python3
import collections
import csv
import os

CSV_FILENAME = 'movie_metadata.csv'
METADATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), CSV_FILENAME)
MOVIE_MIN = 4
YEAR_MIN = 1960
TOP_DIRECTORS = 20
Movie = collections.namedtuple('Movie', 'title year score')


def main():
    directors = collect_director_data()
    directors = collect_director_avg_scores(directors)


def collect_director_avg_scores(directors):
    return {
        (director, _get_average(movies)): movies
        for director, movies in directors.items()
    }


def _get_average(movies):
    all_scores = [movie.imdb_score for movie in movies]
    return round(sum(all_scores) / max(1, len(all_scores)), 1)


def collect_director_data():
    directors = collections.defaultdict(list)
    for row in _row_in_csv():
        try:
            director = row.get('director_name')
            movie = row.get('movie_title')
            year = int(row.get('year', 0))
            score = float(row.get('imdb_score'))
        except ValueError:
            continue
        if year < 1960:
            continue

        directors[director].append(Movie(title=movie, year=year, score=score))
    return _remove_movie_min_not_met(directors)


def _remove_movie_min_not_met(directors):
    for director in directors:
        if len(directors.get(director)) < MOVIE_MIN:
            del directors[director]
    return directors


def _row_in_csv(csv_file=METADATA_FILE):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


if __name__ == '__main__':
    main()
