import csv
from collections import defaultdict, namedtuple, OrderedDict

MOVIE_DATA = '../movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Director = namedtuple('Director', 'name avg_score movies')
Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    movies = defaultdict(list)
    with open(MOVIE_DATA) as f:
        for rec in csv.DictReader(f):
            try:
                name = rec['director_name']
                if int(rec['title_year']) >= MIN_YEAR:
                    movies[name].append(Movie(title=rec['movie_title'].replace('\xa0', ''),
                                              year=int(rec['title_year']), score=float(rec['imdb_score'])))
            except ValueError:
                continue

    directors = {}
    for name in movies:
        if len(movies[name]) >= MIN_MOVIES:
            directors[name] = (Director(name=name, avg_score=_calc_mean(movies[name]), movies=movies[name]))

    return directors


def _calc_mean(movies):
    return round(sum(movie.score for movie in movies) / len(movies), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    for i, director in zip(range(20), sorted(directors.items(), key=lambda x: float(x[1].avg_score), reverse=True)):
        print()
        print(f'{i+1:02d}. {director[0]:<52} {director[1].avg_score}')
        print('-' * 60)
        for movie in sorted(director[1].movies, key=lambda x: float(x.score), reverse=True):
            print(f'{movie.year}] {movie.title:<50} {movie.score}')


def main():
    directors = get_movies_by_director()
    print_results(directors)


if __name__ == '__main__':
    main()
