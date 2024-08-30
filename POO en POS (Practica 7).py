class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f"{self.id_producto}\t{self.nombre.ljust(12)}RD${self.precio}"

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        # Verificamos si el producto ya está en el carrito
        for item in self.items:
            if item['producto'].id_producto == producto.id_producto:
                item['cantidad'] += cantidad
                return
        # Si no está, lo añadimos al carrito
        self.items.append({'producto': producto, 'cantidad': cantidad})

    def calcular_total(self):
        subtotal = sum(item['cantidad'] * item['producto'].precio for item in self.items)
        impuestos = subtotal * 0.18
        total = subtotal + impuestos
        return subtotal, impuestos, total

    def imprimir_factura(self):
        print("\nFactura:")
        print("{:<8}{:<20}{:<20}{:<10}{:<15}".format("ID", "Descripción", "Precio por Unidad", "Cantidad", "Precio Total"))
        for item in self.items:
            producto = item['producto']
            cantidad = item['cantidad']
            total_producto = producto.precio * cantidad
            print("{:<8}{:<20}RD${:<20}{:<10.1f}RD${:<10.2f}".format(
                producto.id_producto, producto.nombre, producto.precio, cantidad, total_producto
            ))

        subtotal, impuestos, total = self.calcular_total()
        print(f"\nSubtotal: RD${subtotal:.2f}")
        print(f"\nImpuesto: RD${impuestos:.2f}")
        print(f"Total (incluye impuestos): RD${total:.2f}")

class Menu:
    def __init__(self):
        self.productos = {
            "15959": Producto("15959", "Arroz", 50),
            "2": Producto("2", "Habichuelas", 80),
            "3": Producto("3", "Aceite", 300),
            "4": Producto("4", "Pollo", 85),
            "1234523": Producto("1234523", "Lechuga", 80),
        }

    def mostrar_menu(self):
        print(">>>>>>>>>>Menú>>>>>>>>>>>>>")
        print("ID\tNombre\t""Precio")
        for producto in self.productos.values():
            print(producto)

# Flujo principal del POS
def main():
    menu = Menu()
    carrito = Carrito()

    while True:
        menu.mostrar_menu()
        id_producto = input("Elija un producto por su ID: ")
        
        # Verificamos que el ID sea válido
        if id_producto not in menu.productos:
            print("ID inválido. Inténtelo de nuevo.")
            continue

        cantidad = int(input("Ingrese la cantidad del producto: "))
        
        # Verificamos que la cantidad no sea negativa
        if cantidad < 0:
            print("Cantidad inválida. Debe ingresar un número positivo.")
            continue

        carrito.agregar_producto(menu.productos[id_producto], cantidad)
        
        continuar = input("¿Deseas añadir otro producto? (S/N): ").lower()
        if continuar != 's':
            break

    # Imprimimos la factura final
    carrito.imprimir_factura()

if __name__ == "__main__":
    main()
