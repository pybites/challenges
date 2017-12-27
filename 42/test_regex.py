from regex import (extract_course_times, split_on_multiple_chars,
                   get_all_hashtags_and_links, match_first_paragraph,
                   find_double_words, match_ip_v4_address)


def test_extract_course_times():
    expected = ['01:47', '32:03', '41:51', '27:48', '05:02']
    assert extract_course_times() == expected


def test_split_on_multiple_chars():
    expected = ['2017-11-03T01:00:02', 'challenge time',
                'regex!', 'hope you join ... soon']
    assert split_on_multiple_chars() == expected


def test_get_all_hashtags_and_links():
    expected = ['http://pybit.es/requests-cache.html', '#python', '#APIs']
    assert get_all_hashtags_and_links() == expected


def test_match_first_paragraph():
    expected = 'pybites != greedy'
    assert match_first_paragraph() == expected


def test_find_double_words():
    expected = 'the the'
    assert find_double_words() == expected


def test_match_ip_address():
    valid_ips = ['1.1.1.1', '255.255.255.255', '192.168.1.1',
                 '10.10.1.1', '132.254.111.10', '26.10.2.10',
                 '127.0.0.1']
    bad_ips = ['10.10.10', '10.10', '10', 'a.a.a.a', '10.0.0.a']
    for valid_ip in valid_ips:
        assert match_ip_v4_address(valid_ip)
    for bad_ip in bad_ips:
        assert match_ip_v4_address(bad_ip) is None
