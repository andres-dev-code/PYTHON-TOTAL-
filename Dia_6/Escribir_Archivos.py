archivo = open('Texto','w')

palabras = ['Hola ','Mundo ','como ','estan? ']
for p in palabras:
    archivo.write(p)
archivo.close()