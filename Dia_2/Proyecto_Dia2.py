#Esta calculadora calcula el 13% de comisiones
user = input("Cual es tu Nombre?:")
ventas = float(input("Cuanto fueron tus ventas?:"))
comisions = round(ventas * 13 / 100, 2)
print(f"\nHola Empleado \"{user}\",tus comisiones fueron de {comisions}$,Felicidades!")