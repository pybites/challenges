import csv
from collections import defaultdict
from collections import namedtuple
from collections import Counter

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 3
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')
DIRECTOR_NAME = 'director_name'
MOVIE_TITLE = 'movie_title'
MOVIE_YEAR = 'title_year'
MOVIE_SCORE = 'imdb_score'


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)"""
    movies = defaultdict(list)
    with open(MOVIE_DATA) as fd:
        for line in csv.DictReader(fd):
            try:
                director = line[DIRECTOR_NAME]
                title = line[MOVIE_TITLE].replace('\xa0', '')
                year = int(line[MOVIE_YEAR])
                score = float(line[MOVIE_SCORE])
            except ValueError:
                continue
            if year >= MIN_YEAR:
                movies[director].append(Movie(title=title,year=year,score=score))
    return movies


def get_average_scores(directors):
    """Filter directors with < MIN_MOVIES and calculate average score"""
    return {(director,_calc_mean(movies)):movies for director,movies in directors.items() if MIN_MOVIES < len(movies)}


def _calc_mean(movies):
    """Helper method to calculate mean of list of Movie namedtuples"""
    return round(sum([movie.score for movie in movies])/len(movies),1)


def print_results(directors):
    """Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output"""
    fmt_director_entry = '{counter:02}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    cnt = Counter()
    for k,movies in directors.items():
        cnt[k[0]] = k[1]

    for c, element in enumerate(cnt.most_common(NUM_TOP_DIRECTORS),1):
        print(fmt_director_entry.format(counter=c, director=element[0], avg=element[1]))
        print(sep_line)
        for movie in sorted(directors[element], key=lambda m:m.score, reverse=True):
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
        print()



def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
