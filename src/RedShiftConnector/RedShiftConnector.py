import os
import psycopg2
from dotenv import load_dotenv

def CreateTableArtists():
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
        create_table_query="CREATE TABLE IF NOT EXISTS luisjimenezrivas_coderhouse.artists (id INTEGER IDENTITY(1,1) PRIMARY KEY, name VARCHAR(255) NOT NULL,popularity INT,followers INT);"
        cursor.execute(create_table_query)
        connection.commit()
    except Exception as e:
        print(f"no se pudo crear la tabla")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            print("Conexión cerrada")

def InsertTableArtists():
    print("Insertar datos a la tabla")