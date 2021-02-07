import pandas as pd
import numpy as np
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.sampledata.us_counties import data as counties
import requests
from bs4 import BeautifulSoup


def main():
    # towns, counties_wiki = scrape_counties()
    # data = clean_data('Personal_Income_Tax_By_Town.csv', towns, counties_wiki)
    # data.to_csv('Income_tax.csv')
    data = pd.read_csv('Income_tax.csv')
    plot(data)


def clean_data(file, towns, counties_wiki):
    raw_data = pd.read_csv('Personal_Income_Tax_By_Town.csv')
    income_tax = raw_data[raw_data['Tax Year'] == 2017]
    income_tax = income_tax.sort_values(by=['Municipality'])['CT Income Tax']
    data = pd.DataFrame(
        {'towns': towns, 'county': counties_wiki, 'income_tax': income_tax})
    return data


def scrape_counties():
    url = 'https://en.wikipedia.org/wiki/List_of_towns_in_Connecticut'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    page = requests.get(url, headers=headers, verify=False).text
    soup = BeautifulSoup(page, 'lxml')
    ancors = soup.select(
        '#mw-content-text > div > table > tbody > tr > td > a') 
    ancors_text = [el.contents[0] for el in ancors if el.contents[0] != 'Podunk']  
    towns = [town for town in ancors_text[::4]]
    counties_wiki = [" ".join(county.split()[:-1]) if county.split()[-1] == 'County' else county for county in ancors_text[3::4]]
    return towns, counties_wiki


def plot(data):
    output_file('report.html')
    palette.reverse()

    counties_info = {
        code: county for code, county in counties.items() if county["state"] == "ct"
    }
    # Latitude and longitude of counties
    count_xs = [county['lons'] for county in counties_info.values()]
    count_ys = [county['lats'] for county in counties_info.values()]
    
    # Names of counties
    county_names = [county['name'] for county in counties_info.values()]    
    county_income_tax = [np.sum(data[data['county'] == name]['income_tax'])
                         for name in county_names]
    
    color_mapper = LogColorMapper(palette=palette)

    data_source = dict(
        x=count_xs,
        y=count_ys,
        name=county_names,
        income_tax=county_income_tax,
    )

    TOOLS = "pan,wheel_zoom,reset,hover,save"
    # hover = HoverTool()
    fig = figure(
        title="Connecticut income tax, 2017", tools=TOOLS,
        x_axis_location=None, y_axis_location=None,
        tooltips=[
            ("Name", "@name"), 
            ("Income Tax)","@income_tax"), 
            ("(Long, Lat)", "($x, $y)")
        ]
    )

    fig.grid.grid_line_color = None
    fig.hover.point_policy = "follow_mouse"

    fig.patches('x', 'y', source=data_source,
                fill_color={'field': 'income_tax', 'transform': color_mapper},
                fill_alpha=0.7, line_color="white", line_width=0.5)

    show(fig)


if __name__ == "__main__":
    main()
