from collections import deque
from ApiConnector.ApiConnector import callApi, getAlbumAPI
from datetime import datetime

def favoriteArtists():
    artists = deque(["6qqNVTkY8uBg9cP3Jd7DAH", "25uiPmTg16RbhZWAqwLBy5", "163tK9Wjr9P9DmM0AVK7lm", "00FQb4jTyendYWaN8pK0wa", "3l0CmX0FuQjFxr8SK7Vqag", "0NB5HROxc8dDBXpkIi1v3d", "0Cp8WN4V8Tu4QJQwCN5Md4", "7GlBOeep6PqTfFi59PTUUN"])
    return artists
def favoriteAlbum():
    albums = deque(["0S0KGZnfBGSIssfF54WSJh"])
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
            "total_tracks": getAlbumAPI(token,album).get("total_tracks"),
            "name": getAlbumAPI(token,album).get("name"),
            "release_date": getAlbumAPI(token,album).get("release_date"),
            "copyright": getAlbumAPI(token,album).get("label"),
        }
        list_of_albums.append(albums_table)
    print(albums_table)
    return list_of_albums