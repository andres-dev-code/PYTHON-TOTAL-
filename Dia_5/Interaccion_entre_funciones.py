from random import *

# lista inicial
palitos = ['-','--','---','----']

#mezclar palitos
def mezclar_palitos(lista):
    shuffle(lista)
    return lista

#intentos
def intentos():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("elige un numero del 1 al 4: ")

    return int(intento)

#comprobar
def comprobar(lista,intento):
    if lista[intento -1] == '-':
        print("perdiste!")
    else:
        print("Ganaste!")

    print(f"Te toco {lista[intento-1]}")

palitos_mezclados = mezclar_palitos(palitos)
seleccion = intentos()
comprobar(palitos_mezclados,seleccion)