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





