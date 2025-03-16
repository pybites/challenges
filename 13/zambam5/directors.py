# python3.11
from collections import defaultdict, namedtuple
import csv
from urllib.request import urlretrieve

# Note to start: in python 3.11 csv.DectReader rows are dicts, not OrderedDicts

MOVIES_FILE = "movie_metadata.csv"
MINIMUM_MOVIES = 4
MINIMUM_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_directors_from_csv() -> defaultdict:
    """
    Organize the data from the provided csv in a convenient way
    No movies before 1960
    Remove superflous data
    Some entries do not have years provided, so we use try-except to ignore those
    """
    directors = defaultdict(list)
    # a dict with directors as keys and a list of data for each of their movies as values
    with open(MOVIES_FILE, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                year = int(row["title_year"])
                if year >= MINIMUM_YEAR:
                    title = row["movie_title"].replace("\xa0", "").replace("\xc2", "")
                    score = float(row["imdb_score"])
                    movie = Movie(title, year, score)
                    directors[row["director_name"]].append(movie)
            except ValueError:
                continue
    return directors


def get_director_average_scores(directors: defaultdict) -> dict:
    """
    Return dict of directors and their average imbd scores
    """
    director_averages = dict()
    for director, movies in directors.items():
        number_of_movies = len(movies)
        total_score = sum([movie.score for movie in movies])
        director_averages[director] = round(total_score / number_of_movies, 1)
    return director_averages


def print_top_directors(directors: defaultdict) -> None:
    """
    Print the top 20 directors as directed in the challenge
    """
    averages = get_director_average_scores(directors)
    averages_filtered = dict()
    for director, movies in directors.items():
        if len(movies) >= MINIMUM_MOVIES:
            averages_filtered[director] = averages[director]
    directors_sorted = sorted(averages_filtered, key=lambda x: -averages_filtered[x])
    for counter, director in enumerate(directors_sorted[:20], 1):
        print(f"{counter:02}. {director:<52} {averages[director]}")
        print("-" * 60)
        for movie in directors[director]:
            print(f"{movie.year}] {movie.title:<50} {movie.score}")
        print(" ")


directors = get_directors_from_csv()
print_top_directors(directors)
