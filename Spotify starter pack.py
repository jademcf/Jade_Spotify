import spotipy 
from spotipy.oauth2 import SpotifyOAuth
from Spotify_Keys import client_id, client_secret, redirect_uri


#Spotify artist album data

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id,
                                               client_secret,
                                               redirect_uri,
                                               scope = "user-library-read"
                                        ))


artist_name = input("What is your artists name? ")

top_songs = input(f"Do you want to find out {artist_name}'s albums? Respond yes or no ")



if top_songs == "yes":
    artist_uri = input(f"""Please can you give me the end url so I can find these out? 
                       You take this as the last digits from the url, 
                       For example Taylpr Swift's url is https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02
                       Therefore her uri is 06HL4z0CvFAxyc27GXpf02. 
                       Please insert the uri for your artist here: 
                       """)
    results = sp.artist_albums(artist_uri, album_type = "album")
    albums = results["items"]
    while results["next"]:
        results = sp.next(results)
        albums.extend(results["items"])

    print(f"Below are {artist_name}'s albums:")
    for album in albums:
        print(album["name"])

else:
    pass
    print("Thank you for your time, I hope we can pull something else for you soon :)")



