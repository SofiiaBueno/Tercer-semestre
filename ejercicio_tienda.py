class Inventariotienda:
    def __init__(self, nom_tienda):
        self.nom_tienda = nom_tienda
        self.productos = []  

    def agregar_producto(self, nombre, precio, cantidad):
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad}
        self.productos.append(producto)
        print(f"Producto '{nombre}' agregado correctamente.")

    
    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"] == nombre:
                producto["cantidad"] -= cantidad
                print(f"Se vendieron {cantidad} unidades de '{nombre}'.")
                return
        print( "producto no existe.")

    def mostrar_inventario(self):
        if not self.productos:
            print("el inventario está vacío.")
            return
        print("Inventario de la tienda:")
        for producto in self.productos:
            print(f"- {producto['nombre']}: Precio ${producto['precio']}, Cantidad {producto['cantidad']}")
        print()

    def producto_mas_caro(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        producto_caro = max(self.productos, key=lambda x: x["precio"])
        print(f"Producto más caro: {producto_caro['nombre']} - Precio ${producto_caro['precio']}")


tienda = Inventariotienda("Mi Tienda")

while True:
    print("Menú de Inventario")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Ver inventario")
    print("4. Producto más caro")
    print("5. Salir")
    eleccion = input("Elige una opción: ")

    if eleccion == "1":
        nombre = input("Nombre del producto: ")
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("ingresa numeros válidos.")
            continue
        tienda.agregar_producto(nombre, precio, cantidad)

    elif eleccion == "2":
        nombre = input("Nombre del producto a vender: ")
        try:
            cantidad = int(input("Cantidad a vender: "))
        except ValueError:
            print("ingresa un número válido del menu.")
            continue
        tienda.vender_producto(nombre, cantidad)

    elif eleccion == "3":
        tienda.mostrar_inventario()

    elif eleccion == "4":
        tienda.producto_mas_caro()

    elif eleccion == "5":
        print("Salir")
        break

    else:
        print("Ingresa otra opcion.")
