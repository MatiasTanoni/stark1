from data_stark import lista_personajes
from stark_biblioteca import *
# Matias Tanoni 1D ###### STARK_2 INTEGRADOR 2


stark_normalizar_datos(lista_personajes)


# dato = obtener_dato(lista_personajes[2],"altura")
# print(dato)


# obtener_nombre(lista_personajes[5])


obtener_nombre_y_dato(lista_personajes[3],"fuerza")


maximo = obtener_maximo(lista_personajes,"altura")
print(maximo)


minimo = obtener_minimo(lista_personajes, "altura")
print(minimo)


maxima_fuerza = obtener_maximo(lista_personajes, "fuerza")
heroes_mas_fuertes = obtener_dato_cantidad(lista_personajes,maxima_fuerza, "fuerza")
print(heroes_mas_fuertes)


#stark_imprimir_heroes(lista_personajes)


suma = sumar_dato_heroe(lista_personajes, "fuerza")
print(suma)


resultado_division = dividir(5,2)
print(resultado_division)

promedio = calcular_promedio(lista_personajes, "fuerza")
print(promedio)

mostrar_promedio = mostrar_promedio_dato(lista_personajes, "fuerza")
print(mostrar_promedio)


stark_marvel_app(lista_personajes, "menu")