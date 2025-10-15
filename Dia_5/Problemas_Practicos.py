#EJERCICIO 1
def devolver_distintos(a,b,c):
    suma = a + b + c
    if suma > 15:
        return max(a,b,c)
    elif suma < 10:
        return min(a,b,c)
    elif suma in range(10,16):
        valores = sorted([a,b,c])
        return valores[1]

print(devolver_distintos(10,1,2))
#EJERCICIO 2
def orden_alfabetico(palabra):
    lista = []
    for letra in palabra:
        lista.append(letra.lower())
    return sorted(set(lista))

print(orden_alfabetico("paralelepipedo"))
#EJERCICIO 3
def zero(*args):
    lista = []
    for arg in args:
        lista.append(arg)
    if lista.count(0) == 2 in lista:
            return True
    else:
            return False

print(zero(1,0,0,2,3,4,5,0))
#EJERCICIO 4
def contar_primos(numero):

    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:

        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos(100))

