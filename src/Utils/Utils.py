from collections import deque
from ApiConnector.ApiConnector import callApi, getAlbumAPI
from datetime import datetime
import pandas as pd

def favoriteArtists():
    artists = deque(["6qqNVTkY8uBg9cP3Jd7DAH", 
                     "25uiPmTg16RbhZWAqwLBy5",
                     "163tK9Wjr9P9DmM0AVK7lm",
                     "00FQb4jTyendYWaN8pK0wa",
                     "3l0CmX0FuQjFxr8SK7Vqag",
                     "0NB5HROxc8dDBXpkIi1v3d",
                     "0Cp8WN4V8Tu4QJQwCN5Md4",
                     "7GlBOeep6PqTfFi59PTUUN",
                     ])
    return artists
def favoriteAlbum():
    albums = deque(["0S0KGZnfBGSIssfF54WSJh", 
                    "2lIZef4lzdvZkiiCzvPKj7",
                    "2B87zXm9bOWvAJdkJBTpzF",
                    "1ORxRsK3MrSLvh7VQTF01F",
                    "4kkVGtCqE2NiAKosri9Rnd",
                    "7HQOEMCDGKY8eJyQPdsnYH",
                    "3ZJSoxsPMkNC9eb6gUn0Q8",
                    "0EiI8ylL0FmWWpgHVTsZjZ",
                    ])
    return albums

def extractData(token, artists):
    list_of_artist = []
    print("[INFO] Obteniendo datos de los artistas desde Spotify API")
    for artist in artists:
        artist_table = {
            "created_at": datetime.now(),
            "name": callApi(token,artist).get("name"),
            "popularity": callApi(token,artist).get("popularity"),
            "followers": callApi(token,artist).get("followers", {}).get("total"),
            "images": callApi(token,artist).get("images")[0]["url"],
            "type": callApi(token,artist).get("type"),
            "genre": callApi(token,artist).get("genres")[0],
            
        }
        list_of_artist.append(artist_table)
    print("[INFO] Informacion obtenida!")
    return list_of_artist

def extractDataAlbum(token, albums):
    list_of_albums = []
    print("[INFO] Obteniendo datos de albums desde Spotify API")
    for album in albums:
        albums_table = {
            "name": getAlbumAPI(token, album).get("artists", [{}])[0].get("name"),
            "total_tracks": getAlbumAPI(token,album).get("total_tracks"),
            "name_album": getAlbumAPI(token,album).get("name"),
            "release_date": getAlbumAPI(token,album).get("release_date"),
            "copyright": getAlbumAPI(token,album).get("label"),
        }
        list_of_albums.append(albums_table)
    return list_of_albums

def joinDataArtistWithAlbum(artists, albums):
    df_artists = pd.DataFrame(artists)
    df_albums = pd.DataFrame(albums)
    return pd.merge(df_artists, df_albums, on='name', how='inner')