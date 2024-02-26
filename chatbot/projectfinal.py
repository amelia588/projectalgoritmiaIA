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
            # PARA CONVERTIR UNA TUPLA EN UNA CADENA
            print("".join(i))
            print("".center(80, '*'))
        print("")
        cursor.close()
        # CREAMOS EL REGISTRO USUARIO
def registro_usuario():

    with sqlite3.connect("database.db") as conexion:
        cursor = conexion.cursor()
        condicionn=False
        while condicionn==False:
            print("\n"+"BIENVENIDO A REGISTRO".center(100,'-'))
            print("Bot: Ingresa su nombre/usuario: ")
            usuario=input("Tú: ")
            print("Bot: Ingresa la contraseña: ")
            contrasenia=input("Tú: ")
            print("Bot: Ingresa su correo : ")
            correo=input("Tú: ")
            consulta0="SELECT usuario,corrreo FROM datos_usuarios WHERE usuario=? OR corrreo=?"
            parametro0=(usuario,correo)
            cursor.execute(consulta0,parametro0)
            if cursor.fetchall():
                print("\n"+"ESOS DATOS DE REGISTRO YA EXISTE, INTENTE CON OTROS DATOS".center(100,'-'))
                print("Bot: Desea intentar de nuevo REGISTRARSE? si/no ")
                sesion=input("Tú: ")
                if sesion=="Si" or sesion=="si" or sesion=="SI" or sesion=="sI" :
                    continue
                else:
                    condicionn=True
                    cursor.close()
                    break
            else:
                consulta = "INSERT INTO datos_usuarios VALUES(?,?,?)"
                parametros = (usuario, contrasenia, correo)
                cursor.execute(consulta, parametros)
                print("SU REGISTRO FUE UN EXITO".center(100,'-')+"\n")
                condicionn=True
