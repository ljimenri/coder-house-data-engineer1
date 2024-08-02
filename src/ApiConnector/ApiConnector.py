import requests
from dotenv import load_dotenv
import os

def getToken():
    # Carga de variables de entorno
    load_dotenv()
    # Definicion de variables de entorno
    url = "https://accounts.spotify.com/api/token"
    # Encabezados de la solicitud
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # Datos del cuerpo de la solicitud
    data = {
        "grant_type": "client_credentials",
        "client_id": os.getenv('CLIENT_ID'),
        "client_secret": os.getenv('CLIENT_SECRET')
    }
    # Configuración de respuesta
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        token = response.json().get('access_token')
        return token
    else:
        print(f"Error en la Api: no se ha podido obtener token")

def callApi(token, artist):
    # Datos del cuerpo de la solicitud
    url="https://api.spotify.com/v1/artists/"+artist
    header_value="Bearer"+" "+token
    headers = {
    "Authorization": header_value
    }
    # Configuración de respuesta
    response=requests.get(url, headers=headers)
    if response.status_code == 200:
        return_api = response.json()
        return return_api
    else:
        print(f"Error en la solicitud: {response.status_code}")
        print(response.text)