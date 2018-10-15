# project/server/main/views.py


import datetime
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import INLINE
from flask import render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy

from project.server.models import Rate


main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/')
def home():
    historical = get_historical_data()
    chart = create_chart(historical)

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(chart)

    return render_template(
        'main/home.html',
        points=len(historical),
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )


def get_historical_data():
    results = Rate.query.all()
    return [u.__dict__ for u in results]


def create_chart(data):
    data.sort(key=lambda d: d['timestamp'])
    # create figure
    p = figure(
        x_axis_label='time',
        y_axis_label='price',
        x_axis_type="datetime",
        width=1000,
        height=500
    )
    # get x and y axis data
    curr_1_x = []
    curr_1_y = []
    curr_2_x = []
    curr_2_y = []
    curr_3_x = []
    curr_3_y = []

    for value in data:
        time = datetime.datetime.strptime(
            str(value['timestamp']), '%Y-%m-%d %H:%M:%S')
        if value['currency'] == 'bitstamp':
            curr_1_x.append(time)
            curr_1_y.append(value['price'])
        if value['currency'] == 'kraken':
            curr_2_x.append(time)
            curr_2_y.append(value['price'])
        if value['currency'] == 'bittrex':
            curr_3_x.append(time)
            curr_3_y.append(value['price'])

    p.line(curr_1_x, curr_1_y, color='red', legend='bitstamp', line_width=2)
    p.line(curr_2_x, curr_2_y, color='green', legend='kraken', line_width=2)
    p.line(curr_3_x, curr_3_y, color='black', legend='bittrex', line_width=2)
    p.legend.location = 'bottom_left'

    return p
