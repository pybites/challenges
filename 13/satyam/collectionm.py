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
    movies_by_directors = defaultdict(list)
    with open(MOVIE_DATA) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie = Movie(row['movie_title'], row['title_year'], row['imdb_score'])
            movies_by_directors[row['director_name']].append(movie)
    return  movies_by_directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    director_average_score = dict()
    for director in directors:
        if len(movies_by_directors[director]) >= MIN_MOVIES:
            director_average_score[director] = _calc_mean(movies_by_directors[director])
    return director_average_score
            


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    scores = [float(m.score) for m in movies]
    avg_score = round(sum(scores) / len(scores),1)
    return avg_score


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    
    for i in range(NUM_TOP_DIRECTORS):
        print(fmt_director_entry.format(counter=i+1, director=directors[i][0], avg=_calc_mean(movies_by_directors[directors[i][0]])))
        print(sep_line)
        sorted_movies = sorted(movies_by_directors[directors[i][0]], key=lambda x: x.score, reverse=True)
        for movie in sorted_movies:
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
        print()
        
def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    movies_by_directors = get_movies_by_director()
    director_average_scores = get_average_scores(movies_by_directors.keys())
    directors_sorted = sorted(director_average_scores.items(), key=lambda x: x[1], reverse=True)
    print_results(directors_sorted)


if __name__ == "__main__":
    main()
