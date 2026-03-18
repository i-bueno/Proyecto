#Desarrollar un programa que simule la tabla de posiciones de un torneo de fútbol. El
#programa debe tener un menú
#interactivo con las siguientes opciones:
#Agregar un equipo al torneo.
#Registrar un resultado ingresando equipo local, equipo visitante y marcador en formato 4 -
#2. El programa debe
#actualizar los puntos automáticamente (3 puntos por victoria, 1 por empate, 0 por derrota).
#Mostrar la tabla de posiciones ordenada de mayor a menor puntaje.
#Eliminar un equipo del torneo.
#Salir del programa.
#Se deben manejar situaciones como intentar agregar un equipo ya existente, registrar un
#resultado con un equipo
#desconocido, o ingresar un marcador con formato inválido. 

num = 0
lista_equipos = {}
cantidad_equipos = 0

#agregar
def accion1(lista,equipos):
    salir = 0
    while salir == 0:
        print()
        equipoact = (input("Introduzca el nombre del equipo a agregar (Presione 'Q' para salir): ").upper())
        repetido = False
        if equipoact == "Q":
            salir = 1
        else:
            for aux in lista:
                if aux == equipoact:
                    print("El equipo ya se encuentra en el torneo.")
                    print("---------------------")
                    repetido = True
            if repetido == False:
                lista.update({equipoact : 0})
                equipos += 1
                print(f"El equipo '{equipoact}' ha sido agregado al torneo correctamente.")
    return lista, equipos    

#Eliminar Equipo
def accion2(lista,equipos):
    salir = 0
    while salir == 0:
        print()
        equipoact = (input("Introduzca el nombre del equipo a eliminar (Presione 'Q' para salir): ").upper())
        if equipoact == "Q":
            salir = 1
        else:
            eliminado = False
            for aux in lista:
                if aux == equipoact:
                    equipos -= 1
                    print("El equipo ha sido eliminado del torneo correctamente.")
                    eliminado = True
            if eliminado == False:
                print("El equipo no se encuentra en el torneo.")
            else:
                lista.pop(equipoact)
    return lista, equipos    

#Registrar resultado
def accion3(lista):
    salir = 0
    while salir == 0:
        valido1 = False
        valido2 = False
        print()
        local = input("Introduzca el nombre del equipo local (Presione 'Q' para salir): ").upper() 
        print()
        if local == "Q":
            salir = 1
        else:
            visitante = input("Introduzca el nombre del equipo visitante: ").upper()

            # Verifico validez de los equipos
            for aux in lista:
                if local == aux:
                    valido1 = True
                elif visitante == aux:
                    valido2 = True
            if valido1 == False or valido2 == False:
                print("Equipo/s no valido/s.")
            else:
                marcador = input("Introduzca el marcador en formato '(x-x)': ")
                # Verifico la validez del formato del marcador.
                while len(marcador) != 3 or marcador[1] != "-" or not marcador[0].isdigit() or not marcador[2].isdigit():
                    print("Marcador con formato inválido.")
                    marcador = input("Introduzca el marcador en formato '(x-x)': ")
                    print()
                
                if int(marcador[0]) > int(marcador[2]):
                    lista.update({local : lista.get(local)+3})
                
                elif int(marcador[0]) < int(marcador[2]):
                    lista.update({visitante : lista.get(visitante)+3})
                    
                else:
                    lista.update({local : lista.get(local)+1})
                    lista.update({visitante : lista.get(visitante)+1})
                print("Resultado guardado correctamente.")
    return lista

# Mostrar tabla ordenada
def accion4 (lista):
    print()
    print("TABLA DE POSICIONES")
    print("---------------------")

    # Verifico equipos
    if len(lista) == 0:
        print("No hay equipos cargados.")
    else:
    
        tabla_ordenada = sorted(lista.values(), reverse=True)
        pos = 1
        mostrados = []

        for puntos in tabla_ordenada:
            for equipo in lista:
                if lista[equipo] == puntos and equipo not in mostrados:
                    print(f"{pos}. {equipo}: {puntos} puntos")
                    mostrados.append(equipo)
                    pos += 1

    print("---------------------")
    return lista

# Programa principal                
while num != "5":
    print("Que acción le gustaría realizar?")
    print("1 - Agregar un equipo al torneo, 2 - Eliminar un equipo del torneo")
    num = input("3 - Registrar un resultado, 4 - Mostrar la tabla de posiciones. 5 - Salir. : ")
    if num == "1":
        lista_equipos, cantidad_equipos = accion1(lista_equipos, cantidad_equipos)
    elif num == "2":
        lista_equipos, cantidad_equipos = accion2(lista_equipos, cantidad_equipos)
    elif num == "3":
        lista_equipos = accion3(lista_equipos)
    elif num == "4":
        lista_equipos = accion4(lista_equipos)
    elif num != "5":
        print("Ingrese un número válido: ")
        print()
print("---------------------")
print("Hasta luego!") 