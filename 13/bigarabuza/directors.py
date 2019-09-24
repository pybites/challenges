import csv
from pathlib import Path
from collections import namedtuple, defaultdict, Counter

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

movie_csv = Path(__file__).resolve().parents[1] / MOVIE_DATA

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=movie_csv):
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

directors = get_movies_by_director()

def get_average_scores(data=directors):
    '''Filter directors with < MIN_MOVIES and calculate average score'''
    directors_filtered = defaultdict(list, {k:v for k,v in data.items() if len(v) > MIN_MOVIES})
    
    for k,v in directors_filtered.items():
        directors_filtered[k] = _calc_mean(v)
    return directors_filtered 

def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    cum_sum = 0
    for movie in movies:
        cum_sum += movie.score
    avg_score = cum_sum/len(movies)
    return avg_score
    
def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)

if __name__ == '__main__':
    main()
    
