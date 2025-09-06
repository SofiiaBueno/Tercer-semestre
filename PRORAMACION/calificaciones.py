calificacion = int(input("Ingresa la calificacion: "))
if calificacion >= 90:
    print("Su nota es A")
elif calificacion >= 80 and calificacion <= 89:
    print("Su nota es B")
elif calificacion >= 70 and calificacion <= 79:
    print("Su nota es C")
elif calificacion >= 60 and calificacion <= 69:
    print("Su nota es D")
else:
    print("Su calificacion es no aproatoria")

