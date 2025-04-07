# Uso de estructuras de datos lineales:
# - Listas: para almacenar libros y usuarios (estructura indexada y ordenada)
# - Cola (simulada con lista): para registrar el historial de préstamos
# - Pila (simulada con lista): para manter el historial individual de libros prestados a cada usuario

import tkinter as tk
from ui.interfaz_main import InterfazBiblioteca

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Gestión de Biblioteca")
    app = InterfazBiblioteca(root)
    root.mainloop()
