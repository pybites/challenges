from pathlib import Path
import csv

movie_csv = Path(__file__).resolve().parents[1] / 'movie_metadata.csv'

with open(movie_csv) as f:
    for line in csv.DictReader(f):
        print(line)

