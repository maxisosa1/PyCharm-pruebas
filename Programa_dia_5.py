from random import choice

#VARIABLES

lista_palabras = ["espacio", "motocicleta", "avion"]
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def palabra_azar(lista_palabras):
    # esta funcion devuelve la palabra a jugar
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas


def palabra_guiones(palabra_azar):
    # esta funcion imprime la palabra al azar en forma de guiones y/o letras correctas
    lista_oculta = []

    for l in palabra_azar:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("-")
    print(" ".join(lista_oculta))



def ingreso():
    # esta funcion pide una letra, verifica que sea una sola, que sea letra y devuelve la misma
    letra = "22"
    while len(letra) != 1 or letra.isalpha() == False:
        letra = input("Por favor, ingresa UNA letra: ")
        if len(letra) != 1 or letra.isalpha() == False:
            print("No has elegido una letra correcta")

    return letra.lower()


def esta_letra(letra, palabra, vidas, coincidencias ):
    # Esta función verifica que la letra elegida cunpla alguna de las tres condiciones: 1- Correcta y no elegida
    # anteriormente 2-Correcta pero ya elegida anteriormente 3- O bien incorrecta
    fin = False

    if letra in palabra and letra not in letras_correctas:
        letras_correctas.append(letra)
        coincidencias += 1
    elif letra in palabra and letra in letras_correctas:
        print("Ya has encontrado esa letra. Prueba con otra diferente.")
    else:
        letras_incorrectas.append(letra)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra)

    return vidas, fin, coincidencias

def perder():
    #Esta función muestra que el jugador perdió
    print("Te has quedado sin vidas")
    print("La palabra oculta era ", palabra)

    return True

def ganar(palabra_descubierta):
    #Esta función muestra que el jugador ganó
    palabra_guiones(palabra_descubierta)
    print("Felicitaciones, has ganado el juego")

    return True



#Proceso del juego
palabra, letras_unicas = palabra_azar(lista_palabras)

while not juego_terminado:
    print("\n" + "*" * 20 + "\n")
    palabra_guiones(palabra)
    print("\n")
    print("Letras incorrectas: " + "-".join(letras_incorrectas))
    print(f"Vidas: {intentos}")
    print("\n" + "*" * 20 + "\n")

    letra = ingreso()

    intentos, terminado, aciertos = esta_letra(letra, palabra, intentos, aciertos)

    juego_terminado = terminado