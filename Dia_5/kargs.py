def atributos_persona(**kwargs):
    return kwargs

c =atributos_persona(pelo ='corto', color ='negro')

print(type(c))

def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f'{clave} es igual a {valor}')
        total += valor
    return total

n = suma(x=5,y=5,c=5)
print(n)

def cantidad_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return len(lista)


y = cantidad_atributos(a = 1, b = 2, c = 3, d = 4, e = 5, f = 6, g = 7, h = 8)
print(y)

def describir_persona(nombre,**kwargs):
    print(f"Características de {nombre}:")
    for claves,valores in kwargs.items():
        print(f"color de {claves}:{valores}")

z = describir_persona("Castro",pelo = 'negro',ojos = 'marrones',piel = 'blanco')
