from collections import deque
from ApiConnector.ApiConnector import callApi

def favoriteArtists():
    artists = deque(["6qqNVTkY8uBg9cP3Jd7DAH", "25uiPmTg16RbhZWAqwLBy5", "163tK9Wjr9P9DmM0AVK7lm", "00FQb4jTyendYWaN8pK0wa", "3l0CmX0FuQjFxr8SK7Vqag", "0NB5HROxc8dDBXpkIi1v3d", "0Cp8WN4V8Tu4QJQwCN5Md4", "7GlBOeep6PqTfFi59PTUUN"])
    return artists

def extractData(token, artists):
    list_of_artist = []
    print("[INFO] Obteniendo datos de los artistas desde Spotify API")
    for artist in artists:
        artist_table = {
            "name": callApi(token,artist).get("name"),
            "popularity": callApi(token,artist).get("popularity"),
            "followers": callApi(token,artist).get("followers", {}).get("total"),
        }
        list_of_artist.append(artist_table)
    print("[INFO] Informacion obtenida!")
    return list_of_artist