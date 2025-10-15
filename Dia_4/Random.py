from random import *

aleatorio = uniform(1,10)
redondeo = round(aleatorio,2)
print(redondeo)

rand = round(random())
print(rand)

participantes = ['Juan','Castro,','Victor','Pablo','Maria','Laura']
sorteo = choice(participantes)
print(f'Felicidades {sorteo} ganaste el sorteo')

numeros = list(range(1,51))
shuffle(numeros)
print(numeros)


