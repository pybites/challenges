import csv
from collections import defaultdict, namedtuple
from pathlib import Path

MOVIE_DATA = './movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

movie_csv = Path(__file__).resolve().parents[0] / MOVIE_DATA

Movie = namedtuple('Movie', 'title year score')


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
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    directors_avg = defaultdict(list, {(k, _calc_mean(v)):v for k, v in directors.items() if len(v) >= MIN_MOVIES})
    return directors_avg


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    cum_sum = 0
    for movie in movies:
        if movie.year < 1960:
            continue
        cum_sum += movie.score
    return round(cum_sum/len(movies), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    data_avg_srt = sorted(directors.keys(), key=lambda key: key[1], reverse=True)
    sep_line = '-' * 60
    
    for i in range(len(data_avg_srt[:20])):
        director = data_avg_srt[i][0]
        avg = data_avg_srt[i][1]
        fmt_director_entry = f'{str(i+1).zfill(2)}. {director:<52} {avg}'
        if i > 0:
            print()
        print(fmt_director_entry, end=f'\n{sep_line}\n')
        for movie in sorted(directors[(director, avg)], key=lambda director: director.score, reverse=True):
            year = movie.year
            title = movie.title
            score = movie.score
            if year < 1960:
                continue
            fmt_movie_entry = f'{year}] {title:<50} {score}'
            print(fmt_movie_entry)


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
