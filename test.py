# Importar la libreria para leer JSON
import json


for json in arreglo_de_queries:
    print(json['query'])


def obtener_alias(archivo_json):
    pass


def obtener_query(archivo_json):
    pass


def cargar_arreglo_de_queries(ruta_del_archivo_json):

    # Abrimos el archivo y lo cargamos en una variable
    # de tipo file.
    archivo = open(ruta_del_archivo_json)

    # Crear un OBJETO de python de tipo JSON, a traves
    # del archivo que abrimos
    datos = json.load(archivo)

    # Sacar la informacion que nos interesa del json
    arreglo_de_queries = datos["ConfMixEngine"]["Queries"]

    # Cerramos el archivo
    archivo.close()

    return arreglo_de_queries
