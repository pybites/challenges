from collections import namedtuple, Counter, defaultdict
import csv
import statistics

MOVIES_DATASET = "movie_metadata.csv"
FROM_YEAR = "1960"
MIN_MOVIES = 4
TOP_N = 20

Movie = namedtuple('Movie', 'director title year rating')


def convert_csv_to_dict(data=MOVIES_DATASET):
    """ Yield Movie(director, title, year, rating) record from input csv file """
    with open(data) as csvfile:
        for movie in csv.DictReader(csvfile):
            yield Movie(
                director=movie['director_name'],
                title=movie['movie_title'].strip(),
                year=movie['title_year'],
                rating=movie['imdb_score']
            )


def from_year(movies, year=FROM_YEAR):
    """ Filter movies based on year"""
    for movie in movies:
        if not year:
            continue
        if movie.year >= year:
            yield movie


def director_filter(movies, min_movies=MIN_MOVIES):
    """ Filter movies whose their director's min movies """
    director_count = Counter(
        movie.director
        for movie in movies
    )

    movies = from_year(convert_csv_to_dict())
    return (
        movie
        for movie in movies
        if director_count[movie.director] >= min_movies
    )


def map_director_movie(movies):
    """ Make a mapping of directors and their movies"""
    def by_rating(movie):
        return movie.rating

    directors = defaultdict(lambda: defaultdict(list))
    for movie in sorted(movies, key=by_rating, reverse=True):
        directors[movie.director]["movies"].append(movie)

    return directors


def calculate_mean_imdb_score(director_movie_map):
    """ Add mean_rating key into the input map"""
    for director, value in director_movie_map.items():
        imdb_scores = []
        for movie in value["movies"]:
            imdb_scores.append(float(movie.rating))
        director_movie_map[director]["mean_rating"] = round(statistics.mean(imdb_scores), 1)
    
    return director_movie_map


def top_n_directors(director_movie_map, n=TOP_N):
    """ Yield top n directors and their movie details """
    def mean_rating(item):
        _, details = item
        return details.get("mean_rating")

    sorted_directors = sorted(director_movie_map.items(), key=mean_rating, reverse=True)
    for idx, (director, details) in enumerate(sorted_directors, start=1):
        yield director, details
        if idx >= n:
            break


if __name__ == "__main__":
    # Parse the csv into bunch of OrderedDict or namedtuples
    movies = convert_csv_to_dict()
    
    # Filter out movies that are made from 1960 onwards
    movies = from_year(movies)
    
    # Filter movies of those directors who have made 4 films or more
    movies = director_filter(movies)

    # Map director to their movies
    director_movie_map = map_director_movie(movies)

    # Calculate the mean imdb score of movies of each director
    directors = calculate_mean_imdb_score(director_movie_map)

    # This is calculated for indented output display
    max_movie_name_len = max(
        len(movie.title)
        for _, details in top_n_directors(directors, n=20)
        for movie in details["movies"]
    )

    # Display the results
    for idx, (director, details) in enumerate(top_n_directors(directors, n=20), start=1):
        mean_rating = details["mean_rating"]
        idx = idx < 10 and f"0{idx}" or f"{idx}"
        print(f'{idx}. {director:<{max_movie_name_len+1}} {mean_rating}')
        print("-" * (max_movie_name_len + 10))
        for movie in details["movies"]:
            print(f"{movie.year}]{movie.title:<{max_movie_name_len}} {movie.rating}")
        print("")
    

