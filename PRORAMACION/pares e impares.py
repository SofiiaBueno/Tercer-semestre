num = int(input("Ingresa un numero: "))
par = 0 
impar = 0
for i in range(0, num + 1):
    if i % 2 == 0:
        par = par + i
    elif i % 2 != 0:
        impar = impar + i
print ("La sumatoria de los pares hasta ", num, "es: ", par)
print("La suma de los inpares hasta ",num, " es:", impar)

        
