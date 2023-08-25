# write_to_db.py

import pymysql
import uuid

def write_random_value():
    # Endpoints y configuración
    writer_endpoint = 'demo.cluster-c8ngcue4bxze.us-east-1.rds.amazonaws.com'
    db_name = 'ragnar'
    user = 'admin'
    password = 'DJVQOB6NdfL8ulTguklP'

    # Generar un valor aleatorio UUID
    random_value = str(uuid.uuid4())

    # Conexión al nodo principal y escritura
    connection = pymysql.connect(host=writer_endpoint, user=user, password=password, database=db_name)
    try:
        with connection.cursor() as cursor:
            # NOTA: Cambié `data` por `value` para coincidir con la estructura de la tabla.
            sql = "INSERT INTO `ragnar` (`value`) VALUES (%s)"
            cursor.execute(sql, (random_value,))
        connection.commit()
        print(f"Valor {random_value} insertado con éxito.")
    finally:
        connection.close()

if __name__ == "__main__":
    write_random_value()
