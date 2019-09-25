# Simple program to received Apple Music Top Songs based on country's code provided
# To received Top Songs list Apple's API is used
# To received Country list country.io API is used. The data is used to map country code to country name
import requests
import json
import collections
import argparse
import sys


def get_data(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        return None

def print_banner(code, update):
    banner = f"Apple's Music Top Songs for {code}"
    lastUpdate = f"Last list update {update}"

    print(f"{banner:^130}")
    print(f"{lastUpdate:^130}")
    print("-"*130)
    print("{0:>2} | {1:<50} | {2:<50} | {3}".format("Rank", "Song", "Artist", "Genres"))
    print("-"*130)

def main():

    parser = argparse.ArgumentParser(description="Display Apple's Music Top Songs")
    parser.add_argument('-c', '--code', required=True, help='Country code (US, DE, AR, PL e.g)')
    parser.add_argument('-l', '--limit', type=int, required=True, help='Number of songs to display (1-100)')
    args = parser.parse_args()

    # Apple's API for music library
    url = "https://rss.itunes.apple.com/api/v1/{}/apple-music/top-songs/all/{}/explicit.json"
    # Country code API
    url_country = "http://country.io/names.json"

    countries = get_data(url_country)

    if args.code.upper() not in countries or args.limit < 1 or args.limit > 100:
        parser.print_help()
        print("Error: Please check help to provide proper values!")
        sys.exit(1)
 
    songs = get_data(url.format(args.code.lower(), args.limit))

    print()
    print_banner(countries[args.code.upper()], songs['feed']['updated'])

    for i, song in enumerate(songs['feed']['results'], start=1):
        print(f"{i:>4} | {song['name'][:50]:<50} | {song['artistName'][:50]:<50} | {song['genres'][0]['name']}")
    print("-"*130)

if __name__ == "__main__":
    main()
