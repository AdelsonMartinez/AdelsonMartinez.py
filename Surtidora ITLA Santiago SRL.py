#Surtidora ITLA Santiago SRL. 
from time import localtime, strftime

class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad_stock, tipo_impuesto):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad_stock = cantidad_stock
        self.tipo_impuesto = tipo_impuesto
        
    def __str__(self):
        return f"{self.id_producto}\t{self.nombre.ljust(12)}RD${self.precio:.2f} (Stock: {self.cantidad_stock})"

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
