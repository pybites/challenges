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

cnt = Counter()
for director, movies in directors.items():
    cnt[director] += len(movies)

print(cnt.most_common(5))



