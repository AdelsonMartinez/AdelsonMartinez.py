import os

class Item: #se agrega la clase item y sus atributos
    def __init__(self, item_id, description, volumen):
        self.item_id = item_id
        self.description = description
        self.volumen = volumen
        
    def __str__(self):  # Se accede a los atributos de la instancia y se muestran en un formato legible
        return f"ID: {self.item_id}, Descripción: {self.description}, Volumen: {self.volumen} m³"
#se agrega la clase almacen
class Almacen:
    def __init__(self, almacen_id, nombre, altura, anchura, longitud):
        self.almacen_id = almacen_id
        self.nombre = nombre
        self.altura = altura
        self.anchura = anchura
        self.longitud = longitud
        self.items = []
        self.capacidad_total = altura * anchura * longitud
        self.capacidad_disponible = self.capacidad_total * 0.8  

    def agregar_item(self, item):
        if self.capacidad_disponible >= item.volumen:
            self.items.append(item)
            self.capacidad_disponible -= item.volumen
            print(f"Ítem {item.item_id} agregado al almacén {self.nombre}.")
        else:
            print(f"No hay suficiente espacio en el almacén {self.nombre} para el ítem {item.item_id}.")

    def retirar_item(self, item_id):  # Se define una función llamada retirar_item 
        for item in self.items:  # Se inicia un bucle que itera sobre cada ítem en la lista llamada self.items
            if item.item_id == item_id:  # Instrucción que verifica si el atributo item_id del objeto item es igual a la variable item_id
                self.items.remove(item)
                self.capacidad_disponible += item.volumen
                print(f"Ítem {item.item_id} retirado del almacén {self.nombre}.")
                return
        print(f"Ítem {item_id} no encontrado en el almacén {self.nombre}.")

    def mostrar_items(self):  # Se agrega el método que se encarga de mostrar los elementos almacenados
        if self.items:
            print(f"Ítems en el almacén {self.nombre}:")
            for item in self.items:
                print(str(item))
        else:
            print(f"No hay ítems en el almacén {self.nombre}.")

    def mostrar_capacidad(self):  # Se agrega el método para mostrar información sobre la capacidad del almacén.
        print(f"Capacidad total del almacén {self.nombre}: {self.capacidad_total} m³")
        print(f"Capacidad disponible del almacén {self.nombre}: {self.capacidad_disponible} m³")

class SistemaGestionAlmacenes:  # Se agrega la clase que gestiona múltiples almacenes.
    def __init__(self):
        self.almacenes = []

    def agregar_almacen(self, almacen):  # Se define el método de la clase 
        self.almacenes.append(almacen)
        print(f"Almacén {almacen.nombre} agregado al sistema.")

    # Se agrega el método mostrar_almacenes que tiene como objetivo presentar información sobre todos los almacenes disponibles.
    def mostrar_almacenes(self): 
        if self.almacenes:
            for almacen in self.almacenes:
                print(f"Almacén ID: {almacen.almacen_id}, Nombre: {almacen.nombre}")
                almacen.mostrar_capacidad()
        else:
            print("No hay almacenes en el sistema.")

# Se define la clase Empleado            
class Empleado:
    def __init__(self, nombre, username, password):  # Se crea una instancia de la clase Empleado que recibe tres parámetros
        self.nombre = nombre
        self.username = username
        self.password = password
        self.autenticado = False

    # Este método permite autenticar al empleado
    def autenticar(self, username, password):
        if self.username == username and self.password == password:
            self.autenticado = True
            print(f"{self.nombre} ha sido autenticado correctamente.")
        else:
            print("Autenticación fallida. Usuario o contraseña incorrectos.")

    # Este método permite al empleado registrar un ítem en almacén
    def registrar_item(self, almacen, item): 
        if not self.autenticado:
            print("Acceso denegado. Por favor, autentíquese para registrar un ítem.")
            return
        print(f"{self.nombre} está registrando el ítem {item.item_id} en el almacén.")
        almacen.agregar_item(item)

    def retirar_item(self, almacen, item_id):  # Se define la función que verifica si el usuario está autenticado antes de permitirle retirar un ítem de un almacén.
        if not self.autenticado:
            print("Acceso denegado. Por favor, autentíquese para retirar un ítem.")
            return
        print(f"{self.nombre} está retirando el ítem {item_id} del almacén.")
        almacen.retirar_item(item_id)

# Impresión de bienvenida al usuario
if __name__ == "__main__":
    print("*****Bienvenido a Almacén Dominicano S.A*****")  
    sistema = SistemaGestionAlmacenes()  # Se crea instancia de la clase SistemaGestionAlmacenes

    # Se crean dos instancias de la clase almacen
    almacen1 = Almacen(1, "Almacén Principal", 10, 5, 20)
    almacen2 = Almacen(2, "Almacén Secundario", 8, 4, 15)

    # Agregar almacenes al sistema
    sistema.agregar_almacen(almacen1)
    sistema.agregar_almacen(almacen2)

    # Creación de empleados con credenciales
    empleado1 = Empleado("Adelson Martinez", "adelsonmp", "data123")
    empleado2 = Empleado("Karol Abreu", "karola12", "welcome123")
    
    # Autenticación del empleado
    username_input = input("Ingrese su nombre de usuario: ")
    password_input = input("Ingrese su contraseña: ")

    # Intentar autenticar al empleado1
    empleado1.autenticar(username_input, password_input)
    
    # Si empleado1 no está autenticado, intentar autenticar a empleado2
    if not empleado1.autenticado:
        empleado2.autenticar(username_input, password_input)

    # Interacción con el sistema después de la autenticación
    if empleado1.autenticado or empleado2.autenticado:
        empleado = empleado1 if empleado1.autenticado else empleado2
        while True:
            # Limpiar pantalla justo antes de mostrar el menú
            os.system('cls' if os.name == 'nt' else 'clear')  

            print(f"\n¿Qué acción desea realizar, {empleado.nombre}?")
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
                empleado.registrar_item(almacen1, nuevo_item)  # Se agrega al almacen1 por defecto

            elif opcion == '2':
                item_id = int(input("Ingrese ID del ítem a retirar: "))
                empleado.retirar_item(almacen1, item_id)  # Se agrega al almacen1 por defecto

            elif opcion == '3':
                almacen1.mostrar_items()  # Se agrega al almacen1 por defecto

            elif opcion == '4':
                almacen1.mostrar_capacidad()  # Se agrega al almacen1 por defecto

            elif opcion == '5':
                almacen2.mostrar_capacidad()  # Muestra la capacidad del almacén secundario

            elif opcion == '6':
                item_id = int(input("Ingrese ID del ítem a modificar: "))
                for item in almacen1.items:
                    if item.item_id == item_id:
                        nueva_descripcion = input("Ingrese la nueva descripción: ")
                        nuevo_volumen = float(input("Ingrese el nuevo volumen (m³): "))
                        item.description = nueva_descripcion
                        item.volumen = nuevo_volumen
                        print(f"Ítem {item_id} modificado correctamente.")
                        break
                else:
                    print(f"Ítem {item_id} no encontrado en el almacén {almacen1.nombre}.")

            elif opcion == '7':
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            else:
                print("Opción no válida, por favor intente de nuevo.")

            # Pausa para que el usuario vea el mensaje antes de limpiar la pantalla 
            input("Presione Enter para continuar...")
    
    # Mostrar todos los almacenes al final
    sistema.mostrar_almacenes()