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
            artistName = track_info['artists'][0]["name"]
            coverImageUrl = track_info['album']['images'][0]['url']  
            
            song_info.append({
                'song_name' : songName ,
                'artist_name' : artistName ,
                'cover_image' : coverImageUrl  
            })
            
        return song_info
            
    def createPlayList(self):
        
        emotionSongs = self.getSongsfromCSV('./files/label_uri.csv' , label = self.label)
        allSongs = self.getSongsfromCSV('./files/label_uri.csv')
        
        emotionSongsInfo = self.getSongInfo(emotionSongs) 
        allSongsInfo = self.getSongInfo(allSongs) 
         
        labels = {0:"Angry", 1:"happy", 2: "Sad", 3 : "Neutral"}
            
        context = {
            'emotion': labels[self.label],
            'emotionSongs' : emotionSongsInfo,
            'allSongs' : allSongsInfo
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
    
    #   class SongListManager:

    # def __init__(self, label):
    #     self.label = label
    #     self.songs = []

    # def add_song(self, song):
    #     self.songs.append(song)

    # def delete_song(self, song):
    #     self.songs.remove(song)

    # def get_songs(self):
    #     return self.songs

    # def load_songs_from_csv(self, file_path):
    #     with open(file_path, 'r') as csvfile:
    #         reader = csv.reader(csvfile)
    #         next(reader) # skip header row
    #         for row in reader:
    #             song = Song(row[0], row[1], row[2])
    #             self.add_song(song)

    # def save_songs_to_csv(self, file_path):
    #     with open(file_path, 'w') as csvfile:
    #         writer = csv.writer(csvfile)
    #         writer.writerow(['title', 'artist', 'duration'])
    #         for song in self.songs:
    #             writer.writerow([song.title, song.artist, song.duration])