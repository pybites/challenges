from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
#from bokeh.util.string import encode_utf8
import pandas as pd


csv_data_url = "static/data/Accidental_Drug_Related_Deaths_2012-2018.csv"

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!<br/><br/><a href="/bokeh">Bokeh</a>'


@app.route('/bokeh')
def bokeh():
    # init a basic bar chart:
    # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
    df = pd.read_csv(csv_data_url, parse_dates=['Date'])
    fig = figure(plot_width=800, plot_height=400, x_axis_type="datetime", title="Accident drug related death")
    fig.grid.grid_line_alpha = 0.3
    fig.xaxis.axis_label = 'Date'
    fig.yaxis.axis_label = 'Age'
    fig.line(df['Date'], df['Age'], color='#A6CEE3', legend_label='ResidenceState', alpha=1)
    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    # render template
    script, div = components(fig)
    html = render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return html.encode("utf-8") #encode_utf8(html)


if __name__ == '__main__':
    app.run(debug=True)
