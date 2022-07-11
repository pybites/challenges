import hashlib  # needed for API auth
import json  # use dumps and loads
import os
import time
from datetime import datetime
import argparse
import requests  # call Marvel API
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import functools

# This articles helped me a lot:
# https://realpython.com/primer-on-python-decorators/
# https://realpython.com/python-data-visualization-bokeh/
# https://realpython.com/command-line-interfaces-python-argparse/
# Cool challenge

today = datetime.today()

PUBLIC_KEY = os.environ['PUBLIC_KEY_MARVEL']
PRIVATE_KEY = os.environ['PRIVATE_KEY_MARVEL']

# https://developer.marvel.com/documentation/authorization
# "Authentication for Server-Side Applications" section
ENDPOINT = 'https://gateway.marvel.com:443/v1/public/{}?ts={}&' \
           'apikey={}&hash={}&limit=50'

MARVEL_OBJECTS = ['comics', 'characters', 'stories', 'series', 'creators']


def user_input():
    """
    Function that handles the inputs from the command line.
    :return:
    """
    parser = argparse.ArgumentParser(prog="marvel_data",
                                     usage="%(prog)s names of endpoints",
                                     description="Fetch data from marvel's API",
                                     epilog="Enjoy! :)")
    parser.add_argument("endpoints",
                        help="make an API request to the specific endpoints",
                        action="store",
                        nargs="+",
                        default="comics")
    args = parser.parse_args()
    endpoints = args.endpoints
    return endpoints


def cache_marvel_data(func):
    """This is a decorator to cache Marvel API JSON data to a .txt file,
        there must be a better way...:( what I do is look if the endpoint is already request in a life time of 1 day.
    """

    @functools.wraps(func)
    def wrapper_cache(end_point):
        with open('cache.txt', 'r+') as f:
            lines = f.read().splitlines()
            try:
                if lines:
                    last_update = lines[0]
                    if end_point not in lines[1:]:
                        f.write('{}\n'.format(end_point))
                        return func(end_point)
                    elif abs(datetime.fromisoformat(last_update) - today).days > 1:
                        f.truncate(0)
                        f.write('{}\n{}\n'.format(today, end_point))
                        return func(end_point)
                else:
                    f.write('{}\n{}\n'.format(today, end_point))
                    return func(end_point)
            except Exception as err:
                print(err)

    return wrapper_cache


@functools.lru_cache(maxsize=32)
@cache_marvel_data
def get_api_endpoint(endpoint):
    """
    Given an endpoint fetch the data corresponding to that endpoint from the Marvel's API, and store tha data in a json
    file to later be processed by the clean_data() function.
    :param endpoint:
    :return:
    """
    time_obj = time.localtime(time.time())
    time_stamp = f'{time_obj.tm_mday}-{time_obj.tm_mon}-{time_obj.tm_year} ' \
                 f'{time_obj.tm_hour}:{time_obj.tm_min}:{time_obj.tm_sec}'
    public_key = PUBLIC_KEY
    h = hashlib.md5()
    text_to_hash = time_stamp + PRIVATE_KEY + public_key
    h.update(text_to_hash.encode('utf-8'))
    hash_param = h.hexdigest()
    try:
        url = ENDPOINT.format(endpoint, time_stamp, public_key, hash_param)
        response = requests.get(url)
        with open(f"{endpoint}.json", 'w') as file:
            json.dump(response.json(), file)
        time.sleep(5)
    except requests.exceptions.HTTPError as err:
        print(err)


def clean_data():
    """
    Prepare the data to be processed by the fit_data() and the graph() functions.
    :return: Cleaned data
    """
    import pandas as pd
    import json
    with open('characters.json') as f:
        js = json.load(f)
    names = [id['name'] for id in js['data']['results']]
    labels = ['comics', 'stories']
    datos = [[id[label]['available'] for label in labels] for id in js['data']['results']]
    data = pd.DataFrame(datos, columns=labels, index=names)
    data = data[data['comics'] > 0].reset_index()
    return data


def fit_data():
    """
    Takes some time to fit a model :(, but it worth it :).
    Here we use sklearn to fit the data according a Linear Regression model, that might be not very accurate
    because the data present some outliers, and also need some reformatting(maybe this is not the appropriate term
    but I refer to a normalization or apply log10 to the data) almost all the data extracted are too close.
    I'm out of time so if you can make it better, good for you....:)!!
    :return:
    """
    import numpy as np
    from sklearn.linear_model import LinearRegression
    model = LinearRegression(fit_intercept=True)
    data = clean_data()
    x = np.array(data['comics'])
    y = np.array(data['stories'])
    model.fit(x[:, np.newaxis], y[:, np.newaxis])
    xfit = np.linspace(1, 300, 1000)
    yfit = model.predict(xfit[:, np.newaxis])
    return xfit, yfit.reshape(1000, )


def graph():
    """
    This function handle the graph of the data extracted from the character.json file,
    where is contain the data fetch from the API. Basically we call this data, also
    call the data from the Linear Regression model(The prediction model) and set up the option of the graph.
    """
    output_file('report.html',
                title="Comics vs stories available")
    data = clean_data()
    xfit, yfit = fit_data()
    # Storing data in a ColumnDataSource
    characters_stats = ColumnDataSource(data)

    # Selection tools
    select_tools = ['box_select', 'box_zoom', 'hover', 'tap', 'reset']
    num_char = data.shape[0]
    fig = figure(plot_height=500,
                 plot_width=600,
                 x_axis_label='Comics available',
                 y_axis_label='Stories available',
                 title=f"Character\'s comics vs stories available(Taken from {num_char} Characters)",
                 toolbar_location='right',
                 tools=select_tools)
    # Adding a square representing each Character
    fig.square(x='comics',
               y='stories',
               source=characters_stats,
               color='royalblue',
               selection_color='deepskyblue',
               nonselection_color='lightgray',
               nonselection_alpha=0.3)
    fig.line(xfit, yfit, line_color='red', line_width=1, alpha=0.7, legend="Linear Regression")
    show(fig)


if __name__ == '__main__':
    """
    In case you wanted to fetch other endpoints you can make use of the command line
    >>> python marvel.py creators comics
    >>>
    This should fetch the resources but the plotting would be only with the characters endpoint.
    The code commented below should be uncommented in this case.
    """
    # This code must be uncommented in the case explain above
    # for endpoint in user_input():
    #     if endpoint in MARVEL_OBJECTS:
    #         get_api_endpoint(endpoint)
    get_api_endpoint('characters')
    print(get_api_endpoint.cache_info())
    graph()
