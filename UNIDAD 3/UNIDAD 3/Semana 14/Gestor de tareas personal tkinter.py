import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class GestorDeTareas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi Agenda Diaria")
        self.ventana.geometry("650x500")
        self.ventana.config(bg="#f0f0f0")

        # ==========================================
        # SECCIÓN DE FORMULARIO
        # ==========================================
        self.panel_superior = tk.Frame(self.ventana, bg="#f0f0f0")
        self.panel_superior.pack(pady=20)

        # Campo: Fecha
        tk.Label(self.panel_superior, text="Seleccionar Fecha:", bg="#f0f0f0", font=("Arial", 10, "bold")).grid(row=0,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="e")
        self.selector_fecha = DateEntry(self.panel_superior, width=12, background='teal', foreground='white',
                                        borderwidth=2)
        self.selector_fecha.grid(row=0, column=1, padx=10, pady=10)

        # Campo: Hora
        tk.Label(self.panel_superior, text="Hora Asignada:", bg="#f0f0f0", font=("Arial", 10, "bold")).grid(row=0,
                                                                                                            column=2,
                                                                                                            padx=10,
                                                                                                            pady=10,
                                                                                                            sticky="e")
        self.caja_hora = tk.Entry(self.panel_superior, width=10)
        self.caja_hora.grid(row=0, column=3, padx=10, pady=10)

        # Campo: Descripción
        tk.Label(self.panel_superior, text="Detalle de la tarea:", bg="#f0f0f0", font=("Arial", 10, "bold")).grid(row=1,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="e")
        self.caja_detalle = tk.Entry(self.panel_superior, width=45)
        self.caja_detalle.grid(row=1, column=1, columnspan=3, padx=10, pady=10, sticky="w")

        # ==========================================
        # SECCIÓN DE BOTONES
        # ==========================================
        self.panel_medio = tk.Frame(self.ventana, bg="#f0f0f0")
        self.panel_medio.pack(pady=5)

        tk.Button(self.panel_medio, text="➕ Agregar Evento", command=self.guardar_registro, bg="#008CBA", fg="white",
                  font=("Arial", 10, "bold"), width=15).grid(row=0, column=0, padx=15)
        tk.Button(self.panel_medio, text="❌ Borrar Selección", command=self.quitar_registro, bg="#e74c3c", fg="white",
                  font=("Arial", 10, "bold"), width=15).grid(row=0, column=1, padx=15)
        tk.Button(self.panel_medio, text="🚪 Salir", command=self.cerrar_app, bg="#2c3e50", fg="white",
                  font=("Arial", 10, "bold"), width=15).grid(row=0, column=2, padx=15)

        # ==========================================
        # SECCIÓN DE TABLA (TREEVIEW)
        # ==========================================
        self.panel_inferior = tk.Frame(self.ventana)
        self.panel_inferior.pack(pady=15, fill="both", expand=True, padx=20)

        estilo = ttk.Style()
        estilo.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        self.tabla_eventos = ttk.Treeview(self.panel_inferior, columns=("col_fecha", "col_hora", "col_desc"),
                                          show="headings")

        self.tabla_eventos.heading("col_fecha", text="Fecha Programada")
        self.tabla_eventos.column("col_fecha", width=120, anchor="center")

        self.tabla_eventos.heading("col_hora", text="Hora")
        self.tabla_eventos.column("col_hora", width=100, anchor="center")

        self.tabla_eventos.heading("col_desc", text="Descripción de la Tarea")
        self.tabla_eventos.column("col_desc", width=350, anchor="w")

        barra_desplazamiento = ttk.Scrollbar(self.panel_inferior, orient="vertical", command=self.tabla_eventos.yview)
        self.tabla_eventos.configure(yscroll=barra_desplazamiento.set)

        self.tabla_eventos.pack(side="left", fill="both", expand=True)
        barra_desplazamiento.pack(side="right", fill="y")

    # ==========================================
    # LÓGICA DE LA APLICACIÓN
    # ==========================================
    def guardar_registro(self):
        """Toma los valores de los Entry y los coloca en la tabla."""
        fecha_texto = self.selector_fecha.get()
        hora_texto = self.caja_hora.get()
        detalle_texto = self.caja_detalle.get()

        # Validación de campos vacíos
        if hora_texto == "" or detalle_texto == "":
            messagebox.showerror("Error de validación", "Falta información. Llena la hora y el detalle.")
            return

        # Insertar en la tabla
        self.tabla_eventos.insert("", tk.END, values=(fecha_texto, hora_texto, detalle_texto))

        # Resetear los campos visuales
        self.caja_hora.delete(0, tk.END)
        self.caja_detalle.delete(0, tk.END)
        messagebox.showinfo("Confirmación", "La tarea ha sido registrada exitosamente.")

    def quitar_registro(self):
        """Verifica si hay un elemento seleccionado y lo elimina con confirmación."""
        item_seleccionado = self.tabla_eventos.selection()

        if not item_seleccionado:
            messagebox.showwarning("Atención", "No has seleccionado ninguna tarea para borrar.")
            return

        # Dialogo opcional requerido en la rúbrica
        seguro = messagebox.askyesno("Confirmación de seguridad", "¿Borrar definitivamente este registro?")

        if seguro:
            for item in item_seleccionado:
                self.tabla_eventos.delete(item)

    def cerrar_app(self):
        """Finaliza la ejecución de la ventana."""
        self.ventana.quit()


# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    raiz = tk.Tk()
    aplicacion = GestorDeTareas(raiz)
    raiz.mainloop()