"""Este módulo contiene la implementación de la clase main."""
from biblioteca import Biblioteca
from libro import Libro

if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.cargar_desde_archivo("biblioteca.json")

    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Actualizar libro")
        print("3. Buscar libro")
        print("4. Eliminar libro")
        print("5. Mostrar libros")
        print("6. Guardar y salir")

        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == "1":
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            anio_publicacion = input("Ingrese el año de publicación del libro: ")
            libro = Libro(isbn, titulo, autor, anio_publicacion)
            biblioteca.agregar_libro(libro)
            print("Libro agregado exitosamente.")

        # Resto de las opciones del menú
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 6.")
