import random
from random import sample
categorias = {
    "programación_general": ["python", "programa"],
    "tipos_de_datos": ["variable","cadena","entero","lista"],
    "estructuras_de_datos": ["funcion","bucle"]
}

print("¡Bienvenido al Ahorcado!")
print()

cat = input("Elige una categoría: programación_general, tipos_de_datos, estructuras_de_datos: (1,2,3) ")
    # Elegir categoría 

while cat != "1" and cat != "2" and cat != "3":
    # Caso de error
    print()
    cat = input("Entrada no válida. Elige una categoría: programación_general, tipos_de_datos, estructuras_de_datos: (1,2,3) ")

    # Sampleo para evitar repetición
if cat == "1":
    palabras = sample(categorias["programación_general"], len(categorias["programación_general"]))
elif cat == "2":
    palabras = sample(categorias["tipos_de_datos"], len(categorias["tipos_de_datos"]))
elif cat == "3":
    palabras = sample(categorias["estructuras_de_datos"], len(categorias["estructuras_de_datos"]))

continuar = "s"
while continuar == "s":
    guessed = []
    attempts = 6
    puntaje = 6
    win = False

    # Tomo y elimino
    word = palabras.pop()
    while attempts > 0 and win == False:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            print(f"Tu puntaje final es: {puntaje}")
            win = True
            break
        
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        
        letter = input("Ingresá una letra: ")
        if len(letter) != 1 or not letter.isalpha():
            print()
            print("Entrada no válida.")
            print()
            continue
        
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.")
        
        print()

    if attempts == 0 and win == False:
        print(f"¡Perdiste! La palabra era: {word}")
        print("Tu puntaje final es: 0")

        #Verifico si hay repetición
    if len(palabras) > 0:
        continuar = input("¿Querés jugar otra vez? (s/n) ").lower()
        while continuar != "s" and continuar != "n":
            print()
            continuar = input("Entrada no válida. (s/n): ").lower()
    else:
        print("Ya no quedan más palabras en esta categoría.")
        continuar = "n"

if continuar != "s":
    print("Gracias por jugar.")