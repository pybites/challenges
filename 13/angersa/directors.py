import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = '/Users/aa/GitHub/challenges/13/movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=MOVIE_DATA):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            if m.year >= MIN_YEAR:
                directors[director].append(m)

    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    director_scores = defaultdict(list)
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            director_scores[(director, _calc_mean(movies))] = movies
    return director_scores


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    total = 0
    for m in movies:
        total += m.score
    return round(total/len(movies), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    rank = 0

    best_directors = sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)
    for director, movies in best_directors[:20]:
        rank += 1
        print(fmt_director_entry.format(counter=rank, director=director[0], avg=director[1]))
        print(sep_line)
        for m in sorted(movies, key=lambda m: m.score, reverse=True):
            print(fmt_movie_entry.format(year=m.year, title=m.title, score=m.score))
        print()


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
