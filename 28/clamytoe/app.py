import webbrowser

from math import pi
from os import path

import pandas as pd

from bokeh.embed import components
from bokeh.models import Title, BoxAnnotation
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    filename = 'dfw.csv'
    exists = path.isfile(filename)

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

    # save to csv file
    if not exists:
        tables = pd.read_html('https://en.tutiempo.net/climate/ws-722590.html', header=0)
        tables[3].to_csv(filename, index=False)

    # import saved data
    data = pd.read_csv('dfw.csv', header=0)

    # convert data into lists
    time_range = []
    avg_temp = []
    avg_max_temp = []
    avg_min_temp = []

    for i, year in enumerate(data.Year):
        T = resource_check(data['T'][i])
        TM = resource_check(data['TM'][i])
        Tm = resource_check(data['Tm'][i])
        # exclude any year that's missing any data
        if T is not None or TM is not None or Tm is not None:
            time_range.append(year)
            avg_temp.append(celsius_to_fahrenheit(T))
            avg_max_temp.append(celsius_to_fahrenheit(TM))
            avg_min_temp.append(celsius_to_fahrenheit(Tm))

    # overall size and look of graph
    fig = figure(title='DFW Average Temperatures ({}-{})'.format(time_range[0], time_range[-1]),
                 toolbar_location="above",
                 plot_width=1024, plot_height=480)

    # x/y axis for the lines
    x = time_range
    average = avg_temp
    maximum = avg_max_temp
    minimum = avg_min_temp

    # upper and lower limits for the box annotations
    lower_limit = (min(average) - max(minimum)) / 2 + max(minimum)
    upper_limit = (min(maximum) - max(average)) / 2 + max(average)
    low_box = BoxAnnotation(top=lower_limit, fill_alpha=0.1, fill_color='blue')
    mid_box = BoxAnnotation(bottom=lower_limit, top=upper_limit, fill_alpha=0.1, fill_color='green')
    high_box = BoxAnnotation(bottom=upper_limit, fill_alpha=0.1, fill_color='red')

    # plot each of the lines
    fig.line(x, average, line_width=2, legend='avg', line_dash=[4, 4], line_color='green')
    fig.line(x, maximum, line_width=2, legend='max', line_color='red')
    fig.line(x, minimum, line_width=2, legend='min', line_color='blue')

    # configure the x axis
    # fig.xaxis.ticker = time_range[::2]
    fig.xaxis.ticker = time_range
    fig.xaxis.major_label_orientation = pi / 4

    # add circles to each data point on the lines
    fig.circle(x, minimum, fill_color=None, line_color='blue', size=8, legend='min')
    fig.circle(x, average, fill_color=None, line_color='green', size=8, legend='avg')
    fig.circle(x, maximum, fill_color=None, line_color='red', size=8, legend='max')
    fig.yaxis[0].axis_label = 'Average Temperatures (Fahrenheit)'

    # tweak the graph
    fig.add_layout(Title(text="Year's not included had missing data", align='center'), 'below')
    fig.add_layout(low_box)
    fig.add_layout(mid_box)
    fig.add_layout(high_box)

    # tweak the legend
    fig.legend.label_standoff = 5
    fig.legend.location = 'top_left'
    fig.legend.background_fill_alpha = 0.5

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

    return encode_utf8(html)


def resource_check(data):
    if '-' not in data:
        return float(data)
    else:
        return None


def celsius_to_fahrenheit(temp):
    """Simple temperature conversion Cº to Fº"""
    return temp * 1.8 + 32


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run()
