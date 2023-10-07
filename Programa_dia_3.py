#INGRESO DE DATOS
texto = input("Por favor, escriba un poema, frase o texto: ")

print("Ok, ahora ingresarás 3 letras a tu gusto")
letra1 = input("Ingresa la letra 1: ")
letra2 = input("Ingresa la letra 2: ")
letra3 = input("Ingresa la letra 3: ")

#PROCESOS
texto = texto.lower()
letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()
print(f"La letra {letra1.upper()} aparece {texto.count(letra1)} veces, la letra {letra2.upper()} aparece {texto.count(letra2)} veces, y la letra {letra3.upper()} aparece {texto.count(letra3)} veces")

texto2 = texto.split()
print(f"\nPor otro lado, tu texto cuenta con {len(texto2)} palabras")


print(f"\nLa primera letra de tu texto es {texto[0]}, y la última es {texto[-1]}")

# Invertir el orden de las palabras
texto2.reverse()
texto_reverse = ' '.join(texto2)
print(f"\nEl texto al revés sería: {texto_reverse}")

dic = {True:"SI", False:"NO"}
print(f"\nLa palabra 'Python' {dic['python' in texto]} aparece")




