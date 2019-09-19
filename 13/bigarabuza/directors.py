import csv
from pathlib import Path
from collections import namedtuple, defaultdict, Counter

movie_csv = Path(__file__).resolve().parents[1] / 'movie_metadata.csv'

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=movie_csv):
    
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

directors = get_movies_by_director()

def get_directors_min_4_movies(data=directors):
    cnt = Counter()
    for director, movies in data.items():
        cnt[director] += len(movies)
        sum(movies.score)
    return [(x, y) for (x, y) in cnt.most_common() if y > 4]
    

directors_min4 = get_directors_min_4_movies()

def get_avg_scores(directors):
    for director in directors_min4:
        directors[director]

