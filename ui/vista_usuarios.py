import tkinter as tk
from tkinter import messagebox, ttk
from modelos import Usuario

# Función para agregar un nuevo usuario
def agregar_usuario(biblio, root):
    def guardar():
        id = entrada_id.get()
        nombre = entrada_nombre.get()
        if id and nombre:
            biblio.agregar_usuario(Usuario(id, nombre))
            messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
            ventana.destroy()
        else:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")

    ventana = tk.Toplevel(root)
    ventana.title("Agregar Usuario")
    ventana.geometry("300x200")

    frame = tk.LabelFrame(ventana, text="Datos del Usuario", padx=10, pady=10)
    frame.pack(padx=15, pady=15, fill="both", expand=True)

    tk.Label(frame, text="ID:").pack(anchor="w")
    entrada_id = tk.Entry(frame, width=30)
    entrada_id.pack()

    tk.Label(frame, text="Nombre:").pack(anchor="w", pady=(10, 0))
    entrada_nombre = tk.Entry(frame, width=30)
    entrada_nombre.pack()

    tk.Button(frame, text="Guardar", command=guardar, width=20).pack(pady=5)

# Función para ver todos los usuarios registrados
def ver_usuarios(biblio, root):
    ventana = tk.Toplevel(root)
    ventana.title("Usuarios Registrados")
    ventana.geometry("600x300")

    frame = tk.LabelFrame(ventana, text="Usuarios en el sistema", padx=10, pady=10)
    frame.pack(padx=10, pady=10, fill="both", expand=True)

    columnas = ("id", "nombre", "libros")
    tabla = ttk.Treeview(frame, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col.capitalize())
    tabla.column("id", width=100, anchor="center")
    tabla.column("nombre", width=200, anchor="center")
    tabla.column("libros", width=250, anchor="center")

    for usuario in biblio.usuarios:
        libros = ", ".join([libro.titulo for libro in usuario.historial]) or "Ninguno"
        tabla.insert("", "end", values=(usuario.id, usuario.nombre, libros))

    tabla.pack(fill="both", expand=True)

# Función para buscar un usuario por ID o nombre
def buscar_usuario(biblio, root):
    def buscar():
        criterio = entrada.get().lower()
        resultados = [usuario for usuario in biblio.usuarios if criterio in usuario.nombre.lower() or criterio == usuario.id]

        resultado = tk.Toplevel(root)
        resultado.title("Resultado de Búsqueda de Usuario")
        resultado.geometry("600x300")

        frame_resultado = tk.LabelFrame(resultado, text="Resultado", padx=10, pady=10)
        frame_resultado.pack(padx=15, pady=15, fill="both", expand=True)

        columnas = ("id", "nombre", "libros")
        tabla = ttk.Treeview(frame_resultado, columns=columnas, show="headings")
        for col in columnas:
            tabla.heading(col, text=col.capitalize())
        tabla.column("id", width=100, anchor="center")
        tabla.column("nombre", width=200, anchor="center")
        tabla.column("libros", width=250, anchor="center")

        if resultados:
            for usuario in resultados:
                libros = ", ".join([libro.titulo for libro in usuario.historial]) or "Ninguno"
                tabla.insert("", "end", values=(usuario.id, usuario.nombre, libros))
        else:
            tabla.insert("", "end", values=("—", "No se encontraron resultados", ""))

        tabla.pack(fill="both", expand=True)
        ventana.destroy()

    ventana = tk.Toplevel(root)
    ventana.title("Buscar Usuario")
    ventana.geometry("300x150")

    frame = tk.LabelFrame(ventana, text="Buscar por ID o Nombre", padx=10, pady=10)
    frame.pack(padx=15, pady=15, fill="both", expand=True)

    entrada = tk.Entry(frame, width=30)
    entrada.pack(pady=5)
    tk.Button(frame, text="Buscar", command=buscar, width=20).pack(pady=5)