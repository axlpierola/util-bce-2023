#!/bin/bash

# Instalar httpd (Apache)
yum update -y
yum install -y httpd

# Crear archivo HTML
echo "<html>
<head><title>Bootcamp Cloud Engineer 2023</title></head>
<body>
<h1>Probando user-data en Bootcamp Cloud Engineer 2023</h1>
<p>¡Bienvenido al mundo de la automatización en AWS con user-data!</p>
</body>
</html>" > /var/www/html/index.html

# Iniciar el servicio de httpd y habilitarlo al inicio
systemctl start httpd
systemctl enable httpd
