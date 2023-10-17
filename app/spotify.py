import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyClient:
    def __init__(self):
        self.client_id = "7aaa956806364910b660dc7a16ad51a4"
        self.client_secret = "74a478d0172840c98442c8720ec00efb"
        
    def initialize_spotify_client(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id,
                                                              client_secret=self.client_secret)
        return spotipy.Spotify(client_credentials_manager= client_credentials_manager)
