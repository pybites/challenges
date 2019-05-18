import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')
Director = namedtuple('Director', 'name movies avg count')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    movies = defaultdict(list)
    with open(MOVIE_DATA) as movie_file:
        for row in csv.DictReader(movie_file):
            if row['title_year'] and int(row['title_year']) >= 1960:
                movies[row['director_name']].append(Movie(row['movie_title'], int(row['title_year']), float(row['imdb_score'])))
    return movies

def get_average_scores(directors):
    scores = {}
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            scores[director] = Director(director, movies, _calc_mean(movies), len(movies))
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    return scores


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(sum([movie.score for movie in movies]) / len(movies), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter:02}. {director:<52} {avg:3.1f}'
    fmt_movie_entry = '{year}] {title:<50} {score:3.1f}'
    sep_line = '-' * 60
    for rank, director in enumerate(sorted(directors.values(), key=lambda d: d.avg, reverse=True)[:NUM_TOP_DIRECTORS]):
        print(fmt_director_entry.format(counter=rank+1, director=director.name, avg=director.avg))
        print(sep_line)
        for movie in sorted(director.movies, key=lambda m: m.score, reverse=True):
            print(fmt_movie_entry.format(year=movie.year, title=movie.title[:50], score=movie.score))
        print()


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
