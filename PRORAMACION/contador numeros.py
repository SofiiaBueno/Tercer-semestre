num = int(input("Ingresa un número: "))
contador = 0
numero = abs(num)



if num == 0:
    contador = 1
else:
    while num > 0:
        num //= 10  
        contador = contador + 1

print("El número tiene", contador, "dígitos.")
