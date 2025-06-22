# main.py
from models import init_db
from controllers import BibliotecaController
from views import BibliotecaView

class AplicacionBiblioteca:
    def __init__(self):
        init_db()  # Asegura que la base de datos y tablas existan
        self.controller = BibliotecaController()
        self.view = BibliotecaView()

    def ejecutar(self):
        while True:
            opcion_principal = self.view.mostrar_menu_principal()

            if opcion_principal == '1':
                self.gestionar_autores()
            elif opcion_principal == '2':
                self.gestionar_generos()
            elif opcion_principal == '3':
                self.gestionar_libros()
            elif opcion_principal == '4':
                self.view.mostrar_mensaje("Saliendo de la aplicación. ¡Hasta pronto!")
                self.controller.cerrar_sesion()
                break
            else:
                self.view.mostrar_error("Opción inválida. Por favor, intente de nuevo.")

    def gestionar_autores(self):
        while True:
            opcion = self.view.mostrar_menu_gestion("Autores")
            if opcion == '1':
                nombre, apellido = self.view.pedir_datos_nuevo_autor()
                if nombre and apellido:
                    autor = self.controller.crear_autor(nombre, apellido)
                    if autor:
                        self.view.mostrar_mensaje(f"Autor '{autor.nombre} {autor.apellido}' creado con éxito (ID: {autor.id}).")
            elif opcion == '2':
                autores = self.controller.obtener_autores()
                self.view.mostrar_autores(autores)
            elif opcion == '3':
                autor_id = self.view.pedir_id_autor()
                if autor_id is not None:
                    nombre, apellido = self.view.pedir_datos_actualizar_autor()
                    if self.controller.actualizar_autor(autor_id, nombre, apellido):
                        self.view.mostrar_mensaje(f"Autor con ID {autor_id} actualizado con éxito.")
                    else:
                        self.view.mostrar_error(f"No se pudo actualizar el autor con ID {autor_id}.")
            elif opcion == '4':
                autor_id = self.view.pedir_id_autor()
                if autor_id is not None:
                    if self.controller.eliminar_autor(autor_id):
                        self.view.mostrar_mensaje(f"Autor con ID {autor_id} eliminado con éxito.")
                    else:
                        self.view.mostrar_error(f"No se pudo eliminar el autor con ID {autor_id}.")
            elif opcion == '5':
                break
            else:
                self.view.mostrar_error("Opción inválida. Por favor, intente de nuevo.")

    def gestionar_generos(self):
        while True:
            opcion = self.view.mostrar_menu_gestion("Géneros")
            if opcion == '1':
                nombre = self.view.pedir_datos_nuevo_genero()
                if nombre:
                    genero = self.controller.crear_genero(nombre)
                    if genero:
                        self.view.mostrar_mensaje(f"Género '{genero.nombre}' creado con éxito (ID: {genero.id}).")
            elif opcion == '2':
                generos = self.controller.obtener_generos()
                self.view.mostrar_generos(generos)
            elif opcion == '3':
                genero_id = self.view.pedir_id_genero()
                if genero_id is not None:
                    nuevo_nombre = self.view.pedir_datos_actualizar_genero()
                    if nuevo_nombre:
                        if self.controller.actualizar_genero(genero_id, nuevo_nombre):
                            self.view.mostrar_mensaje(f"Género con ID {genero_id} actualizado con éxito.")
                        else:
                            self.view.mostrar_error(f"No se pudo actualizar el género con ID {genero_id}.")
            elif opcion == '4':
                genero_id = self.view.pedir_id_genero()
                if genero_id is not None:
                    if self.controller.eliminar_genero(genero_id):
                        self.view.mostrar_mensaje(f"Género con ID {genero_id} eliminado con éxito.")
                    else:
                        self.view.mostrar_error(f"No se pudo eliminar el género con ID {genero_id}.")
            elif opcion == '5':
                break
            else:
                self.view.mostrar_error("Opción inválida. Por favor, intente de nuevo.")

    def gestionar_libros(self):
        while True:
            opcion = self.view.mostrar_menu_gestion("Libros")
            if opcion == '1':
                titulo, isbn, autor_id, genero_id, fecha_publicacion_str = self.view.pedir_datos_nuevo_libro()
                if titulo and isbn and autor_id is not None and genero_id is not None:
                    libro = self.controller.crear_libro(titulo, isbn, autor_id, genero_id, fecha_publicacion_str)
                    if libro:
                        self.view.mostrar_mensaje(f"Libro '{libro.titulo}' creado con éxito (ID: {libro.id}).")
                else:
                    self.view.mostrar_error("Faltan datos o ID de autor/género inválidos.")
            elif opcion == '2':
                libros = self.controller.obtener_libros()
                self.view.mostrar_libros(libros)
            elif opcion == '3':
                libro_id = self.view.pedir_id_libro()
                if libro_id is not None:
                    nuevo_titulo, nuevo_isbn, nuevo_autor_id, nuevo_genero_id, nueva_fecha_publicacion_str = self.view.pedir_datos_actualizar_libro()
                    if self.controller.actualizar_libro(libro_id, nuevo_titulo, nuevo_isbn, nuevo_autor_id, nuevo_genero_id, nueva_fecha_publicacion_str):
                        self.view.mostrar_mensaje(f"Libro con ID {libro_id} actualizado con éxito.")
                    else:
                        self.view.mostrar_error(f"No se pudo actualizar el libro con ID {libro_id}.")
            elif opcion == '4':
                libro_id = self.view.pedir_id_libro()
                if libro_id is not None:
                    if self.controller.eliminar_libro(libro_id):
                        self.view.mostrar_mensaje(f"Libro con ID {libro_id} eliminado con éxito.")
                    else:
                        self.view.mostrar_error(f"No se pudo eliminar el libro con ID {libro_id}.")
            elif opcion == '5':
                break
            else:
                self.view.mostrar_error("Opción inválida. Por favor, intente de nuevo.")

if __name__ == '__main__':
    app = AplicacionBiblioteca()
    app.ejecutar()