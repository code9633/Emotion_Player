from .spotify import SpotifyClient
from .models import Song
import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SongListManager:
    
    def __init__(self, label):
        self.label = label
        
        
    def create_playlist(self):
        spotify_client = SpotifyClient().initialize_spotify_client()
        
        songs = []
        song_info = []
        
        with open('./files/label_uri.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader :
                if  int(row['labels']) == self.label:
                    songs.append({
                        'uri' : row['uri'],
                    })
                    
                    if len(songs) >= 5:
                        break
                    
        for song in songs:
            track_info = spotify_client.track(song['uri'])
            song_name = track_info['name']
            artist_name = track_info['artists'][0]['name']
            cover_image_url = track_info['album']['images'][0]['url']
  
            song_info.append({
                'song_name' : song_name,
                'artist_name' : artist_name,
                'cover_image' : cover_image_url
                
            })
            
            
        labels = {0:"Angry", 1:"happy", 2: "Sad", 3 : "Neutral"}
            
        context = {
            'emotion': labels[self.label],
            'songs' : song_info
        }
        
        return context
        
            
            
 # def create_playlist(self):
    #     spotify_client = SpotifyClient()
        
    #     songs = Song.objects.filter(labels = int(self.label)).values_list("uri", flat = True)
    #     print("sonngs", songs)
        
    #     # initialize lists to store song infomation
    #     song_info = []
        
    #     for uri in songs:
    #         track_info = spotify_client.track(uri)
    #         song_name = track_info['name']
    #         artist_name = track_info['artist'][0]['name']
    #         cover_image_url = track_info['album']['images'][0]['url']
            
    #         song_info.append({
    #             'song_name' : song_name,
    #             'artist_name' : artist_name,
    #             'cover_image_url' : cover_image_url
    #         })  
    
      