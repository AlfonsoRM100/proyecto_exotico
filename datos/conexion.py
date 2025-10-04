import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",       # o la IP del servidor si no es tu PC
            user="root",            # tu usuario de MySQL
            password="", # la contraseña que pusiste al instalar MySQL
            database="red_social"   # el nombre de tu base de datos
        )
        print(" Conexión exitosa a MySQL")
        return conexion
    except mysql.connector.Error as err:
        print(f" Error al conectar: {err}")
        return None
