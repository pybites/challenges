import csv
import numpy as np
from collections import Counter, defaultdict
filename_movies = '../movie_metadata.csv'

movies = defaultdict(list)

with open(filename_movies,'r',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for r in reader:
        if r['director_name'] == '' or r['title_year'] == '' or r['imdb_score'] == '':
            continue
        else:
            if int(r['title_year']) >= 1960:
                if r not in movies[r['director_name']]:
                    movies[r['director_name']].append(r)

ratings = Counter()
for d,m in movies.items():
    if len(m) >= 4:
        ratings[d] = np.mean([float(x['imdb_score']) for x in m])

rank = 1
for director, score in ratings.most_common(20):
    print(f"{rank:0=2d}. {director: <52} {score:.1f}")
    print('------------------------------------------------------------')
    for movie in sorted(movies[director], key=lambda x : float(x['imdb_score']), reverse=True):
        imdb_score = float(movie['imdb_score'])
        print(f"{movie['title_year']}] {movie['movie_title']: <51}{imdb_score:.1f}")
    print()
    rank += 1

