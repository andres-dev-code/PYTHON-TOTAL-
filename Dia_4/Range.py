lista = list(range(1,101))
par = 0
impar = 0

for num in lista:
    if num%2 == 0:
        par += num
    else:
        impar += num

print(par,impar)