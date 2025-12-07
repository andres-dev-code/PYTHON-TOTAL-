from pathlib import Path
import os

ruta_actual = os.getcwd()
print(f'La ruta actual es: {ruta_actual}')

nueva_carpeta = os.makedirs('C:\\Users\\Usuario\\Desktop\\Nueva carpeta')
nueva_ruta = os.chdir("C:\\Users\\Usuario\\Desktop\\Nueva carpeta")
nuevo_archivo = open('Nuevo Archivo.txt','w')
nuevo_archivo.write('You get hacked nigga')
nuevo_archivo.close()
ruta_nuevo_archivo = Path("C:/Users/Usuario/Desktop/Nueva carpeta") / 'Nuevo Archivo.txt'
print(ruta_nuevo_archivo.read_text())

