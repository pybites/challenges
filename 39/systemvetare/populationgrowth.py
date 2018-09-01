from collections import namedtuple
from urllib.request import urlretrieve
import csv

# this script retrieves a csv of UN population data and prints the countries with the highest absolute growth 1950-2015

# number of countries to list
MAX_COUNTRIES = 10

# retrieves the csv
Country = namedtuple('Country', 'population_1950 population_2015 absolute_growth relative_growth')
population_data = 'https://raw.githubusercontent.com/curran/data/gh-pages/un/population/wpp2017/' \
                  'WPP2017_POP_F01_1_TOTAL_POPULATION_BOTH_SEXES.csv'
population_csv = 'population.csv'
urlretrieve(population_data, population_csv)


# reads the csv and returns a dict of named tuples (countries)
def get_population_by_country(data=population_csv):
    with open(data, encoding='utf-8') as f:
        countries = dict()
        for line in csv.DictReader(f):
            try:
                if int(line['Country code']) < 900:  # filters out *most* regions, subregions or areas
                    country = line['Region, subregion, country or area *']
                    population_1950 = int(line['1950'].replace(' ', '')) * 1000
                    population_2015 = int(line['2015'].replace(' ', '')) * 1000
                else:
                    continue
            except ValueError:
                print(f'Ignoring ValueError')
                continue
            countries[country] = Country(population_1950=population_1950, population_2015=population_2015,
                                         absolute_growth=get_absolute_growth(population_2015, population_1950),
                                         relative_growth=get_relative_growth(population_2015, population_1950))
        return countries


# calculates the absolute growth in population 1950 - 2015
def get_absolute_growth(population_2015, population_1950):
    return population_2015 - population_1950


# calculates the relative growth in population 1950 - 2015
def get_relative_growth(population_2015, population_1950):
    return round(((get_absolute_growth(population_2015, population_1950)) / population_1950) * 100, 1)


# prints the results, could be prettier
def print_results(countries):
    sorted_countries = sorted(countries.items(), key=lambda c: c[1].absolute_growth,
                              reverse=True)  # sorts descending by absolute growth
    for counter, country in enumerate(sorted_countries):
        print(f'{counter+1}. {country[0]}: 1950:{country[1].population_1950}, 2015:{country[1].population_2015}, '
              f'{country[1].absolute_growth}, {country[1].relative_growth}%')
        if counter == MAX_COUNTRIES-1:
            break


def main():
    countries = get_population_by_country()
    print_results(countries)


if __name__ == '__main__':
    main()



