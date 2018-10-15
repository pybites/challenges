import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials as SpotifyAuth

# thanks fhopp
# https://github.com/plamere/spotipy/issues/194#issuecomment-315458391
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
manager = SpotifyAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=manager)
