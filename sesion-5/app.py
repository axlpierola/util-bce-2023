import pymysql
import boto3
import os
import json
import datetime
from flask import Flask, jsonify

# Especificar la región de AWS
AWS_REGION = 'us-east-1'  # Cambia esto a la región donde tienes tus recursos

app = Flask(__name__)

@app.route('/')
def insert_timestamp():
    try:
        # Inicializar los clientes de Secrets Manager y Parameter Store con la región especificada
        secrets_client = boto3.client('secretsmanager', region_name=AWS_REGION)
        ssm_client = boto3.client('ssm', region_name=AWS_REGION)

        # Recuperar las credenciales desde Secrets Manager
        secret_value_response = secrets_client.get_secret_value(SecretId=os.environ['SECRET_ID'])
        secret_values = json.loads(secret_value_response['SecretString'])

        # Recuperar el nombre de la DB y el endpoint desde Parameter Store
        param_db_name_response = ssm_client.get_parameter(Name=os.environ['DB_NAME_PARAM'])
        param_endpoint_response = ssm_client.get_parameter(Name=os.environ['DB_ENDPOINT_PARAM'])
        
        db_name = param_db_name_response['Parameter']['Value']
        db_endpoint = param_endpoint_response['Parameter']['Value']

        # Conectar a RDS
        connection = pymysql.connect(
            host=db_endpoint,
            user=secret_values['username'],
            password=secret_values['password'],
            db=db_name
        )

        cursor = connection.cursor()
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insert_query = f"INSERT INTO timestamp_logs (timestamp) VALUES ('{current_time}')"
        
        cursor.execute(insert_query)
        connection.commit()
        connection.close()

        return jsonify({"message": "Insert successful", "timestamp": current_time}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)