# views.py
import datetime

class BibliotecaView:
    def mostrar_mensaje(self, mensaje):
        print(f"\n--- {mensaje} ---")

    def mostrar_error(self, error_mensaje):
        print(f"\n!!! ERROR: {error_mensaje} !!!")

    def mostrar_menu_principal(self):
        print("\n--- Menú Principal de la Biblioteca ---")
        print("1. Gestionar Autores")
        print("2. Gestionar Géneros")
        print("3. Gestionar Libros")
        print("4. Salir")
        return input("Seleccione una opción: ")

    def mostrar_menu_gestion(self, tipo_entidad):
        print(f"\n--- Gestión de {tipo_entidad} ---")
        print(f"1. Crear {tipo_entidad[:-1]}") # Elimina la 's' al final
        print(f"2. Ver todos los {tipo_entidad}")
        print(f"3. Actualizar {tipo_entidad[:-1]}")
        print(f"4. Eliminar {tipo_entidad[:-1]}")
        print("5. Volver al Menú Principal")
        return input("Seleccione una opción: ")

    # --- Entradas de usuario para Autores ---
    def pedir_datos_nuevo_autor(self):
        nombre = input("Ingrese el nombre del autor: ")
        apellido = input("Ingrese el apellido del autor: ")
        return nombre, apellido

    def pedir_id_autor(self):
        try:
            return int(input("Ingrese el ID del autor: "))
        except ValueError:
            self.mostrar_error("ID de autor inválido. Debe ser un número entero.")
            return None

    def pedir_datos_actualizar_autor(self):
        nuevo_nombre = input("Ingrese el nuevo nombre del autor (dejar en blanco para no cambiar): ")
        nuevo_apellido = input("Ingrese el nuevo apellido del autor (dejar en blanco para no cambiar): ")
        return nuevo_nombre if nuevo_nombre else None, nuevo_apellido if nuevo_apellido else None

    def mostrar_autores(self, autores):
        if not autores:
            self.mostrar_mensaje("No hay autores registrados.")
            return
        print("\n--- Lista de Autores ---")
        for autor in autores:
            print(f"ID: {autor.id}, Nombre: {autor.nombre} {autor.apellido}")

    # --- Entradas de usuario para Géneros ---
    def pedir_datos_nuevo_genero(self):
        return input("Ingrese el nombre del género: ")

    def pedir_id_genero(self):
        try:
            return int(input("Ingrese el ID del género: "))
        except ValueError:
            self.mostrar_error("ID de género inválido. Debe ser un número entero.")
            return None

    def pedir_datos_actualizar_genero(self):
        return input("Ingrese el nuevo nombre del género: ")

    def mostrar_generos(self, generos):
        if not generos:
            self.mostrar_mensaje("No hay géneros registrados.")
            return
        print("\n--- Lista de Géneros ---")
        for genero in generos:
            print(f"ID: {genero.id}, Nombre: {genero.nombre}")

    # --- Entradas de usuario para Libros ---
    def pedir_datos_nuevo_libro(self):
        titulo = input("Ingrese el título del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")
        autor_id = self.pedir_id_autor()
        genero_id = self.pedir_id_genero()
        fecha_publicacion_str = input("Ingrese la fecha de publicación (YYYY-MM-DD, dejar en blanco para hoy): ")
        return titulo, isbn, autor_id, genero_id, fecha_publicacion_str

    def pedir_id_libro(self):
        try:
            return int(input("Ingrese el ID del libro: "))
        except ValueError:
            self.mostrar_error("ID de libro inválido. Debe ser un número entero.")
            return None

    def pedir_datos_actualizar_libro(self):
        nuevo_titulo = input("Ingrese el nuevo título del libro (dejar en blanco para no cambiar): ")
        nuevo_isbn = input("Ingrese el nuevo ISBN del libro (dejar en blanco para no cambiar): ")
        nuevo_autor_id = input("Ingrese el nuevo ID de autor (dejar en blanco para no cambiar): ")
        nuevo_genero_id = input("Ingrese el nuevo ID de género (dejar en blanco para no cambiar): ")
        nueva_fecha_publicacion_str = input("Ingrese la nueva fecha de publicación (YYYY-MM-DD, dejar en blanco para no cambiar): ")

        return (
            nuevo_titulo if nuevo_titulo else None,
            nuevo_isbn if nuevo_isbn else None,
            int(nuevo_autor_id) if nuevo_autor_id.isdigit() else None,
            int(nuevo_genero_id) if nuevo_genero_id.isdigit() else None,
            nueva_fecha_publicacion_str if nueva_fecha_publicacion_str else None
        )

    def mostrar_libros(self, libros):
        if not libros:
            self.mostrar_mensaje("No hay libros registrados.")
            return
        print("\n--- Lista de Libros ---")
        for libro in libros:
            autor_nombre = libro.autor.nombre if libro.autor else 'N/A'
            autor_apellido = libro.autor.apellido if libro.autor else ''
            genero_nombre = libro.genero.nombre if libro.genero else 'N/A'
            fecha_publicacion = libro.fecha_publicacion.strftime("%Y-%m-%d") if libro.fecha_publicacion else 'N/A'
            print(f"ID: {libro.id}, Título: {libro.titulo}, ISBN: {libro.isbn}, "
                  f"Autor: {autor_nombre} {autor_apellido}, Género: {genero_nombre}, "
                  f"Fecha Pub.: {fecha_publicacion}")