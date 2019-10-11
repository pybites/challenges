import requests


class Spotify:
    """
    Wrapper class to call Spotify APIs which are based on 'Client Credentials Flow'
    """
    DEFAULT_ALBUM_LIMIT = 20

    def __init__(self, auth_token):
        """
        Spotify class construction.
        Expects an access token
        :param auth_token:
        """
        self.base_api_url = 'https://api.spotify.com/v1/'
        self.auth_token = auth_token

    def get_auth_headers(self):
        """
        Function to generate the header with the Authorization token
        :return:
        """
        return {'Authorization': 'Bearer {0}'.format(self.auth_token)}

    def _get(self, url, payload=None):
        """
        Helper method to call the Spotify APIs
        Expects the sub url and payload (if any)
        :param url:
        :param payload:
        :return:
        """
        headers = self.get_auth_headers()
        response = requests.get(self.base_api_url + url, headers=headers, params=payload)

        if response.status_code != 200:
            response.raise_for_status()

        data = response.json()
        return data

    def get_artist_id(self, artist):
        """
        Public method to get Spotify ID of an artist
        Expects artist name
        :param artist:
        :return:
        """
        data = self._get(f'search?query={artist}&type=artist&limit=1')

        if data['artists']['items']:
            return data['artists']['items'][0]['id']
        else:
            return None

    def get_albums(self, artist_id, limit=DEFAULT_ALBUM_LIMIT):
        """
        Public method to get albums of an artist
        Expects artist's spotify ID
        :param artist_id:
        :param limit:
        :return:
        """
        params = {'limit': limit}
        data = self._get(f'artists/{artist_id}/albums', payload=params)

        if data['items']:
            albums = data['items']
            return [album['name'] for album in albums]
        else:
            return None

    def get_users_playlists(self, user_id):
        """
        Public method to get user's playlists.
        Expectes user's Spotify id
        :param user_id:
        :return:
        """
        data = self._get(f'users/{user_id}/playlists')

        if data['items']:
            playlists = data['items']
            return [list['name'] for list in playlists]
        else:
            return None

    def get_users_playlists_tracks(self, user_id):
        """
        Public method to get user's tracks
        Expects user's Spotify ID
        :param user_id:
        :return:
        """
        playlists = self._get(f'users/{user_id}/playlists')

        if playlists['items']:
            for item in playlists['items']:
                tracks = item['tracks']
                tracks_url = tracks['href'][tracks['href'].find('playlists'):]
                tracks = (self._get(tracks_url))

                if tracks['items']:
                    return [item['track']['name'] for item in tracks['items']]
        else:
            return None

    def get_top_tracks(self, artist_id, market=None):
        """
        Public method to get artists top tracks
        Expects artist Spotify ID
        :param artist_id:
        :param market:
        :return:
        """
        params = {'market': market}
        data = self._get(f'artists/{artist_id}/top-tracks', payload=params)

        if data['tracks']:
            tracks = data['tracks']
            return [track['album']['name'] for track in tracks]
        else:
            return None

