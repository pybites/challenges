import json
from pprint import pformat, pprint

from flask import Flask, Response, render_template, request, jsonify, session
from flask_jsglue import JSGlue
from flask_session import Session

from gbooks import get_book_info, search_books

BOOK_ENTRY = '''<div class="entry" id="{id}">\
    <img src="{thumb}" alt="{title}">\
    <p>{title} <br /><a target="_blank" href="{link}">(more ...)</a></p>\
</div>'''
DEFAULT_THUMB = 'http://fbreadinglist.com/i/logo.png'

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

jsglue = JSGlue(app)


def get_thumb(book):
    try:
        thumb = book['volumeInfo']['imageLinks']['smallThumbnail']
    except KeyError: 
        thumb = DEFAULT_THUMB
    return thumb


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    books = search_books(search)
    if not books.get('items'):
        return "No Books Found"
    else:
        results = []
        for book in books['items']:
            thumb = get_thumb(book)        
            entry = BOOK_ENTRY.format(id=book['id'],
                                      thumb=thumb,
                                      title=book['volumeInfo']['title'],
                                      link=book['selfLink'])
            results.append(entry)
        return '\n'.join(results)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("main.html", books=session.get('viewed'))

@app.route('/book/<book_id>')
def show_book(book_id):
    book = get_book_info(book_id)
    if not book.get('volumeInfo'):
        return render_template("main.html", error=error)
    thumb = get_thumb(book) 
    book['volumeInfo']['thumb'] = thumb
    if not session.get('viewed'):
        session['viewed'] = {}
    session['viewed'][book_id] = thumb
    return render_template("book.html", book=book['volumeInfo'], pp=pformat)


if __name__ == '__main__':
    app.run(debug=True)
