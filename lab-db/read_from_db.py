import pymysql

def fetch_values():
    # Endpoints y configuración
    reader_endpoint = 'xxxxxxxxxxxxxxx.us-east-1.rds.amazonaws.com'  # Aquí el endpoint del nodo de lectura
    db_name = 'example'
    user = 'example'
    password = 'example'

    # Conexión al nodo de lectura y lectura
    connection = pymysql.connect(host=reader_endpoint, user=user, password=password, database=db_name)
    try:
        with connection.cursor() as cursor:
            # NOTA: Cambié  `ragnar` por `su-tabla`  para coincidir con el nmbre de la tabla.
            sql = "SELECT `value` FROM `ragnar`"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row[0])
    finally:
        connection.close()

if __name__ == "__main__":
    fetch_values()
