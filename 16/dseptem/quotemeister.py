import webbrowser
from json import JSONDecodeError
from multiprocessing import Process
from flask import Flask, render_template, abort
import requests
import webview

app = Flask(__name__)

quotes_url = 'http://api.forismatic.com/api/1.0/'
wiki_url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={title}&redirects=1&utf8=1&exintro=1&explaintext=1'


@app.route("/")
def wisdom():
    quote, author = get_random_quote()
    bio = get_author_bio(author)
    return render_template('index.html', quote=quote, author=author, bio=bio)


def get_random_quote():
    errors = 0
    while True:
        if errors > 2:
            abort(500)
        try:
            j = requests.post(quotes_url, data={'method': 'getQuote', 'format': 'json', 'lang': 'en'}).json()
            return j['quoteText'], j['quoteAuthor']
        except JSONDecodeError:
            errors += 1
            continue


def get_author_bio(author_name):
    query_url = wiki_url.format(title=author_name)
    try:
        j = requests.get(query_url).json()
        for p in j['query']['pages']:
            if 'may refer to' in j['query']['pages'][p]['extract']:
                return "Biography not available =("
            return j['query']['pages'][p]['extract']
    except:
        return "Biography not available =("


def start_web():
    app.run()


def start_view():
    webview.create_window('Wisdom of the Ages', 'http://127.0.0.1:5000')

if __name__ == "__main__":
    command = input('(S)imple view or (W)eb view?')
    while command.lower() not in ['s', 'w']:
        input('(S)imple view or (W)eb view?')
    server = Process(target=start_web)
    server.start()
    if command == 's':
        view = Process(target=start_view)
        view.start()
        view.join()
        server.terminate()
    else:
        webbrowser.open('http://127.0.0.1:5000')
