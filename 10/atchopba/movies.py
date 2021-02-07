import random
import re

MOVIE_TITLE = re.compile(r'\d+\.\s+(.*)\s\(.*').sub


def get_movie():
    """Source 100 movies: 
    http://www.infoplease.com/ipea/A0760906.html"""
    with open('movies.txt') as f:
        rand_line = random.choice(f.readlines())
        return MOVIE_TITLE(r'\1', rand_line.rstrip())


if __name__ == '__main__':
    movie = get_movie()
    print(movie)
