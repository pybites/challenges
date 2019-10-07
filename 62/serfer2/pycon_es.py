# coding=utf-8 -*-

import json
import requests
import sys
import pandas
import matplotlib.pyplot as plt

from scraper import NameScraper

GENDER_API_KEY = 'ERTTRyulCoHJXVhUEF'
NAMES_CACHE_FNAME = 'names.csv'
RESULTS_FNAME = 'results.csv'
PYCON_ES_SOURCES = (
    {
        'year': '2018',
        'url': 'https://2018.es.pycon.org/#schedule',
        'xpath': '//div[@class="schedule__talk--speaker"]/div/p/text()'
    }, {
        'year': '2017',
        'url': 'https://2017.es.pycon.org/es/schedule/',
        'xpath': '//div[@class="slot-inner"]/p/strong/text()'
    }, {
        'year': '2016',
        'url': 'http://2016.es.pycon.org/es/schedule/',
        'xpath': '//div[@class="slot-inner"]/p/strong/text()'
    }, {
        'year': '2015',
        'url': 'http://2015.es.pycon.org/es/schedule/',
        'xpath': '//div[@class="slot-inner"]/p/strong/text()'
    }, {
        'year': '2014',
        'url': 'http://2014.es.pycon.org/talks',
        'xpath': '//div[@id="onlytext"]/h1[@class="text-center"]/text()'
    },
    {
        'year': '2013',
        'url': 'http://2013.es.pycon.org/#agenda',
        'xpath': '//ul[@class="schedule-list"]/li/div/a[@target="_blank"]/text()'
    }
)
KNOWN_GENDERS = ['male', 'female', 'unknown']


def get_gender(name):
    """
    Gets name gender from https://gender-api.com
    """
    name_data = json.loads(requests.get(f'https://gender-api.com/get?name={name}&key={GENDER_API_KEY}').content)
    return name_data.get('gender', '')


def load_names_cache():
    """
    Read local files with names by gender
    """
    names = dict()
    with open(NAMES_CACHE_FNAME, 'r') as fi:
        lines = fi.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            name, gender = line.split(';')
            names[name] = gender
    return names


def save_names_cache(names):
    """
    Saves names and gendes in CSV
    """
    with open(NAMES_CACHE_FNAME, 'w') as fo:
        for name, gender in names.items():
            fo.write(f'{name};{gender}\n')


def save_results(results):
    """
    saves resulting data to CSV
    """
    with open(RESULTS_FNAME, 'w') as fo:
        fo.write('year,total,male,male %,female,female %\n')
        for year, res in results.items():
            female_pcnt = 0
            male_qty = len(res.get('male', []))
            female_qty = len(res.get('female', []))
            qty = female_qty + male_qty
            if qty > 0:
                female_pcnt = float(female_qty * 100.0 / qty)
                male_pcnt = float(male_qty * 100.0 / qty)
            line = '%s,%d,%d,%.02f,%d,%.02f\n' %\
                (year, qty, male_qty, male_pcnt, female_qty, female_pcnt)
            fo.write(line)


def viz_data():
    """
    Result data visualization
    """
    data_frame = pandas.read_csv(RESULTS_FNAME).sort_values('year')
    data_frame.plot(
        x='year',
        y=['male %', 'female %'],
        legend=True,
        title='speaker\'s gender evolution (%)',
        xticks=data_frame['year'].tolist(),
        kind='bar'
    )
    plt.show()


def main():
    """
    Pycon_ES girls data study
    """

    results = dict()
    names_to_gender = load_names_cache()

    for config in PYCON_ES_SOURCES:

        results[config['year']] = dict()

        scraper = NameScraper(config)
        speakers = scraper.get_names()
        results[config['year']]['speakers'] = speakers

        for gender in KNOWN_GENDERS:
            results[config['year']][gender] = list()

        for speaker in speakers:
            name = speaker.split()[0]
            gender = ''
            if name in names_to_gender:
                gender = names_to_gender[name]
            if not gender:
                gender = get_gender(name)
            names_to_gender[name] = gender
            results[config['year']][gender].append(speaker)

        data = results[config["year"]].get('female', [])
        _sp = results[config['year']]['speakers']
        if data:
            print(f'\n--- {config["year"]} ---\n{config["url"]}\n({len(data)} / {len(_sp)}): {data}')

    save_names_cache(names_to_gender)
    save_results(results)
    viz_data()

    return 0


if __name__ == '__main__':
    sys.exit(main())
