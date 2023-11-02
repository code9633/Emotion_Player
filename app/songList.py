from .spotify import SpotifyClient
from .models import Song
import csv

class SongListManager:
    
    def __init__(self, label):
        self.label = label
        
        
    def getSongsfromCSV(self,filePath , maxSongs = 15, label = None): 
        # create array for the fetch the song from the csv file
        songs = [] 
        
        with open(filePath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                if label is None or int(row['labels']) == label:
                    songs.append({
                        'uri' : row['uri']
                    })
                    
                    if len(songs) >= maxSongs:
                        break
        # print(songs)
        return songs
    
    
    def getSongInfo(self, songs):
        song_info = []
        spotify_client = SpotifyClient().initialize_spotify_client()
        
        for song in songs:
            uri = song['uri']
            track_info = spotify_client.track(uri)
            songName = track_info['name']
            previewUrl = track_info['preview_url']
            artistName = track_info['artists'][0]["name"]
            coverImageUrl = track_info['album']['images'][0]['url']  
            
            song_info.append({
                'song_name' : songName ,
                "previewUrl" : previewUrl,
                'artist_name' : artistName ,
                'cover_image' : coverImageUrl  
            })
            
        return song_info
            
    def createPlayList(self):
        
        emotionSongs = self.getSongsfromCSV('./files/label_uri.csv' , label = self.label)
        allSongs = self.getSongsfromCSV('./files/label_uri.csv')
        
        emotionSongsInfo = self.getSongInfo(emotionSongs) 
        allSongsInfo = self.getSongInfo(allSongs) 
         
        labels = {0:"Angry", 1:"Happy", 2: "Sad", 3 : "Neutral"}
            
        context = {
            'emotion': labels[self.label],
            'emotionSongs' : emotionSongsInfo,
            'allSongs' : allSongsInfo
        }
        
        return context
        
        