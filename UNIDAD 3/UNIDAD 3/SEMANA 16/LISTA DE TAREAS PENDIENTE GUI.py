import tkinter as tk
from tkinter import messagebox



# Funciones de la Aplicación

def crear_tarea(event=None):
    """Obtiene el texto del campo y lo añade a la lista."""
    nueva_tarea = campo_entrada.get()

    if len(nueva_tarea.strip()) > 0:
        visor_tareas.insert(tk.END, nueva_tarea)
        campo_entrada.delete(0, tk.END)
    else:
        messagebox.showinfo("Campo vacío", "Por favor, escribe una tarea antes de añadirla.")


def marcar_hecho(event=None):
    """Modifica la tarea para indicar que está lista."""
    seleccion = visor_tareas.curselection()

    if seleccion:
        indice = seleccion[0]
        texto_tarea = visor_tareas.get(indice)

        # Comprobamos que no esté marcada ya
        if not texto_tarea.startswith("✔️ "):
            visor_tareas.delete(indice)
            # Modificamos el texto y lo volvemos a insertar
            visor_tareas.insert(indice, f"✔️ {texto_tarea}")
            # Feedback visual alternativo: Fondo verde claro y texto oscuro
            visor_tareas.itemconfig(indice, {'bg': '#d4edda', 'fg': '#155724'})
            visor_tareas.select_set(indice)


def quitar_tarea(event=None):
    """Borra el elemento que esté seleccionado en la lista."""
    seleccion = visor_tareas.curselection()
    if seleccion:
        visor_tareas.delete(seleccion[0])


def salir_programa(event=None):
    """Termina la ejecución de la interfaz."""
    raiz.destroy()



# Configuración Principal

raiz = tk.Tk()
raiz.title("Lista de Tareas - Proyecto")
raiz.geometry("500x450")
raiz.config(bg="#f4f4f4", padx=15, pady=15)


# Creación y Posicionamiento de Widgets

# Sección superior: Entrada y botón de añadir
frame_superior = tk.Frame(raiz, bg="#f4f4f4")
frame_superior.pack(fill=tk.X, pady=(0, 10))

tk.Label(frame_superior, text="Nueva tarea:", bg="#f4f4f4", font=("Helvetica", 10, "bold")).pack(side=tk.LEFT)

campo_entrada = tk.Entry(frame_superior, width=30, font=("Helvetica", 12))
campo_entrada.pack(side=tk.LEFT, padx=10)

boton_crear = tk.Button(frame_superior, text="Añadir", bg="#007bff", fg="white", command=crear_tarea)
boton_crear.pack(side=tk.LEFT)

# Sección central: Lista de tareas
visor_tareas = tk.Listbox(raiz, font=("Helvetica", 12), height=12, selectbackground="#007bff")
visor_tareas.pack(fill=tk.BOTH, expand=True)

# Sección inferior: Botones de control
frame_inferior = tk.Frame(raiz, bg="#f4f4f4")
frame_inferior.pack(fill=tk.X, pady=(10, 0))

boton_hecho = tk.Button(frame_inferior, text="Marcar como Completada", bg="#28a745", fg="white", command=marcar_hecho)
boton_hecho.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

boton_quitar = tk.Button(frame_inferior, text="Eliminar Tarea", bg="#dc3545", fg="white", command=quitar_tarea)
boton_quitar.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=(5, 0))


# Configuración de Atajos de Teclado

campo_entrada.bind('<Return>', crear_tarea)
raiz.bind('<c>', marcar_hecho)
raiz.bind('<C>', marcar_hecho)
raiz.bind('<Delete>', quitar_tarea)
raiz.bind('<d>', quitar_tarea)
raiz.bind('<D>', quitar_tarea)
raiz.bind('<Escape>', salir_programa)

# Arranque de la aplicación
raiz.mainloop()