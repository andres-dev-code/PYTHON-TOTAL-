#este codigo analiza textos cortos como poemas o haikus,te pedira que ingreses 3 letras y del analisis te devolvera 6 datos

texto = input("Introduce tu texto:")
texto = texto.lower()

letras1 = input("ingresa tu primera letra a buscar:").lower()
letras2 = input("ingresa tu segunda letra a buscar:").lower()
letras3 = input("ingresa tu tercera letra a buscar:").lower()

buscar_letras1 = texto.count(letras1)
buscar_letras2 = texto.count(letras2)
buscar_letras3 = texto.count(letras3)

print("\n")
print("LETRAS ENCONTRADAS")
print(f"la letra \"{letras1}\" se repite un total de:{buscar_letras1}")
print(f"la letra \"{letras2}\" se repite un total de:{buscar_letras2}")
print(f"la letra \"{letras3}\" se repite un total de:{buscar_letras3}")

division = texto.split()
largo = len(division)

print("\n")
print("LARGO DE LAS PALABRAS")
print(f"Tu texto tiene:{largo} palabras de largo")

largo_carc = len(texto)

print("\n")
print("LARGO DE CARACTERES")
print(f"Tu texto  tiene:{largo_carc} caracteres de largo")

primera_letra = texto[0]
ultima_letra = texto[-1]

print("\n")
print("PRIMERA Y ULTIMA LETRA")
print(f"La primera letra es: \"{primera_letra}\" y la ultima letra es \"{ultima_letra}\"")

reversa = division.reverse()
junto = " ".join(division)

print("\n")
print("TEXTO EN REVERSA")
print(f"Asi seria tu texto en reversa: \n {junto}")

buscar_python = "python" in texto
dic = {True:"si",False:"no"}
print("\n")
print("BUSCANDO LA PALABRA PYTHON...")
print(f"la palabra python {dic[buscar_python]} se encuentra en tu texto")