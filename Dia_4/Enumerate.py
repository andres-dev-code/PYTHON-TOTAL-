
text = """cuando pasa una estrella fugaz en el cielo, cuando cae la primera hoja de un árbol o cuando llueve sobre un río."""

for i in enumerate(text):
    print(i)


lista = [1,2,3,4,5]

sets = list(enumerate(lista)) #tuple en una lista

for i in sets:
     print(sets)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombres in enumerate(lista_nombres):
    if nombres.startswith("M"):
        print(f"{nombres},{indice}")