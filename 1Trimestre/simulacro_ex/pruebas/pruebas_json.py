'''
    TEST JSON file
'''
import json
'''

    PRUEBA ALMACENAR DATOS EN JSON.
    
    contactos = {'CONTACTOS': [
    {'name': 'daniel', 'phone': '454545454', 'email': 'dani@gmai.com'},
    {'name': 'daniel', 'phone': '454545454', 'email': 'dani@gmai.com'},
    {'name': 'daniel', 'phone': '454545454', 'email': 'dani@gmai.com'},
    {'name': 'daniel', 'phone': '454545454', 'email': 'dani@gmai.com'},
    {'name': 'daniel', 'phone': '454545454', 'email': 'dani@gmai.com'}]}
    
    # Metodo para guardar los contactos en un archivo json.
    with open('contactos.json', 'w', encoding='utf-8') as file:
        json.dump(contactos, file, indent=4, sort_keys=True)
'''
'''
        PRUEBA ALMACENAR LISTA EN JSON + CARGAR LISTA + MOSTRAR.

class Contact:
    def __init__(self, name, phone, email):
         self.name = name
         self.phone = phone
         self.email = email

    def to_dict(self):
        return {'name': self.name, 'phone': self.phone, 'email': self.email}

    @staticmethod
    def save_contacts(contacts, filename):
        contacts_serializados = [contact.to_dict() for contact in contacts]
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({'CONTACTOS': contacts_serializados}, file, indent=4, sort_keys=True)

    @staticmethod
    def load_contacts(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                contactos_serializados = json.load(file)['CONTACTOS']
                return [Contact(contact['name'], contact['phone'], contact['email']) for contact in contactos_serializados]
        except FileNotFoundError:
            return []

    @staticmethod
    def show_contacts(filename):
        new_contacts = Contact.load_contacts(filename)
        for contact in new_contacts:
            print(contact.name, contact.phone, contact.email)

contactos = []

c1 = Contact('dani', '45454544', 'kenaa@example.com')
c2 = Contact('dani', '45454544', 'kenaa@example.com')
c3 = Contact('dani', '45454544', 'kenaa@example.com')

contactos.extend([c1, c2, c3])

Contact.save_contacts(contactos, 'contactos.json')
Contact.show_contacts('contactos.json')
'''
