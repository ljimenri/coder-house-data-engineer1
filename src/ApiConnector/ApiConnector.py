import requests
from dotenv import load_dotenv
import os
def getToken():
    
    load_dotenv()
    #Definicion de variables de entorno
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

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error en la Api: no se ha podido obtener token")

