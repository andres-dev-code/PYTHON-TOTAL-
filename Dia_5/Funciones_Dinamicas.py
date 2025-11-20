#Chequea numeros de 3 cifras
def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

result = chequear_3_cifras([55,99,600])
print(result)



