from random import *

#esta funcion saluda a una persona
def saludar_persona(nombre):
    print(f"Hola {nombre}")

saludar_persona(input("Dime tu nombre:"))

lista_de_numeros = [1,2,2,3,3,4,5,10]

def reducir_lista(lista):
    lista_sin_duplicados = list(set(lista))
    mayor = max(lista_sin_duplicados)
    lista_sin_duplicados.remove(mayor)
    return lista_sin_duplicados

result1 = reducir_lista(lista_de_numeros)
print(result1)

def promedio(lista_nueva):
    return sum(lista_nueva) / len(lista_nueva)

print(promedio(result1))

cara_cruz = ['Cara','Cruz']
lista_numeros = [1,2,3,4,5]

def lanzar_moneda():
    x = choice(cara_cruz)
    return x

a = lanzar_moneda()
print(a)

def probar_suerte(resultado,lista):
    if resultado == 'Cara':
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista

y = probar_suerte(a,lista_numeros)
print(y)

def saludar(nombre):
    if nombre == 'Castro':
        return 'Hola Castro!'
    else:
        return 'No se tu nombre'

print(saludar('Castro'))

def saludar_otro_nombre(nombre):
    if nombre != 'Castro':
        return f'Hola {nombre}!'
    else:
        return 'Yo ya te salude!'

print(saludar_otro_nombre('Castro'))


def sumar(num1,num2):
    return num1 + num2
print(sumar(3,2))

def multiplicar(num1,num2):
    return num1 * num2

print(multiplicar(sumar(3,2),5))