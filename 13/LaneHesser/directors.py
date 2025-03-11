import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movie_data():
    """Gets the movie data from the csv file and returns a dictionary of
       directors mapped to movies."""
    directors = defaultdict(list)
    with open(MOVIE_DATA) as f:
        data = csv.DictReader(f)
        for row in data:
            movie_info = _parse_row(row)
            director = row['director_name']

            if director and movie_info is not None:
                movie = Movie(**movie_info)
                directors[director].append(movie)

    return _filter_directors_by_movie_min(directors)


def _filter_directors_by_movie_min(directors):
    """Returns a dictionary mapping director name to a list of movies from the
       director, sorted in descending order by the movie scores."""
    return {
        director: sorted(movies, key=lambda movie: movie.score, reverse=True)
        for director, movies in directors.items()
        if len(movies) >= MIN_MOVIES
    }


def _parse_row(row):
    """Parses the row and returns the movie info back in a dictionary."""
    if (not row['title_year'] or
            not row['movie_title'] or
            not row['imdb_score'] or
            int(row['title_year']) < MIN_YEAR):

        return None

    return {
        'title': row['movie_title'][:-1],
        'year': int(row['title_year']),
        'score': float(row['imdb_score'])
    }


def get_average_scores(movie_data):
    """Accepts the movie data and gets the average score for each director, sorted descending."""
    directors_avg_scores = {
        director: round(sum(movie.score for movie in movies) / len(movies), 1)
        for director, movies in movie_data.items()
    }

    return sorted(directors_avg_scores.items(),
                  key=lambda x: x[1],
                  reverse=True)


def main():
    movie_data = get_movie_data()
    directors_avg_scores = get_average_scores(movie_data)
    counter = 1
    sep_line = '-' * 60

    for director, avg_score in directors_avg_scores[:9]:
        print(f'{str(counter).zfill(2)}. {director:<52} {avg_score}')
        print(sep_line)
        for movie in movie_data[director]:
            print(f'{movie.year}] {movie.title:<50} {movie.score}')

        counter += 1
        print()


if __name__ == '__main__':
    main()
