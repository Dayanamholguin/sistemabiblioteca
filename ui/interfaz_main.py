import tkinter as tk
from tkinter import LabelFrame
from ui.vista_libros import *
from ui.vista_usuarios import *
from ui.vista_prestamos import *
from biblioteca import Biblioteca

class InterfazBiblioteca:
    def __init__(self, root):
        self.biblio = Biblioteca()
        self.root = root
        
        # Contenedor principal
        self.main_frame = tk.Frame(root, padx=20, pady=20, bg="#f0f0f0")
        self.main_frame.pack(fill="both", expand=True)

        # Título
        tk.Label(self.main_frame, text="Sistema de Gestión de Biblioteca",
                font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=(0, 20))

        # Sección para la gestión de libros
        libros_frame = LabelFrame(self.main_frame, text="Libros", padx=10, pady=10)
        libros_frame.pack(fill="x", pady=5)
        
        tk.Button(libros_frame, text="Agregar Libro", command=lambda: agregar_libro(self.biblio, root)).pack(pady=2)
        tk.Button(libros_frame, text="Ver Libros", command=lambda: ver_libros(self.biblio, root)).pack(pady=2)
        tk.Button(libros_frame, text="Buscar Libro", command=lambda: buscar_libro(self.biblio, root)).pack(pady=2)

        # Sección para la gestión de usuarios
        usuarios_frame = LabelFrame(self.main_frame, text="Usuarios", padx=10, pady=10)
        usuarios_frame.pack(fill="x", pady=5)
        
        tk.Button(usuarios_frame, text="Agregar Usuario", command=lambda: agregar_usuario(self.biblio, root)).pack(pady=2)
        tk.Button(usuarios_frame, text="Ver Usuarios", command=lambda: ver_usuarios(self.biblio, root)).pack(pady=2)
        tk.Button(usuarios_frame, text="Buscar Usuario", command=lambda: buscar_usuario(self.biblio, root)).pack(pady=2)
        tk.Button(usuarios_frame, text="Ver Libros Prestados", command=lambda: ver_libros_usuario(self.biblio, root)).pack(pady=2)

        # Sección para la gestión de préstamos
        prestamos_frame = LabelFrame(self.main_frame, text="Gestín de Préstamos", padx=10, pady=10)
        prestamos_frame.pack(fill="x", pady=5)
        
        tk.Button(prestamos_frame, text="Prestar Libro", command=lambda: prestar_libro(self.biblio, root)).pack(pady=2)
        tk.Button(prestamos_frame, text="Devolver Libro", command=lambda: devolver_libro(self.biblio, root)).pack(pady=2)
        tk.Button(prestamos_frame, text="Ver Historial de Préstamos", command=lambda: ver_historial(self.biblio, root)).pack(pady=2)


        # Centrado automático de la ventana
        root.update_idletasks()

        ancho_ventana = root.winfo_width()
        alto_ventana = root.winfo_height()
        
        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()
        
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2 - 50
        
        root.geometry(f"+{x}+{y}")