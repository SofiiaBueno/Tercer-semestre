fecha = int(input("Ingrese el año: "))

if fecha % 4 == 0 and fecha % 400 != 0 and fecha % 100 != 0:
    print("es un ano bisiesto")
else:
    print("no un ano bisiesto")