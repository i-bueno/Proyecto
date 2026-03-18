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
                    print("El equipo ha siido eliminado del torneo correctamente.")
                    eliminado = True
            if eliminado == False:
                print("El equipo no se encuentra en el torneo.")
            else:
                lista.pop(equipoact)
    return lista, equipos    

while num != 5:
    print("Que acción le gustaría realizar?")
    print("1 - Agregar un equipo al torneo, 2 - Eliminar un equipo del torneo")
    num = int(input("3 - Registrar un resultado, 4 - Mostrar la tabla de posiciones. 5 - Salir. : "))
    if num == 1:
        lista_equipos, cantidad_equipos = accion1(lista_equipos, cantidad_equipos)
    elif num == 2:
        lista_equipos, cantidad_equipos = accion2(lista_equipos, cantidad_equipos)
print("---------------------")
print("Hasta luego!") 