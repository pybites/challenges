import csv
from collections import defaultdict, namedtuple
from statistics import mean

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')
DirectorAvg = namedtuple('Library', 'director avg')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    data_dict = defaultdict(list)
    with open(MOVIE_DATA, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        for r in reader:
            try:
                if int(r["title_year"]) >= MIN_YEAR:
                    data_dict[r["director_name"]].append(Movie(r["movie_title"], r["title_year"], float(r["imdb_score"])))
            except ValueError:
                continue
    return data_dict

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    directoravg_dict = {}
    for d, m in directors.items():
        if len(m) >= MIN_MOVIES:
            tmp = DirectorAvg(director=d, avg=_calc_mean(m))
            directoravg_dict[tmp] = m
    return directoravg_dict
    
def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(mean([r.score for r in movies]), 1)

def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    #
    directors = sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)
    for counter in range(0, NUM_TOP_DIRECTORS+1):
        d = directors[counter]
        print (fmt_director_entry.format(counter=counter, director=d[0].director, avg=d[0].avg))
        print (sep_line)
        for m in d[1]:
            print (fmt_movie_entry.format(year=str(m.year), title=m.title, score=m.score))
        print ("\n")


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
