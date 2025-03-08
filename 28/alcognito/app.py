'''10 May 2020

https://codechalleng.es/challenges/28/ - Integrate a Bokeh Chart Into Flask

The instructions point to a flask-bokeh tutorial from July 2017, which includes
flask==0.12.2 and bokeh==0.12.6
(https://github.com/realpython/flask-bokeh-example/blob/master/tutorial.md)

I used the latest available versions of flask(==1.1.2) & bokeh(==2.0.2)
I had to make some minor changes to the code as per the notes included below
as encode_utf8 was removed from bokeh==2.0.0
'''

from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
#from bokeh.util.string import encode_utf8  #encode_utf8 has been removed from this library

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bokeh')
def bokeh():

    # init a basic bar chart:
    # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
    fig = figure(plot_width=600, plot_height=600)
    fig.vbar(
        x=[1, 2, 3, 4],
        width=0.5,
        bottom=0,
        top=[1.7, 2.2, 4.6, 7.6],
        color='navy'
    )

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(fig)
    html = render_template(
        'wyndham.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return html # this line used to be return encode_utf8(html)

@app.route('/wyndham')
def wyndham():
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
    a = r.json()


    res = json_normalize(a['features'])
    res['properties.date_stamp'] = pd.to_datetime(res['properties.date_stamp'])
    gby = res.groupby('properties.system_name')
    sites = res['properties.system_name'].unique()
    num_sites = len(sites)

    #output_file('wyndham.html')
    plot_colors = linear_palette(Viridis256, num_sites)
    p = figure(width=1800, height=900, x_axis_type="datetime")

    count = 0
    for key, grp in gby:
        line_col = plot_colors[count]
        g = grp.sort_values(by='properties.date_stamp')
        site_data = g[['properties.date_stamp','properties.energy_prod(KWh)']]
#        site_data['properties.date_stamp'] = pd.to_datetime(site_data['properties.date_stamp'])
        site_cds = ColumnDataSource(site_data) 
        p.line(x=site_data['properties.date_stamp'], y=site_data['properties.energy_prod(KWh)'], 
                legend_label=key, line_width = 2, line_color = line_col)
        count += 1

    #show(p)
    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(p)
    html = render_template(
        'wyndham.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return html



if __name__ == '__main__':
    app.run(debug=True)