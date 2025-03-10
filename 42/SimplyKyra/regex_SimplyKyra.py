import re
from datetime import datetime


def extract_course_times():
    '''Use re.findall to capture all mm:ss timestamps in a list'''
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    return re.findall(r'\d\d:\d\d', flask_course)


def split_on_multiple_chars():
    '''Use re.split to split log line by ; , .
       but not on the last ... so list should have len of 4
       (hint check re.split docs for extra switches)'''
    logline = ('2017-11-03T01:00:02;challenge time,regex!.'
               'hope you join ... soon')
    return re.split(r'[;.,]', logline, 3)


def get_all_hashtags_and_links():
    '''Use re.findall to extract the URL and 2 hashtags of this tweet'''
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    return re.findall(r'http://\S+|#\S+', tweet)


def match_first_paragraph():
    '''Use re.sub to extract the content of the first paragraph (excl tags)'''
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    return re.sub(r'^<p>(.*?)</p>.*$', r'\1', html)


def find_double_words():
    '''Use re.search(regex, text).group() to find the double words'''
    text = 'Spain is so nice in the the spring'
    return re.search(r' (\w+) \1', text).group().strip()


def match_ip_v4_address(ip):
    '''Use re.match to match an ip v4 address (no need for exact IP ranges)'''
    value = re.match(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', ip)
    return value


# Added regex


def replace_word_in_string(text, word, replacement_word):
    ''' Uses re.subn to take a text and replace all occasions of word with replacement_word'''
    return re.subn(word, replacement_word, text)


def grab_date(text):
    ''' Uses re.search to find a date of form dd/Mon/year:hour:minute:second timezone for example: 21/Feb/2020:15:42:42 +0000'''
    date_log = re.search(r'\d{1,2}/\w{0,3}/\d{4}:\d{1,2}:\d{1,2}:\d{1,2} \+\d{4}', text)
    return datetime.strptime(date_log.group(), '%d/%b/%Y:%H:%M:%S %z')


def grab_url(text):
    ''' Grab the url from the text assuming it starts with http(s):// and is encircled by quotes. If not present returns "" '''
    myurl = re.search(r'"https*:\/\/(www){0,1}.\w+[\S]+"', text)
    if myurl is not None:
        return myurl.group()[1:len(myurl.group())-1]
    return ""


def grab_get(text):
    ''' gets any command starting with "GET " and ending with " HTTP/num.num" containing letters and slashes'''
    get_request = re.search(r'GET (\/\w+)* HTTP\/\d+.\d+', text)
    if get_request:
        return get_request.group()
    else:
        return ""

