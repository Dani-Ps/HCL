import os
import csv
from assignment.contact import Contact

class ContactManager:
    def __init__(self, filename='contacts.csv'):
        self.filename = filename
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def save_contacts(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "e-mail"])
            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone, contact.email])

    def load_contacts(self):
        if os.path.isfile(self.filename):
            with open(self.filename, newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Asegurarse de que la fila no esté vacía
                        self.contacts.append(Contact(row[0], row[1], row[2]))
        else:
            self.save_contacts()
