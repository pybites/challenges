import re
def extract_course_times():

    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    return re.findall(r'\d{2}:\d{2}', flask_course)


def split_on_multiple_chars():

    logline = ('2017-11-03T01:00:02;challenge time,regex!.'
               'hope you join ... soon')
    return re.split(r'[;,\.]', logline, maxsplit=3)


def get_all_hashtags_and_links():
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    return re.findall(r'(?:http\S*)|(?:#\S*)', tweet)


def match_first_paragraph():
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    return re.sub(r'<p>(.*)</p><p>.*</p>', lambda x: x.group(1), html)


def find_double_words():
    text = 'Spain is so nice in the the spring'
    return re.search(r'(\w{2,}) \1', text).group(0)


def match_ip_v4_address(ip):
    return re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip)
