import tkinter as tk
from tkinter import ttk, messagebox


# LÓGICA DE LA APLICACIÓN Y MANEJO DE EVENTOS


def agregar_tarea(event=None):
    """
    Extrae el texto del Entry y lo inserta en el Treeview.
    Se enlaza al botón y a la tecla Enter.
    """
    texto_tarea = entrada_tarea.get().strip()
    if texto_tarea:
        # Se inserta en el Treeview. 'values' espera una tupla, por eso la coma.
        arbol_tareas.insert('', tk.END, values=(texto_tarea,))
        entrada_tarea.delete(0, tk.END) # Limpiamos la caja de texto
    else:
        messagebox.showwarning("Campo Vacío", "Escribe una descripción para la tarea.")

def marcar_completada(event=None):
    """
    Utiliza el sistema de 'tags' del Treeview para cambiar el color de la fila,
    indicando visualmente que la tarea está terminada.
    """
    seleccion = arbol_tareas.selection()
    if seleccion:
        item = seleccion[0]
        # Se asigna la etiqueta 'completada' al elemento seleccionado
        arbol_tareas.item(item, tags=('completada',))
    else:
        messagebox.showinfo("Aviso", "Selecciona una tarea de la lista para completarla.")

def eliminar_tarea(event=None):
    """
    Elimina del Treeview el elemento que esté seleccionado.
    Responde tanto al botón de la interfaz como a la tecla 'Suprimir'.
    """
    seleccion = arbol_tareas.selection()
    if seleccion:
        for item in seleccion:
            arbol_tareas.delete(item)
    else:
        messagebox.showinfo("Aviso", "Selecciona una tarea para poder eliminarla.")


#
# CONFIGURACIÓN DE LA INTERFAZ GRÁFICA (GUI)
#

# 1. Configuración principal de la ventana
ventana = tk.Tk()
ventana.title("Mis Tareas Pendientes")
ventana.geometry("450x450")

# Uso de un Frame principal con padding para mejorar el diseño
# Decisión de diseño: Usar 'grid' en lugar de 'pack' permite alinear elementos como en una tabla.
marco_principal = ttk.Frame(ventana, padding="15")
marco_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# 2. Área de Entrada de Tareas
entrada_tarea = ttk.Entry(marco_principal, font=("Helvetica", 11))
entrada_tarea.grid(row=0, column=0, padx=(0, 10), pady=10, sticky=(tk.W, tk.E))
# Evento: Presionar Enter añade la tarea
entrada_tarea.bind("<Return>", agregar_tarea)

btn_agregar = ttk.Button(marco_principal, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.grid(row=0, column=1, pady=10)

# 3. Componente de Lista (Treeview en lugar de Listbox)
# Decisión de diseño: Treeview luce más estructurado y permite columnas si el proyecto crece en el futuro.
columnas = ('Tarea',)
arbol_tareas = ttk.Treeview(marco_principal, columns=columnas, show='headings', selectmode='browse')
arbol_tareas.heading('Tarea', text='Descripción de la Tarea')
arbol_tareas.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

# Configuración visual para las tareas completadas (Fondo verde claro, texto gris)
arbol_tareas.tag_configure('completada', background='#d4edda', foreground='#6c757d')

# Scrollbar para el Treeview
scrollbar = ttk.Scrollbar(marco_principal, orient=tk.VERTICAL, command=arbol_tareas.yview)
arbol_tareas.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=2, sticky=(tk.N, tk.S), pady=5)

# Ajuste de expansión de la grilla
marco_principal.rowconfigure(1, weight=1)
marco_principal.columnconfigure(0, weight=1)

# Eventos adicionales (Requisito opcional)
arbol_tareas.bind("<Double-1>", marcar_completada) # Doble clic izquierdo completa la tarea
arbol_tareas.bind("<Delete>", eliminar_tarea)      # Tecla Suprimir (Del) elimina la tarea

# 4. Botones de Acción
marco_botones = ttk.Frame(marco_principal)
marco_botones.grid(row=2, column=0, columnspan=2, pady=15)

btn_completar = ttk.Button(marco_botones, text="✓ Completar", command=marcar_completada)
btn_completar.grid(row=0, column=0, padx=10)

btn_eliminar = ttk.Button(marco_botones, text="✗ Eliminar", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=1, padx=10)

# Iniciar la aplicación
ventana.mainloop()