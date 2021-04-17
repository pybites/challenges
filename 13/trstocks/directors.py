import csv
from collections import defaultdict, namedtuple, OrderedDict

MOVIE_DATA = '../movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(MOVIE_DATA, newline='') as csv_file:
        for row in csv.DictReader(csv_file):
            try:
                director = row.get('director_name')
                title = row.get('movie_title').strip()
                year = int(row.get('title_year'))
                score = float(row.get('imdb_score'))
            except ValueError:
                continue
            movie = Movie(title=title, year=year, score=score)
            directors[director].append(movie)
    return directors


def filter_movies_by_year(directors: defaultdict):
    # Take movies of year >= 1960.
    for d in directors:
        movies = directors[d]
        #  remove all movies made before 1960
        movies = [m for m in movies if m.year >= MIN_YEAR]
        directors[d] = movies
    return directors


def filter_directors_min_movies(directors: defaultdict):
    # Only consider directors with a minimum of 4 movies, otherwise you get misrepresentative data.
    # However going to min 5 movies we miss Sergio Leone :(
    return {key: val for key, val in directors.items() if len(val) > MIN_MOVIES}


def get_average_scores(directors: defaultdict):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    directors = filter_movies_by_year(directors)
    directors = filter_directors_min_movies(directors)
    restructure_directors = defaultdict(list)
    for d in directors:
        movies = directors[d]
        restructure_directors[d].append(movies)
        restructure_directors[d].append(_calc_mean(movies))
    return restructure_directors


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    avg = lambda x_list: round(sum(x.score for x in x_list) / len(x_list), 1)
    return avg(movies)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    # Print the top 20 highest rated directors with their movies ordered desc on rating.
    # sorted(cityPopulation.iteritems(),key=lambda (k,v): v[0],reverse=True)

    ord_directors = OrderedDict(sorted(directors.items(), key=lambda k: k[1][0][0].score , reverse=True))
    def get_score(movie):
        return movie.score
    for cnt, d in enumerate(ord_directors, 1):
        movies, avg = directors[d]
        ord_movies = sorted(movies, key=get_score, reverse=True)
        print(fmt_director_entry.format(counter=cnt, director=d, avg=avg))
        print(sep_line)
        [print(fmt_movie_entry.format(year=m.year, title=m.title, score=m.score)) for m in ord_movies]
        print()
        if cnt == 20:
            break


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
