#!/bin/bash
# Actualizar paquetes e instalar httpd
yum update -y
yum install -y httpd

# Crear la estructura de directorio para el servicio1
mkdir -p /var/www/html/servicio1

# Agregar una página de prueba
echo '<h1>Servicio 1 está funcionando!</h1>' > /var/www/html/servicio1/index.html

# Crear una página para el health check
echo 'Healthy' > /var/www/html/health.html

# Iniciar y habilitar el servicio httpd
systemctl start httpd
systemctl enable httpd