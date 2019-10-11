# QUERY SPOTIFY API USING SPOTIPY

See the blog challange details here: https://codechalleng.es/challenges/53/

## Getting Started

Make sure you have created your app here: https://developer.spotify.com/dashboard/login. 
Create `.env` file in the root folder of this project. In the `.env` file, put the 
following keys:
```
CLIENT_ID="your app client id"
CLIENT_SECRET="your app client secret"
```
Copy your created app `client_id` and `client_secret` values and replace the values in
`.env` file respectively

Also make sure you have created and activated your virtual environment. See https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/ on how to do that.
### Prerequisites

NB: I used python 3.7 on my end.

```
Python 3.6+
```

### Installing/Running project scripts

With your virtual environment for project active, run the following to install the
required packages for the project

```
pip install -r requirements.txt
```

Then you can run either of the file in this project as you wish.
```
python my_playlist.py

```
or
```
python artist_albums_names.py
```
or 
```
python top_tracks.py
```

NB: For my case my spotify username is `psdz7utwhf4qx7b4m5d5n9bmk` and my artist name is `Capital Kings` or `Lil Wayne`

I used black to format my code: https://black.readthedocs.io/en/stable/ 