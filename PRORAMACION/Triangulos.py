a = int(input("Ingrese la pirmer medidad de su triangulo: "))
b = float(input("Ingrese la segunda medidad de su triangulo: "))
c = float(input("Ingrese la tecer medidad de su triangulo: "))

if a == b and b == c:
    print ("Es un triangulo equilatero.")
elif (a != b and a == c) or (a!= c and a == c):
    print("Es un trianguo isoceles. ")
else:
    print("Es un triangulo escaleno.")

    a



           