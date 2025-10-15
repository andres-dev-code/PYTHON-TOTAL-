#esta funcion calcula el area de un triangulo segun los parametros del usuario
def area(base,altura):
    return base * altura // 2

triangle = area(int(input("Dime la base de tu triangulo:")),int(input("Dime la altura de tu triangulo:")))
print(f"El area de tu Triangulo es de {triangle} cm")

#esta funcion calcula el perimetro de un rectangulo
def perimetro(largo, ancho):
    return (largo + ancho) * 2

rectangulo = perimetro(int(input("Dime el largo de tu rectangulo:")),int(input("Dime el ancho de tu triangulo:")))
print(f"El perimetro de tu rectangulo es de {rectangulo} cm")
