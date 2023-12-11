import csv
from collections import defaultdict, namedtuple
from operator import attrgetter


MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960


Movie = namedtuple('Movie', 'title year score')
Director = namedtuple('Director', 'director average_score')
movie_dd = defaultdict(list)


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''

    with open(MOVIE_DATA, newline='', encoding="utf8") as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')

        for row in csv_reader:

            # Filter out any row whose 'title_year' meets or exceeds the minimum year
            if row['title_year'] >= str(MIN_YEAR):
                
                # Construct the movie defaultdict
                # key = director_name, value = Movie Tuple(title, year, score)
                movie_dd[row['director_name']].append(Movie(row['movie_title'], row['title_year'], row['imdb_score']))
        
        
    # Sort the list of namedtuples by score from highlest to lowest
    for director in movie_dd:
        movie_dd[director] = sorted(movie_dd[director], key=attrgetter('score'), reverse=True)

    return movie_dd


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''

    # Eventually will be a list of tuples like [('director', 'average_score')]
    avg_scores = []

    # Loop through the directors defaultdict and calculate the director's average movie score
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            avg_scores.append((director, _calc_mean(movies)))
            
    # Found here: https://pythonguides.com/python-sort-list-of-tuples/
    # Sort the averages list by the second element ('average_score') going from highest to lowest
    avg_scores.sort(key=lambda y: y[1], reverse=True)

    # Return only the first 20 items of the sorted list
    # This shoud equate to the top 20 directors and their movie score averages
    return avg_scores[0:NUM_TOP_DIRECTORS]


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    total_score = 0
    for movie in movies:
        total_score += float(movie.score)
    
    # Round the division to return a float to one decimal point (ex: 8.5)
    avg_score = round(total_score / len(movies), 1)
    return avg_score


def print_directors_and_averages(directors, averages):
    counter = 1

    # Loop through the list of tuple averages (ex: [('director', 'average_score')])
    for d1, avg in averages:

        # No need to sort as the averages tuple list is already sorted by average from highest to lowest
        print('\n')
        print(f'{counter:02d}. {d1:<52} {avg}')
        print('-' * 60)

        # Loop through the defaultdict of movies
        for d2, movies in directors.items():

            # Print the list of movies if the director is found in both
            # Movies are printed in order as is since movie defaultdict is already sorted by 'score'
            if d2 == d1:
                for movie in movies:
                    print(f'{movie.year}] {movie.title:<50} {movie.score}')
        counter += 1


def main():
    directors = get_movies_by_director()
    averages = get_average_scores(directors)
    print_directors_and_averages(directors, averages)


if __name__ == '__main__':
    main()

    