from Spotify import Spotify
from Auth import Auth
import os
import sys

"""Client script which calls the Spotify helper class methods to do the following.
1. Query Spotify and grab a list of album names for any given artist. Bonus points if the script allows the user to
    specify the artist!
2. Create a playlist on your account if you don't already have one. Write a script that queries Spotify for the playlist
    and returns all tracks/songs in the playlist.
3. Write a script that obtains a list of the top tracks for an artist and see if any of those songs exist in your
playlist.

Pre-requisites:
Create a python venv (Optional)
pip install -r requirements.txt
Create an account (preferably free) with www.spotify.com
Note down the Spotify user id .
Create an environment variable 'SPOTIFY_USER_ID' with the value in Spotify user's account profile id
Create and register an application in the Spotify profile, which will give a Client ID and Client secret
Create environment variables SPOTIPY_CLIENT_ID & SPOTIPY_CLIENT_SECRET and store the client ID and secret in them.
"""
MAX_ALBUM_LIMIT_SET_BY_SPOTIFY = 50
FIFTY_TIMES = 50
DEFAULT_MARKET_COUNTRY_CODE = 'US'


def main():
    try:
        auth = Auth()
        token = auth.get_access_token()

        sp = Spotify(token)

        artist = input("Please enter your favourite artist's name: ").lstrip().rstrip().lower()

        # If an invalid input, print error message and exit
        if not artist:
            print('Please enter a valid artist name.')
            sys.exit(1)

        # Get the spotify ID of artist
        artist_id = sp.get_artist_id(artist)

        # Get user's Spotify ID
        user_id = os.getenv('SPOTIFY_USER_ID')

        # Do necessary error check. If artist exists in Spotify, then continue with data
        if artist_id:
            # Get artists albums
            albums = sp.get_albums(artist_id, limit=MAX_ALBUM_LIMIT_SET_BY_SPOTIFY)

            # If there are albums, print them
            if albums:
                print()
                print('*' * FIFTY_TIMES)
                print(f'{artist.title()} - ALBUMS')
                print('*' * FIFTY_TIMES)
                for album in albums:
                    print(album)
                print()

                # Get the top tracks of artists and if exists, print them
                top_tracks = sp.get_top_tracks(artist_id, market=DEFAULT_MARKET_COUNTRY_CODE)
                if top_tracks:
                    print()
                    print('*' * FIFTY_TIMES)
                    print(f'{artist.title()} - Top tracks in {DEFAULT_MARKET_COUNTRY_CODE}')
                    print('*' * FIFTY_TIMES)
                    for track in top_tracks:
                        print(track)
                    print()

                    # Get user's tracks (the tracks in the public playlists)
                    my_tracks = sp.get_users_playlists_tracks(user_id)

                    # Get the top tracks of artist which are in your collection.
                    for track in my_tracks:
                        for top_track in top_tracks:
                            if track in top_track:
                                print(f'You have {top_track} in your collection!')
                                break
                    print()
                else:
                    print(f'No top tracks for {artist} in {market}')
            else:
                print(f'No albums found for {artist.title()}')
        else:
            print(f'No albums found for {artist.title()}')

        # Get your play lists. Print them if any.
        playlists = sp.get_users_playlists(user_id)

        if playlists:
            print()
            print('*' * FIFTY_TIMES)
            print('My Play lists')
            print('*' * FIFTY_TIMES)
            for name in playlists:
                print(name)
            print()
        else:
            print("You don't have any public play lists.")

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
