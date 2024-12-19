import os 
os.system

##Formato Json
import json

def abrirArchivo(archivo):
    with open(f"./archivosM/{archivo}.json","r") as abrirArchivo:
        final = json.load(abrirArchivo)
    return final
def guardarArchivo(archivo,diccionario):
    objetoJson= json.dumps(diccionario, indent=4)
    with open(f'./archivosM/{archivo}.json',"w") as abrirArchivo:
        abrirArchivo.write(objetoJson)

BASE_DATOS_MOVISTAR = 'datosmovistar'

datosmovistar = abrirArchivo('datosmovistar')        



##Funciones
def pressEnter():
    print("Ta bien")
    input("Presion enter para continuar......")


## Datos Registro Usuario
def NuevoUsuario(datosmovistar):
    print("======Empieza a registrarte ;)======")
    print("=====Porfavor ingresa tus siguientes datos=====")
    nombre = input("Nombre: ")
    apellido  = input("Apellido: ")
    identificacion = int(input("Identificacion: "))
    for i in range(len(datosmovistar["usuario"])):
        if datosmovistar["usuario"][i]["identificacion"] == identificacion:
            print (datosmovistar["camper"][i]["cedula"],"ya se encuentra registrado :)")
            pressEnter()
            return datosmovistar
    direccion = input("direccion: ")
    telefono = int("Telefono: ")
    correo = input("Correo: ")
    genero = input("Genero: ")
    edad = int(input("Edad: "))
    estado = {"En proceso": True,
                "Cliente Nuevo": False,
                "Cliente Regular": False,
                "Cliente Leal": False,
                }
    
    usuario = {
        'nombre':nombre,
        'apellido':apellido,
        'identificacion':identificacion,
        'direccion':direccion,
        'telefono':telefono,
        'correo':correo,
        'genero':genero,
        'edad': edad,
        'estado': estado
    }

    pressEnter()
    datosmovistar['usuario'].append(usuario)
    return datosmovistar

def addCandidato():
    datosmovistar = abrirArchivo(BASE_DATOS_MOVISTAR)
    datosmovistar = NuevoUsuario(datosmovistar)
    guardarArchivo(BASE_DATOS_MOVISTAR, datosmovistar)

    



