import csv
from collections import defaultdict, namedtuple
from pprint import pprint

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    # Read the CSV File
    directors = defaultdict(list)
    with open('movie_metadata.csv',mode='r') as f:
        csvDict = csv.DictReader(f)
        
        for row in csvDict:
                Movie = namedtuple('Movie', 'title year score')
                Movie.title = row['movie_title']
                Movie.year = row['title_year']
                Movie.score = float(row['imdb_score'])
                director = row['director_name']
                directors[director].append(Movie)
    return directors

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    result = []
    for director,movies in directors.items():
        if len(movies) < MIN_MOVIES:
            pass
        else:
            d = {}
            average_movies_score = sum([ movie.score for movie in movies]) / len(movies)
            d['name'] = director   # string
            d['avg_score'] = average_movies_score  # string
            d['movies'] = movies   # List

            result.append(d)

    return result


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    pass


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    director_list = sorted(directors,key=lambda x: x['avg_score'],reverse=True)
    for index, director in enumerate(director_list[:5],start=1):
        
        fmt_director_entry = '{counter}. {name:<46} {score:10.2}'.format(
                                                                counter=index,
                                                                name=director.get('name',''),
                                                                score=director.get('avg_score',-1)                                                                
                                                                )
        print(fmt_director_entry)
        sep_line = '-' * 60
        print(sep_line)
        for movie in director['movies']:

            fmt_movie_entry = '{year}] {title:<50} {score}'.format(
                                                                year=movie.year,
                                                                title=movie.title,
                                                                score=movie.score
                                                                )
            print(fmt_movie_entry)
        
        print('\n')
        


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    #test_director = 'James Cameron'
    # for movie in directors[test_director]:
    #     print(movie.title, movie.year)
    directors = get_average_scores(directors)
    #print(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
