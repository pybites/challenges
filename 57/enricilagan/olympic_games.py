import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
import os
import zipfile

# upload the data to Python

loc = '/Users/enricilagan/100days/pycharm/data/olympic-games.zip'
dst = '/Users/enricilagan/100days/pycharm/data/'
wrk_dir = '/Users/enricilagan/100days/pycharm'

if not os.path.isfile(dst+'summer.csv'):
    print('Extract Zip File')
    with zipfile.ZipFile(loc, 'r') as zf:
        zf.extractall(dst)

if not os.getcwd() == wrk_dir:
    os.chdir(wrk_dir)

summer = pd.read_csv('data/summer.csv')
winter = pd.read_csv('data/winter.csv')
dct = pd.read_csv('data/dictionary.csv')

# Inspect the data

print(winter[0:5])

print(summer[0:5])
print()

# Tidying Data
print('Getting Columns')
print(summer.columns)
print()
print('Getting Shape of file')
print(summer.shape)
print()

# Check for missing values
print(summer.info())

summer['Season'] = 'Summer'
winter['Season'] = 'Winter'

total = pd.concat([summer, winter])
print()

# Since URS is now Russia, change all URS to RUS

summer.loc[summer['Country'] == 'URS', 'Country'] = 'RUS'
summer.loc[summer['Country'] == 'FRG', 'Country'] = 'GER'
summer.loc[summer['Country'] == 'GDR', 'Country'] = 'GER'

for x in 'Men Women'.split():
    athlete = Counter(summer['Athlete'][summer.Gender == x])
    a = athlete.most_common(1)[0]
    name = ' '.join(a[0].title().split(', '))
    print('{} won the most number for medals for {}, total of {} medals'.format(name, x, a[1]))

print()

for x in 'Men Women'.split():
    country = Counter(summer['Country'][summer.Gender == x])
    print('Top 10 countries with most medal won for {}'.format(x))
    b = country.most_common(10)
    print(b)
print()




