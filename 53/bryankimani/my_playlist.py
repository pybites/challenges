import os
import spotipy
import spotipy.oauth2 as oauth2
import requests
from dotenv import load_dotenv

load_dotenv()


def print_header():
    print("-------------------------------------")
    print("         MY PLAYLIST TRACKS          ")
    print("-------------------------------------")
    print()


def spotify_auth():
    client_credentials_manager = oauth2.SpotifyClientCredentials(
        client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET")
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp


def show_tracks(tracks):
    for i, item in enumerate(tracks["items"]):
        try:
            track = item["track"]
            print("   %d %32.32s %s" % (i, track["artists"][0]["name"], track["name"]))
        except TypeError:
            break


def my_playlist():
    username = input("Please enter your spotify username: ")
    try:
        playlists = spotify_auth().user_playlists(username)
        for playlist in playlists["items"]:
            if playlist["owner"]["id"] == username:
                print()
                print(
                    "Your",
                    playlist["name"],
                    "playlist has",
                    playlist["tracks"]["total"],
                    " total tracks",
                )
                results = spotify_auth().user_playlist(
                    username, playlist["id"], fields="tracks,next"
                )
                tracks = results["tracks"]
                show_tracks(tracks)
                while tracks["next"]:
                    tracks = spotify_auth().next(tracks)
                    show_tracks(tracks)
    except spotipy.client.SpotifyException:
        print("Invalid username. Try again")
    except requests.exceptions.ConnectionError:
        print("Check your internet connection")


my_playlist()
