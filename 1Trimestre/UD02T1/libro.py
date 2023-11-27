"""Este módulo contiene la implementación de la clase Libro."""


class Libro:
    """Clase que representa una biblioteca."""

    def __init__(self, isbn, titulo, autor, anio_publicacion):
        """Inicializa una instancia de la clase Libro con los atributos dados."""
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_info(self):
        """Muestra la información del libro en la consola."""
        print(
            f"ISBN: {self.isbn}, "
            f"Título: {self.titulo}, "
            f"Autor: {self.autor}, "
            f"Año de Publicación: {self.anio_publicacion}"
        )

    def __dict__(self):
        """Devuelve un diccionario que representa el libro."""
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "anio_publicacion": self.anio_publicacion,
        }