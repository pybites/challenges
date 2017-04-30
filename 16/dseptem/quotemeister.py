import webbrowser
from json import JSONDecodeError
from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

quotes_url = 'http://api.forismatic.com/api/1.0/'
wiki_url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={title}&redirects=1&utf8=1&exintro=1&explaintext=1'

MAX_TRIES = 3


@app.route("/")
def wisdom():
    quote, author = get_random_quote()
    if not quote:
        error = 'Something went terribly wrong getting your quote, try again please!'
        return render_template('index.html', error=error), 500

    bio = get_author_bio(author)
    return render_template('index.html', quote=quote, author=author, bio=bio)


def get_random_quote():
    tries = 0
    while tries < MAX_TRIES:
        try:
            j = requests.post(quotes_url, data={'method': 'getQuote', 'format': 'json', 'lang': 'en'}).json()
            return j['quoteText'], j['quoteAuthor']
        except JSONDecodeError:
            tries += 1
    else:
        return None, None


def get_author_bio(author_name):
    query_url = wiki_url.format(title=author_name)
    not_available = "Biography not available =("
    try:
        j = requests.get(query_url).json()
        pages = j['query']['pages']
        for page in pages:
            return pages[page]['extract'] if 'may refer to' not in pages[page]['extract'] else not_available
    except (KeyError, JSONDecodeError):
        return not_available


if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000')
    app.run()
