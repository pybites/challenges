import csv
from collections import defaultdict, namedtuple, Counter
from urllib.request import urlretrieve

MOVIE_DATA = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
MOVIE_CSV = 'movies.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

urlretrieve(MOVIE_DATA, MOVIE_CSV)
Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=MOVIE_CSV):
    '''Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    cnt = Counter()
    del_lst = []
    for director, movies in directors.items():
        cnt[director] += len(movies)
        if cnt[director] < MIN_MOVIES:
            del_lst.append(director)

    for item in del_lst:
        del directors[item]


    score_average = {}
    for director, movies in directors.items():
        total_score = 0
        count = 0
        for movie in movies:
            if movie[1] < MIN_YEAR:
                del movie
            else:
                total_score += movie[2]
                count += 1
        score_average[director] = total_score / count

    score_average_sorted = sorted(score_average.items(), key=lambda x: x[1], reverse=True)
    return score_average_sorted

directors = get_movies_by_director()
score_average_sorted = get_average_scores(directors)

def print_results(score_average_sorted, directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    counter = 1
    for director_name in score_average_sorted:
        print(f'{counter}. {director_name[0]:<52} {director_name[1]:.1f}')
        print(f'-' * 60)

        for director, movies in directors.items():
            if director_name[0] == director:
                # print(director)
                for movie in movies:
                    if movie[1] < MIN_YEAR:
                        del movie
                    else:
                        print(f'{movie.year}] {movie.title:<50} {movie.score}')
        print(" ")
        counter += 1


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    score_average_sorted = get_average_scores(directors)
    print_results(score_average_sorted, directors)


if __name__ == '__main__':
    main()
