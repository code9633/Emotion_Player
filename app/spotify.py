import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyClient:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.spotify = self.initialize_spotify_client()
        
    def initialize_spotify_client(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id,
                                                              client_secret=self.client_secret)
        return spotipy.Spotify(client_credentials_manager= client_credentials_manager)




sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials(client_id= SPOTIFY_CLIENT_ID,
                                                                          client_secret=SPOTIFY_CLIENT_SECRET))