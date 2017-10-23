from bokeh.embed import components
from bokeh.plotting import figure
from flask import Flask, render_template, request
import pandas as pd
import asutosh

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():

    # Default values to take care of a GET request.
    first_country = "India"
    second_country = "Pakistan"
    attribute = "per_capita_income"

    if request.method == "POST":
        first_country = request.form["first_country_name"]
        second_country = request.form["second_country_name"]
        attribute = request.form["attribute_name"]

    # Create the plot
    plot = asutosh.create_figure(first_country, second_country, attribute)

    # get countries available in the dataset
    country_names = asutosh.get_countries()  

    # attributes
    attribute_names = ["population", "per_capita_income", "life_expectancy"]

    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    return render_template("index.html", script = script, div = div,
        attribute_names = attribute_names,  current_attribute_name = attribute, 
        country_names = country_names, first_country = first_country, second_country = second_country)

# With debug=True, Flask server will auto-reload 
# when there are code changes

def main():
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    main()
