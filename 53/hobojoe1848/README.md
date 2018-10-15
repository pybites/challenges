#Spotify Checker

A script/web tool to list out the Albums of a specified Artist. Pulls data using the Spotify API.

##Relevant Data

You can search for artists and IDs using the Spotify Searcher: [https://developer.spotify.com/console/get-search-item/](https://developer.spotify.com/console/get-search-item/).

Some Artist IDs to try:

Def Leppard: 6H1RjVyNruCmrBEWRbD0VZ
Neon Trees: 0RpddSzUHfncUWNJXKOsjy
Muse: 12Chz98pHFMPJEknJQMWvI
The Fratellis: 3M4ThdJR28z9eSMcQHAZ5G
Taylor Swift: 06HL4z0CvFAxyc27GXpf02
The Eagles: 0ECwFtbIWEVNwjlrfc6xoL
Metallica: 2ye2Wgw4gimLv2eAKyk1NB


##Issues

1. The app does not capture errors in the ID entry. If you enter an invalid ID or leave the field empty and submit, you get an Internal Server Error.

2. You NEED to use the Artist ID. You can't search by band name unfortunately - not with the way I've coded this.

3. I had to code the authentication into the index function. I wasn't able to figure out how to authenticate in a different function and keep the authenticated object globally accessible. That is, auth once, use many. The app currently authenticates every time the page is refreshed.

##TODO

1. Change the lookup method of the `spotipy` search to do an actual search on the artist NAME as oppose to searching on the artist ID. The "decoding" of the dictionary/JSON return will need to be changed to suit.

2. Implement some testing.

3. Capture errors!

