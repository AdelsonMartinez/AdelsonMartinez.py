import os

class Item:
    def __init__(self, item_id, description, volumen):
        self._item_id = item_id
        self._description = description
        self._volumen = volumen
        
    def get_item_id(self):
        return self._item_id

    def get_description(self):
        return self._description

    def get_volumen(self):
        return self._volumen
    
    def __str__(self):
        return f"ID: {self.get_item_id()}, Descripción: {self.get_description()}, Volumen: {self.get_volumen()} m³"

class Almacen:
    def __init__(self, almacen_id, nombre, altura, anchura, longitud):
        self._almacen_id = almacen_id
        self._nombre = nombre
        self._altura = altura
        self._anchura = anchura
        self._longitud = longitud
        self._items = []
        self._capacidad_total = altura * anchura * longitud
        self._capacidad_disponible = self._capacidad_total * 0.8  

    def agregar_item(self, item):
        if self._capacidad_disponible >= item.get_volumen():
            self._items.append(item)
            self._capacidad_disponible -= item.get_volumen()
            print(f"Ítem {item.get_item_id()} agregado al almacén {self.get_nombre()}.")
        else:
            print(f"No hay suficiente espacio en el almacén {self.get_nombre()} para el ítem {item.get_item_id()}.")

    def retirar_item(self, item_id):
        for item in self._items:
            if item.get_item_id() == item_id:
                self._items.remove(item)
                self._capacidad_disponible += item.get_volumen()
                print(f"Ítem {item.get_item_id()} retirado del almacén {self.get_nombre()}.")
                return
        print(f"Ítem {item_id} no encontrado en el almacén {self.get_nombre()}.")

    def mostrar_items(self):
        if self._items:
            print(f"Ítems en el almacén {self.get_nombre()}:")
            for item in self._items:
                print(str(item))
        else:
            print(f"No hay ítems en el almacén {self.get_nombre()}.")

    def mostrar_capacidad(self):
        print(f"Capacidad total del almacén {self.get_nombre()}: {self._capacidad_total} m³")
        print(f"Capacidad disponible del almacén {self.get_nombre()}: {self._capacidad_disponible} m³")
    
    def get_nombre(self):
        return self._nombre

class SistemaGestionAlmacenes:
    def __init__(self):
        self._almacenes = []

    def agregar_almacen(self, almacen):
        self._almacenes.append(almacen)
        print(f"{almacen.get_nombre()} agregado al sistema.")

    def mostrar_almacenes(self):
        if self._almacenes:
            for almacen in self._almacenes:
                print(f"Almacén ID: {almacen._almacen_id}, Nombre: {almacen.get_nombre()}")
                almacen.mostrar_capacidad()
        else:
            print("No hay almacenes en el sistema.")

class Empleado:
    def __init__(self, nombre, username, password):
        self._nombre = nombre
        self._username = username
        self._password = password
        self._autenticado = False

    def autenticar(self, username, password):
        if self._username == username and self._password == password:
            self._autenticado = True
            print(f"{self.get_nombre()} ha sido autenticado correctamente.")
        else:
            print("Autenticación fallida. Usuario o contraseña incorrectos.")

    def registrar_item(self, almacen, item):
        if not self._autenticado:
            print("Acceso denegado. Por favor, autentíquese para registrar un ítem.")
            return
        print(f"{self.get_nombre()} está registrando el ítem {item.get_item_id()} en el almacén.")
        almacen.agregar_item(item)

    def retirar_item(self, almacen, item_id):
        if not self._autenticado:
            print("Acceso denegado. Por favor, autentíquese para retirar un ítem.")
            return
        print(f"{self.get_nombre()} está retirando el ítem {item_id} del almacén.")
        almacen.retirar_item(item_id)

    def get_nombre(self):
        return self._nombre

# Impresión de bienvenida al usuario
if __name__ == "__main__":
    print("*****Bienvenido a Almacén Dominicano S.A*****")  
    sistema = SistemaGestionAlmacenes()

    almacen1 = Almacen(1, "Almacén Principal", 10, 5, 20)
    almacen2 = Almacen(2, "Almacén Secundario", 8, 4, 15)

    sistema.agregar_almacen(almacen1)
    sistema.agregar_almacen(almacen2)

    empleado1 = Empleado("Adelson", "adelsonmp", "data123")
    empleado2 = Empleado("Carolina", "karola12", "welcome123")
    
    username_input = input("Ingrese su nombre de usuario: ")
    password_input = input("Ingrese su contraseña: ")

    empleado1.autenticar(username_input, password_input)
    
    if not empleado1._autenticado:
        empleado2.autenticar(username_input, password_input)

    if empleado1._autenticado or empleado2._autenticado:
        empleado = empleado1 if empleado1._autenticado else empleado2
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  

            print(f"\n¿Qué acción desea realizar, {empleado.get_nombre()}?")
            print("1. Agregar ítem al almacén principal")
            print("2. Retirar ítem del almacén principal")
            print("3. Mostrar ítems en el almacén principal")
            print("4. Mostrar capacidad del almacén principal")
            print("5. Mostrar capacidad del almacén secundario")
            print("6. Modificar ítem en el almacén principal")
            print("7. Salir")

            opcion = input("Seleccione una opción (1-7): ")

            if opcion == '1':
                item_id = int(input("Ingrese ID del ítem: "))
                descripcion = input("Ingrese descripción del ítem: ")
                volumen = float(input("Ingrese volumen del ítem (m³): "))
                nuevo_item = Item(item_id, descripcion, volumen)
                empleado.registrar_item(almacen1, nuevo_item)

            elif opcion == '2':
                item_id = int(input("Ingrese ID del ítem a retirar: "))
                empleado.retirar_item(almacen1, item_id)

            elif opcion == '3':
                almacen1.mostrar_items()

            elif opcion == '4':
                almacen1.mostrar_capacidad()

            elif opcion == '5':
                almacen2.mostrar_capacidad()

            elif opcion == '6':
                item_id = int(input("Ingrese ID del ítem a modificar: "))
                for item in almacen1._items:
                    if item.get_item_id() == item_id:
                        nueva_descripcion = input("Ingrese la nueva descripción: ")
                        nuevo_volumen = float(input("Ingrese el nuevo volumen (m³): "))
                        item._description = nueva_descripcion
                        item._volumen = nuevo_volumen
                        print(f"Ítem {item_id} modificado correctamente.")
                        break
                else:
                    print(f"Ítem {item_id} no encontrado en el almacén {almacen1.get_nombre()}.")

            elif opcion == '7':
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            else:
                print("Opción no válida, por favor intente de nuevo.")

            input("Presione Enter para continuar...")

    sistema.mostrar_almacenes()
