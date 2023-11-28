"""Este módulo contiene la implementación de la clase main."""
from biblioteca import Biblioteca
from libro import Libro

def validar_numero_4_digitos(valor, mensaje):
    """Valida que el valor sea un número de 4 dígitos."""
    while not (len(valor) == 4 and valor.isdigit()):
        print(f"{mensaje} debe ser un número de 4 dígitos.")
        valor = input(f"Ingrese {mensaje.lower()}: ")
    return valor

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=====================")
    print("      MENÚ PRINCIPAL")
    print("=====================")
    print("1.  Agregar libro")
    print("2.  Actualizar libro")
    print("3.  Buscar libro")
    print("4.  Eliminar libro")
    print("5.  Mostrar libros")
    print("6.  Guardar y salir")
    print("=====================")

def menu_principal(biblioteca):
    """Maneja el flujo principal de la aplicación."""
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la operación que desea realizar: ")

        try:
            opcion = int(opcion)

            if opcion == 1:
                agregar_libro(biblioteca)
            elif opcion == 2:
                actualizar_libro(biblioteca)
            elif opcion == 3:
                buscar_libro(biblioteca)
            elif opcion == 4:
                eliminar_libro(biblioteca)
            elif opcion == 5:
                biblioteca.mostrar_libros()
            elif opcion == 6:
                biblioteca.guardar_en_archivo("biblioteca.json")
                break
            else:
                print("Opción inválida. Por favor, ingrese un número del 1 al 6.")

        except ValueError:
            print("Por favor, ingrese un número válido.")

def agregar_libro(biblioteca):
    """Agrega un libro a la biblioteca."""
    isbn = input("Ingrese el ISBN del libro: ")
    if len(isbn) == 13 and isbn.isdigit():
        titulo = input("Ingrese el título del libro: ")
        titulo = validar_longitud(titulo, "El título")
        autor = input("Ingrese el autor del libro: ")
        autor = validar_longitud(autor, "El autor")
        anio_publicacion = input("Ingrese el año de publicación del libro: ")
        anio_publicacion = validar_numero_4_digitos(anio_publicacion, "El año de publicación")

        libro = Libro(isbn, titulo, autor, anio_publicacion)
        biblioteca.agregar_libro(libro)
    else:
        print("ISBN inválido. Debe tener 13 dígitos y ser numérico.")
def actualizar_libro(biblioteca):
    """Actualiza un libro en la biblioteca."""
    isbn = input("Ingrese el ISBN del libro que desea actualizar: ")
    if len(isbn) == 13 and isbn.isdigit():
        titulo = input("Ingrese el nuevo título del libro: ")
        titulo = validar_longitud(titulo, "El nuevo título")
        autor = input("Ingrese el nuevo autor del libro: ")
        autor = validar_longitud(autor, "El nuevo autor")
        anio_publicacion = input("Ingrese el nuevo año de publicación del libro: ")
        anio_publicacion = validar_numero_4_digitos(anio_publicacion, "El nuevo año de publicación")

        if biblioteca.actualizar_libro(isbn, titulo, autor, anio_publicacion):
            print("Libro actualizado exitosamente.")
        else:
            print("ISBN no encontrado. No se pudo actualizar el libro.")
    else:
        print("ISBN inválido. Debe tener 13 dígitos y ser numérico.")

def buscar_libro(biblioteca):
    """Busca un libro en la biblioteca."""
    isbn = input("Ingrese el ISBN del libro que desea buscar: ")
    libro = biblioteca.buscar_libro(isbn)
    if libro:
        libro.mostrar_info()
    else:
        print("ISBN no encontrado. No se pudo encontrar el libro.")

def eliminar_libro(biblioteca):
    """Elimina un libro de la biblioteca."""
    isbn = input("Ingrese el ISBN del libro que desea eliminar: ")
    if biblioteca.eliminar_libro(isbn):
        print("Libro eliminado exitosamente.")
    else:
        print("ISBN no encontrado. No se pudo eliminar el libro.")


def validar_longitud(valor, mensaje):
    """Valida la longitud de una cadena."""
    while not 1 <= len(valor) <= 50:
        print(f"{mensaje} debe tener entre 1 y 50 caracteres.")
        valor = input(f"Ingrese {mensaje.lower()}: ")
    return valor

if __name__ == "__main__":
    biblioteca = Biblioteca()
    # Casos de uso predefinidos
    libros_auto = [
        Libro("1234567890123", "Libro 1", "Autor 1", "2020"),
        Libro("2345678901234", "Libro 2", "Autor 2", "2018"),
        Libro("3456789012345", "Libro 3", "Autor 3", "2015"),
        Libro("4567890123456", "Libro 4", "Autor 4", "2012"),
        Libro("5678901234567", "Libro 5", "Autor 5", "2010"),
    ]

    for libro in libros_auto:
        biblioteca.agregar_libro(libro)

    biblioteca.cargar_desde_archivo("biblioteca.json")
    menu_principal(biblioteca)

# Casos de NO VALIDOS
# libro_invalido_isbn = Libro("ISBNInvalido", "Libro Inválido", "Autor Inválido", "2022")
# libro_invalido_titulo = Libro("1234567890123", "Este es un título muy largo que supera los 50 caracteres", "Autor Inválido", "2022")
# libro_invalido_autor = Libro("Este es un autor muy largo que supera los 50 caracteres")
# libro_invalido_anio = Libro("1234567890123", "Libro Inválido", "Autor Inválido", "AñoInválido")
