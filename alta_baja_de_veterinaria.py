# Iniciamos el código importando la librería sys:
# Este módulo de Python proporciona acceso a variables y funciones específicas del sistema. 
# Sys.exit() #finaliza la ejecución de mi programa.
import sys

# Creamos una lista compuesta por diccionarios para su consulta. 
datos_mascotas= [{'nombre': 'Scooby Doo', 'edad': 49, 'dueño': 'Shaggy','diagnostico': 'diabetes','telefono':'154758444'},
                 {'nombre': 'Hachiko', 'edad': 11, 'dueño': 'Richard Gere','diagnostico':'ataque cardíaco','telefono': '42581234'}] 

# Creamos un diccionario vacío que será cargado más adelante.
dato_mascota = {} 
# Mensaje de bienvenida no se vuelve a repetir hasta que se vuelva a ejecutar el programa.
print("Bienvenido al portal de las mascotas.") 

# A continuación esta la función "immprimir_menu_principal"
# Las primeras líneas muestran al usuario las funciones que puede realizar.
#solcicita al usuario introduzca la opción que desea.
#opcion 1 invoca la función "menu_de_alta" para la carga de pacientes.
#opcion 2 invoca la funcion "menu_de_modificación" de los registros realizados.
#opcion 3 invoca a una funcion "menu_de_consulta" de los pacientes
#opcion 4 invoca la funcion "imprimir_reporte_html" de la lista de mascotas a un archivo html
#opcion 5 envía mensaje de despedida y cierra el programa
#else   envía mensaje de corrección y deriva a la funcion del menu principal
def imprimir_menu_principal():
    print("Ingresa una opcion para continuar") 
    print("1 - Carga de paciente")
    print("2 - Modificacion de ficha del paciente.")
    print("3 - Consultar datos de pacientes.")
    print("4 - Dar de baja un paciente")
    print("5 - Imprimir reporte de pacientes.")
    print("6 - Finalizar el programa.")
    opcion = input("elija su opcion: ") 
    if opcion == "1":
        menu_de_alta() 
    elif opcion == "2":
        menu_de_modificacion() 
    elif opcion == "3":
        menu_de_consulta()
    elif opcion =="4":
        menu_de_baja() 
    elif opcion == "5":
        imprimir_reporte_html(datos_mascotas) 
    elif opcion == "6":
        print("gracias vuelva pronto") 
        sys.exit()
    else:
        print("opcion incorrecta intente denuevo") 
        imprimir_menu_principal()

# A continuación esta función "menu_de_alta" que es utilizada para la carga de pacientes.
#creamos una variable cuyo valor es un booleano
#entramos al ciclo while con la condición True para mantenerse dentro del ciclo
#cargamos los datos al diccionario dato_mascota 
#Luego cargamos dichos datos a la lista datos_mascotas con la función append()
#le damos la opción al usuario de seguir cargando datos
#si el usuario responde 1 es true continua el while pero 
#si es distinto a 1 se asigna false a la variable control_menu y finaliza el ciclo
#imprime una separación para una mejor visualización para el usuario
#invoca al menu principal 
def menu_de_alta(): 
    control_menu = True 
    while control_menu == True:
        dato_mascota = {}  
        dato_mascota['nombre']= input("Ingrese el nombre del animal: ") 
        dato_mascota['edad']= int(input("Ingrese la edad del animal: "))
        dato_mascota['dueño']= input("Ingrese el dueño del animal: ")
        dato_mascota['diagnostico']=input("Ingrese el diagnostico del animal: ")
        dato_mascota['telefono']=input("Ingrese un telefono de contacto: ")
        datos_mascotas.append(dato_mascota) 
        opcion = input("Ingrese 1 para continuar ingresando pacientes o un numero distinto para volver al menu principal: ") 
        if opcion != "1": 
            control_menu= False
         
    print("===========================================================")
    imprimir_menu_principal()

# A continuación esta función "menu_de_baja" es utilizada para eliminar algun paciente registrado
# primero creamos una variable cuyo valor es un booleano que vamos a utilizar para poder salir del ciclo while una vez entremos
# la condicion while indica que mientras el valor de la variable siga siendo True continuará el ciclo
# luego el programa solicita que el usuario ingrese nombre de la mascota y su dueño
# luego entra dentro del ciclo for para iterar dentro de la lista "datos_mascotas" en las iteraciones el ciclo debe corroborar
# que algun registro coincida nombre dueño y nombre mascota si solo si
# lo encuentra enviará notificacion al usuario y procederá a eliminar dicho registro
# posteriormente solicita al usuario introducir un valor para continuar dentro del ciclo while o salir del mismo
# el programa finaliza invocando la funcion de menu principal.
def menu_de_baja():
    control_menu= True
    while control_menu==True:
        nombre_mascota=input("introduzca el nombre de la mascota que desea eliminar: ")
        nombre_dueño=input("introduzca el nombre del dueño: ")
        for mascota in datos_mascotas:
            if mascota['nombre']==nombre_mascota and mascota['dueño']==nombre_dueño:
                print("mascota encontrada y eliminada")
                datos_mascotas.remove(mascota)
        opcion=input("Ingrese 1 para buscar otro registro o un numero distinto para salir al menu principal: ")
        if opcion!="1":
            control_menu= False
    print("============================================================")
    imprimir_menu_principal()        
    
# A continuación esta funcion "menu_de_consulta" que es utilizada para realizar consultas sobre los pacientes
# primero designamos la variable opción con un valor inicial
# entramos al ciclo while cuya condición de salida es que el usuario introduzca la opción 6
# el programa imprime todas las funciones disponibles para el usuario
# 1- invoca la funcion que retorna al paciente con mayor edad
# 2- invoca la funcion que retorna al paciente con menor edad
# 3- invoca la funcion que obtiene el promedio de edad de los pacientes
# 4- imprime directamente la cantidad de registros de la lista datos_mascotas 
# 5- imprime directamente la totalidad de los registros almacenados
# 6- sale del ciclo while y vuelve con la funcion imprimir_menu_principal()
# 7- imprime mensaje de despedida y cierra el programa
def menu_de_consulta():
    opcion= -1
    while opcion != '6':
        print("Ingresa una opcion para continuar")
        print("1 - Informar mascota con mayor edad.")
        print("2 - Informar mascota con menor edad.")
        print("3 - Informar el promedio de edad de las mascotas.")
        print("4 - Informar la cantidad de pacientes registrados.")
        print("5 - Informar todos los registros.")
        print("6 - Volver al menu principal.")
        print("7 - Finalizar el programa")
        opcion = input("ingrese su opcion: ")
        if opcion == "1":
            print(informar_mascota_mayor_edad(datos_mascotas))
        elif opcion == "2":
            print(informar_mascota_menor_edad(datos_mascotas))
        elif opcion == "3":
            print(promedio_edad(datos_mascotas))
        elif opcion == "4":
            print("la cantidad de registros es: "+ str(len(datos_mascotas)))
        elif opcion== "5":
            print("los registros son: "+ str(datos_mascotas))
        elif opcion == "7":
            print("gracias vuelva pronto")
            sys.exit()
    imprimir_menu_principal()

# A continuación esta función "menu_de_modificacion" que es utilizada para la modificacion de un registro existente
# primero cargamos a la variable opcion un valor inicial
# entramos al ciclo while con la condicion de salida que el usuario introduzca el numero 2
# cargamos dos variables dueño y nombre_mascota 
# entramos al ciclo for iterando en la lista "datos_mascotas"
# el ciclo valida si la variable dueño es igual igual a la iteración mascota en la clave ["dueño"] del diccionario
# y tambien tiene que coincidir con la variable nombre_mascota igual igual a mascota con la clave ["nombre"]
# si encuentra la coincidencia imprime la iteracion de la lista
# y tambien imprime un menu de opciones a ejecutar 
# opcion 1- pide una nueva edad que almacena en la iteracion mascota en la clave ["edad"] y hace un break
# la instruccion "break" finaliza la ejecucion de una instruccion en este caso finaliza del "for" y el control pasa a la siguiente instrucción
# la opcion 2 tambien es un break y continua al imput opcion para continuar o volver al menu
# la opcion 3 mensaje de despedida y termina el programa
# una vez que finaliza el ciclo while vuelve a invocar la funcion menu principal
def menu_de_modificacion():
    opcion = -1
    print("Ingresa el nombre del dueño y del animal que desea modificar: ")
    while opcion != '2':
        dueño = input("¿Cual es el nombre del dueño? ")
        nombre_mascota = input("¿Cual es el nombre de su mascota? ")
        for mascota in datos_mascotas:
            if dueño == mascota["dueño"] and nombre_mascota == mascota["nombre"]:
                print("Mascota encontrada: " + str(mascota))
                print("Ingresa una opcion:")
                print("1 - Actualizar su edad y diagnostico")
                print("2 - Volver al menu anterior.")
                print("3 - Finalizar el programa.")
                opcion = input("ingrese su opcion: ")
                if opcion== "1":
                    nueva_edad = int(input("Ingresa su nueva edad: "))
                    mascota["edad"] = nueva_edad
                    nuevo_diagnostico=input("Ingrese su nuevo diagnostico: ")
                    mascota["diagnostico"]=nuevo_diagnostico
                    break
                elif opcion== "2":
                    break
                elif opcion== "3":
                    print("gracias vuelva pronto")
                    sys.exit()
        opcion = input ("Ingrese 2 para volver al menu principal y otro numero para hacer otra modificacion: ")
        
    imprimir_menu_principal()

# A continuación esta la funcion "informar_mascota_mayor_edad" y le enviamos por parámetro la lista "datos_mascotas"
# la lista datos_mascotas viene acompañada por " : list" esto es una buena práctica en programación con Python 
# para aumentar la legibilidad de la función,
# es decir, es una aclaración de que los datos que estan cargados a la función son una lista.
# inicializamos una variable edad con un valor inicial
# llamamos al ciclo for e iteramos en la lista datos_mascotas
# si el valor de la iteracion ['edad'] es mayor a la variable edad se cargará ese valor a la variable edad
# también se guardará la iteración dentro de la variable mascota_mayor
# para luego retornar esa variable.    
def informar_mascota_mayor_edad(datos_mascotas: list):
    edad=-1
    for mascota in datos_mascotas:
        if mascota['edad']>edad:
            edad=mascota['edad']
            mascota_mayor = mascota
    return mascota_mayor

#A continuación esta la funcion "informar_mascota_menor_edad"
# esta funcion opera igual a la anterior con la diferencia que 
# la variable edad debe comenzar con un valor inicial alto yaque, lo que se busca aquí es el valor mas bajo
# y le cambiamos el simbolo > por < para que busque el dato menor.
def informar_mascota_menor_edad(datos_mascotas: list):
    edad=50
    for mascota in datos_mascotas:
        if mascota['edad']<edad:
            edad=mascota['edad']
            mascota_menor = mascota
    return mascota_menor

# A continuación esta la funcion "promedio_edad"
# inicializamos una variable con un valor 0
# iniciamos un ciclo for que va a iterar en la lista y va ir sumando los valores de mascota['edad'] en la variable edad,
# luego en la variable promedio opera la variable edad dividido la cantidad de registros utilizando len()
# retorna un string y el resultado de la variable promedio
def promedio_edad(datos_mascotas: list):
    edad=0
    for mascota in datos_mascotas:
        edad=edad+mascota['edad']
    promedio=edad/len(datos_mascotas)
    return "el promedio es: "+str(round(promedio))

# A continuación esta la funcion "imprimir_reporte_html"
#iniciamos una variable "estilos" que inicia la estructura html incorpora el estilo que tendra mi tabla con css
#luego creo una variable "registros_tabla" con un valor inicial
#llamo al ciclo for que va a recorrer la lista "datos_mascotas" y va a almacenar en la variable "registros_tabla"
#lo que retorne la funcion "crear_registros"
#luego abro un archivo llamado "tabla.html" y va a tratar de escribir la variable "estilos" concatenada con "registros_tabla" 
# concatenada con el cierre del body y del html
# envía un mensaje de notificación, cierra el archivo e invoca el menu principal para volver.
def imprimir_reporte_html(datos_mascotas: list):
    estilos = '''
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
    }

    td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 4px;
    display: inline-block;
    }

    th {
        background-color: #dddddd;
        width: 20%;
    }

    td{
        width: 70%;
    }
    </style>
    </head>
    <body>
    <h2>Reporte de pacientes</h2>
    '''
    registros_tabla = ""
    for mascota in datos_mascotas:
        registros_tabla = registros_tabla + crear_registros(mascota)

    reporte = open('tabla.html', 'w')
    try:
        reporte.write(estilos + registros_tabla + "</body></html>")
        print("impresion realizada")
    except:
        print("no se pudo crear la tabla")
    finally:
        reporte.close()
    imprimir_menu_principal()    

# A continuación esta la funcion "crear_registros" con el diccionario "mascota" como parámetro
# la función almacena en una variable las cabeceras del la tabla html vinculadas con el diccionario "mascota" para su posterior retorno
def crear_registros(mascota: dict):
    registro_mascota = "<table><tr><th>Nombre del animal</th><td>" + mascota['nombre'] + "</td></tr><tr><th>Edad del animal</th><td>" + str(mascota['edad']) + "</td></tr><tr><th>Nombre del dueño</th><td>"+ mascota['dueño'] + "</td></tr><tr><th>Diagnostico del animal</th><td>" + mascota['diagnostico'] + "</td></tr><tr><th>Telefono</th><td>" + mascota['telefono'] + "</td></tr></table><br>" 
    return registro_mascota

# Finalmente invocamos la función que nos deriva al menu principal.
imprimir_menu_principal()


