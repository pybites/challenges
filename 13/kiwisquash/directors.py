import os
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

def mean(listOfN):
    l = len(listOfN)
    if l == 0:
        return 0
    return sum(listOfN)/l

def directorScore(director):
    if director == "":
        return 0
    scores = []
    for movie in directorData[director]:
        scores.append(movie.score)
    return mean(scores) 
    
def movieScore(movie):
    return movie.score 

def printDirectorStats(director, index):
    print(f"{str(index).zfill(2)}. {director.ljust(30)} {round(directorScore(director),1):>5}")
    print(30*"-")
    for movie in directorData[director]:
        print(f"{movie.year}] {movie.title}"+2*"\t"+f" {movie.score}")
        
directorList = []
for director in directorData.keys():
    if len(directorData[director])>3:
        print(director)
        directorList.append(director)

topList = sorted(directorList[:20],key = directorScore, reverse=True)

for director in directorList[21:]:
    for i in range(20):
        if directorScore(topList[i])<directorScore(director):
            topList.pop()
            topList.insert(i,director)
            break

os.system('clear')
index = 1
for director in topList:
    printDirectorStats(director,index)
    index+=1
    print()
    print()
