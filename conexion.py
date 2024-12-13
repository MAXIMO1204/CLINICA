import mysql.connector
from mysql.connector import Error

# Configuración de conexión a la base de datos
config = {
    "user": "root",
    "password": "maximo2213",
    "host": "localhost",
    "database": "usuarios"
}

# Función para obtener una conexión a la base de datos
def obtener_conexion():
    try:
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
