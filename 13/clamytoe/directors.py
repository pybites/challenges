import csv
from collections import defaultdict, namedtuple
from statistics import mean
from typing import Any, DefaultDict, Dict, List, NamedTuple

MOVIE_DATA: str = "movie_metadata.csv"
NUM_TOP_DIRECTORS: int = 20
MIN_MOVIES: int = 4
MIN_YEAR: int = 1960


class Movie(NamedTuple):
    """Movie namedtuple object"""

    title: str
    year: int
    score: float


class Director(NamedTuple):
    """Director namedtuple object"""

    avg: float
    movies: List[Movie]

    def __len__(self):
        return len(self.movies)


def get_movies_by_director() -> DefaultDict[str, List[Movie]]:
    """Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)"""
    directors: DefaultDict[str, List[Movie]] = defaultdict(list)

    with open(MOVIE_DATA) as source_file:
        for row in csv.DictReader(source_file):
            title_year: str = row["title_year"]

            if _validate_year(title_year):
                director_name: str = row["director_name"]
                title: str = row["movie_title"].rstrip()
                imdb_score: str = row["imdb_score"]
                year: int = int(title_year)
                score: float = float(imdb_score)

                directors[director_name].append(Movie(title, year, score))
    return directors


def get_average_scores(
    directors: DefaultDict[str, List[Movie]]
) -> DefaultDict[Any, Any]:
    """Filter directors with < MIN_MOVIES and calculate average score"""
    updated_directors: DefaultDict[Any, Any] = defaultdict(dict)

    for director in directors:
        movies: List[Movie] = directors[director]
        if len(movies) >= MIN_MOVIES:
            average: float = _calc_mean(movies)
            updated_directors[director] = Director(average, movies)

    return updated_directors


def _calc_mean(movies):
    """Helper method to calculate mean of list of Movie namedtuples"""
    return round(mean([movie.score for movie in movies]), 1)


def _validate_year(year):
    """Helper function to determine if the year meets the requirements"""
    return True if year and year.isnumeric() and int(year) >= MIN_YEAR else False


def print_results(directors) -> None:
    """Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output"""
    s_directors = sorted(directors.items(), key=lambda d: d[1].avg, reverse=True)

    for counter, director_listing in enumerate(s_directors, 1):
        if counter <= NUM_TOP_DIRECTORS:
            director = director_listing[0]
            avg = director_listing[1].avg
            fmt_director_entry = f"{str(counter).zfill(3):<}. {director:<52} {avg}"
            sep_line = "-" * 60
            print(fmt_director_entry)
            print(sep_line)

            movies = sorted(
                directors[director].movies, key=lambda m: m.score, reverse=True
            )

            for movie in movies:
                title = movie.title
                year = movie.year
                score = movie.score
                fmt_movie_entry = f"[{year}] {title:<50} {score}"
                print(fmt_movie_entry)

            print()


def main():
    """Sample run of script"""
    directors = get_movies_by_director()
    updated = get_average_scores(directors)

    print_results(updated)


if __name__ == "__main__":
    main()
