#!/bin/bash
yum update -y
yum install -y python3 git

# Instalar pip si es necesario
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

# Instalar Flask y pymysql
pip3 install Flask pymysql boto3

# Clonar el repositorio y moverse al directorio del proyecto
git clone https://github.com/tu_usuario_de_github/my_aws_app.git
cd my_aws_app

# Establecer variables de entorno (puedes ponerlas en un archivo .env o exportarlas aquí)
export SECRET_ID='arnSecret'
export DB_NAME_PARAM='MyDBName'
export DB_ENDPOINT_PARAM='MyDBEndpoint'

# Ejecutar la aplicación
nohup python3 app.py > app.log 2>&1 &