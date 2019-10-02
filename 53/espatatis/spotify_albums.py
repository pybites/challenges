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

token = util.prompt_for_user_token(username,scope, client_id = '6b1358d2a8f54d6b86356e66d4b5c144', client_secret = '06713d07f16643b0ad1c5cafe7b9a09e',redirect_uri = 'http://google.com/' )
print(str(token))
if token:
    sp = spotipy.Spotify(auth = token)
    searchQuery = input("Enter artists' name : ")
    search = sp.search(searchQuery,1,0,"artist")
    print(json.dumps(search, sort_keys = True, indent = 4))
    print()
    for i in range(len(search['artists']['items'])):
        if(searchQuery in search['artists']['items'][i]['name']):
            print(search['artists']['items'][i]['uri'] + ' is ' + search['artists']['items'][i]['name'])
    #albums = sp.artist_albums(artist_id, album_type = 'album')
    #print("List of albums by Amit Trivedi : ")
    #for i in range(len(albums['items'])):  
       # values = albums['items'][i]['name']
      #  print(i+1, values)
else:
    print('No token found')
