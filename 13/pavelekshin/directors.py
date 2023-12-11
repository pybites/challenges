import csv
from collections import defaultdict, namedtuple, OrderedDict, Counter
from pprint import pprint

MOVIE_DATA = "movie_metadata.csv"
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960
Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)"""
    with open(MOVIE_DATA, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        d = defaultdict(list)
        for row in reader:
            try:
                director = row["director_name"]
                title = row["movie_title"].replace("\xa0", "")
                year = int(row["title_year"])
                score = float(row["imdb_score"])
            except ValueError:
                continue
            if year > MIN_YEAR:
                d[director].append(Movie(title=title, year=year, score=score))
    return d


def get_average_scores(directors):
    """Filter directors with < MIN_MOVIES and calculate averge score"""
    fd, dd = {}, {}
    Movie = namedtuple("Movie", "score movies")
    for k, movies in directors.items():
        if not len(movies) < MIN_MOVIES:
            score = _calc_mean(movies)
            fd[k] = Movie(score=score, movies=movies)
    sd = OrderedDict(
        {k: v for k, v in sorted(fd.items(), key=lambda x: x[1][0], reverse=True)}
    )
    return sd


def _calc_mean(movies):
    """Helper method to calculate mean of list of Movie namedtuples"""
    return round(sum(i.score for i in movies) / len(movies), 1)


def most_film_directors(directors):
    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies[1])
    return cnt.most_common(5)


def print_results(directors):
    """Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output"""
    directors = dict(list(directors.items())[:20])
    fmt_director_entry = "{counter:02}. {director:<52} {avg}"
    fmt_movie_entry = "{year} {title:<50} {score}"
    sep_line = "-" * 60
    for count, (director, movies) in enumerate(directors.items(), 1):
        print(
            fmt_director_entry.format(
                counter=count, director=director, avg=movies.score
            )
        )
        print(sep_line)
        for title, year, score in sorted(
            movies.movies, key=lambda x: x[2], reverse=True
        ):
            print(fmt_movie_entry.format(year=year, title=title, score=score))
        print("\n")


def main():
    """This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py"""
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    # pprint(most_film_directors(directors))
    print_results(directors)


if __name__ == "__main__":
    main()
