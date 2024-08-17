import os
import psycopg2
from dotenv import load_dotenv

def CreateTableArtists():
    print("[INFO] Creando tabla en la base de datos...")
    connection = None
    cursor = None
    load_dotenv()
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('NAME_DATABASE'),
            user=os.getenv('NAME_USER_DATABASE'),
            password=os.getenv('PASS_USER_DATABASE'),
            host=os.getenv('HOST_DATABASE'),
            port=os.getenv('PORT_DATABASE')
        )
        cursor = connection.cursor()
        create_table_query="CREATE TABLE IF NOT EXISTS luisjimenezrivas_coderhouse.artists (id INTEGER IDENTITY(1,1) PRIMARY KEY, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, name VARCHAR(255) NOT NULL,popularity INT,followers INT, images VARCHAR(255) NOT NULL, type VARCHAR(255) NOT NULL, genre VARCHAR(255) NOT NULL);"
        cursor.execute(create_table_query)
        connection.commit()
        print("[INFO] Tabla creada!")
    except Exception as e:
        print("[ERROR] No se pudo crear la tabla")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            print("[INFO] Tabla ya existente: se cierra la conexion!")

def InsertTableArtists(list_of_artists):
    print("[INFO] Insertando artistas en la base de datos...")
    connection = None
    cursor = None
    load_dotenv()
    list_of_tuples = [(artist["created_at"], artist["name"], artist["popularity"], artist["followers"], artist["images"], artist["type"],artist["genre"], ) for artist in list_of_artists]
    insert_query = """
    INSERT INTO luisjimenezrivas_coderhouse.artists (created_at, name, popularity, followers, images, type, genre)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('NAME_DATABASE'),
            user=os.getenv('NAME_USER_DATABASE'),
            password=os.getenv('PASS_USER_DATABASE'),
            host=os.getenv('HOST_DATABASE'),
            port=os.getenv('PORT_DATABASE')
        )
        cursor = connection.cursor()
        cursor.executemany(insert_query, list_of_tuples)
        connection.commit()
        print("[INFO] Datos insertados!")
    except psycopg2.Error as e:
        print(f"[ERROR] Al insertar datos: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
