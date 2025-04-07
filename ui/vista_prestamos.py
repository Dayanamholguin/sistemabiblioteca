import tkinter as tk
from tkinter import messagebox, ttk

# Función para prestar un libro
def prestar_libro(biblio, root):
    if not biblio.libros or not biblio.usuarios:
        messagebox.showerror("Error", "Debe haber al menos un libro y un usuario registrados.")
        return

    libros_disponibles = [libro for libro in biblio.libros if libro.disponible]
    if not libros_disponibles:
        messagebox.showwarning("Sin libros", "No hay libros disponibles para prestar.")
        return

    ventana = tk.Toplevel(root)
    ventana.title("Prestar Libro")
    ventana.geometry("350x250")

    frame = tk.LabelFrame(ventana, text="Datos para el Préstamo", padx=10, pady=10)
    frame.pack(padx=15, pady=15, fill="both", expand=True)

    tk.Label(frame, text="Seleccione Libro:").pack(anchor="w")
    libro_var = tk.StringVar()
    libro_var.set(f"{libros_disponibles[0].titulo} ({libros_disponibles[0].id})")
    opciones_libros = [f"{libro.titulo} ({libro.id})" for libro in libros_disponibles]
    tk.OptionMenu(frame, libro_var, *opciones_libros).pack(fill="x", pady=5)

    tk.Label(frame, text="Seleccione Usuario:").pack(anchor="w")
    usuario_var = tk.StringVar()
    usuario_var.set(f"{biblio.usuarios[0].nombre} ({biblio.usuarios[0].id})")
    opciones_usuarios = [f"{usuario.nombre} ({usuario.id})" for usuario in biblio.usuarios]
    tk.OptionMenu(frame, usuario_var, *opciones_usuarios).pack(fill="x", pady=5)

    def prestar():
        id_libro = libro_var.get().split("(")[-1].strip(")")
        id_usuario = usuario_var.get().split("(")[-1].strip(")")
        if biblio.prestar_libro(id_libro, id_usuario):
            messagebox.showinfo("Éxito", "Libro prestado correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo prestar el libro.")
        ventana.destroy()

    tk.Button(frame, text="Confirmar Préstamo", command=prestar, width=25).pack(pady=10)

# Función para devolver un libro
def devolver_libro(biblio, root):
    if not biblio.usuarios:
        messagebox.showerror("Error", "No hay usuarios registrados.")
        return

    ventana = tk.Toplevel(root)
    ventana.title("Devolver Libro")
    ventana.geometry("350x250")

    frame = tk.LabelFrame(ventana, text="Devolución de Libro", padx=10, pady=10)
    frame.pack(padx=15, pady=15, fill="both", expand=True)

    tk.Label(frame, text="Seleccione Usuario:").pack(anchor="w")
    usuario_var = tk.StringVar()
    usuario_var.set(f"{biblio.usuarios[0].nombre} ({biblio.usuarios[0].id})")
    opciones_usuarios = [f"{u.nombre} ({u.id})" for u in biblio.usuarios]
    tk.OptionMenu(frame, usuario_var, *opciones_usuarios).pack(fill="x", pady=5)

    libro_var = tk.StringVar()
    libros_menu = None
    opciones_libros = []

    def actualizar_libros():
        nonlocal libros_menu
        id_usuario = usuario_var.get().split("(")[-1].strip(")")
        usuario = next((u for u in biblio.usuarios if u.id == id_usuario), None)

        if usuario and usuario.historial:
            opciones_libros.clear()
            opciones_libros.extend([f"{libro.titulo} ({libro.id})" for libro in usuario.historial])
            libro_var.set(opciones_libros[0])

            if libros_menu:
                libros_menu['menu'].delete(0, 'end')
                for op in opciones_libros:
                    libros_menu['menu'].add_command(label=op, command=tk._setit(libro_var, op))
        else:
            libro_var.set("")
            if libros_menu:
                libros_menu['menu'].delete(0, 'end')
                libros_menu['menu'].add_command(label="Sin libros prestados", command=tk._setit(libro_var, ""))

    usuario_var.trace_add("write", actualizar_libros)

    tk.Label(frame, text="Seleccione Libro a devolver:").pack(anchor="w")
    libro_var.set("")
    libros_menu = tk.OptionMenu(frame, libro_var, "")
    libros_menu.pack(fill="x", pady=5)

    actualizar_libros()

    def devolver():
        id_usuario = usuario_var.get().split("(")[-1].strip(")")
        id_libro = libro_var.get().split("(")[-1].strip(")") if libro_var.get() else None

        if not id_libro:
            messagebox.showwarning("Advertencia", "Este usuario no tiene libros prestados.")
            return

        if biblio.devolver_libro(id_libro, id_usuario):
            messagebox.showinfo("Éxito", "Libro devuelto correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo devolver el libro.")
        ventana.destroy()

    tk.Button(frame, text="Confirmar Devolución", command=devolver, width=25).pack(pady=10)

# Función para ver el historial de prestamos
def ver_historial(biblio, root):
    ventana = tk.Toplevel(root)
    ventana.title("Historial de Préstamos")
    ventana.geometry("650x300")

    frame = tk.LabelFrame(ventana, text="Historial completo", padx=10, pady=10)
    frame.pack(padx=10, pady=10, fill="both", expand=True)

    columnas = ("usuario", "libro", "estado")
    tabla = ttk.Treeview(frame, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col.capitalize())
    tabla.column("usuario", width=200, anchor="center")
    tabla.column("libro", width=300, anchor="center")
    tabla.column("estado", width=100, anchor="center")

    for usuario, libro in biblio.prestamos:
        estado = "Prestado" if not libro.disponible else "Devuelto"
        tabla.insert("", "end", values=(usuario.nombre, libro.titulo, estado))

    tabla.pack(fill="both", expand=True)

# Función para ver los libros prestados a un usuario
def ver_libros_usuario(biblio, root):
    if not biblio.usuarios:
        messagebox.showwarning("Sin usuarios", "No hay usuarios registrados.")
        return

    ventana = tk.Toplevel(root)
    ventana.title("Libros Prestados por Usuario")
    ventana.geometry("600x350")

    frame = tk.LabelFrame(ventana, text="Seleccionar Usuario", padx=10, pady=10)
    frame.pack(padx=10, pady=10, fill="x")

    usuario_var = tk.StringVar()
    usuario_var.set(f"{biblio.usuarios[0].nombre} ({biblio.usuarios[0].id})")
    opciones_usuarios = [f"{u.nombre} ({u.id})" for u in biblio.usuarios]
    tk.OptionMenu(frame, usuario_var, *opciones_usuarios).pack(fill="x")

    resultado_frame = tk.LabelFrame(ventana, text="Libros Prestados", padx=10, pady=10)
    resultado_frame.pack(padx=10, pady=10, fill="both", expand=True)

    columnas = ("id", "titulo", "autor")
    tabla = ttk.Treeview(resultado_frame, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col.capitalize())
    tabla.column("id", width=80, anchor="center")
    tabla.column("titulo", width=300, anchor="center")
    tabla.column("autor", width=200, anchor="center")
    tabla.pack(fill="both", expand=True)

    def mostrar():
        for row in tabla.get_children():
            tabla.delete(row)

        id_usuario = usuario_var.get().split("(")[-1].strip(")")
        usuario = next((u for u in biblio.usuarios if u.id == id_usuario), None)

        if usuario and usuario.historial:
            for libro in usuario.historial:
                tabla.insert("", "end", values=(libro.id, libro.titulo, libro.autor))
        else:
            messagebox.showinfo("Información", "Este usuario no tiene libros prestados.")

    tk.Button(frame, text="Ver Libros", command=mostrar).pack(pady=10)