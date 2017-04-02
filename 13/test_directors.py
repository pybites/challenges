from directors import get_movies_by_director, get_average_scores, _calc_mean


def test():
    directors = get_movies_by_director()

    assert 'Sergio Leone' in directors
    assert 'Andrew Stanton' in directors  # has 3 movies, but not yet filtered
    assert len(directors['Sergio Leone']) == 4
    assert len(directors['Peter Jackson']) == 12

    movies_sergio = directors['Sergio Leone']
    movies_nolan = directors['Christopher Nolan']
    assert _calc_mean(movies_sergio) == 8.5
    assert _calc_mean(movies_nolan) == 8.4

    directors = get_average_scores(directors)
    assert 'Andrew Stanton' not in directors  # director 3 movies now filtered out

    expected_directors = ['Sergio Leone', 'Christopher Nolan', 'Quentin Tarantino',
                          'Hayao Miyazaki', 'Frank Darabont', 'Stanley Kubrick']
    expected_avg_scores = [8.5, 8.4, 8.2, 8.2, 8.0, 8.0]
    expected_num_movies = [4, 8, 8, 4, 4, 7]
    report = sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)
    for counter, (i, j, k) in enumerate(
                            zip(expected_directors,
                                expected_avg_scores, expected_num_movies)):
        assert report[counter][0] == (i, j)
        assert len(report[counter][1]) == k
        assert  _calc_mean(report[counter][1]) == j

    return "tests pass"


if __name__ == '__main__':
    print(test())
