import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyClient:
    def __init__(self):
        self.client_id = "2551ec0d2e20460e9f3fe80199706248"
        self.client_secret = "6a781c83c6c74f42a7a0ca864f2c4ab4"
        
    def initialize_spotify_client(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id,
                                                              client_secret=self.client_secret)
        return spotipy.Spotify(client_credentials_manager= client_credentials_manager)
