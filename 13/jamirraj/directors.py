import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """
    Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)
    """
    movies_by_director = defaultdict(list)
    with open(MOVIE_DATA, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                director_name = row["director_name"]
                movie_title = str(row["movie_title"])
                title_year = int(row["title_year"])
                movie_score = float(row["imdb_score"])
            except ValueError:
                continue

            if title_year >= MIN_YEAR:
                movie_details = Movie(title=movie_title, year=title_year, score=movie_score)
                movies_by_director[director_name].append(movie_details)

    return movies_by_director


def get_average_scores(directors):
    """
    Filter directors with < MIN_MOVIES and calculate average score
    """

    directors_scores = {director: _calc_mean(movies) for director, movies in directors.items()
                        if len(movies) >= MIN_MOVIES}

    return sorted(directors_scores.items(), key=lambda x: x[1], reverse=True)


def _calc_mean(movies):
    """
    Helper method to calculate mean of list of Movie namedtuples
    """

    movie_scores = [movie.score for movie in movies]
    return round(sum(movie_scores) / len(movies), 1)


def print_results(directors, directors_avg_score):
    """
    Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    """
    for counter, director in enumerate(directors_avg_score):
        print("\n{}. {:<52} {}".format(counter + 1, director[0], director[1]))
        print('-' * 60)
        for movie in sorted(directors[director[0]], key=lambda x: x.score, reverse=True):
            print("{}] {:<50} {}".format(movie.year, movie.title, movie.score))

        if counter == NUM_TOP_DIRECTORS - 1:
            break


def main():
    directors = get_movies_by_director()
    directors_avg_score = get_average_scores(directors)
    print_results(directors, directors_avg_score)


if __name__ == '__main__':
    main()
