from flask import Flask, render_template

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

import pandas as pd

app = Flask(__name__)

CBA = 'data_sets/cba.csv'
NAB = 'data_sets/nab.csv'
ANZ = 'data_sets/anz.csv'
WESTPAC = 'data_sets/wbc.csv'


@app.route("/")
def stock_price_chart():

    # Reading the Stock prices using Pandas CSV function
    anz = pd.read_csv(ANZ, parse_dates=['Date'])
    cba = pd.read_csv(CBA, parse_dates=['Date'])
    nab = pd.read_csv(NAB, parse_dates=['Date'])
    westpac = pd.read_csv(WESTPAC, parse_dates=['Date'])

    # Creating the figure and setting the necessary parameters for the plot
    price = figure(width=800, height=400, x_axis_type="datetime", title="AUS Big 4 Banks Historical Price Series from "
                                                                        "2006")
    price.grid.grid_line_alpha = 0.3
    price.xaxis.axis_label = 'Date'
    price.yaxis.axis_label = 'Price'

    price.line(anz['Date'], anz['Adj Close'], color='#A6CEE3', legend='ANZ', alpha=1)
    price.line(cba['Date'], cba['Adj Close'], color='#B2DF8A', legend='CBA', alpha=1)
    price.line(nab['Date'], nab['Adj Close'], color='#33A02C', legend='NAB', alpha=1)
    price.line(westpac['Date'], westpac['Adj Close'], color='#FB9A99', legend='WESTPAC', alpha=1)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(price)

    # Render the html template
    html = render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources
    )

    return encode_utf8(html)


if __name__ == '__main__':
    app.run(debug=True)
