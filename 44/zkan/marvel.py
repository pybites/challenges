from collections import Counter, namedtuple
import csv
import re


DATA = 'marvel-wikia-data.csv'

Character = namedtuple('Character', 'pid name sid align sex appearances year')


def convert_csv_to_dict(data=DATA):
    '''write a function to parse marvel-wikia-data.csv, see
       https://docs.python.org/3.7/library/csv.html#csv.DictReader
       should return a list of OrderedDicts or a list of Character
       namedtuples (see Character namedtuple above')'''
    with open(data) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield Character(
                pid=row['page_id'],
                name=row['name'].split('(')[0].strip(),
                sid=row['ID'],
                align=row['ALIGN'],
                sex=row['SEX'],
                appearances=row['APPEARANCES'] if row['APPEARANCES'] else 0,
                year=row['Year'],
            )


data = list(convert_csv_to_dict())


def most_popular_characters(n=5):
    '''get the most popular character by number of appearances
       accept an argument of n (int) of most popular characters
       to return (leave default of 5)'''
    sorted_data = sorted(data, key=lambda x: int(x.appearances), reverse=True)
    return [each.name for each in sorted_data][:n]


def max_and_min_years_new_characters():
    '''Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)'''
    years = [each.year for each in data if each.year]
    cnt = Counter(years)
    max_year = cnt.most_common()[0][0]
    min_year = cnt.most_common()[-1][0]
    return (max_year, min_year)


def percentage_female():
    '''Get the percentage of female characters, only look at male and female
       for total, ignore the rest, return a percentage rounded to 2 digits'''
    character_sex = [each.sex for each in data]
    cnt = Counter(character_sex)
    total = cnt['Male Characters'] + cnt['Female Characters']
    return round(cnt['Female Characters'] / total * 100, 2)


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
    if sex.lower() not in ('male', 'female'):
        raise ValueError

    characters = [each.align for each in data if sex.title() in each.sex]
    cnt = Counter(characters)
    total = (cnt['Bad Characters'] +
             cnt['Good Characters'] +
             cnt['Neutral Characters'])

    return {
        'Bad Characters': round((cnt['Bad Characters'] / total) * 100),
        'Good Characters': round((cnt['Good Characters'] / total) * 100),
        'Neutral Characters': round((cnt['Neutral Characters'] / total) * 100),
    }


if __name__ == '__main__':
    most_popular_characters()
    max_and_min_years_new_characters()
    percentage_female()
    good_vs_bad('female')
    good_vs_bad('male')
