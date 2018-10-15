import json
from functools import wraps
from pprint import pprint

def pretty_print(func):
    ''' Decorator to pretty print a return output from function '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        out = func(*args, **kwargs)
        pprint(out)
        return out
    return wrapper

@pretty_print
def get_movie_data(infile='data.json'):
    with open(infile, 'r') as f:
        data = json.load(f)
        return data

data = get_movie_data()
