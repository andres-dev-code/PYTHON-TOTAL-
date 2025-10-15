nombres = ['Juan','Castro','Victor','Maria','Mario']

for nombre in nombres:
   if nombre.startswith('M'):
       print(f"Hola {nombre}!")


lista = ['a','b','c','d']

for letra in lista:
    numero_de_letra = lista.index(letra) + 1
    print(f"\n Letra {numero_de_letra}: {letra}")

numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)

palabra = 'PYTHON'

for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic = {'c1':'a','c2':'b','c3':'c'}

for item in dic.items():
    print(item)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero%2 == 0:
      suma_pares = suma_pares + numero
    elif numero%2 == 1:
        suma_impares = suma_impares + numero

print(suma_impares,suma_pares)

dic = {"Clave1":"a","Clave2":"b","Clave3":"c","Clave4":"d"}

for a,b in dic.items():
    print(a)
    print(b)


