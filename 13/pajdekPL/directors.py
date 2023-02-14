import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = '../movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def movie_data_generator():
    with open(MOVIE_DATA) as file:
        movie_data = csv.DictReader(file)
        for record in movie_data:
            yield record


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors_movies = defaultdict(list)
    movie_data = movie_data_generator
    for record in movie_data():
        if record['title_year'] and int(record['title_year']) >= MIN_YEAR:
            directors_movies[record['director_name']].append(Movie(title=record['movie_title'],
                                                                   year=int(record['title_year']),
                                                                   score=float(record['imdb_score'])))
    return directors_movies


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    return {(director, _calc_mean(movies)): movies for director, movies in directors.items()
            if len(movies) >= MIN_MOVIES}

def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(sum((movie.score for movie in movies))/len(movies), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    counter = 0
    for director in sorted(directors.items(), key=lambda x: x[0][1], reverse=True):
        print()
        print(fmt_director_entry.format(counter=counter, director=director[0][0], avg=director[0][1]))
        print(sep_line)
        for movie in director[1]:
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
        counter += 1


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)
    # print(get_movies_by_director())


if __name__ == '__main__':
    main()
