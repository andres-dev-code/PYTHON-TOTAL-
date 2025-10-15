A = {0,1,2,3,4}
B = {5,6,7,8,9}

C = A.union(B)
print(C)

element = int(input("escoje un numero: "))

if element in C:
    print(f"{element} ∈ C")
else:
    print(f"{element} ∉ C")
