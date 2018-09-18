from flask import Flask, render_template, request
import pandas as pd
from bokeh.plotting import figure, output_file
from bokeh.embed import components

app = Flask(__name__)

# Load the Iris Data Set
data = pd.read_csv('data/gapminder.csv')
data = data[(data.Year >= 1950)]
country_names = list(set(data.Country))
attribute_names = data.columns[2:-1].values.tolist()


# Create the main plot
def create_figure(first_country='India',
                  second_country='Pakistan',
                  selected_attribute='income'):

    # filter datasets according to country
    first_country_data = data[(data.Country == first_country)]
    second_country_data = data[(data.Country == second_country)]

    first_country_data_attribute = list(first_country_data[selected_attribute])
    second_country_data_attribute = list(second_country_data[selected_attribute])

    years = list(first_country_data["Year"])
    # output to static HTML file
    output_file("gapminder.html")

    # create a new plot
    p = figure(title="Country Data Analysis", x_axis_label='Years',width=1280, height=720)

    p.line(years, first_country_data_attribute, legend=first_country, line_color="blue", line_width=3)

    p.line(years, second_country_data_attribute, legend=second_country, line_color="green", line_width=3)
    return p


# Index page
@app.route('/', methods=['GET', 'POST'])
def index():
    first_country = "India"
    second_country = "Pakistan"
    selected_attribute = "income"
    if request.method == 'POST':
        first_country = request.form["first_country"]
        second_country = request.form["second_country"]
        selected_attribute = request.form["selected_attribute"]
    # Create the plot
    plot = create_figure(first_country, second_country, selected_attribute)
    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    return render_template("index.html",
                           script=script,
                           div=div,
                           country_names=country_names,
                           attribute_names=attribute_names,
                           selected_attribute=selected_attribute,
                           first_country=first_country,
                           second_country=second_country)


# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)
