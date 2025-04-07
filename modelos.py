# Definición de la clase Libro
# Esta clase representa un libro en la biblioteca.
class Libro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

# Definición de la clase Usuario
# Esta clase representa a un usuario del sistema de biblioteca.
class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.historial = []