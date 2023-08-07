from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure, output_file, show
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, and welcome to the basic Flask with Bokeh preview.'

@app.route('/bokeh')
def bokeh():
    # init a basic circle plot
    fig = figure(plot_width=600, plot_height=600)
    fig.circle(
        [1, 2, 3, 4, 5],
        [6, 7, 2, 4, 5],
        size=30,
        color='teal',
        alpha=0.6
    )
    show(fig)

    #grab the static resources
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
