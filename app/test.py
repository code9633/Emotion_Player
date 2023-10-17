from .spotify import SpotifyClient
from .models import Song


spotify_client = SpotifyClient()
        
songs = Song.objects.filter(labels = 0).values_list("uri", flat = True)
print("songs", songs)

# initialize lists to store song infomation
# song_info = []

# for uri in songs:
#     track_info = spotify_client.track(uri)
#     song_name = track_info['name']
#     artist_name = track_info['artist'][0]['name']
#     cover_image_url = track_info['album']['images'][0]['url']
    
#     song_info.append({
#         'song_name' : song_name,
#         'artist_name' : artist_name,
#         'cover_image_url' : cover_image_url
#     })