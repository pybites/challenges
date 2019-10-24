import pandas as pd
from collections import Counter

"""
Put the movie_metadata.csv in the same directory where is going to run the script.
"""
FILE = 'movie_metadata.csv'


def filter():
    """
    Filter the dataset with the directors with at least 4 movies, and the year of the movie.
    """
    movie = pd.read_csv(FILE)
    c = Counter(movie['director_name'])
    four_movies = [key for key, value in c.items() if value > 3]
    four_check = movie['director_name'].isin(four_movies)
    year_check = movie['title_year'] >= 1960
    movie = movie[four_check & year_check]
    return movie


def rating(filtered):
    """"
    Filter de dataset after been passed by filter(), to extract the directors with highest
    rating based on their average movie imdb ratings.
    """
    movie_score = filtered.sort_values(by=['imdb_score'])
    director_mean = {key: movie_score[movie_score['director_name'] == key]
                     ['imdb_score'].mean() for _, key in enumerate(movie_score['director_name'])}
    rank_directors = sorted(zip(director_mean.values(), director_mean.keys()))[-20:][::-1]                         
    return rank_directors

def out_screen(rank_directors, movie_data):
    """
    Printing the results.
    """
    for i,(mean, director_name) in enumerate(rank_directors):
        print(f" {i+1}--{director_name:44} {mean:.1f}")
        print("-"*53)
        titles = movie_data[movie_data['director_name'] == director_name]['movie_title'] 
        imdb_score = movie_data[movie_data['director_name'] == director_name]['imdb_score']
        title_year = movie_data[movie_data['director_name'] == director_name]['title_year']
        generator = zip(title_year, titles, imdb_score)
        for year, title, imdb in generator:
            print(f"{int(year):5} {title:43} {imdb:.1f}")
        print()
        
def main():
    movie = filter()
    rank = rating(movie)
    out_screen(rank, movie)

if __name__ == "__main__":
    main()
