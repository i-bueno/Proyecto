import random
categorias = {
    "programación_general": ["python", "programa"],
    "tipos_de_datos": ["variable","cadena","entero","lista"],
    "estructuras_de_datos": ["funcion","bucle"]
}


guessed = []
attempts = 6
puntaje = 6

print("¡Bienvenido al Ahorcado!")
print()

# Elegir categoría
cat = input("Elige una categoría: programación_general, tipos_de_datos, estructuras_de_datos: (1,2,3) ")

while cat != "1" and cat != "2" and cat != "3":
    # Caso de error
    print()
    cat = input("Entrada no válida. Elige una categoría: programación_general, tipos_de_datos, estructuras_de_datos: (1,2,3) ")

if cat == "1":
    categorias = categorias["programación_general"]
elif cat == "2":
    categorias = categorias["tipos_de_datos"]
elif cat == "3":
    categorias = categorias["estructuras_de_datos"]

word = random.choice(categorias)

while attempts > 0:
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

else:
    print(f"¡Perdiste! La palabra era: {word}")
    print("Tu puntaje final es: 0")