import tkinter as tk
from tkinter import messagebox, ttk
from modelos import Libro

# Función para agregar un nuevo libro
def agregar_libro(biblio, root):
    def guardar():
        id = entrada_id.get()
        titulo = entrada_titulo.get()
        autor = entrada_autor.get()
        if id and titulo and autor:
            biblio.agregar_libro(Libro(id, titulo, autor))
            messagebox.showinfo("Éxito", "Libro agregado correctamente.")
            ventana.destroy()
        else:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")

    ventana = tk.Toplevel(root)
    ventana.title("Agregar Libro")
    ventana.geometry("300x250")

    frame = tk.LabelFrame(ventana, text="Datos del Libro", padx=10, pady=10)
    frame.pack(padx=15, pady=15, fill="both", expand=True)

    tk.Label(frame, text="ID:").pack(anchor="w")
    entrada_id = tk.Entry(frame, width=30)
    entrada_id.pack()

    tk.Label(frame, text="Título:").pack(anchor="w", pady=(10, 0))
    entrada_titulo = tk.Entry(frame, width=30)
    entrada_titulo.pack()

    tk.Label(frame, text="Autor:").pack(anchor="w", pady=(10, 0))
    entrada_autor = tk.Entry(frame, width=30)
    entrada_autor.pack()

    tk.Button(frame, text="Guardar", command=guardar, width=20).pack(pady=5)

# Función para ver todos los libros registrados
def ver_libros(biblio, root):
    ventana = tk.Toplevel(root)
    ventana.title("Libros Registrados")
    ventana.geometry("600x300")

    frame = tk.LabelFrame(ventana, text="Libros en el sistema", padx=10, pady=10)
    frame.pack(padx=10, pady=10, fill="both", expand=True)

    columnas = ("id", "titulo", "autor", "estado")
    tabla = ttk.Treeview(frame, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col.capitalize())
    tabla.column("id", width=80, anchor="center")
    tabla.column("titulo", width=200, anchor="center")
    tabla.column("autor", width=150, anchor="center")
    tabla.column("estado", width=100, anchor="center")

    for libro in biblio.libros:
        estado = "Disponible" if libro.disponible else "Prestado"
        tabla.insert("", "end", values=(libro.id, libro.titulo, libro.autor, estado))

    tabla.pack(fill="both", expand=True)

# Función para buscar un libro por ID o título
def buscar_libro(biblio, root):
    def buscar():
        criterio = entrada.get().lower()
        resultados = [libro for libro in biblio.libros if criterio in libro.titulo.lower() or criterio == libro.id]

        resultado = tk.Toplevel(root)
        resultado.title("Resultado de Búsqueda de Libro")
        resultado.geometry("600x300")

        frame_resultado = tk.LabelFrame(resultado, text="Resultado", padx=10, pady=10)
        frame_resultado.pack(padx=15, pady=15, fill="both", expand=True)

        columnas = ("id", "titulo", "autor", "estado")
        tabla = ttk.Treeview(frame_resultado, columns=columnas, show="headings")
        for col in columnas:
            tabla.heading(col, text=col.capitalize())
        tabla.column("id", width=80, anchor="center")
        tabla.column("titulo", width=200, anchor="center")
        tabla.column("autor", width=150, anchor="center")
        tabla.column("estado", width=100, anchor="center")

        if resultados:
            for libro in resultados:
                estado = "Disponible" if libro.disponible else "Prestado"
                tabla.insert("", "end", values=(libro.id, libro.titulo, libro.autor, estado))
        else:
            tabla.insert("", "end", values=("—", "No se encontraron resultados", "", ""))

        tabla.pack(fill="both", expand=True)
        ventana.destroy()

    ventana = tk.Toplevel(root)
    ventana.title("Buscar Libro")
    ventana.geometry("300x150")

    frame = tk.LabelFrame(ventana, text="Buscar por ID o Título", padx=10, pady=10)
    frame.pack(padx=15, pady=15, fill="both", expand=True)

    entrada = tk.Entry(frame, width=30)
    entrada.pack(pady=5)
    tk.Button(frame, text="Buscar", command=buscar, width=20).pack(pady=5)