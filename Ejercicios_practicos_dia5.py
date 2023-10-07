"""FUNCION 1"""
def devolver_distintos(a, b, c):
    suma = a + b + c
    lista = [a ,b, c]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos(12,1,1))

#FUNCION 2

def palabra_ordenada(palabra):
    lista = []
    for arg in palabra:
        lista.append(arg)
    lista = list(set(lista))
    lista.sort()
    return lista

print(palabra_ordenada("entretenido"))

#FUNCION 3
def ceros_vecinos(*args):
    contador = 0

    for n in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

#FUNCION 4
def contar_primos(numero):
    primos = [2]

    if numero < 2:
        return 0

    iteracion = 3
    while iteracion <= numero:
        es_primo = True
        for n in range(2, int(iteracion ** 0.5) + 1):
            if iteracion % n == 0:
                es_primo = False
                break

        if es_primo:
            primos.append(iteracion)

        iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos(200))








