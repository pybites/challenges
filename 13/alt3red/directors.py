import csv
from collections import defaultdict, namedtuple
from statistics import mean

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)"""
    result = defaultdict(list)
    with open(MOVIE_DATA, 'r') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            if row['title_year'] and int(row['title_year']) >= MIN_YEAR:
                result[row['director_name']].append(Movie(row['movie_title'], row['title_year'], row['imdb_score']))
    return result


def get_average_scores(directors):
    """Filter directors with < MIN_MOVIES and calculate averge score"""
    new_list = defaultdict(list)
    result = defaultdict(list)
    averages = dict()
    for name, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            new_list[name] = movies
            averages[name] = round(_calc_mean(movies), 1)
    sorted_averages = sorted(averages, key=averages.get, reverse=True)
    for s in sorted_averages[:NUM_TOP_DIRECTORS]:
        result[s] = new_list[s]
    return result


def _calc_mean(movies):
    """Helper method to calculate mean of list of Movie namedtuples"""
    scores = []
    for m in movies:
        scores.append(float(m.score))
    return mean(scores)


def print_results(directors):
    """Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output"""
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    for counter, director in enumerate(directors):
        avg = round(_calc_mean(directors[director]), 1)
        print(fmt_director_entry.format(counter=counter + 1, director=director, avg=avg))
        print(sep_line)
        for m in sorted(directors[director], key=lambda tup: tup[2], reverse=True):
            print(fmt_movie_entry.format(year=m.year, title=m.title, score=m.score))
        print()


def main():
    """This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py"""
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
