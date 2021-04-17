import csv
from decimal import Decimal
from collections import defaultdict, namedtuple
from statistics import mean
from pathlib import Path


MOVIE_DATA = "../movie_metadata.csv"
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)"""
    with Path(MOVIE_DATA).open(encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        movies_by_director = defaultdict(list)

        for r in reader:
            director = r["director_name"]
            movie = Movie(
                title=r["movie_title"], year=r["title_year"], score=r["imdb_score"]
            )
            movies_by_director[director].append(movie)
        return movies_by_director


def get_average_scores(directors):
    """Filter directors with < MIN_MOVIES and calculate averge score"""
    records = {
        director: movies
        for director, movies in directors.items()
        if len(movies) >= MIN_MOVIES
    }
    return {
        director: {"average": _calc_mean(movies), "movies": movies}
        for director, movies in records.items()
    }


def _calc_mean(movies):
    _mean = mean(Decimal(movie.score) for movie in movies)
    return round(float(_mean), 1)


def print_results(directors):
    """Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output"""
    fmt_director_entry = "{counter}. {director:<52} {avg}"
    fmt_movie_entry = "{year}] {title:<50} {score}"
    sep_line = "-" * 60
    for counter, data in enumerate(
        sorted(directors.items(), key=lambda x: x[1]["average"], reverse=True)[:20]
    ):
        counter += 1
        director = data[0]
        avg = data[1]["average"]

        print()
        print(
            fmt_director_entry.format(
                counter=str(counter).zfill(2), director=director, avg=avg
            )
        )

        print(sep_line)
        movies = sorted(
            (
                m
                for m in data[1]["movies"]
                if m.year.isdigit() and int(m.year) >= MIN_YEAR
            ),
            key=lambda x: x.score,
            reverse=True,
        )
        for movie in movies:
            print(
                fmt_movie_entry.format(
                    year=movie.year, title=movie.title, score=movie.score
                )
            )


def main():
    """This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py"""
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == "__main__":
    main()
