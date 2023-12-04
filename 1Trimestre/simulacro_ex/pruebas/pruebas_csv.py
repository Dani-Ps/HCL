'''
    TEST CSV file
'''
import csv
class Contact:
    def __init__(self, name, phone, email):
         self.name = name
         self.phone = phone
         self.email = email

    def to_list(self):
        return [self.name, self.phone, self.email]

    @staticmethod
    def save_contacts(contactos, filename):
        with open(filename, 'w',newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'e-mail'])
            for c in contactos:
                writer.writerow(c.to_list())
    @staticmethod
    def load_contactos(filename):
        contactos = []
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) # Para eliminar la primera fila (Cabecera: ['Name', 'Phone', 'e-mail']).
            for row in reader:
                if row:
                    contactos.append(Contact(row[0], row[1], row[2]))
        return contactos

    @staticmethod
    def show_contacts(filename):
        new_contactos = Contact.load_contactos(filename)
        for contact  in new_contactos:
            print(contact.name, contact.phone, contact.email)


c1 = Contact('dani', '45454544', 'kenaa@example.com')
c2 = Contact('dani', '45454544', 'kenaa@example.com')
c3 = Contact('dani', '45454544', 'kenaa@example.com')

contactos = [c1, c2, c3]

Contact.save_contacts(contactos, 'contactos.csv')

Contact.show_contacts('contactos.csv')
