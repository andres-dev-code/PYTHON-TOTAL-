#Pequeño juego de adivinanza,tienes que adivinar el numero secreto,solo tienes 8 intentos

from random import *

n_aleatorio = randint(1,100)
user = input("Dime tu nombre: ")
intentos = 0
user_respuesta = 0

print(f"Bueno {user},he pensado en un numero entre el 1 y 100,tienes 8 intentos para adivinar")

while user_respuesta != n_aleatorio:
    intentos += 1
    user_respuesta = int(input("Adivina el Numero:"))
    if (user_respuesta < 1) or (user_respuesta > 100):
        print("Numero Fuera de Rango")
    elif user_respuesta < n_aleatorio:
        print("Numero equivocado,Mas arriba")
    elif user_respuesta > n_aleatorio:
        print("Numero equivocado,Mas abajo")
    else:
        print(f"Adivinaste! te ha tomado {intentos} intentos!")
        break
    if intentos == 8:
        print(f"Se acabo! Ya no tienes mas intentos,el numero secreto era {n_aleatorio}")
        break