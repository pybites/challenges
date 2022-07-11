import csv
from collections import defaultdict, namedtuple
from functools import reduce

MOVIE_DATA = '../movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(MOVIE_DATA, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['title_year'] and int(row['title_year']) >= MIN_YEAR:
                directors[row['director_name']].append(
                    Movie(row['movie_title'], row['title_year'], float(row['imdb_score'])))
    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    new_dict = {}
    for k, v in directors.copy().items():
        if len(v) >= MIN_MOVIES:
            new_dict[(k, _calc_mean(directors[k]))] = v
    return new_dict


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(reduce(lambda a, b: a+b, [m.score for m in movies]) / len(movies), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter:02d}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    report = sorted(directors.items(),
                    key=lambda x: float(x[0][1]), reverse=True)
    for counter, (k, v) in enumerate(report, 1):
        print()
        print(fmt_director_entry.format(
            counter=counter, director=k[0], avg=k[1]))
        print(sep_line)
        for m in v:
            title = f'{m.title[:45]}...' if len(m.title) > 45 else m.title
            print(fmt_movie_entry.format(
                year=m.year, title=title, score=m.score))
        if counter >= NUM_TOP_DIRECTORS:
            break


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
