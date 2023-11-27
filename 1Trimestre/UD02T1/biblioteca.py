"""Este módulo contiene la implementación de la clase Biblioteca."""
import json
from libro import Libro


class Biblioteca:
    """Clase que representa una biblioteca."""

    def __init__(self):
        """Inicializa una instancia de la clase Biblioteca con una lista vacía de libros."""
        self.libros = []
        self.lista_isbn = []


    def agregar_libro(self, libro):
        """Agrega un libro a la biblioteca."""
        self.libros.append(libro)
        self.lista_isbn.append(libro.isbn)

    def actualizar_libro(self, isbn, titulo, autor, anio_publicacion):
        """Actualiza la información de un libro en la biblioteca, identificado por su ISBN."""
        for libro in self.libros:
            if libro.isbn == isbn:
                libro.titulo = titulo
                libro.autor = autor
                libro.anio_publicacion = anio_publicacion
                return True
        return False

    def buscar_libro(self, isbn):
        """Busca un libro en la biblioteca por su ISBN
        y devuelve el libro si lo encuentra, de lo contrario, devuelve None."""
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def eliminar_libro(self, isbn):
        """Elimina un libro de la biblioteca por su ISBN."""
        for libro in self.libros:
            if libro.isbn == isbn:
                self.libros.remove(libro)
                self.lista_isbn.remove(isbn)
                return True
        return False

    def mostrar_libros(self):
        """Muestra la información de todos los libros en la biblioteca."""
        for libro in self.libros:
            libro.mostrar_info()

    def guardar_en_archivo(self, nombre_archivo):
        """Guarda la información de los libros de la biblioteca en un archivo JSON."""
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            libros_serializados = []
            for libro in self.libros:
                libros_serializados.append(
                    {
                        "isbn": libro.isbn,
                        "titulo": libro.titulo,
                        "autor": libro.autor,
                        "anio_publicacion": libro.anio_publicacion,
                    }
                )
            json.dump(libros_serializados, archivo)

    def cargar_desde_archivo(self, nombre_archivo):
        """Carga la información de los libros de un archivo JSON a la biblioteca."""
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                libros_serializados = json.load(archivo)
                for libro_serializado in libros_serializados:
                    self.libros.append(
                        Libro(
                            libro_serializado["isbn"],
                            libro_serializado["titulo"],
                            libro_serializado["autor"],
                            libro_serializado["anio_publicacion"],
                        )
                    )
        except FileNotFoundError:
            print("El archivo no existe. Creando una nueva biblioteca.")
