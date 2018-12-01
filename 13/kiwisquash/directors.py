import os
import collections, csv

#For convenience, I will use namedtuple to store the movie information 
movie = collections.namedtuple("movie", "title year score")

#Read information from movie_metadata.csv
with open('../movie_metadata.csv',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    directorData = collections.defaultdict(list)
    for row in reader:
        year = row['title_year']
        try: 
            year = int(year) # Only grab movies with years
            if year >= 1960: # Only grab movies with years 1960 or higher
                director = row['director_name']
                score = float(row['imdb_score'])
                title = row['movie_title']
                directorData[director].append(movie(title,year,score))
        except:
            pass

def mean(listOfN): #This is the function I will be using to calculate the director's average rating.
    l = len(listOfN)
    if l == 0: #There will be directors with no movies past 1960
        return 0
    return sum(listOfN)/l

def directorScore(director): #Calculate the director's rating based on movies released on or after 1960.
    if director == "":
        return 0
    scores = []
    for movie in directorData[director]:
        scores.append(movie.score)
    return mean(scores) 
    
def movieScore(movie): #I will use this to sort the movies.
    return movie.score 

# Function for making pretty print out of movie data
def printDirectorStats(director, index, length):
    print(f"{str(index).zfill(2)}. {director.ljust(length)} {round(directorScore(director),1):2.1f}")
    print((length+8)*"-")
    movieList = sorted(directorData[director],key=movieScore,reverse=True)
    for movie in movieList:
        print(f"{movie.year}] {movie.title.ljust(length-2)} {round(movie.score,1):2.1f}")

# Create a list of directors that have at least 4 movies from 1960s or later
directorList = []
for director in directorData.keys():
    if len(directorData[director])>3:
        directorList.append(director)

# Create the first version of the top 20 directors by just selecting the first 20 in the list
topList = sorted(directorList[:20],key = directorScore, reverse=True)

# Go through the remaining director list and modify the "topList"
for director in directorList[21:]:
    for i in range(20):
        if directorScore(topList[i])<directorScore(director):
            topList.pop()
            topList.insert(i,director)
            break

# Find the movie with the longest title. This information will be useful for making pretty output
lenList = []
for director in topList:
    for movie in directorData[director]:
        lenList.append(len(movie.title))
maxTitleLength = max(lenList)


os.system('clear')
index = 1
for director in topList:
    printDirectorStats(director,index,maxTitleLength)
    index+=1
    print()
    print()
