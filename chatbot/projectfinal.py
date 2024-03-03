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
# LLAMAMOS AL MEOTOD REGISTRO USUARIO
# registro_usuario()
def consulta_producto():
    with sqlite3.connect("database.db") as conexion:
        cursor = conexion.cursor()
        print("\n"+"ESTOS SON LOS PRODUCTOS QUE VENDEMOS".center(100,'-'))
        consulta = "SELECT * FROM productos"
        cursor.execute(consulta)
        recoger = cursor.fetchall()
        print("")
        print("".center(80, '*'))
        print(" PRODUCTOS".center(80, '_'))
        print("|")
        for i in recoger:

 # consulta_producto()



def iniciar_sesion():
    with sqlite3.connect("database.db") as conexion:
        cursor = conexion.cursor()
        condicion0=False
        
        while condicion0==False:
            
            print("Bot: Ingresa su nombre/usuario: ")
            usuario=input("Tú: ")
            print("Bot: Ingresa la contraseña: ")
            contrasenia=input("Tú: ")
            consulta = "SELECT * FROM datos_usuarios WHERE usuario=? AND contrasenia=?"
            parametro = (usuario, contrasenia)
            cursor.execute(consulta, parametro)
            if cursor.fetchall():  # si exite el curso
                print("\n"+"SESION INICIADA CORRECTAMENTE".center(100,'-'))
                print("AHORA PUEDE COMPRAR EL PRODUCTO".center(100,'-')+"\n")
                consulta_producto()
                condicion = False
                while condicion == False:
                    # upper() para convertir en mayuscula el text ingresado
                    print("Bot: Ingresa el NOMBRE del producto que va comprar: ")
                    producto=input("Tú: ").upper()
                    consulta = "SELECT * FROM productos WHERE nombre_produc =? OR pro2=? OR pro4=? OR pro5=? OR pro6=? OR pro7=?"
                    parametro = (producto,producto,producto,producto,producto,producto)
                    cursor.execute(consulta, parametro)
                    if cursor.fetchall():
                        print("\n"+"PRODUCTO DISPONIBLE".center(100,'-'))
                        try:
                            obtener_precio=f'SELECT precio FROM  precio_productos WHERE nombre="{producto}" '
                            cursor.execute(obtener_precio)
                            precio=cursor.fetchone()
                           
                            res=""
                            for i in precio:
                                res+=str(i)
                            res=int(res)                            
                            #print("Bot: Ingresa el PRECIO del producto que seleccionó: ")
                            #precio=int(input("Tú: "))
                            print("Bot: Ingresa la CANTIDAD que desea comprar: ")
                            cantidad=int(input("Tú: "))
                            precio_fin = res*cantidad
                            print("Bot: Ingrese su UBICACION para la entrega de productos: ")
                            ubicacion=input("Tú: ")
                            consulta1 = "INSERT INTO venta_producto VALUES (?,?,?,?,?,?)"
                            parametro1 = (usuario, producto, res,cantidad, precio_fin, ubicacion)
                            cursor.execute(consulta1, parametro1)
                            print("\n"+"SE REGISTRO SU COMPRA CORRECTAMENTE".center(100,'-'))
                        except Exception as e:
                            print("INGRESA LOS TIPO DE DATO CORRECTO".center(100,'-'))
                            
                        print("Bot: DESEA SEGUIR COMPRANDO? si/no: ")
                        pregunta2=input("Tú: ")

                        if pregunta2 == "SI" or pregunta2 == "Si" or pregunta2 == "si" or pregunta2 == "sI":
                                continue
                            
                        else:
                             print("Bot : OK GRACIAS BUEN DIA")
                            #PONER REPORTE DIRECTO
                            print("BOLETA".center(100,'-'))
                            print(f'PRODUCTO: {producto}')
                            print(f'CANTIDAD {cantidad}')
                            print(f'PRECIO: {precio}')
                            print(f'PRECIO FINAL{precio_fin}')
                            print(f'DIRECCION DE ENTREGA: {ubicacion}')
                            
                            print("Bot : OK GRACIAS BUEN DIA")
                            
                            
                            condicion = True
                            return

                    else:
                        print("Bot: EL PRODUCTO NO SE ENCONTRO")
                        print("Bot: DESEA VER LOS PRODUCTOS QUE TENEMOS? : SI/NO ")
                        consulta =input("Tú: ")
                        if consulta == "SI" or consulta == "Si" or consulta == "si" or consulta == "sI":
                            consulta_producto()

                        else:
                            print("Bot: OK su operacion termino ")
                            condicion = True
                            return
                    #cursor.close()

                ###

            else:
