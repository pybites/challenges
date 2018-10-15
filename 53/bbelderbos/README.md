# PyBites Code Challenge 53 - Query the Spotify API

[Challenge URL](https://codechalleng.es/challenges/53/)

I used [Spotipy](https://github.com/plamere/spotipy) and a little bit of [Flask](http://flask.pocoo.org) to build this:

![screenshot](demo.png)

Requires the following two env variables (set in your venv/bin/activate):

	export CLIENT_ID='abc'
	export CLIENT_SECRET='def'

... which you get when making an app on Spotify (after agreeing to dev terms).

[This comment by fhopp](https://github.com/plamere/spotipy/issues/194#issuecomment-315458391) helped a lot getting the auth part working!
