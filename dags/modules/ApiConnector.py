import requests
from dotenv import load_dotenv
import os

def getToken():
    print("[INFO] Obteniendo token desde Spotify API...")
    load_dotenv()
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": os.getenv('CLIENT_ID'),
        "client_secret": os.getenv('CLIENT_SECRET')
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        token = response.json().get('access_token')
        print("[INFO] Token Obtenido!")
        return token
    else:
        print("[ERROR] No se ha podido obtener el token desde Spotify API")

def callApi(token, artist):
    url="https://api.spotify.com/v1/artists/"+artist
    header_value="Bearer"+" "+token
    headers = {
    "Authorization": header_value
    }
    response=requests.get(url, headers=headers)
    if response.status_code == 200:
        return_api = response.json()
        return return_api
    else:
        print(f"[ERROR] Error en la solicitud:{response.status_code}")

def getAlbumAPI(token, album):
    url="https://api.spotify.com/v1/albums/"+album
    header_value="Bearer"+" "+token
    headers = {
    "Authorization": header_value
    }
    response=requests.get(url, headers=headers)
    if response.status_code == 200:
        return_api_album = response.json()
        return return_api_album
    else:
        print(f"[ERROR] Error en la solicitud:{response.status_code}")