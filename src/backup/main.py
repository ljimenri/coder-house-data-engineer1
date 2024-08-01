import requests

# URL de la API de Spotify para obtener el token
url = "https://accounts.spotify.com/api/token"

# Encabezados de la solicitud
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Datos del cuerpo de la solicitud
data = {
    "grant_type": "client_credentials",
    "client_id": "ce4d73ecc9eb45d985817229c03d5075",
    "client_secret": "0b01882da1df46ad896258a5334429e0"
}

# Realizar la solicitud POST
response = requests.post(url, headers=headers, data=data)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    token_info = response.json()
    print(token_info)
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)

# 2 Con el token obtenido a anteriormente consultar la api de spotify


# URL de la API de Spotify para obtener el token
url2 = "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb"

# Encabezados de la solicitud
headers2 = {
    "Authorization": "Bearer BQBkXAU8jAfP6J8_lQp_WUbDtuGl_r9fJSqzZqy_twHpALhGgKuv4kzMqb9s7tzN2sSroU3m7l-_E2oklHR23CnTEHfB32MK_fHzzslGhpS4Jw-mmKw"
}

# Realizar la solicitud POST
response2 = requests.get(url2, headers=headers2)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    token_info2 = response2.json()
    print(token_info2)
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response2.text)