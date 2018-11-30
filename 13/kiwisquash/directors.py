import collections, csv

movieInfo = collections.namedtuple("movieInfo", "title year score")
with open('../movie_metadata.csv',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    directorData = collections.defaultdict(list)
    for row in reader:
        year = row['title_year']
        try: 
            year = int(year)
            if year >= 1960:
                director = row['director_name']
                score = float(row['imdb_score'])
                title = row['movie_title']
                directorData[director].append(movieInfo(title,year,score))
        except:
            pass
print(directorData)
for director in directorData:
    if len(directorData[director])>3:
        print(director,":",directorData[director][0].year)
