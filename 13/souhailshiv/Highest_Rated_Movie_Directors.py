from collections import *
import csv
from urllib.request import urlretrieve
from statistics import *
import pandas as pd
from termcolor import colored
from math import *

movie_data = "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv"
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)
Movie = namedtuple("Movie", "title year score")
MIN_MOVIES = 4
MIN_YEAR = 1960

directors = defaultdict(list)


def get_movies_by_director(data=movies_csv):
    with open(data, encoding="utf-8") as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            global m
            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
    return directors


def avrage_score(directors):

    cnt = Counter()
    newDict = dict()

    for director, movies in directors.items():
        cnt[director] += len(movies)
        c = dict(cnt)
    for k, v in c.items():
        if v >= MIN_MOVIES:
            newDict[k] = v
    avrege = dict()

    for k in newDict.keys():
        moviescores = list()
        for item in directors[str(k)]:
            if int(item[1]) >= MIN_YEAR:
                moviesscores = moviescores.append(item[2])

        avrege.update({k: mean(moviescores)})

    return avrege


def print_results(avrege, directors):
    avrege = {k: v for k, v in sorted(
        avrege.items(), key=lambda item: item[1], reverse=True)}
    i = 0
    for k, v in avrege.items():
        i = i+1
        if i == 21:
            break
        print(f'\n{colored("%.2d"%i,"magenta")} {k}',
              " "*40, colored("%.2f" % v, "magenta"))
        print("-"*60)
        for item in directors[k]:
            if item[1] >= MIN_YEAR:
                print(colored(item[1], "magenta"), colored(
                    "]", "red"), item[0], " "*20, colored(item[2], "magenta"))


def main():
    directors = get_movies_by_director()
    avrage = avrage_score(directors)
    print_results(avrage, directors)


if __name__ == '__main__':
    main()
