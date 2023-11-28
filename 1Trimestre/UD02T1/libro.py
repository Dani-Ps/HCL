"""Este módulo contiene la implementación de la clase Libro."""
class Libro:
    """Clase que representa un libro."""

    def __init__(self, isbn, titulo, autor, anio_publicacion):
        """Inicializa una instancia de la clase Libro con los atributos dados."""
        # Utilizo isbn en vez de id ya que es una palabra reservada
        # y el pylint me lo daba como fallo.
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_info(self):
        """Muestra la información del libro en la consola de manera mejorada."""
        print(f"{'=' * 40}")
        print(f"ISBN: {self.isbn}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.anio_publicacion}")

    def to_dict(self):
        """Devuelve un diccionario que representa el libro."""
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "anio_publicacion": self.anio_publicacion,
        }

    def validar_isbn(self, isbn):
        """Valida que el ISBN tenga 13 caracteres y sean todos números."""
        return len(isbn) == 13 and isbn.isdigit()

    def set_isbn(self, isbn):
        """Establece el ISBN del libro con validación."""
        if not self.validar_isbn(isbn):
            raise ValueError("ISBN inválido. Debe tener 13 dígitos y ser numérico.")
        self.isbn = isbn
