import sqlite3
import re
import random
def reporte():
    with sqlite3.connect("database.db") as conexion:
        cursor = conexion.cursor()
        print("\n"+"ESTOS SON reportes".center(100,'-'))
        print("Bot: Ingresa su nombre/usuario: ")
        usuario=input("Tú: ")
        consulta = f'SELECT * FROM venta_producto where nombre_cliente="{usuario}" '
        cursor.execute(consulta)
        recoger = cursor.fetchone()
        print("")
        print("".center(80, '*'))
        print(" PRODUCTOS".center(80, '_'))
        print("|")
        for i in recoger: