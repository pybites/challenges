import spotipy.util as util
import spotipy
import json

scope = 'playlist-read-private'
username = 'sz08l1r9jm94jvyaeohhp9gjm'
user_id = 'spotify:user:sz08l1r9jm94jvyaeohhp9gjm'
client_id = '6b1358d2a8f54d6b86356e66d4b5c144'
client_secret = '06713d07f16643b0ad1c5cafe7b9a09e'
playlist_id = '2yCf2Kzabxcn8AowvBPoN0'
redirect_uri = 'http://google.com/'

token = util.prompt_for_user_token(username,scope, client_id = '6b1358d2a8f54d6b86356e66d4b5c144', client_secret = '06713d07f16643b0ad1c5cafe7b9a09e',redirect_uri = 'http://google.com/' )
if token:
    sp = spotipy.Spotify(auth = token)
    playlist_tracks = sp.user_playlist_tracks(user_id,playlist_id)
    print('List of tracks in the playlist "For the app": ')
    for i in range(len(playlist_tracks['items'])):   
        print(i+1,playlist_tracks['items'][i]['track']['name'])
else:
    print('No token found')




