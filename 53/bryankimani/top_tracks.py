import os
import spotipy
import spotipy.oauth2 as oauth2
import requests
from dotenv import load_dotenv

load_dotenv()

username = input("Please enter your spotify username: ")
artist_name = input("Please Enter Artist Name: ")


def print_header():
    print("------------------------------------------")
    print(" ARTIST TOP TRACKS THAT ARE IN MY PLAYLIST ")
    print("------------------------------------------")
    print()


def spotify_auth():
    client_credentials_manager = oauth2.SpotifyClientCredentials(
        client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET")
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp


def my_playlist():
    try:
        playlists = spotify_auth().user_playlists(username)
        for playlist in playlists["items"]:
            if playlist["owner"]["id"] == username:
                results = spotify_auth().user_playlist(
                    username, playlist["id"], fields="tracks,next"
                )
                tracks = results["tracks"]
                while tracks["next"]:
                    results = spotify_auth().next(tracks)
                    tracks.extend(results["items"])
                return tracks
    except spotipy.client.SpotifyException:
        print()
        print("Enter a valid client username")
    except requests.exceptions.ConnectionError:
        print(" No internet")


def get_artist_id():
    # return the artist id from the entered artist name
    try:
        results_artist_name = spotify_auth().search(
            q="artist:" + artist_name, type="artist"
        )
        artist_items = results_artist_name["artists"]["items"]
        artist_id = artist_items[0]["id"]
        return artist_id
    except spotipy.client.SpotifyException:
        print("Enter a valid artist name")
    except IndexError:
        print()
        print(" We did not get any record for artist, " + artist_name)
    except requests.exceptions.ConnectionError:
        print(" No internet")


def top_tracks():
    try:
        artist_top_tracks = spotify_auth().artist_top_tracks(get_artist_id())
        tracks = [artist_track for artist_track in artist_top_tracks["tracks"]]
        return tracks
    except AttributeError:
        print()
        print(" We did not get any record the entered artist name")
    except requests.exceptions.ConnectionError:
        print("Check your internet connection")
    except TypeError:
        print("Enter a valid artist name")


def my_playlist_tracks():
    try:
        tracks = my_playlist()
        playlist_track = [item["track"] for item in tracks["items"]]
        return playlist_track
    except TypeError:
        print("Invalid username")


def top_tracks_in_playlist():
    # Check if my artist top tracks are in my playlist
    try:
        top_tracks_id = [top_track["id"] for top_track in top_tracks()]
        playlist_tracks_id = [
            playlist_track["id"] for playlist_track in my_playlist_tracks()
        ]
        tracks_in_playlist = set(top_tracks_id).intersection(playlist_tracks_id)
        for top_track in top_tracks():
            if top_track["id"] in list(tracks_in_playlist):
                print("Track Name              : " + top_track["name"])
                print("Track URI               : " + top_track["uri"])
                print()

    except TypeError:
        print("Something went wrong")


print_header()
top_tracks_in_playlist()
