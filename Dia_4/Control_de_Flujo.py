num1 = int(input("Introduce un Numero:"))
num2 = int(input("Introduce otro Numero:"))
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num1} es menor que {num2}")


animales = ["loro","perro","gato","hamster","serpiente","pajaro","paloma","pez","conejo"]

pet = input("que mascota tienes?:")

if pet in animales:
    print(f"tienes un {pet}")
elif pet == "perro":
    print("tienes un perro")
else:
    print("No se que animal tienes")


habla_ingles = True
sabe_python = False
if (habla_ingles == True) and (sabe_python == True):
    print("Cumples con los requisitos para postularte")
elif habla_ingles == False:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif sabe_python == False:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")


text = input("Tienes 18 años? Y/N:")
dic = {"Y":True,"N":False}

if text == "Y".lower():
    print("Puedes entrar")
else:
    print("no puedes entrar")


