import csv
from decimal import Decimal
from collections import defaultdict, namedtuple
from statistics import mean
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()


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
            try:
                director = r["director_name"]
                movie = Movie(
                    title=r["movie_title"],
                    year=int(r["title_year"]),
                    score=float(r["imdb_score"]),
                )
                movies_by_director[director].append(movie)
            except Exception:
                continue
        return movies_by_director


def get_average_scores(directors):
    """Filter directors with < MIN_MOVIES and calculate averge score"""
    records = {
        director: movies
        for director, movies in directors.items()
        if len(movies) >= MIN_MOVIES
    }
    return {
        (director, _calc_mean(movies)): movies for director, movies in records.items()
    }


def _calc_mean(movies):
    _mean = mean(Decimal(movie.score) for movie in movies if movie.year >= MIN_YEAR)
    return round(float(_mean), 1)


def _create_table():
    table = Table(show_header=True, header_style="bold magenta")
    table.title = "[not italic]:popcorn:[/] Top 20 Directors [not italic]:popcorn:[/]"
    table.add_column("Rank", style="dim", width=12)
    table.add_column("Director")
    table.add_column("Score", justify="right")
    return table


def _get_director_row_data(movies):
    return sorted(
        (m for m in movies if m.year >= MIN_YEAR),
        key=lambda x: x.score,
        reverse=True,
    )


def print_results(directors):
    """Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output"""

    movie_table = _create_table()
    sorted_directors = sorted(directors.items(), key=lambda x: x[0][1], reverse=True)[:NUM_TOP_DIRECTORS]

    for counter, data in enumerate(sorted_directors, start=1):
        director, avg = data[0]
        movies = data[1]

        # start new section for director
        movie_table.add_row(
            str(counter).zfill(2), director, str(avg), style="blue", end_section=True
        )

        # add all rows for the director to the table
        director_row = _get_director_row_data(movies)
        for movie in director_row:
            movie_table.add_row(str(movie.year), movie.title, str(movie.score))

        # end section with a line
        movie_table.add_row(end_section=True)
    console.print(movie_table)


def main():
    """This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py"""
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == "__main__":
    main()
