from random import choice

#INICIO JUEGO
lista_de_palabras = ['Book','Cat','Atomic Habits','Python','Java','Coffe']
palabra_oculta = choice(lista_de_palabras)
user = ''

#IINGRESO USUARIO
def ingreso_usuario(usuario):
    usuario = input("Dame una letra:")

ingreso_usuario(user)


#CHEQUEAR LETRA VALIDA
def chequear_letra(letra):
    if letra == str in ingreso_usuario(user):
        pass
    else:
        return "Letra no valida"

#CHEQUEAR LETRA EN PALABRA
def chequear_letra_palabra(letra):
    if letra in chequear_letra(user):
        while letra in palabra_oculta:
            print("debug")
        else:
            pass

#RESTAR VIDA
contador = 6
def menos_vida(vida):
        vida -= 1
        pass