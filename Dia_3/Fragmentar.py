#[a:b] = extrae caracteres desde el indice a hasta el indice b
# si el  indice b esta vacio python lo tomara como hasta donde se pueda
#[:b] = si a esta vacio empezara desde el indice 0
#[a:b:c] = la c son los saltos
#[a:b:-c] = el - va a comenzar a buscar sub-strings de derecha a izquierda si c = 1 no hay saltos
# si c = 1 no hay saltos,si c = 2 salta de uno en uno,si c = 3 salta de 2 en dos y asi...
# ["desde el indice":"hasta el indice","saltos"]
text = "ABCDEFGHIJKLM"
fragmento = text[2:10:1]
print(fragmento)


