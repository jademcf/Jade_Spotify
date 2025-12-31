import spotipy
from Spotify_Keys import client_id, client_secret, redirect_uri
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

Name =input("What is your name? ")

sp = spotipy.Spotify(auth_manager= SpotifyOAuth(client_id,
                                                client_secret, 
                                        redirect_uri, 
                                        scope = "user-read-recently-played"))


results = sp.current_user_recently_played(limit=50)


recently_played = results["items"] #This is a list which represents one playback event 

songs_data = []
for song in recently_played:
    song_info = song["track"]
    song_name = song_info["name"]
    artist_name = song_info["artists"][0]["name"]
    # album_name = song_info["album"][0]["name"]
    popularity = song_info["popularity"]
    album_release_date = song_info["album"]["release_date"]
    user_listened_to = song["played_at"]

    song_row = {"Name": song_name,
     "Artist": artist_name,
    #  "Album": album_name,
     "Song_Popularity": popularity,
     "Date_Listened_To": user_listened_to,
     "Album_Release_Date": album_release_date
     }
    
    songs_data.append(song_row)
    

df = pd.DataFrame(songs_data)

df.to_csv(f"{Name}'s 50 recently played spotify songs.csv")


#     print(f"{song_name} by {artist_name} released on {album_release_date} and listened to by me at {user_listened_to}")

