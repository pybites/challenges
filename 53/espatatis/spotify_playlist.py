import spotipy.util as util
import spotipy
import json

scope = 'playlist-read-private'
username = 'sz08l1r9jm94jvyaeohhp9gjm'
user_id = 'spotify:user:something'
client_id = 'something'
client_secret = 'something'
playlist_id = 'something'
redirect_uri = 'http://google.com/'
artist_id = 'spotify:artist:7HCqGPJcQTyGJ2yqntbuyr'

token = util.prompt_for_user_token(username,scope, client_id = client_id, client_secret = client_secret,redirect_uri = redirect_uri )
if token:
    sp = spotipy.Spotify(auth = token)
    playlist_tracks = sp.user_playlist_tracks(user_id,playlist_id)
    print('List of tracks in the playlist "For the app": ')
    for i in range(len(playlist_tracks['items'])):   
        print(i+1,playlist_tracks['items'][i]['track']['name'])
else:
    print('No token found')




