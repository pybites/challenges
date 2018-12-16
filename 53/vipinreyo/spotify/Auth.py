import os
import requests


class Auth:
    """
    Class to get authentication access token application created in user's profile
    """
    SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

    def __init__(self):
        """
        Constructor.
        Expects client id and secret.
        Throws exceptions if they are not set
        """
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

        if not self.client_id:
            raise Exception('No client id set.')

        if not self.client_secret:
            raise Exception('No client secret set.')

    def get_access_token(self):
        """
        Call the API token api get access token
        :return:
        """
        payload = {'grant_type': 'client_credentials'}
        response = requests.post(self.SPOTIFY_TOKEN_URL, data=payload, auth=(self.client_id, self.client_secret))

        if response.status_code != 200:
            response.raise_for_status()

        data = response.json()
        return data['access_token']
