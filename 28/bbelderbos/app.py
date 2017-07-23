from flask import Flask, render_template

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.models import ColumnDataSource, LabelSet

from get_data import get_word_counts_per_month

TITLE = 'Word count of PyBites over time'

app = Flask(__name__)


@app.route('/')
def index():
    x_values, y_values = get_word_counts_per_month()

    # init a basic bar chart:
    # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
    fig = figure(plot_width=1200,
                 plot_height=600,
                 title=TITLE,
                 x_axis_type="datetime")

    fig.background_fill_color = "#dddddd"
    fig.grid.grid_line_color = "white"

    fig.vbar(
        x=x_values,
        width=0.5,
        bottom=0,
        top=y_values,
        fill_color="#b3de69",
    )

    # add labels
    # http://bokeh.pydata.org/en/latest/docs/user_guide/annotations.html
    top_counts = [(x, y, '{} ({})'.format(x, y))
                  for x, y in zip(x_values, y_values)
                  if y > 1000]

    source = ColumnDataSource(data=dict(months=[x[0] for x in top_counts],
                                        wcs=[x[1] for x in top_counts],
                                        labels=[x[2] for x in top_counts]))

    labels = LabelSet(x='months',
                      y='wcs',
                      text='labels',
                      level='glyph',
                      x_offset=5,
                      y_offset=5,
                      source=source,
                      render_mode='canvas',
                      text_font_size='7pt')
    fig.add_layout(labels)

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


if __name__ == '__main__':
    app.run(debug=True)
