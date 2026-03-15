import tkinter as tk
from tkinter import messagebox


class GestorBibliotecaGUI:
    def __init__(self, master):
        """
        Constructor que inicializa la ventana principal y los widgets.
        """
        self.master = master
        # Requisito: Título descriptivo
        self.master.title("Gestor de Biblioteca - Registro de Libros")
        self.master.geometry("450x450")
        self.master.config(padx=20, pady=20)

        # --- Requisito: Diseño de la Interfaz ---

        # Etiqueta para el campo de entrada
        self.lbl_titulo = tk.Label(master, text="Título del Libro o Material:", font=("Helvetica", 11, "bold"))
        self.lbl_titulo.pack(anchor="w", pady=(0, 5))

        # Campo de texto para ingresar el libro
        self.entry_libro = tk.Entry(master, width=45, font=("Helvetica", 10))
        self.entry_libro.pack(fill="x", pady=(0, 15))

        # Contenedor para los botones
        self.frame_acciones = tk.Frame(master)
        self.frame_acciones.pack(pady=(0, 15))

        # Requisito: Botón "Agregar"
        self.btn_registrar = tk.Button(self.frame_acciones, text="Registrar Libro", bg="#2196F3", fg="white",
                                       font=("Helvetica", 10), command=self.registrar_libro)
        self.btn_registrar.pack(side=tk.LEFT, padx=10)

        # Requisito: Botón "Limpiar"
        self.btn_eliminar = tk.Button(self.frame_acciones, text="Eliminar Selección", bg="#FF9800", fg="white",
                                      font=("Helvetica", 10), command=self.eliminar_registro)
        self.btn_eliminar.pack(side=tk.LEFT, padx=10)

        # Etiqueta para la lista de libros
        self.lbl_inventario = tk.Label(master, text="Inventario Actual:", font=("Helvetica", 11, "bold"))
        self.lbl_inventario.pack(anchor="w", pady=(10, 5))

        # Requisito: Lista (Listbox) para mostrar los datos
        self.lista_libros = tk.Listbox(master, width=50, height=10, font=("Helvetica", 10))
        self.lista_libros.pack(fill="both", expand=True)

    # --- Requisito: Eventos y Funcionalidad ---

    def registrar_libro(self):
        """
        Toma el texto del Entry y lo inserta en el Listbox.
        Verifica que no se ingresen datos vacíos.
        """
        nuevo_libro = self.entry_libro.get()

        # Validación básica para no agregar cadenas vacías
        if nuevo_libro.strip() != "":
            self.lista_libros.insert(tk.END, f"📚 {nuevo_libro}")
            self.entry_libro.delete(0, tk.END)  # Limpia el campo después de agregar
        else:
            messagebox.showwarning("Atención", "Por favor, ingrese el título de un libro antes de registrar.")

    def eliminar_registro(self):
        """
        Elimina el libro que el usuario haya seleccionado en la lista.
        También limpia el campo de texto superior.
        """
        # Limpiar el campo de texto
        self.entry_libro.delete(0, tk.END)

        # Obtener el índice seleccionado y borrarlo
        seleccion = self.lista_libros.curselection()
        if seleccion:
            self.lista_libros.delete(seleccion)
        else:
            messagebox.showinfo("Información", "Seleccione un libro de la lista para eliminarlo.")


# Ejecución principal del programa
if __name__ == "__main__":
    raiz = tk.Tk()
    app = GestorBibliotecaGUI(raiz)
    raiz.mainloop()