import collections, csv

with open('../movie_metadata.csv',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    directorData = collections.defaultdict(list)
    for row in reader:
        director = row['director_name']
        score = row['imdb_score']
        year = row['title_year']
        title = row['movie_title']
        directorData[director].append((title,year,score))

for director in directorData:
    print(director,":",directorData[director])
