# Clase Biblioteca que gestiona los datos y operaciones del sistema
class Biblioteca:
    def __init__(self):
        # Lista de libros registrados (estructura lineal)
        self.libros = []

        # Lista de usuarios registrados (estructura lineal)
        self.usuarios = []

        # Historial general de préstamos (estructura tipo cola simulada con lista)
        self.prestamos = []

    # Método para agregar un libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Método para agregar un usuario a la biblioteca
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    # Método para prestar un libro a un usuario
    def prestar_libro(self, id_libro, id_usuario):
        libro = next((l for l in self.libros if l.id == id_libro and l.disponible), None)
        usuario = next((u for u in self.usuarios if u.id == id_usuario), None)

        if libro and usuario:
            libro.disponible = False
            # Historial del usuario como pila
            usuario.historial.append(libro)
            # Agrega al historial global como cola
            self.prestamos.append((usuario, libro))
            return True
        return False

    # Método para devolver un libro
    def devolver_libro(self, id_libro, id_usuario):
        usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
        if usuario:
            for libro in usuario.historial:
                if libro.id == id_libro:
                    libro.disponible = True
                    usuario.historial.remove(libro)
                    return True
        return False