import os
import spotipy
import spotipy.oauth2 as oauth2
import requests
from dotenv import load_dotenv

load_dotenv()


def print_header():
    print("-------------------------------------")
    print("         ARTIST ALBUMS NAMES         ")
    print("-------------------------------------")
    print()


def spotify_auth():
    client_credentials_manager = oauth2.SpotifyClientCredentials(
        client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET")
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp


def get_artist_id():
    # return the artist id from the entered artist name
    artist_name = input("Please Enter Artist Name: ")
    results_artist_name = spotify_auth().search(
        q="artist:" + artist_name, type="artist"
    )
    artist_items = results_artist_name["artists"]["items"]
    artist_id = artist_items[0]["id"]
    return artist_id


def get_artist_albums():
    print("-- The albums will be printed below shortly --")
    print()
    try:
        results = spotify_auth().artist_albums(get_artist_id(), album_type="album")
        for item in results["items"]:
            print("Album Name          : " + item["name"])
            print("Album URI           : " + item["uri"])
            print("Album Release Date  : " + item["release_date"])
            print("Album Total Track   : " + str(item["total_tracks"]))
            print("Album Cover photo   : " + item["images"][0]["url"])
            print()

    except spotipy.client.SpotifyException:
        print(" Make sure you have entered a valid artist name")
    except IndexError:
        print(" Make sure you have entered a valid artist name")
    except requests.exceptions.ConnectionError:
        print("Check your internet connection")


def main():
    get_artist_albums()


main()
