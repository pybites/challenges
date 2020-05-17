import pandas as pd
import json
from datetime import datetime
from pandas import json_normalize
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import linear_palette, Viridis256


output_file('wyndham.html')


with open('wyndham_data.txt', 'r') as f:
    a = json.load(f)

res = json_normalize(a['features'])
gby = res.groupby('properties.system_name')

sites = res['properties.system_name'].unique()
#print(sites)
num_sites = len(sites)
#print(num_sites)

plot_colors = linear_palette(Viridis256, num_sites)
p = figure(width=1800, height=800, x_axis_type="datetime", title = "Wyndham Wind Farm Scheme Daily Power Output")
p.yaxis.axis_label = "Daily Power Output (kW.h)"

count = 0
for key, grp in gby:
    line_col = plot_colors[count]
    g = grp.sort_values(by='properties.date_stamp')
    site_data = g[['properties.date_stamp','properties.energy_prod(KWh)']]
    site_data['properties.date_stamp'] = pd.to_datetime(site_data['properties.date_stamp'])
    #print(site_data['properties.date_stamp'])
    site_cds = ColumnDataSource(site_data)
    
    p.line(x=site_data['properties.date_stamp'], y=site_data['properties.energy_prod(KWh)'], 
            legend_label=key, line_width = 2, line_color = line_col)
    count += 1

show(p)


#for key, grp in gby:
#    g = grp.sort_values(by='properties.date_stamp')
#    p.multi_line(g)
    #print(f'xs = {xs}, ys = {ys}')


#    sorted['properties.date_stamp', 'properties.energy_prod(KWh)']]
#    xs = grp['']
#    print(grp)



#plot_colors = Spectral11[0:num_sites]





#for key, item in gby:
#    g = item.sort_values(by='properties.date_stamp')
#    source = ColumnDataSource(x = g[['properties.date_stamp']], 
#            y = g[['properties.energy_prod(KWh)']])
#    p.line(x = properties.date_stamp , y= properties.energy_prod(KWh), source=source)


#show(p)

#print(source)
    #item[sorted['properties.date_stamp', 'properties.energy_prod(KWh)']])

#dfs = [pd.DataFrame(res.loc[i].values, columns = res.columns) for i in res['properties.system_name'].str.strip('\xa0 ').unique()]
#source = ColumnDataSource(dict(x = [res['properties.date_stamp'].values  for df in dfs], y = [res['properties.energy_prod(KWh)'].values for df in dfs]))
#p = figure()
#p.multi_line(x, y, source = source )
#show(p)


#print(res[['properties.system_name', 'properties.date_stamp', 'properties.energy_prod(KWh)']].sort_values(by='properties.system_name'))
#for feature in res:
#    print(feature)


#df = pd.read_json(a)
#print(df.head())