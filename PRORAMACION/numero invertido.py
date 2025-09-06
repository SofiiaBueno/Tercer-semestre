num = input("Ingresa un numero positivo: ")

numinv = ""
for i in range(len(num)-1, -1, -1):  
    numinv += num[i]

print("Elnumero al reves:", numinv)
