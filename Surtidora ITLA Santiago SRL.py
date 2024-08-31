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
