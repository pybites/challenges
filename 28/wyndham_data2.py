import requests
import pandas as pd
import json
from datetime import datetime
from pandas import json_normalize
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import linear_palette, Viridis256

URL = "https://data.gov.au/data/dataset/aa75879c-1d3e-4ad2-b331-826032c6b84b/resource/6e309687-023b-436b-9079-582b7e2fb074/download/wyndham-solar-energy-production.json"

r = requests.get(URL)
a = json.loads(r.text)


res = json_normalize(a['features'])
gby = res.groupby('properties.system_name')
sites = res['properties.system_name'].unique()
num_sites = len(sites)

output_file('wyndham.html')
plot_colors = linear_palette(Viridis256, num_sites)
p = figure(width=1200, height=1200, x_axis_type="datetime")

count = 0
for key, grp in gby:
    line_col = plot_colors[count]
    g = grp.sort_values(by='properties.date_stamp')
    site_data = g[['properties.date_stamp','properties.energy_prod(KWh)']]
    site_data['properties.date_stamp'] = pd.to_datetime(site_data['properties.date_stamp'])
    site_cds = ColumnDataSource(site_data) 
    p.line(x=site_data['properties.date_stamp'], y=site_data['properties.energy_prod(KWh)'], 
            legend_label=key, line_width = 2, line_color = line_col)
    count += 1

show(p)
