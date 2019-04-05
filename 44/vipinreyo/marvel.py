from collections import Counter, namedtuple
import csv

DATA = 'marvel-wikia-data.csv'

Character = namedtuple('Character', 'pid name sid align sex appearances year')


def convert_csv_to_dict(data=DATA):
    '''write a function to parse marvel-wikia-data.csv, see
       https://docs.python.org/3.7/library/csv.html#csv.DictReader
       should return a list of OrderedDicts or a list of Character
       namedtuples (see Character namedtuple above')'''
    with open(data) as csv_file:
        return [row for row in csv.DictReader(csv_file)]


data = list(convert_csv_to_dict())


def most_popular_characters(n=5):
    '''get the most popular character by number of appearances
       accept an argument of n (int) of most popular characters
       to return (leave default of 5)'''
    return [character['name'].split('(')[0].strip() for character in sorted(data, key=lambda x: int(x['APPEARANCES'])
            if x['APPEARANCES'] else 0, reverse=True)][:n]


def max_and_min_years_new_characters():
    '''Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)'''
    years = [character['Year'] for character in data if character['Year']]
    cnt = Counter(years)
    max_year = cnt.most_common()[0][0]
    min_year = cnt.most_common()[-1][0]
    return max_year, min_year


def percentage_female():
    '''Get the percentage of female characters, only look at male and female
       for total, ignore the rest, return a percentage rounded to 2 digits'''
    human_characters = [character['SEX'] for character in data if character['SEX'] in ('Male Characters',
                                                                                       'Female Characters')]
    cnt_human_characters = Counter(human_characters)
    total_characters = (cnt_human_characters['Female Characters'] + cnt_human_characters['Male Characters'])
    female_characters = cnt_human_characters['Female Characters']
    return round((female_characters/total_characters) * 100, 2)


def good_vs_bad(sex):
    '''Return a dictionary of bad vs good vs neutral characters.
       This function receives an arg 'sex' and should be validated
       to only receive 'male' or 'female' as valid inputs (should
       be case insensitive, so could also pass it MALE)

       The expected result should be a the following dict. The values are
       rounded (int) percentages (values made up here):

       expected = {'Bad Characters': 33,
                   'Good Characters': 33,
                   'Neutral Characters': 33})
    '''

    if not sex.lower() in ('male', 'female'):
        raise ValueError

    characters = [character['ALIGN'] for character in data if sex.title() in character['SEX']]
    cnt_characters = Counter(characters)
    total_characters = (cnt_characters['Bad Characters'] + cnt_characters['Good Characters'] +
                        cnt_characters['Neutral Characters'])

    return {
            'Bad Characters': round((cnt_characters['Bad Characters'] / total_characters) * 100),
            'Good Characters': round((cnt_characters['Good Characters'] / total_characters) * 100),
            'Neutral Characters': round((cnt_characters['Neutral Characters'] / total_characters) * 100)
            }


if __name__ == '__main__':
    most_popular_characters()
    max_and_min_years_new_characters()
    percentage_female()
    good_vs_bad('female')
    good_vs_bad('male')
