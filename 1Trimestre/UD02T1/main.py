
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

        try:
            opcion = int(opcion)  # Convertir la entrada a un número entero

            if opcion == 1:
                isbn = input("Ingrese el ISBN del libro: ")
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                anio_publicacion = input("Ingrese el año de publicación del libro: ")
                libro = Libro(isbn, titulo, autor, anio_publicacion)
                biblioteca.agregar_libro(libro)

            elif opcion == 2:
                isbn = input("Ingrese el ISBN del libro que desea actualizar: ")
                titulo = input("Ingrese el nuevo título del libro: ")
                autor = input("Ingrese el nuevo autor del libro: ")
                anio_publicacion = input("Ingrese el nuevo año de publicación del libro: ")
                if biblioteca.actualizar_libro(isbn, titulo, autor, anio_publicacion):
                    print("Libro actualizado exitosamente.")
                else:
                    print("ISBN no encontrado. No se pudo actualizar el libro.")

            elif opcion == 3:
                isbn = input("Ingrese el ISBN del libro que desea buscar: ")
                libro = biblioteca.buscar_libro(isbn)
                if libro:
                    libro.mostrar_info()
                else:
                    print("ISBN no encontrado. No se pudo encontrar el libro.")

            elif opcion == 4:
                isbn = input("Ingrese el ISBN del libro que desea eliminar: ")
                if biblioteca.eliminar_libro(isbn):
                    print("Libro eliminado exitosamente.")
                else:
                    print("ISBN no encontrado. No se pudo eliminar el libro.")

            elif opcion == 5:
                biblioteca.mostrar_libros()

            elif opcion == 6:
                biblioteca.guardar_en_archivo("biblioteca.json")
                break

            else:
                print("Opción inválida. Por favor, ingrese un número del 1 al 6.")

        except ValueError:
            print("Por favor, ingrese un número válido.")
