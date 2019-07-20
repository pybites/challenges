import csv
from collections import defaultdict, namedtuple, Counter

MOVIE_DATA = '../movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(MOVIE_DATA, encoding='UTF-8') as fn:
        for row in csv.DictReader(fn):
            try:
                director = row['director_name'].strip()
                title = row['movie_title'].strip()
                year = int(row['title_year'])
                score = float(row['imdb_score'])
            except ValueError:
                continue
            if year >= MIN_YEAR:
                m = Movie(title=title, year=year, score=score)
            directors[director].append(m)  
    return directors
      

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    directors = Counter({(key, _calc_mean(value)): sorted(value, key=lambda x: x.score, reverse=True) for key, value in directors.items() if len(value) >= MIN_MOVIES})
    return directors

def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(sum(average.score for average in movies)/len(movies),1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter:02}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    
    report = sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)[:NUM_TOP_DIRECTORS]
    for counter, ((director,avg), movie) in enumerate(report):
        print(fmt_director_entry.format(counter=counter+1, director=report[counter][0][0], avg=report[counter][0][1]))
        print(sep_line)
        for movie in report[counter][1]:
           print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))   
        print('') 


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
