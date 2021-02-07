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
    with open(MOVIE_DATA, "r") as movie_data_csv_file:
        reader = csv.DictReader(movie_data_csv_file)
        directors = defaultdict(list)
        for entry in reader:
            # Handle entries with missing field
            try:
                m = Movie(
                        title=entry['movie_title'].strip(),
                        year=int(entry['title_year']),
                        score=float(entry['imdb_score'])
                    )
            except ValueError:
                continue

            # Handle duplicate
            if m not in directors[entry['director_name']]:
                directors[entry['director_name']].append(m)
        return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    new_directors = defaultdict(list)
    # Create a new dict with key=(director_name, avg_score) value=list(Movie)
    for d in directors.items():
        if len(d[1]) > MIN_MOVIES:
            recent_movies = list(filter(lambda movie: movie.year >= MIN_YEAR, directors[d[0]]))
            new_directors[(d[0], _calc_mean(recent_movies))] = recent_movies
    return new_directors


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    mean = 0
    for movie in movies:
        mean = mean + movie.score
    return mean / len(movies)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<53} {avg:.1f}'
    fmt_movie_entry = '{year}] {title:<50.50} {score}'
    sep_line = '-' * 60
    # Sort directors by avg_score
    directors = sorted(directors.items(), key=lambda d: float(d[0][1]), reverse=True)
    for counter, director in enumerate(directors[:NUM_TOP_DIRECTORS]):
        print(fmt_director_entry.format(counter=counter+1, director=director[0][0], avg=director[0][1]))
        print(sep_line)
        # Sort movies by score
        for movie in sorted(director[1], key=lambda x: float(x.score), reverse=True):
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
        print("\n")


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
