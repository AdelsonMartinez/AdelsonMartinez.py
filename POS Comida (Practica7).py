# Definimos el menú de productos como un diccionario
menu = {
    "15959": {"nombre": "Arroz", "precio": 50},
    "2": {"nombre": "Habichuelas", "precio": 80},
    "3": {"nombre": "Aceite", "precio": 300},
    "4": {"nombre": "Pollo", "precio": 85},
    "1234523": {"nombre": "Lechuga", "precio": 80},
}
# Lista para almacenar los productos del carrito
carrito = []

def mostrar_menu():
    print("ID\tNombre\t\tPrecio")
    for id_producto, detalles in menu.items():
        print(f"{id_producto}\t{detalles['nombre'].ljust(12)}\tRD${detalles['precio']}")

def agregar_al_carrito(id_producto, cantidad):
    # Verificamos si el producto ya está en el carrito
    for item in carrito:
        if item['id'] == id_producto:
            item['cantidad'] += cantidad
            return
    # Si no está, lo añadimos al carrito
    carrito.append({'id': id_producto, 'cantidad': cantidad})

def calcular_total():
    subtotal = sum(item['cantidad'] * menu[item['id']]['precio'] for item in carrito)
    impuesto = subtotal * 0.18
    total = subtotal + impuesto
    return subtotal, total

def imprimir_factura():
    print("\nFactura:")
    print("ID\tDescripción\t\tPrecio por Unidad\tCantidad\tPrecio Total")
    for item in carrito:
        id_producto = item['id']
        cantidad = item['cantidad']
        precio_unitario = menu[id_producto]['precio']
        total_producto = precio_unitario * cantidad
        print(f"{id_producto}\t{menu[id_producto]['nombre'].ljust(12)}\tRD${precio_unitario}\t{cantidad}\t\tRD${total_producto}")

    subtotal, total = calcular_total()
    print(f"\nSubtotal: RD${subtotal}")
    print(f"Total (incluyendo impuestos): RD${total:.2f}")

# Flujo principal del POS
while True:
    mostrar_menu()
    id_producto = input("Elija un producto por su ID: ")
    
    # Verificamos que el ID sea válido
    if id_producto not in menu:
        print("ID inválido. Inténtelo de nuevo.")
        continue
    
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    # Verificamos que la cantidad no sea negativa
    if cantidad < 0:
        print("Cantidad inválida. Debe ingresar un número positivo.")
        continue

    agregar_al_carrito(id_producto, cantidad)
    
    continuar = input("¿Deseas añadir otro producto? (S/N): ").lower()
    if continuar != 's':
        break

# Imprimimos la factura final
imprimir_factura()
