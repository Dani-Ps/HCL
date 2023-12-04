import csv
# Clase contato con metodo constructor y para almacaenar contactos en un archivo csv.
class Contact:
    # Constructor de la clase
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    # Método para guardar los datos en un archivo csv
    def __str__(self):
        return f"{self.name},{self.phone},{self.email}"

    # Método para comparar dos contactos
    def __eq__(self, other):
        return self.name == other.name and self.phone == other.phone and self.email == other.email
