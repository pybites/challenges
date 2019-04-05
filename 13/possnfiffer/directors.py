import csv
from collections import defaultdict, namedtuple, Counter

MOVIE_DATA = "../movie_metadata.csv"

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director(data=MOVIE_DATA):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding="utf-8") as f:
        for line in csv.DictReader(f):
            try:
                director = line["director_name"]
                movie = line["movie_title"].replace("\xa0", "")
                year = int(line["title_year"])
                score = float(line["imdb_score"])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


def get_top_five_directors_with_most_movies(directors):
    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies)

    return cnt.most_common(5)


def main():
    directors = get_movies_by_director()
    top_five_directors = get_top_five_directors_with_most_movies(directors)
    print(top_five_directors)


if __name__ == "__main__":
    main()
