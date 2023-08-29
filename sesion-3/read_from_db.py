# read_from_db.py

import pymysql

def fetch_values():
    # Endpoints y configuración
    reader_endpoint = 'demo.cluster-c8ngcue4bxze.us-east-1.rds.amazonaws.com'  # Aquí el endpoint del nodo de lectura
    db_name = 'ragnar'
    user = 'admin'
    password = 'DJVQOB6NdfL8ulTguklP'

    # Conexión al nodo de lectura y lectura
    connection = pymysql.connect(host=reader_endpoint, user=user, password=password, database=db_name)
    try:
        with connection.cursor() as cursor:
            # NOTA: Cambié `data` por `value` y `test_table` por `ragnar` para coincidir con la estructura de la tabla.
            sql = "SELECT `value` FROM `ragnar`"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row[0])
    finally:
        connection.close()

if __name__ == "__main__":
    fetch_values()
