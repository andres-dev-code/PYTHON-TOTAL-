'''from pathlib import *

carpeta = Path('C:/Users/Usuario/Desktop/alternativo') / 'texto_alternativo.txt'

ruta_wn = PureWindowsPath(carpeta)

print(ruta_wn)'''



archivo = open('Prueba.txt')

def abrir_leer(texto):
    return texto.read()

print(abrir_leer(archivo))

archivo.close()