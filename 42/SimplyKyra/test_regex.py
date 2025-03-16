from regex_SimplyKyra import (extract_course_times, split_on_multiple_chars,
                   get_all_hashtags_and_links, match_first_paragraph,
                   find_double_words, match_ip_v4_address, replace_word_in_string,
                   grab_date, grab_url, grab_get)
from datetime import datetime


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


# Added tests
def test_replace_word_in_string():
    text = "Here is a string with the word George. How many George's can you replace? George Gorge George Go"
    return_val = replace_word_in_string(text, "George", "Fred")
    assert return_val[0] == "Here is a string with the word Fred. How many Fred's can you replace? Fred Gorge Fred Go"
    assert return_val[1] == 4


# Tests the two lined log file.
def test_log_files():
    file = open('log_file.txt', mode='r')
    lines = file.read().split("\n")
    file.close()

    assert match_ip_v4_address(lines[0]).group() == "10.32.4.88"
    assert grab_date(lines[0]) == datetime.strptime("21/Feb/2020:15:42:42 +0000", '%d/%b/%Y:%H:%M:%S %z')
    assert grab_url(lines[0]) == ""
    assert grab_get(lines[0]) == "GET /health HTTP/1.1"

    assert match_ip_v4_address(lines[1]).group() == "10.32.104.90"
    assert grab_date(lines[1]) == datetime.strptime("21/Feb/2020:15:42:43 +0000", '%d/%b/%Y:%H:%M:%S %z')
    assert grab_url(lines[1]) == "https://randomurl.com/l3K4bpvbNa/Pixie-Lott?foo=bar&bas=bar"
    assert grab_get(lines[1]) == "GET /api/v2/notifications HTTP/1.1"

