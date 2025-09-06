a = int(input("Ingrese el primer numero entero: "))
b = int(input("Ingrese el segundo numero entero: "))
c = int(input("Ingrese el tercer numero entero: "))           

if (a > b and a > c): 
    mayor = a 
    print("El numero mayor es: ",a)
elif (b > a and b > c):
    mayor = b
else:
    mayor = c 

if (a < b and a < c): 
    menor = a 
elif (b < a and b < c):
    menor = b
else:
    menor = c 

print("El numero mayor es: ", mayor, " y el menor: ", menor)

