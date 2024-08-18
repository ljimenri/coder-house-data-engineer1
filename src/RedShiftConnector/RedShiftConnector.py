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
        create_table_query = """
        CREATE TABLE IF NOT EXISTS luisjimenezrivas_coderhouse.artists (
            id INTEGER IDENTITY(1,1) PRIMARY KEY,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            name VARCHAR(255) NOT NULL,
            popularity INT,
            followers INT,
            images VARCHAR(255) NOT NULL,
            type VARCHAR(255) NOT NULL,
            genre VARCHAR(255) NOT NULL,
            total_tracks INT,
            name_album VARCHAR(255) NOT NULL,
            release_date VARCHAR(255) NOT NULL,
            copyright VARCHAR(255) NOT NULL
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("[INFO] Tabla creada!")
    except Exception as e:
        print(f"[ERROR] No se pudo crear la tabla: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            print("[INFO] Tabla ya existente: se cierra la conexion!")

def InsertTableArtists(list_of_artists):
    print("[INFO] Insertando artistas en la base de datos...")
    load_dotenv()
    connection = None
    cursor = None
    try:
        list_of_tuples = list(list_of_artists.itertuples(index=False, name=None))
        
        for i, t in enumerate(list_of_tuples):
            if len(t) != 11:
                print(f"Error en la tupla {i}: {t} (longitud: {len(t)})")
                return

        insert_query = """
        INSERT INTO luisjimenezrivas_coderhouse.artists 
        (created_at, name, popularity, followers, images, type, genre, total_tracks, name_album, release_date, copyright)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

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
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
