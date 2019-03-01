import csv
import pprint
from collections import Counter, defaultdict, namedtuple

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')
DirectorAndAverage = namedtuple('DirectorAndAverage', 'director average_score')


def get_movies_by_director(data=MOVIE_DATA):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate average score'''
    directors_filtered = {}

    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            k = DirectorAndAverage(director=director, average_score=_calc_mean([movie for movie in movies if movie.year >= MIN_YEAR]))
            directors_filtered[k] = movies
    
    return directors_filtered


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(sum([movie.score for movie in movies])/len(movies), 1)
    

def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter:02d}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    report = sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)
    for counter in range(20):
        print(fmt_director_entry.format(counter=counter+1, director=report[counter][0].director, 
                                            avg=report[counter][0].average_score))
        print(sep_line)
        for movie in sorted(report[counter][1], key=lambda movie: movie.score, reverse=True):
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
        print('')


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''    
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
