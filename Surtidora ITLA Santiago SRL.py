#Surtidora ITLA Santiago SRL. 
from time import localtime, strftime
#Se agrega la clase Producto
class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad_stock, tipo_impuesto):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad_stock = cantidad_stock
        self.tipo_impuesto = tipo_impuesto
        
    def __str__(self):
        return f"{self.id_producto}\t{self.nombre.ljust(12)}RD${self.precio:.2f} (Stock: {self.cantidad_stock})"
#Se agrega la clase Carrito 
class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        # Verificamos que haya suficiente stock
        if cantidad > producto.cantidad_stock:
            print(f"No hay suficiente stock para {producto.nombre}. Stock actual: {producto.cantidad_stock}")
            return
        # Verificamos si el producto ya está en el carrito
        for item in self.items:
            if item['producto'].id_producto == producto.id_producto:
                item['cantidad'] += cantidad
                producto.cantidad_stock -= cantidad  
                return
        # Si no está, se añade al carrito
        self.items.append({'producto': producto, 'cantidad': cantidad})
        producto.cantidad_stock -= cantidad  # Reducir stock

    def calcular_total(self):
        subtotal = 0
        impuestos_totales = 0

        for item in self.items:
            producto = item['producto']
            cantidad = item['cantidad']
            subtotal += producto.precio * cantidad
           
            # Calcular impuestos según el tipo
            if producto.tipo_impuesto == "01":
                impuestos_totales += (producto.precio * cantidad) * 0.18
            elif producto.tipo_impuesto == "02":
                impuestos_totales += (producto.precio * cantidad) * 0.16
            
        total = subtotal + impuestos_totales
        return subtotal, impuestos_totales, total

    def obtener_fecha_hora(self):
        # Función para obtener la fecha y hora actual
        return strftime("%d/%m/%Y %H:%M", localtime())

    def imprimir_factura(self, nombre_cliente, id_cliente):
        print("\nFactura:")
        print(f"Cliente: {nombre_cliente}")
        print(f"ID Cliente: {id_cliente}")
        print(f"Fecha: {self.obtener_fecha_hora()}")
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
        print(f"Impuestos: RD${impuestos:.2f}")
        print(f"Total (incluye impuestos): RD${total:.2f}")
class Menu:
    def __init__(self):
        self.productos = {
            "15959": Producto("15959", "Arroz", 50, 20, "01"),
            "2": Producto("2", "Habichuelas", 80, 10, "01"),
            "3": Producto("3", "Aceite", 300, 15, "02"),
            "4": Producto("4", "Pollo", 85, 25, "01"),
            "1234523": Producto("1234523", "Lechuga", 80, 30, "00"),
        }

    def mostrar_menu(self):
        print(">>>>>>>>>>Menú>>>>>>>>>>>>>")
        print("ID\tNombre\t""Precio")
        for producto in self.productos.values():
            print(producto)
def main():
    menu = Menu()
    carrito = Carrito()
    
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    id_cliente = input("Ingrese el ID del cliente: ")
    
    while True:
        menu.mostrar_menu()
        id_producto = input("Elija un producto por su ID: ")
