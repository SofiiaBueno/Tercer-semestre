edad = int(input("Ingresa tu edad: "))

if edad <= 11:
    costo = 50
elif edad >= 12 and edad <= 17:
    costo = 80
else:
    costo = 100

print("Su costo por boleto sera de $", costo)