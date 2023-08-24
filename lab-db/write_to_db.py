# Módulo pymysql requerido, instalar con pip:
# pip3 install pymysql

import pymysql
import uuid

def write_random_value():
    try:
        print("Intentando escribir en la base de datos...")
        
        # Endpoints y configuración
        writer_endpoint = 'xxxxxxxxxxxxxxx.us-east-1.rds.amazonaws.com'
        db_name = 'example'
        user = 'example'
        password = 'example'

        # Generar un valor aleatorio UUID
        random_value = str(uuid.uuid4())

        # Conexión al nodo principal y escritura
        connection = pymysql.connect(host=writer_endpoint, user=user, password=password, database=db_name)
        with connection.cursor() as cursor:
            sql = "INSERT INTO `ragnar` (`value`) VALUES (%s)"
            cursor.execute(sql, (random_value,))
        connection.commit()
        print(f"Valor {random_value} insertado con éxito.")

    except Exception as e:
        print(f"Error durante la inserción: {e}")
    finally:
        if 'connection' in locals():
            connection.close()
