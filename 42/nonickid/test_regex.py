from regex import (extract_course_times, split_on_multiple_chars,
                   get_all_hashtags_and_links, match_first_paragraph,
                   find_double_words, match_ip_v4_address, find_all_dates,
                   change_function_name, find_flight_connections, match_email_address)


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


def test_find_all_dates():
    expected = ['27 February, 2020', '2 November, 2019', '3 December, 2019', '12 July, 2019', '12 July, 2019']
    assert find_all_dates() == expected

def test_change_function_name():
    expected = '2019-06-24 14:56 - function process_data() completed'
    assert change_function_name() == expected

def test_find_flight_connections():
    expected = '15:00 Frankfurt - NewYork'
    assert find_flight_connections() == expected

def test_match_email_address():
    valid_emails = ['john@gmail.com', 'phil@test.de', 'carol_56@yahoo.com']
    bad_emails = ['adam@gmail', 'megan3@gmail.commmmo']
    for valid_email in valid_emails:
        assert match_email_address(valid_email)
    for bad_email in bad_emails:
        assert match_email_address(bad_email) is None