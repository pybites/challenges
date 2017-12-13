from collections import Counter, namedtuple
from decimal import Decimal
import csv

DATA = 'marvel-wikia-data.csv'

Character = namedtuple('Character', 'pid name sid align sex appearances year')


def convert_csv_to_dict(data=DATA):
    """write a function to parse marvel-wikia-data.csv, see
       https://docs.python.org/3.7/library/csv.html#csv.DictReader
       should return a list of OrderedDicts or a list of Character
       namedtuples (see Character namedtuple above')"""
    with open(data) as f:
        return [row for row in csv.DictReader(f)]


data = list(convert_csv_to_dict())


def most_popular_characters(n=5):
    """get the most popular character by number of appearances
       accept an argument of n (int) of most popular characters
       to return (leave default of 5)"""
    max_appearance = []
    count = 0
    for row in data:
        if count < n:
            max_appearance.append(row['name'].split(' (')[0])
            count += 1
    return max_appearance


def max_and_min_years_new_characters():
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)"""
    first_appeared_years = []
    for row in data:
        year = row['Year']
        if year:
            first_appeared_years.append(year)
    c = Counter(first_appeared_years)
    max_ = c.most_common()[0][0]
    min_ = c.most_common()[-1][0]
    return max_, min_


def percentage_female():
    """Get the percentage of female characters, only look at male and female
       for total, ignore the rest, return a percentage rounded to 2 digits"""
    characters = []
    for row in data:
        sex = row['SEX'].lower()
        if sex.startswith('male') or sex.startswith('female'):
            characters.append(sex)

    c = Counter(characters)
    percent = Decimal(c['female characters'] / sum(c.values())) * 100
    return float(round(percent, 2))


def good_vs_bad(sex):
    """Return a dictionary of bad vs good vs neutral characters.
       This function receives an arg 'sex' and should be validated
       to only receive 'male' or 'female' as valid inputs (should
       be case insensitive, so could also pass it MALE)

       The expected result should be a the following dict. The values are
       rounded (int) percentages (values made up here):

       expected = {'Bad Characters': 33,
                   'Good Characters': 33,
                   'Neutral Characters': 33})
    """
    alignments = []
    valid_genders = ['female', 'male']
    gender = sex.lower()

    if gender in valid_genders:
        for row in data:
            if row['SEX'].lower().startswith(gender):
                align = row['ALIGN']
                if align:
                    alignments.append(align)

        raw_stats = Counter(alignments)

        good = round(Decimal(raw_stats['Good Characters'] / sum(raw_stats.values()) * 100))
        bad = round(Decimal(raw_stats['Bad Characters'] / sum(raw_stats.values()) * 100))
        neutral = round(Decimal(raw_stats['Neutral Characters'] / sum(raw_stats.values()) * 100))

        stats = {'Bad Characters': bad,
                 'Good Characters': good,
                 'Neutral Characters': neutral}

        return stats
    else:
        raise ValueError


if __name__ == '__main__':
    most_popular_characters()
    max_and_min_years_new_characters()
    percentage_female()
    good_vs_bad('female')
    good_vs_bad('male')
