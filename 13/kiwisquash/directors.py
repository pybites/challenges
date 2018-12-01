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

def directorScore(director):
    scores = []
    for movie in directorData[director]:
        scores.append(movie.score)
    return sum(scores)/len(scores)

def getKey(item):
    return item.score 

print(directorData)
for director in directorData:
    if len(directorData[director])>3:
        # print(director,round(directorScore(director),1))
        print(director,":",sorted(directorData[director],key = getKey, reverse = True))
