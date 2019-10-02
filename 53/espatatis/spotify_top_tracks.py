import spotipy.util as util
import spotipy

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
    tracks = sp.artist_top_tracks(artist_id)
    print("Top 10 songs by Amit Trivedi : ", end = '\t')
    for i in range(len(tracks['tracks'])): 
        values = tracks['tracks'][i]['name']
        print(values)
else:
    print('No token found')
