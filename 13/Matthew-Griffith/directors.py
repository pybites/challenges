import csv
import collections
import os
import statistics

Movie = collections.namedtuple('Movies', 'title, score, year')
DirectorScore = collections.namedtuple('DirectorScore', 'name, avg_score')


def main():
    # get the path for the file
    file_path = get_file()
    # load the csv into a dict
    directors_movie = load_movie_data(file_path)
    # compute each directors average
    directors_score = get_score(directors_movie)
    # sort the director score for a list of namedtuples
    directors_score.sort(key=lambda s: -s.avg_score)
    # show the top 20
    print_top_directors(directors_score[:20], directors_movie)


def print_top_directors(list_directors, directors_movie):
    for i in range(len(list_directors)):
        print(f'\n{i + 1}. {list_directors[i].name}: {list_directors[i].avg_score}')
        print('-------------------------------------------------------------')

        current_director = directors_movie[list_directors[i].name]
        for movie in current_director:
            print(f'{movie.year}] {movie.title}: {movie.score}')


def get_score(director_dict):
    directors_score = []
    for k, v in director_dict.items():
        score_list = [
            m.score
            for m in v
            if m.year >= 1960 and len(v) >= 4
        ]
        if score_list:
            directors_score.append(DirectorScore(
                name=k, avg_score=statistics.mean(score_list)))

    return directors_score


def load_movie_data(path):
    with open(path, encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        director_dict = collections.defaultdict(list)
        for line in reader:
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                score = float(line['imdb_score'])
                year = int(line['title_year'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            director_dict[director].append(m)

        return director_dict


def get_file():
    base_folder = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(base_folder, 'movie_metadata.csv')
    return path


if __name__ == "__main__":
    main()
