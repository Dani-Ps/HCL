import unittest
from assignment.contact import Contact
from assignment.contact_manager import ContactManager
import os

class TestContactManager(unittest.TestCase):
    """Pruebas unitarias para la clase ContactManager."""

    def setUp(self):
        """Preparación antes de cada método de prueba."""
        self.filename = "test_contacts.csv"
        self.manager = ContactManager(self.filename)
        self.contact = Contact("John Doe", "123456789", "john@example.com")
        self.manager.add_contact(self.contact)

    def tearDown(self):
        """Limpieza después de cada método de prueba."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_add_contact(self):
        """Prueba que se pueda agregar un contacto."""
        self.assertIn(self.contact, self.manager.contacts, "El contacto debería estar en la lista de contactos.")

    def test_find_contact(self):
        """Prueba la búsqueda de un contacto por nombre."""
        found = self.manager.find_contact("John Doe")
        self.assertEqual(found, self.contact, "El contacto encontrado debería coincidir con el agregado.")

    def test_save_and_load_contacts(self):
        """Prueba que los contactos se puedan guardar y luego cargar desde un archivo."""
        self.manager.save_contacts()
        self.manager.contacts = []
        self.manager.load_contacts()
        self.assertIn(self.contact, self.manager.contacts, "El contacto debería ser cargado desde el archivo.")

    def test_save_contacts_ioerror(self):
        """Prueba el manejo de errores al intentar guardar en un archivo no accesible."""
        self.manager.filename = "/path/to/nonexistent/directory/contacts.csv"
        with self.assertRaises(IOError):
            self.manager.save_contacts()

    def test_load_contacts_ioerror(self):
        """Prueba el manejo de errores al intentar cargar desde un archivo no accesible."""
        self.manager.filename = "/path/to/nonexistent/directory/contacts.csv"
        with self.assertRaises(IOError):
            self.manager.load_contacts()

if __name__ == '__main__':
    unittest.main()
