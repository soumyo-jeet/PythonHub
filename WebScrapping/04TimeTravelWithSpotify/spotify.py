import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
from timetravelwithmusic import top_songs_h, date

scope = "playlist-modify-private"
client_id = "1383df9e65f147fb93d71eca29516e76"
client_secret = "6b1415b5ade44b56a73c616da8017659"
redirect_uri = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

prof_id= sp.current_user()['id']


#Search for the songs
song_uris = [sp.search(q=song, type="track")['tracks']['items'][0]['uri'] for song in top_songs_h]

print(top_songs_h)
print(song_uris)

#Creating playlist
year = date.split("-")[0]
playlist_name = f"{year} BillBoard 100..."
playlist_id = sp.user_playlist_create(user = prof_id, name = playlist_name, public=False)['id']

sp.user_playlist_add_tracks(playlist_id=playlist_id, tracks=song_uris, user=prof_id)