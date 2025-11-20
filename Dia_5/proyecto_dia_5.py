from random import choice

#INICIO JUEGO
lista_de_palabras = ['book','cat','atomic','habits','python','java','coffe']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

#ELEGIR PALABRA
def elegir_palabra(lista):
    palabra_random = choice(lista_de_palabras)
    letras = len(set(palabra_random))

    return palabra_random,letras

#PEDIR Y VERIFICAR LETRA
def pedir_letra():
    letra = ''
    es_valida = False
    abecedario = "abcdefghijklmnopqrstuvwxyz"

    while not es_valida:
        letra = input("Dame una letra:").lower()
        if letra in abecedario and len(letra) == 1:
            es_valida = True
        else:
            return 'Letra no valida'

    return letra

#MOSTRAR TABLERO
def tablero(palabra_elegida):

    lista_palabra_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_palabra_oculta.append(l)
        else:
            lista_palabra_oculta.append("-")

    print(' '.join(lista_palabra_oculta))

#CHEQUEAR LETRA
def chequear(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Ya has encontrado esa letra. Intenta de nuevo')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

#PERDER
def perder():
    print("Has perdido todas tus vidas")
    print(f"La palabra oculta era {palabra} ")

    return True

#GANAR
def ganar(palabra_descubierta):
    tablero(palabra_descubierta)
    print("Felicitaciones has encontrado la palabra oculta")

    return True

palabra,letras_unicas = elegir_palabra(lista_de_palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    tablero(palabra)
    print('\n')
    print("letras incorrectas: " + '-'.join(letras_incorrectas))
    print(f"Vidas: {intentos}")
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos,terminado,aciertos = chequear(letra,palabra,intentos,aciertos)

    juego_terminado = terminado