-- Por favor reemplaza 'ragnar' por el nombre de tu ejemplo.

-- Creamos la base de datos llamada 'ragnar'.
CREATE DATABASE ragnar;

-- Seleccionamos la base de datos 'ragnar' para operar sobre ella.
USE ragnar;

-- Ahora vamos a crear una tabla llamada 'ragnar' dentro de la base de datos 'ragnar'.
CREATE TABLE ragnar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    value INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);