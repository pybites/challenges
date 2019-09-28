import csv
from collections import defaultdict, namedtuple, Counter

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    Movies  = namedtuple('Movies', ['title','year','score'])
    movies_by_director = defaultdict(list)
    with open(MOVIE_DATA) as csvfile:
        reader = csv.DictReader(csvfile)
        for rows in reader:
            try:
                director = rows['director_name']
                title = rows['movie_title'].replace('\xa0','')
                year =  int(rows['title_year'])
                score = float(rows['imdb_score'])
            except ValueError:
                continue
            movie = Movies(title=title, year=year, score=score)
            movies_by_director[director].append(movie)     
    return movies_by_director

def filter_directors(directors):
    directors_with_less_than_min_movies = []
    for director,movies in directors.items():
        d,m = director,len(movies)
        if m < MIN_MOVIES:
            directors_with_less_than_min_movies.append(d)
    for _ in directors_with_less_than_min_movies:
        del directors[_]
    return directors    

    
def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    rating_ranks = defaultdict(list)
    for director, movies in directors.items():
        rating_ranks[director].append(_calc_mean(movies) )
    mylist = Counter(rating_ranks).most_common(20)
    return directors,mylist

def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(sum(movie.score for movie in movies) / len(movies),1)


def print_results(directors,final_list):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    sep_line = '-' * 60
    for i in range(len(final_list)):
        counter = str((i+1)).zfill(2)+ '.'
        d = final_list[i][0]
        av = final_list[i][1]
        print("{} {} {}".format(counter,str(d).ljust(50),av))
        print(sep_line)
        print_Movie_list_by_director(directors,d)
        print()

def print_Movie_list_by_director(directors,director):
    m = directors[director]
    for i in range(len(m)):
        if m[i][1] >= MIN_YEAR:
            print(str(m[i][1])+']',str(m[i][0]).ljust(50),m[i][2])

def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = filter_directors(directors)
    directors, final_list = get_average_scores(directors)
    print_results(directors,final_list)


if __name__ == '__main__':
    main()
