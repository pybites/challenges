import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(MOVIE_DATA) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title']
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            if year and year < MIN_YEAR:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    return { (director, _calc_mean(movies)): movies
                for director, movies in directors.items()
                if len(movies) >= MIN_MOVIES }


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    ratings = [m.score for m in movies]
    mean = sum(ratings) / max(1, len(ratings))
    return round(mean, 1)


def print_results(directors):
    fmt_director_entry = '{counter:>02}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60

    for counter, (director_rating, movies) in \
        enumerate(sorted(directors.items(), key=lambda x: float(x[0][1]),
                  reverse=True)[:NUM_TOP_DIRECTORS], 1):
        director, avg = director_rating

        print()
        print(fmt_director_entry.format(counter=counter,
                                        director=director, avg=avg))
        print(sep_line)

        for m in sorted(movies, key=lambda m: m.score, reverse=True):
            print(fmt_movie_entry.format(year=m.year,
                                         title=m.title[:50], score=m.score))


def main():
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
