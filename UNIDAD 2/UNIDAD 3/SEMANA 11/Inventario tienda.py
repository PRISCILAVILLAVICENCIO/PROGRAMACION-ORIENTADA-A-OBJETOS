import os

# 1. Clase Articulo (Nombre distinto para variar)
class Articulo:
    def __init__(self, id_art, nombre, stock, costo):
        self.id_art = id_art
        self.nombre = nombre
        self.stock = stock
        self.costo = costo

    def __str__(self):
        return f"[{self.id_art}] {self.nombre} - Stock: {self.stock} - Costo: ${self.costo}"

# 2. Clase GestionInventario
class GestionInventario:
    def __init__(self):
        # Uso de colección (Diccionario)
        self.lista_articulos = {}
        self.nombre_archivo = "datos_inventario.txt"
        self.leer_archivo()

    def registrar(self, art):
        if art.id_art not in self.lista_articulos:
            self.lista_articulos[art.id_art] = art
            self.escribir_archivo()
            print("Registrado correctamente.")
        else:
            print("El ID ya está en uso.")

    def borrar(self, id_art):
        if self.lista_articulos.pop(id_art, None):
            self.escribir_archivo()
            print("Artículo borrado.")
        else:
            print("No se encontró el artículo.")

    def modificar(self, id_art, n_stock, n_costo):
        if id_art in self.lista_articulos:
            self.lista_articulos[id_art].stock = n_stock
            self.lista_articulos[id_art].costo = n_costo
            self.escribir_archivo()
            print("Datos actualizados.")
        else:
            print("ID no válido.")

    def buscar_nombre(self, texto):
        for art in self.lista_articulos.values():
            if texto.lower() in art.nombre.lower():
                print(art)

    def listar_articulos(self):
        for art in self.lista_articulos.values():
            print(art)

    # 4. Manejo de Archivos (Persistencia)
    def escribir_archivo(self):
        with open(self.nombre_archivo, "w") as f:
            for a in self.lista_articulos.values():
                f.write(f"{a.id_art},{a.nombre},{a.stock},{a.costo}\n")

    def leer_archivo(self):
        if os.path.exists(self.nombre_archivo):
            with open(self.nombre_archivo, "r") as f:
                for linea in f:
                    # Deserialización manual
                    parts = linea.strip().split(",")
                    if len(parts) == 4:
                        obj = Articulo(parts[0], parts[1], int(parts[2]), float(parts[3]))
                        self.lista_articulos[obj.id_art] = obj

# 5. Interfaz de Consola
def ejecutar_programa():
    sistema = GestionInventario()
    while True:
        print("\n--- MENÚ DE TIENDA ---")
        print("A. Agregar | B. Borrar | C. Actualizar | D. Buscar | E. Ver Todo | F. Salir")
        sel = input("Opción: ").upper()

        if sel == 'A':
            sistema.registrar(Articulo(input("ID: "), input("Nombre: "), int(input("Stock: ")), float(input("Precio: "))))
        elif sel == 'B':
            sistema.borrar(input("ID a eliminar: "))
        elif sel == 'C':
            id_m = input("ID: ")
            st = int(input("Nuevo Stock: "))
            pr = float(input("Nuevo Precio: "))
            sistema.modificar(id_m, st, pr)
        elif sel == 'D':
            sistema.buscar_nombre(input("Palabra clave: "))
        elif sel == 'E':
            sistema.listar_articulos()
        elif sel == 'F':
            break

if __name__ == "__main__":
    ejecutar_programa()