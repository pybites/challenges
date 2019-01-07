from collections import namedtuple
from csv import DictReader
from itertools import groupby

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')
Filmography = namedtuple('Filmography', 'director movies avg_score')


def get_movies_by_director():
    with open('movie_metadata.csv') as file:
        reader = DictReader(file)
        movies = sorted([(movie['director_name'],
                          Movie(movie['movie_title'].strip(), movie['title_year'], float(movie['imdb_score']))
                          ) for movie in reader],
                        key=lambda m: m[0])

        return {director: [movie[1] for movie in movies]
                for director, movies in groupby(movies, key=lambda k: k[0])}


def get_top_directors_filmographies(directors):
    films = [Filmography(director,
                         sorted(filter(lambda x: _by_prod_year(x.year), movies), key=lambda x: x.score, reverse=True),
                         _calc_mean(movies))
             for director, movies in directors.items()]

    return sorted(filter(lambda x: len(x.movies) >= MIN_MOVIES, films),
                  key=lambda x: x.avg_score, reverse=True)[:NUM_TOP_DIRECTORS]


def _by_prod_year(year):
    return year.isdigit() and int(year) > MIN_YEAR


def _calc_mean(movies):
    return sum(movie.score for movie in movies)/len(movies) if movies else 0


def print_results(filmographies):
    fmt_director_entry = '{counter}. {director:<52} {avg:.1f}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    for filmography, i in zip(filmographies, range(1, len(filmographies)+1)):
        print(fmt_director_entry.format(counter=i, director=filmography.director, avg=filmography.avg_score))
        print(sep_line)
        for movie in filmography.movies:
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))


def main():
    directors = get_movies_by_director()
    filmographies = get_top_directors_filmographies(directors)
    print_results(filmographies)


if __name__ == '__main__':
    main()
