print("""-----------------------
JUEGO ADIVINA EL NÚMERO
-----------------------""")

#VARIABLES INICIALES
from random import *
nombre = input("Hola!, por favor, indica tu nombre: ")
intentos = 8
numero_maquina = 1
numero_jugador = 0
jugados = 0
print(f"\nBueno, {nombre}, he pensado un número entre 1 y 100, te daré 8 intentos para que aciertes el número")

#EMPIEZA EL JUEGO
while numero_jugador != numero_maquina:
    jugados = 0
    intentos = 8
    numero_maquina = randint(1, 100)
    while intentos > 0:
        numero_jugador = int(input("\nCuál crees que ha sido el número que he pensado?: "))
        if numero_jugador < 1 or numero_jugador > 100:
            intentos -= 1
            jugados += 1
            print("\nHas elegido un número que no está permitido,¡Recuerda que sólo puedes elegir números del 1 al 100!")
            print(f"te quedan {intentos} intentos")
        elif numero_jugador < numero_maquina:
            intentos -= 1
            jugados += 1
            print(f"\nEl número que has elegido es menor al número secreto, te quedan {intentos} intentos")
        elif numero_jugador > numero_maquina:
            intentos -= 1
            jugados += 1
            print(f"\nEl número que has elegido es mayor al número secreto, te quedan {intentos} intentos")
        elif numero_jugador == numero_maquina:
            jugados += 1
            break
    if numero_jugador == numero_maquina:
        print(f"\nFelicidades, el número correcto es {numero_maquina}, lo has logrado en {jugados} intentos.")
    else:
        print(
            f"Lo lamento, no has encontrado el número que pensé({numero_maquina}), pero buscaré otro número y te daré 8 intentos mas!")

