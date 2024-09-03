#Se agrega la clase Item y sus atributos
class Item: 
    def __init__(self, item_id, description, volumen):
        self.item_id = item_id
        self.description = description
        self.volumen = volumen

    def __str__(self): #se accede a los atributos de la instancia y se muestran en un formato legible
        return f"ID: {self.item_id}, Descripción: {self.description}, Volumen: {self.volumen} m³" 
