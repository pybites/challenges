import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from flask import render_template, request
from program import app

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    albums = []
    sp = setup_creds()
    if request.method == 'POST' and 'artistchoice' in request.form:
        artistid = request.form.get('artistchoice')
        albums = get_albums(sp, artistid)
    return render_template('index.html', albums=albums)

def setup_creds():
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp

def get_albums(sp, artistid):
    result = sp.artist_albums(artistid)
    album_list = []
    for i in result['items']:
        [album_list.append(val) for key, val in i.items() if key == 'name' and val not in album_list]
    return album_list


if __name__ == "__main__":
    pass
