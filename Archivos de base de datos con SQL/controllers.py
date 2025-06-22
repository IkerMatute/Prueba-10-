# controllers.py
from models import Session, Autor, Genero, Libro
import datetime

class BibliotecaController:
    def __init__(self):
        self.session = Session()

    # --- Operaciones para Autores ---
    def crear_autor(self, nombre, apellido):
        try:
            nuevo_autor = Autor(nombre=nombre, apellido=apellido)
            self.session.add(nuevo_autor)
            self.session.commit()
            return nuevo_autor
        except Exception as e:
            self.session.rollback()
            print(f"Error al crear autor: {e}")
            return None

    def obtener_autores(self):
        return self.session.query(Autor).all()

    def obtener_autor_por_id(self, autor_id):
        return self.session.query(Autor).get(autor_id)

    def actualizar_autor(self, autor_id, nuevo_nombre=None, nuevo_apellido=None):
        autor = self.obtener_autor_por_id(autor_id)
        if autor:
            try:
                if nuevo_nombre:
                    autor.nombre = nuevo_nombre
                if nuevo_apellido:
                    autor.apellido = nuevo_apellido
                self.session.commit()
                return True
            except Exception as e:
                self.session.rollback()
                print(f"Error al actualizar autor: {e}")
                return False
        return False

    def eliminar_autor(self, autor_id):
        autor = self.obtener_autor_por_id(autor_id)
        if autor:
            try:
                self.session.delete(autor)
                self.session.commit()
                return True
            except Exception as e:
                self.session.rollback()
                print(f"Error al eliminar autor: {e}")
                return False
        return False

    # --- Operaciones para Géneros ---
    def crear_genero(self, nombre):
        try:
            nuevo_genero = Genero(nombre=nombre)
            self.session.add(nuevo_genero)
            self.session.commit()
            return nuevo_genero
        except Exception as e:
            self.session.rollback()
            print(f"Error al crear género: {e}")
            return None

    def obtener_generos(self):
        return self.session.query(Genero).all()

    def obtener_genero_por_id(self, genero_id):
        return self.session.query(Genero).get(genero_id)

    def actualizar_genero(self, genero_id, nuevo_nombre):
        genero = self.obtener_genero_por_id(genero_id)
        if genero:
            try:
                genero.nombre = nuevo_nombre
                self.session.commit()
                return True
            except Exception as e:
                self.session.rollback()
                print(f"Error al actualizar género: {e}")
                return False
        return False

    def eliminar_genero(self, genero_id):
        genero = self.obtener_genero_por_id(genero_id)
        if genero:
            try:
                self.session.delete(genero)
                self.session.commit()
                return True
            except Exception as e:
                self.session.rollback()
                print(f"Error al eliminar género: {e}")
                return False
        return False

    # --- Operaciones para Libros ---
    def crear_libro(self, titulo, isbn, autor_id, genero_id, fecha_publicacion_str=None):
        autor = self.obtener_autor_por_id(autor_id)
        genero = self.obtener_genero_por_id(genero_id)

        if not autor:
            print(f"Error: Autor con ID {autor_id} no encontrado.")
            return None
        if not genero:
            print(f"Error: Género con ID {genero_id} no encontrado.")
            return None

        fecha_publicacion = datetime.date.today()
        if fecha_publicacion_str:
            try:
                fecha_publicacion = datetime.datetime.strptime(fecha_publicacion_str, "%Y-%m-%d").date()
            except ValueError:
                print("Formato de fecha incorrecto. Usando la fecha actual.")

        try:
            nuevo_libro = Libro(
                titulo=titulo,
                isbn=isbn,
                fecha_publicacion=fecha_publicacion,
                autor=autor,
                genero=genero
            )
            self.session.add(nuevo_libro)
            self.session.commit()
            return nuevo_libro
        except Exception as e:
            self.session.rollback()
            print(f"Error al crear libro: {e}")
            return None

    def obtener_libros(self):
        return self.session.query(Libro).all()

    def obtener_libro_por_id(self, libro_id):
        return self.session.query(Libro).get(libro_id)

    def actualizar_libro(self, libro_id, nuevo_titulo=None, nuevo_isbn=None, nuevo_autor_id=None, nuevo_genero_id=None, nueva_fecha_publicacion_str=None):
        libro = self.obtener_libro_por_id(libro_id)
        if libro:
            try:
                if nuevo_titulo:
                    libro.titulo = nuevo_titulo
                if nuevo_isbn:
                    libro.isbn = nuevo_isbn
                if nuevo_autor_id:
                    nuevo_autor = self.obtener_autor_por_id(nuevo_autor_id)
                    if nuevo_autor:
                        libro.autor = nuevo_autor
                    else:
                        print(f"Advertencia: Autor con ID {nuevo_autor_id} no encontrado. No se actualizó el autor.")
                if nuevo_genero_id:
                    nuevo_genero = self.obtener_genero_por_id(nuevo_genero_id)
                    if nuevo_genero:
                        libro.genero = nuevo_genero
                    else:
                        print(f"Advertencia: Género con ID {nuevo_genero_id} no encontrado. No se actualizó el género.")
                if nueva_fecha_publicacion_str:
                    try:
                        libro.fecha_publicacion = datetime.datetime.strptime(nueva_fecha_publicacion_str, "%Y-%m-%d").date()
                    except ValueError:
                        print("Formato de fecha incorrecto para la actualización. No se actualizó la fecha.")

                self.session.commit()
                return True
            except Exception as e:
                self.session.rollback()
                print(f"Error al actualizar libro: {e}")
                return False
        return False

    def eliminar_libro(self, libro_id):
        libro = self.obtener_libro_por_id(libro_id)
        if libro:
            try:
                self.session.delete(libro)
                self.session.commit()
                return True
            except Exception as e:
                self.session.rollback()
                print(f"Error al eliminar libro: {e}")
                return False
        return False

    def cerrar_sesion(self):
        self.session.close()