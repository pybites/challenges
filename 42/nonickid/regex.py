import re


def extract_course_times():
    '''Use re.findall to capture all mm:ss timestamps in a list'''
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    return re.findall(r'\d{2}:\d{2}', flask_course)


def split_on_multiple_chars():
    '''Use re.split to split log line by ; , .
       but not on the last ... so list should have len of 4
       (hint check re.split docs for extra switches)'''
    logline = ('2017-11-03T01:00:02;challenge time,regex!.'
              'hope you join ... soon')
    return re.split('[;.,]', logline, maxsplit=3)


def get_all_hashtags_and_links():
    '''Use re.findall to extract the URL and 2 hashtags of this tweet'''
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    return re.findall(r'((?:#|http)\S+)', tweet)


def match_first_paragraph():
    '''Use re.sub to extract the content of the first paragraph (excl tags)'''
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    return re.sub(r'^<p>(.*?)</p>.*$', r'\1', html)


def find_double_words():
    '''Use re.search(regex, text).group() to find the double words'''
    text = 'Spain is so nice in the the spring'
    return re.search(r'(\b\w+)\s+\1', text).group()


def match_ip_v4_address(ip):
    '''Use re.match to match an ip v4 address (no need for exact IP ranges)'''
    return re.match(r'\d+?\.\d+?\.\d+?\.\d+', ip)


def find_all_dates():
    ''' User re.findall to extract all dates '''
    concerts_dates = ('Metallica - 27 February, 2020'
                      'Sting - 2 November, 2019'
                      'Deep Purple - 3 December, 2019'
                      'Bon Jovi - 12 July, 2019'
                      'Ed Sheeran - 12 July, 2019')
    return re.findall(r'([0-9]{1,2} +?\S+, +?[0-9]{4})', concerts_dates)


def change_function_name():
    ''' Use re.sub to change function name process() to process_data() in the log file '''
    logfile = ('2019-06-24 14:56 - function process() completed')
    return re.sub(r'(\s+)(process\(\))(\s+)', r'\1process_data()\3', logfile, re.M)


def find_flight_connections():
    ''' Use re.match to find connection at 15:00'''
    flights = ('12:30 Warsaw - Munich'
               '14:30 London - Moscow'
               '15:00 Frankfurt - NewYork'
               '15:10 Cracow - Frankfurt'
               '15:18 Milano - Lisbon')
    return re.search(r'15:00 [A-Za-z]+ ?\- ?[A-Za-z]+', flights).group()

def match_email_address(email):
    ''' User re.match to match an email address '''
    return re.match(r'.+?@.+?\.[A-Za-z0-9]{1,3}$', email)

print(find_flight_connections())