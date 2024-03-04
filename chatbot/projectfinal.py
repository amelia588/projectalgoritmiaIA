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
                print("Bot: NOOO USUARIO Y CONTRASEÑA INCORRECTO ")
                print("Bot: Desea intentar de nuevo INICIAR SESION? si/no ")
                sesion=input("Tú: ")
                if sesion=="Si" or sesion=="si" or sesion=="SI" or sesion=="sI" :
                    continue
                else:
                    condicion0=True
                    print("\n"+"AHORA PROCEDERA A REGISTRARSE".center(100,'-'))
                print("Bot: Desea registrarse SI/NO :")
                registro_nuevo=input("Tú: ")
                if registro_nuevo == "SI" or registro_nuevo == "Si" or registro_nuevo == "si" or registro_nuevo == "sI":
                    registro_usuario()
                print("Bot: ¿Quieres seguir INICIADO SESION ? si /no")
                nuevose=input("Tú: ")
                if nuevose=="SI" or nuevose=="si" or nuevose=="Si" or nuevose =="sI":
                    print("\n"+"AHORA VA INICIAR SESION NUEVAMENTE".center(100,'-'))
                    iniciar_sesion()
                else:
                    print("Bot: OK hasta luego ")
                    condicion0=True
                    break
            cursor.close()
#***********************************************************************************
print("\n"+"".center(150,'*'))
print("BIEVENIDO A MI TIENDA".center(150,'-'))
print("".center(150,'*')+"\n")
print("Bot: hola mi nombre es Alexa y soy tu asistente virtual ")

def get_respuesta(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    
    respuesta = revisar_todas_respuestas(split_message)
    if respuesta=="desea INICIAR SESION Y COMPRAR PRODUCTOS?":
        registro_usuario()
    elif respuesta=="hola de nuevo":
        iniciar_sesion()
    elif respuesta=="esos son los PRODUCTOS que VENDEMOS , desea comprar?":
        consulta_producto()
    elif respuesta=='estos son los reportes':
        reporte()
        
    return respuesta

def mensaje_probabilidad(user_message, recognized_words, single_respuesta=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))
    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_respuesta:
        return int(percentage * 100)
    else:
        return 0
def revisar_todas_respuestas(message):
        highest_prob = {}

        def respuesta(bot_respuesta, list_of_words, single_respuesta = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_respuesta] = mensaje_probabilidad(message, list_of_words, single_respuesta, required_words)

        respuesta('hola',['hola', 'saludos','buenas','buenos dias','buenas tardes','buenas noches'], single_respuesta = True)
        respuesta('estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        respuesta('estoy de maravillas tu?', ['tal'], single_respuesta = True)
        respuesta('que bien ! en que puedo servirle? ',['estoy bien', 'bien','genial','tambien','igualmente','igual'],single_respuesta = True)
        respuesta('estos son los reportes', ['lista','repor','reporte'], single_respuesta=True)        
        respuesta('desea INICIAR SESION Y COMPRAR PRODUCTOS?',['registrar', 'registro','registrarme','nuevo'], single_respuesta = True)
        respuesta('esos son los PRODUCTOS que VENDEMOS , desea comprar?', ['ver','vende','productos', 'disponible', 'muestra', 'stock','vendes'], single_respuesta=True)
       
        
        respuesta('hola de nuevo',['si', 'SI','Si','comprar','sesion','iniciar'], single_respuesta = True)
        respuesta('estoy trabajando como tu asistente',[ 'haces','haciendo','trabajas','dedicas','planes'], single_respuesta = True)
        respuesta('Estamos ubicados en la calle 23 de la avenida central N° 345', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_respuesta=True)
        respuesta('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks','ok','muchas gracias'], single_respuesta=True)
        

        

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    respuesta = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return respuesta

while True:
    
    print("Bot: " + get_respuesta(input('Tú: ')))

