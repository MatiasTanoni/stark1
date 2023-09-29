from data_stark import *

#1
def stark_normalizar_datos(lista_personajes: list):
    """
    Brief: 

    Parametros:

    Retorno: 
    
    
    """

    bandera_modificacion = False
    for personaje in lista_personajes:
        for clave in personaje:
    
            if clave == "fuerza" and type(personaje[clave]) != int:
                personaje[clave] = int(personaje[clave])
                bandera_modificacion = True
            elif type(personaje[clave]) != float and (clave == "peso" or clave == "altura"):
                personaje[clave] = float(personaje[clave])
                bandera_modificacion = True
    
    if bandera_modificacion == True:
        print("Datos normalizados")
    else:
        print("Error!!")

#1.1
def obtener_dato (personaje: dict, clave_ingresada: str):
    """
    Brief: 

    Parametros:

    Retorno: 
    
    
    """
    validacion = False

    if len(personaje) != 0:
        for llave in personaje:
            if llave == clave_ingresada:
                validacion = True

    cadena = f"{clave_ingresada}: {personaje[clave_ingresada]}"

    if validacion:
        return cadena
    else:
        return False

#1.2
def obtener_nombre(personaje: dict):
    """
    Brief: 

    Parametros:

    Retorno: 
    
    
    """
    
    nombre = obtener_dato(personaje, "nombre")

    if nombre != False:
        return nombre
    else:
        return False

#2
def obtener_nombre_y_dato(personaje:dict, clave:str):
    """
    Brief: 

    Parametros:

    Retorno: 
    
    
    """

    dato = obtener_dato(personaje,clave)
    nombre = obtener_nombre(personaje)

    if dato != False:
        print(f"{nombre} | {dato}")
    else:
        return False

#3.1
def obtener_maximo(lista_de_personajes:list, clave:str):
    """
    Brief: 

    Parametros:

    Retorno: 
    
    
    """
    validacion = False
    maximo = 0
    if len(lista_de_personajes) != 0:
        for personaje in lista_de_personajes:
            if type(personaje[clave]) == int or type(personaje[clave]) == float:
                if personaje[clave] >= maximo:
                    maximo = personaje[clave]
                    validacion = True 
    
    if validacion:
        return maximo
    else:
        return validacion

#3.2
def obtener_minimo(lista_de_personajes:list, clave:str):
    """
    Brief: 

    Parametros:

    Retorno: 
    
    
    """
    validacion = False
    minimo = 0
    bandera_minimo = True

    if len(lista_de_personajes) != 0:
        for personaje in lista_de_personajes:
            if type(personaje[clave]) == int or type(personaje[clave]) == float:
                if personaje[clave] <= minimo or bandera_minimo == True:
                    minimo = personaje[clave]
                    validacion = True 
                    bandera_minimo = False

    if validacion == True:
        return minimo
    else:
        return validacion

#3.3
def obtener_dato_cantidad(lista_personajes:list, valor:int, clave:str):
    """
    Brief: 

    Parametros:

    Retorno: 
    
    
    """
    lista = []
    validacion = False

    if len(lista_personajes) != 0:
        for personaje in lista_personajes:
            if personaje[clave] == valor:
                lista.append(personaje["nombre"])
                validacion = True

    if validacion == True:
        return lista
    else:
        return validacion

#3.4
def stark_imprimir_heroes(lista_de_personajes:list):
    """
    Brief: 

    Parametros:

    Retorno: 
    
    
    """
    if len(lista_de_personajes) != 0:
        for personaje in lista_de_personajes:
            for clave in personaje:
                print(f"{clave}: {personaje[clave]}")
                print("\n")           
    else:
        return False
    
#4.1
def sumar_dato_heroe(lista_de_personajes:list, clave:str):
    """
    Brief: Suma una clave en especifico entre todos los heroes.

    Parametros: -   lista_de_personajes (list): Se utiliza para acceder a todos los personajes
                -   clave (str): Se utila para acced
    Retorno: Te retorna la suma total de las claves.
    """
    validacion = False
    suma = 0

    for personaje in lista_de_personajes:
        if type(personaje[clave]) != dict and type(personaje[clave]) != 0:
            if type(personaje[clave]) == int or type(personaje[clave]) == float:
                suma += personaje[clave]
                validacion = True
    
    if validacion:
        return suma
    else:
        return validacion
    
#4.2
def dividir(dividendo:int,divisor:int):
    validacion = True
    resultado = dividendo / divisor

    if resultado == 0:
        validacion = False

    if validacion:
        return resultado
    else:
        return validacion
    
#4.3
def calcular_promedio(lista_de_personajes:list, clave:str):

    suma_clave = sumar_dato_heroe(lista_de_personajes,clave)
    promedio = dividir(suma_clave, len(lista_de_personajes))
    return promedio

#4.4
def mostrar_promedio_dato(lista_de_personajes:list, clave:str):
    validacion = True
    for personaje in lista_de_personajes:
        if type(personaje[clave]) != int and type(personaje[clave]) != float or len(lista_personajes) == 0:
            validacion = False
    if validacion == False:
        return validacion

#5.1 
def imprimir_menu(menu: str):
    """
    Brief: 
        Imprime por consola el dato pasado por parametro.
    Parametros:
        - menu (str): El dato que queremos imprimir por consola.
    Retorno:
        - El menu con opciones.
    """
    print(menu)

#5.2 
def validar_entero(cadena:int):
    validacion = False
    if type(cadena) == int:
        validacion = True
        return validacion
    else:
        return validacion

#5.3
def stark_menu_principal(menu:str):
    """
    Brief: 
        Imprime el menu de opciones, valida y castea a entero la opcion solicitada.
    Parametros:
        - menu (str): El menu que debe mostrar por consola.
    Retorno:
        - La opcion elegida casteada a entero.
        - False si la opcion no cumple con la validacion.
    """
    imprimir_menu(menu)
    opcion = input("Ingrese la opcion: ")
    validacion = validar_entero(opcion)

    if validacion:
        return int(opcion)
    else:
        return False
    


def obtener_personajes_por_genero(lista_personajes: list, genero: str):
    """
    Brief: 
        Recorre la lista y obtiene una lista con el genero solicitado por parametro.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
        - genero (str): Tipo de datos que queremos obtener.
    Retorno:
        - Una lista con todos los personajes del genero solicitado.
        - False si la lista esta vacia.
    """
    lista_personajes_genero = []
    validacion = False
    if len(lista_personajes) != 0 and (genero == "NB" or genero == "M" or genero == "F"):
        validacion = True
        for personaje in lista_personajes:
            if personaje["genero"] == genero:
                lista_personajes_genero.append(personaje)

    if validacion:
        return lista_personajes_genero
    else:
        return False

#6
def stark_marvel_app(lista_personajes: list, menu: str):

    while True:

        opcion = stark_menu_principal(menu)

        match opcion:
            case 1:
                stark_normalizar_datos(lista_personajes)
            case 2:
                dato = obtener_dato(lista_personajes[0], "genero")
                print(f"El dato obtenido es: {dato}")
            case 3:
                nombre = obtener_nombre(lista_personajes[5])
                print(f"El nombre del personaje es: {nombre}")
            case 4:
                clave = "identidad"
                nombre_y_dato = obtener_nombre_y_dato(lista_personajes[3], clave)
                print(nombre_y_dato)
            case 5:
                clave = "peso"
                maximo = obtener_maximo(lista_personajes, clave)
                print(f"El maximo de {clave} es: {maximo}")
            case 6:
                clave = "altura"
                minimo = obtener_minimo(lista_personajes, clave)
                print(f"El minimo de {clave} es: {minimo}")
            case 7:
                clave = "fuerza"
                lista_personajes_fuerza = obtener_dato_cantidad(lista_personajes, 15, clave)
                if lista_personajes_fuerza != False:
                    stark_imprimir_heroes(lista_personajes_fuerza)
            case 8:
                stark_imprimir_heroes(lista_personajes)
            case 9:
                clave = "peso"
                suma = sumar_dato_heroe(lista_personajes, clave)
                print(f"El resultado de la suma de todos los {clave} es: {suma}")
            case 10:
                dividendo = 100
                divisor = 50
                resultado = dividir(dividendo, divisor)
                print(f"El resultado de la division es: {resultado}")
            case 11:
                clave = "altura"
                promedio = calcular_promedio(lista_personajes, clave)
                print(f"El promedio de {clave} es: {promedio}")
            case 12:
                clave = "peso"
                promedio = mostrar_promedio_dato(lista_personajes, clave)
                print(f"El promedio de {clave} es: {promedio}")
            case 13:
                genero = "F"
                lista_personajes_por_genero = obtener_personajes_por_genero(lista_personajes, genero)
                stark_imprimir_heroes(lista_personajes_por_genero)
            case 14:
                break
            case _:
                print("Opcion incorrecta")
#7
def segundo_menu(lista_personajes: list, menu: str):

    while True:

            opcion = stark_menu_principal(menu)

            match opcion:
                case 1:
                    stark_normalizar_datos(lista_personajes)
                case 2:
                    # Recorrer la lista imprimiendo por consola el nombre de cada personaje de género NB.
                    for personaje in lista_personajes:
                        nombre_y_dato = obtener_nombre_y_dato(personaje, "genero")
                        if personaje["genero"] == "NB":
                            print(nombre_y_dato)
                case 3:
                    # Recorrer la lista y determinar cuál es el personaje más alto de género F.
                    lista_genero_femenino = obtener_personajes_por_genero(lista_personajes, "F")
                    maximo_altura = obtener_maximo(lista_genero_femenino, "altura")
                    lista_femenino_maximo_altura = obtener_dato_cantidad(lista_genero_femenino, maximo_altura, "altura")
                    print(f"\n---El/los superheroe mas alto de genero femenino es/son---\n")
                    stark_imprimir_heroes(lista_femenino_maximo_altura)
                case 4:
                    # Recorrer la lista y determinar cuál es el personaje más alto de género M.
                    lista_genero_masculino = obtener_personajes_por_genero(lista_personajes, "M")
                    maximo_altura = obtener_maximo(lista_genero_masculino, "altura")
                    lista_masculino_maximo_altura = obtener_dato_cantidad(lista_genero_masculino, maximo_altura, "altura")
                    print(f"\n---El/los personaje mas alto de genero masculino es/son---\n")
                    stark_imprimir_heroes(lista_masculino_maximo_altura)
                case 5:
                    # Recorrer la lista y determinar cuál es el personaje más débil de género M.
                    lista_genero_masculino = obtener_personajes_por_genero(lista_personajes, "M")
                    minimo_fuerza = obtener_minimo(lista_genero_masculino, "fuerza")
                    lista_masculino_minimo_fuerza = obtener_dato_cantidad(lista_genero_masculino, minimo_fuerza, "fuerza")
                    print(f"\n---El/los personaje mas debil de genero masculino es/son---\n")
                    stark_imprimir_heroes(lista_masculino_minimo_fuerza)
                case 6:
                    # Recorrer la lista y determinar cuál es el personaje más débil de género NB.
                    lista_genero_no_binario = obtener_personajes_por_genero(lista_personajes, "NB")
                    minimo_fuerza = obtener_minimo(lista_genero_no_binario, "fuerza")
                    lista_no_binario_minimo_fuerza = obtener_dato_cantidad(lista_genero_no_binario, minimo_fuerza, "fuerza")
                    print(f"\n---El/los personaje mas debil de genero no binario es/son---\n")
                    stark_imprimir_heroes(lista_no_binario_minimo_fuerza)
                case 7:
                    # Recorrer la lista y determinar la fuerza promedio de los personajes de género NB.
                    lista_genero_no_binario = obtener_personajes_por_genero(lista_personajes, "NB")
                    promedio = mostrar_promedio_dato(lista_genero_no_binario, "fuerza")
                    print(f"El promedio de fuerza de los personajes de genero NB es: {promedio}")
                case 8:
                    # Determinar cuántos personajes tienen cada tipo de color de ojos.
                    color_ojos = "Brown"
                    lista_color_ojos = listar_personajes_por_color_de_ojos(lista_personajes, color_ojos)
                    contador = len(lista_color_ojos)
                    print(f"La cantidad de personajes con ojos {color_ojos} es: {contador}")
                case 9:
                    # Determinar cuántos personajes tienen cada tipo de color de pelo.
                    tipo_pelo = "Auburn"
                    contador = cantidad_personajes_por_color_de_pelo(lista_personajes, tipo_pelo)
                    print(f"La cantidad de personajes con pelo {tipo_pelo} es: {contador}")
                case 10:
                    # Listar todos los personajes agrupados por color de ojos.
                    color_ojos = "Brown"
                    lista_color_ojos = listar_personajes_por_color_de_ojos(lista_personajes, color_ojos)
                    print(f"Lista de personajes con color de ojos {color_ojos}---\n")
                    stark_imprimir_heroes(lista_color_ojos)
                case 11:
                    # Listar todos los personajes agrupados por tipo de inteligencia.
                    inteligencia = "good"
                    lista_inteligencia = listar_personajes_por_inteligencia(lista_personajes, inteligencia)
                    print(f"Lista de personajes con inteligencia {inteligencia}---\n")
                    stark_imprimir_heroes(lista_inteligencia)
                case 12:
                    break
                case _:
                    print("Opcion incorrecta") 
                
def listar_personajes_por_inteligencia(lista_personajes: list, tipo_inteligencia: str):
    """
    Brief: 
        Agrupa los personajes por inteligencia.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
        - tipo_inteligencia (str): El dato por el cual vamos a agrupar.
    Retorno:
        - Una lista de superheroes que cumpla con la condicion.
    """
    lista_inteligencia = []
    for personaje in lista_personajes:
        inteligencia = obtener_dato(personaje, "inteligencia") 
        if inteligencia == tipo_inteligencia:
            lista_inteligencia.append(personaje)

    return lista_inteligencia

def listar_personajes_por_color_de_ojos(lista_personajes: list, tipo_ojos: str):
    """
    Brief: 
        Agrupa los personajes por color de ojos.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
        - tipo_ojos (str): El dato por el cual vamos a agrupar.
    Retorno:
        - Una lista de superheroes que cumpla con la condicion.
    """
    lista_color_ojos = []

    for personaje in lista_personajes:
        color_ojos = obtener_dato(personaje, "color_ojos")
        if color_ojos == tipo_ojos:
            lista_color_ojos.append(personaje)


    return lista_color_ojos

def cantidad_personajes_por_color_de_pelo(lista_personajes: list, tipo_pelo: str):
    """
    Brief: 
        Cuenta los personajes segun su tipo de pelo.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
        - tipo_pelo (str): El dato por el cual vamos a agrupar.
    Retorno:
        - La cantidad de personajes que cumpla la condicion.
    """
    contador = 0
    for personaje in lista_personajes:
       pelo = obtener_dato(personaje, "color_pelo") 
       if pelo == tipo_pelo:
           contador += 1

    return contador
