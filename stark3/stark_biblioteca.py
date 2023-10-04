from data_stark import *
import re

def extraer_iniciales(nombre_heroe:str):
    validacion = True
    if type(nombre_heroe) == str and len(nombre_heroe) != 0:
        if re.search("the", nombre_heroe) != None:
            nombre_heroe = re.sub("the"," ",nombre_heroe)
        elif re.search("-", nombre_heroe) != None:
            nombre_heroe = re.sub("-"," ", nombre_heroe)
        validacion = True
    else:
        validacion = False

    iniciales = re.sub("[a-z]", " ", nombre_heroe)
    iniciales = re.sub(r"\s+"," ", iniciales)
    iniciales = iniciales.replace(" ", ".")

    cadena = "N/A"

    if validacion:
        return iniciales
    else:
        return cadena