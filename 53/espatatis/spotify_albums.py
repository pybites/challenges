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
    albums = sp.artist_albums(artist_id, album_type = 'album')
    print("List of albums by Amit Trivedi : ")
    for i in range(len(albums['items'])):  
        values = albums['items'][i]['name']
        print(i+1, values)
else:
    print('No token found')
