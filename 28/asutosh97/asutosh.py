# get both the countries and attribute value from drop-down
import pandas as pd
from bokeh.plotting import figure, show, output_file

def read_data():
	data = pd.read_csv('datasets/gapminder.csv')
	data = data[(data.Year >= 1950)]
	return data

def create_figure(first_country, second_country, attribute):
	# read from csv
	data = read_data()

	# filter datasets according to country
	first_country_data = data[(data.Country == first_country)]
	
	second_country_data = data[(data.Country == second_country)]

	# get required attribute out of filtered datasets of both countries and turn them to list
	first_country_data_attribute = list(first_country_data[attribute])
	second_country_data_attribute = list(second_country_data[attribute])
	years = list(first_country_data["Year"])

	# create a new plot
	p = figure(title = (first_country + " Vs " + second_country + " in " + attribute), x_axis_label='Years', plot_width=1280, plot_height=720)

	# plot for first-country
	p.line(years, first_country_data_attribute, legend = first_country, line_color="blue", line_width=3)

	# plot for second-country
	p.line(years, second_country_data_attribute, legend = second_country, line_color="green", line_width=3)

	return p

def get_countries():
	# get countries column as a list
	return sorted(list(set(read_data()['Country'])))

def main():
	p = create_figure("India", "Pakistan", "income")
	output_file('output_files/new.html')
	show(p)

if __name__ == "__main__":
	main()