from collections import Counter, namedtuple
import csv


DATA = 'marvel-wikia-data.csv'

Character = namedtuple('Character', 'pid name sid align sex appearances year')


def main():
    most_popular_characters()
    max_and_min_years_new_characters()
    percentage_female()
    good_vs_bad('female')
    good_vs_bad('male')


def convert_csv_to_dict(data=DATA):
    '''write a function to parse marvel-wikia-data.csv, see
       https://docs.python.org/3.7/library/csv.html#csv.DictReader
       should return a list of OrderedDicts or a list of Character
       namedtuples (see Character namedtuple above')'''
    with open(data) as csv_file:
        reader = csv.DictReader(csv_file)
        return [
            Character(
                pid=int(row['page_id']),
                name=row['name'],
                sid=row['ID'],
                align=row['ALIGN'],
                sex=row['SEX'],
                appearances=row['APPEARANCES'],
                year=row['Year']
            )
            for row in reader
        ]


data = convert_csv_to_dict()


def most_popular_characters(n=5):
    '''get the most popular character by number of appearances
       accept an argument of n (int) of most popular characters
       to return (leave default of 5)'''
    return [
        character.name.split(sep=' (')[0]
        for character in data[:n]
    ]


def max_and_min_years_new_characters():
    '''Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)'''
    counter = Counter(
        character.year
        for character in data
        if character.year
    )

    min_year = min(counter, key=lambda key: counter[key])
    max_year = max(counter, key=lambda key: counter[key])
    return max_year, min_year


def percentage_female():
    '''Get the percentage of female characters, only look at male and female
       for total, ignore the rest, return a percentage rounded to 2 digits'''
    counter = Counter(
        character.sex
        for character in data
        if character.sex in {'Male Characters', 'Female Characters'}
    )
    total = sum(counter.values())
    return round((counter['Female Characters'] / total) * 100, 2)


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
    sex = sex.lower()
    if sex not in {'male', 'female'}:
        raise ValueError('Sex must be male or female.')

    sex = 'Female Characters' if sex == 'female' else 'Male Characters'
    counter = Counter(
        character.align
        for character in data
        if character.sex == sex and character.align
    )

    return {
        character_type: round((count / sum(counter.values())) * 100)
        for character_type, count in counter.items()
    }


if __name__ == '__main__':
    main()
