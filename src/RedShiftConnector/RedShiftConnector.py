import os
import psycopg2
from dotenv import load_dotenv

def DataBaseConnection():
    connection = None
    cursor = None
    load_dotenv()
    try:
        # Establecer la conexión a la base de datos
        connection = psycopg2.connect(
            dbname=os.getenv('NAME_DATABASE'),
            user=os.getenv('NAME_USER_DATABASE'),
            password=os.getenv('PASS_USER_DATABASE'),
            host=os.getenv('HOST_DATABASE'),
            port=os.getenv('PORT_DATABASE')
        )

        # Crear un cursor
        cursor = connection.cursor()

        # Ejecutar una consulta de prueba
        cursor.execute("select * from persona p")
        version = cursor.fetchone()
        print(f"Conectado a: {version}")

    except Exception as e:
        print(f"Error al conectar: {e}")

    finally:
        # Cerrar el cursor si fue creado
        if cursor is not None:
            cursor.close()

        # Cerrar la conexión si fue creada
        if connection is not None:
            connection.close()
            print("Conexión cerrada")

