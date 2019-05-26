import csv
from collections import defaultdict, namedtuple
from statistics import mean

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')
Director = namedtuple('Director', 'avg_rating movies')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    movies = defaultdict(list)

    with open(MOVIE_DATA, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            try:
                if int(r['title_year']) >= MIN_YEAR:
                    movies[r['director_name']].append(Movie(r['movie_title'], r['title_year'], r['imdb_score']))
            except ValueError:
                continue
    return movies


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score.
    According to the tests the returned result should be a dictionary
    with a tuple consisting of (director_name, avg_score) as the key
    and the movie list as the value'''

    ratings = dict()
    for director, movies in directors.items():
        if director == '':
            continue
        filtered_movies = []
        for movie in movies:
            if movie.title == '':
                continue
            if movie.score == '':
                continue

            filtered_movies.append(movie)

        if len(filtered_movies) >= MIN_MOVIES:
            ratings[director, _calc_mean(filtered_movies)] = filtered_movies
    return ratings


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(mean([float(x.score) for x in movies]), 1)

def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''

    sorted_directors = sorted(directors.items(), key=lambda x : x[0][1], reverse=True)
    sep_line = '-' * 60
    counter = 1
    for director, movies in sorted_directors[:NUM_TOP_DIRECTORS]:
        print(f'{counter:0=2d}. {director[0]:<52} {director[1]}')
        print(sep_line)
        for m in sorted(movies, key= lambda x : x.score, reverse=True):
            print(f'{m.year}] {m.title:<50} {m.score}')
        print()
        counter += 1



def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()