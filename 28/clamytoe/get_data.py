import pandas as pd

# header info
#  T: Average annual temperature
# TM: Annual average maximum temperature
# Tm: Average annual minimum temperature
# PP: Rain or snow precipitation total annual
#  V: Annual average wind speed
# RA: Number of days with rain
# SN: Number of days with snow
# TS: Number of days with storm
# FG: Number of foggy days
# TN: Number of days with tornado
# GR: Number of days with hail
tables = pd.read_html('https://en.tutiempo.net/climate/ws-722590.html', header=0)
# tables[3].to_csv('dfw.csv', index=False)
print(tables[3])
print('\nDescribe:')
print(tables[3]['TM'].describe())
print('\nGroup By:')
print(tables[3].groupby('TM').count())
print('\nUnique:')
print(tables[3]['Year'].unique())
