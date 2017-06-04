import csv
import os
from pprint import pprint as pp
import re

import requests
from bs4 import BeautifulSoup as soup

# Eurostat
# Electricity prices components for domestic consumers
# filtered on 2016 / Band DC 2500-5000 kWh
# http://ec.europa.eu/eurostat/web/energy/data/database
DATA_DIR = 'data'
PRICES_CSV = os.path.join(DATA_DIR, 'nrg_pc_204_c_1_Data.csv')
POWER_TABLE = os.path.join(DATA_DIR, 'power-table')
POWER_TABLE_URL = 'https://www.wholesalesolar.com/solar-information/how-to-save-energy/power-table'


def get_energy_prices():
    with open(PRICES_CSV) as f:
        for row in csv.DictReader(f):
            yield row['GEO'], row['Value']


def _get_power_table():
    try:
        with open(POWER_TABLE) as f:
            html = f.read()
    except IOError:
        print('no local power table, get it from the web')
        r = requests.get(POWER_TABLE_URL)
        html = r.text
    s = soup(html, 'lxml')
    return s.find('table', attrs={'class': 'powerTable'})


def get_appliance_wattages():
    table = _get_power_table()
    rows = table.findAll('tr')
    for tr in rows:
        cols = tr.findAll('td')
        for td in cols:
            # Flat is better than nested.
            # still bit too long, need to refactor
            # parsing html tables sucks
            try:
                bgcolor = td["bgcolor"].lower()
            except KeyError:
                continue
            if 'e0e0e0' not in bgcolor:
                continue
            appliance = td.text.strip()
            if not appliance:
                continue
            wattage = td.findNext('td')
            wattage = wattage.text.strip()
            if not wattage or not re.search(r'^[0-9]', wattage):
                continue
            if '/day' in wattage:
                continue
            wattage = re.sub(r'([-,0-9]+).*', r'\1', wattage)
            wattage = wattage.replace(',', '')
            if '-' in wattage:
                low, high = wattage.split('-')
                wattage = (int(low) + int(high)) / 2
            yield appliance, int(wattage)


wattages = dict(get_appliance_wattages())
prices = dict(get_energy_prices())


if __name__ == '__main__':
    # WTF Spain 2nd?!
    pp(sorted(prices.items(),
              key=lambda x: x[1],
              reverse=True))

    pp(wattages)
