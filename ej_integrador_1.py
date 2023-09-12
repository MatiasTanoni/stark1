from data_stark import lista_personajes

#
# Matias Tanoni 1°D
#

#A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
# for heroe in lista_personajes:
#     nombre = heroe ["nombre"]
#     identidad = heroe ["identidad"]
#     empresa = heroe ["empresa"]
#     altura = heroe ["altura"]
#     peso = heroe ["peso"]
#     genero = heroe ["genero"]
#     color_ojos = heroe ["color_ojos"]
#     color_pelo = heroe ["color_pelo"]
#     fuerza = heroe ["fuerza"]
#     inteligencia = heroe ["inteligencia"]

###############################################------MENU DE OPCIONES-----###############################################
while True:
    respuesta = input("""A.Todos los datos de cada superhéroe\n
                        B. La identidad y el peso del superhéroe con mayor fuerza \n
                        C. Nombre e identidad del superhéroe más bajo\n
                        D. El peso promedio de los superhéroes masculinos\n
                        E. Mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino\n
                        F. Salir\n
                        Elija una opcion:""")

    match respuesta:
        case "A":
            for heroe in lista_personajes:
                nombre = heroe ["nombre"]
                identidad = heroe ["identidad"]
                empresa = heroe ["empresa"]
                altura = heroe ["altura"]
                peso = heroe ["peso"]
                genero = heroe ["genero"]
                color_ojos = heroe ["color_ojos"]
                color_pelo = heroe ["color_pelo"]
                fuerza = heroe ["fuerza"]
                inteligencia = heroe ["inteligencia"]  
                print(nombre, identidad, empresa, altura, peso, genero, color_ojos, color_pelo, fuerza, inteligencia)    

        case "B":
            #ARREGLAR PORQUE HAY 2 SUPERHEROES QUE TIENEN 100 DE FUERZA
            bandera = False
            maximo_fuerza = 0
            for heroe in lista_personajes:
                fuerza = int(heroe ["fuerza"])
                peso = float(heroe["peso"])
                identidad = heroe ["identidad"]
                
                if bandera == False or fuerza > maximo_fuerza:
                    maximo_fuerza = fuerza
                    identidad_mas_fuerza = identidad
                    peso_mas_fuerza = peso
                    bandera = True
            print(f"El superheroe con mas fuerza es: {identidad_mas_fuerza} con fuerza de: {maximo_fuerza} y su peso es de: {peso_mas_fuerza}kg")

        case "C":  #C. Nombre e identidad del superhéroe más bajo\ 
            ## !!!!NO FUNCIONA EL MAS BAJO 
            bandera = False
            minimo_altura = None

            for heroe in lista_personajes:
                altura = heroe ["altura"]
                nombre = heroe ["nombre"]
                identidad = heroe ["identidad"]

                if bandera == False or altura < minimo_altura:
                    minimo_altura = altura
                    nombre_mas_bajo = nombre
                    identidad_mas_bajo = identidad
                    bandera = True

            print(f"Nombre: {nombre_mas_bajo} e indentidad: {identidad_mas_bajo} es el superheroe mas bajo conc: {minimo_altura}mts")        

        case "D":
            acumulador = 0
            for heroe in lista_personajes:
                peso = heroe ["peso"] 
                float(peso)
                acumulador += peso

            promedio = acumulador / len(lista_personajes)
            print(promedio)

        case "E":
            print("Opcion E")

            
        case "F":
            print("¡Gracias!")
            break