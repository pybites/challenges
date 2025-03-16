import csv
from collections import defaultdict, namedtuple
from typing import Counter

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960


Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors_movies=defaultdict(list)
    with open(MOVIE_DATA, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            data_director=line["director_name"]
            data_title=(line["movie_title"]).replace('\xa0','')
            if line["title_year"]!='':
                data_year=int(line["title_year"])
            data_score=float(line["imdb_score"])
            m=Movie(data_title, data_year, data_score)
            
            if data_year>=MIN_YEAR:
                directors_movies[data_director].append(m)

    return directors_movies


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    filtered_movies=defaultdict(list)
    for dir in directors:
        if len(directors[dir])>=MIN_MOVIES:
            AvgScore=_calc_mean(directors[dir])
            filtered_movies[dir].append(AvgScore)
            filtered_movies[dir].append(directors[dir])

    return filtered_movies



def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    Score=0
    for movies_tuple in movies:
        Score= Score + (movies_tuple.score)
    return round(Score / len(movies),1)



def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    orderNo=1

    top_directors=(Counter(directors).most_common(20))
    for dir, mov in (top_directors):
        print(fmt_director_entry.format(counter=orderNo,director=dir,avg=mov[0]))
        print(sep_line)
        for top_movies in sorted(mov[1], key=lambda x:x.score, reverse=True):
            print(fmt_movie_entry.format(year=top_movies.year, title=top_movies.title, score=top_movies.score ))
        print()
        orderNo+=1

def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()