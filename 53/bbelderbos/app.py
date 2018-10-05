from flask import Flask, render_template, request

from spotify import sp

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/<artist>', methods=['GET', 'POST'])
def index(artist=None):
    artist = request.args.get('artist', artist or None)
    tracks = None
    if artist:
        results = sp.search(q=artist, limit=50)
        tracks = results['tracks']['items']
    return render_template('index.html',
                           tracks=tracks,
                           artist=artist or '')
