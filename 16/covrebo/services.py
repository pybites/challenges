import json
import requests


def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {'User-Agent': 'My Library (https://github.com/clark_griswold)',
               'Accept': 'application/json'}
    r = requests.get(url, headers=headers)
    joke = json.loads(r.text)
    return joke['joke']
