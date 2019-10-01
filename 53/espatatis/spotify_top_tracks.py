import spotipy.util as util
import spotipy

scope = 'playlist-read-private'
username = 'sz08l1r9jm94jvyaeohhp9gjm'
user_id = 'spotify:user:sz08l1r9jm94jvyaeohhp9gjm'
client_id = '6b1358d2a8f54d6b86356e66d4b5c144'
client_secret = '06713d07f16643b0ad1c5cafe7b9a09e'
playlist_id = '2yCf2Kzabxcn8AowvBPoN0'
redirect_uri = 'http://google.com/'
artist_id = 'spotify:artist:7HCqGPJcQTyGJ2yqntbuyr'

token = util.prompt_for_user_token(username,scope, client_id = '6b1358d2a8f54d6b86356e66d4b5c144', client_secret = '06713d07f16643b0ad1c5cafe7b9a09e',redirect_uri = 'http://google.com/' )
if token:
    sp = spotipy.Spotify(auth = token)
    tracks = sp.artist_top_tracks(artist_id)
    print("Top 10 songs by Amit Trivedi : ", end = '\t')
    for i in range(len(tracks['tracks'])): 
        values = tracks['tracks'][i]['name']
        print(values)
else:
    print('No token found')
