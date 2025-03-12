from directors import get_movies_by_director, _calc_mean

def test():
    directors = get_movies_by_director()

    assert 'Sergio Leone' in directors
    assert len(directors['Sergio Leone'].movies) == 4
    assert len(directors['Peter Jackson'].movies) == 12

    movies_sergio = directors['Sergio Leone'].movies
    movies_nolan = directors['Christopher Nolan'].movies
    assert _calc_mean(movies_sergio) == 8.5
    assert _calc_mean(movies_nolan) == 8.4

    assert 'Andrew Stanton' not in directors

    expected_directors = ['Sergio Leone', 'Christopher Nolan', 'Quentin Tarantino',
                          'Hayao Miyazaki', 'Frank Darabont', 'Stanley Kubrick']
    expected_avg_scores = [8.5, 8.4, 8.2, 8.2, 8.0, 8.0]
    expected_num_movies = [4, 8, 8, 4, 4, 7]
    report = sorted(directors.items(), key=lambda x: float(x[1].avg_score), reverse=True)
    for counter, (i, j, k) in enumerate(zip(expected_directors, expected_avg_scores, expected_num_movies)):
        assert (report[counter][0], report[counter][1].avg_score) == (i, j)
        assert len(report[counter][1].movies) == k
        assert _calc_mean(report[counter][1].movies) == j

    return "tests pass"


if __name__ == '__main__':
    print(test())
