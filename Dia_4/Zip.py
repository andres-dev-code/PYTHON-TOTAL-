nombres = ["Juan","Carlos","Castro"]
edades = [12,43,34]
ciudades = ['Peru','Mexico','Cuba']

for nombre,edad,ciudad in zip(nombres,edades,ciudades):
    print(f"Nombre:{nombre},su edad es: {edad},y son de: {ciudades}")

enteros = list(range(1,101))
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

conjunto = list(zip(enteros,letras))

for ent,let in zip(letras,enteros):
    print(f'{ent},{let}')

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for cap,pais in zip(capitales,paises):
    print(f"La capital de {pais} es {cap}")

esp = ['uno','dos','tres','cuatro','cinco']
pt = ['um','dois','três','quatro','cinco']
eng = ['one','two','three','four','five']

numeros = list(zip(esp,pt,eng))
print(numeros)

