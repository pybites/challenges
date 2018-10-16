import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 6
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(MOVIE_DATA, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        movies = namedtuple('movies', 'title year score')
        for row in reader:
            try:
                director = row['director_name']
                movie = row['movie_title'].replace('\xa0', '').strip()
                score = float(row['imdb_score'])
                year = int(row['title_year'])
            except ValueError:
                continue
            if year > 1960:
                m = Movie(title=movie, year=year, score=score)
                directors[director].append(m)
    return directors

def get_average_scores(directors):
    import collections
    '''Filter directors with < MIN_MOVIES and calculate average score'''
    directors = {k:v for k,v in directors.items() if len(v) >= MIN_MOVIES}
    scr = collections.Counter()
    for director, movies in directors.items():
        scr[director] += _calc_mean(movies)
    return scr.most_common()



def _calc_mean(movies_in):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    sum = 0
    i = 0
    for film in movies_in:
        sum += film.score
        i += 1
    mean = sum / i
    return round(mean, 1)




def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {direct:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    counter = 1
    k = 0
    for director in directors:
        print(sep_line)
        direct = director[0]
        avg = director[1]
        print('{}. {:<52} {}'.format(counter, direct, avg))
        print(sep_line)
        films = get_movies_by_director()[director[0]]
        films_sorted = sorted(films, key=lambda x: float(x[2]), reverse=True)
        for movie in films_sorted:
            print('{}] {:<50} {}'.format(movie.year, movie.title, movie.score))
        counter +=1
        k+=1
        if k == NUM_TOP_DIRECTORS:
            break



def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
