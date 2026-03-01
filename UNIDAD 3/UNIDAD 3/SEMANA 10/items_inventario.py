import os


# ARCHIVO: items_inventario.py (Clase Producto)
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self): return self.id

    def get_nombre(self): return self.nombre

    def get_cantidad(self): return self.cantidad

    def get_precio(self): return self.precio

    # Setters
    def set_cantidad(self, cantidad): self.cantidad = cantidad

    def set_precio(self, precio): self.precio = precio

    def to_string(self):
        return f"[{self.id}] {self.nombre} - Cant: {self.cantidad} - Precio: ${self.precio}"

    # Nuevo método para formatear los datos y guardarlos en el archivo de texto
    def to_linea_archivo(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"


# ARCHIVO: sistema_gestion.py (Lógica Principal)
class GestionInventario:
    def __init__(self, archivo="inventario.txt"):
        self.inventario = {}
        self.archivo = archivo
        # Requisito 2: Cargar automáticamente los productos al iniciar
        self.cargar_desde_archivo()

    # --- NUEVAS FUNCIONES DE ARCHIVOS Y EXCEPCIONES ---

    def cargar_desde_archivo(self):
        """Lee el archivo de texto y reconstruye el inventario."""
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        id_prod, nombre, cant, precio = linea.split(',')
                        self.inventario[id_prod] = Producto(id_prod, nombre, int(cant), float(precio))
            print(f"[Éxito] Inventario cargado correctamente desde '{self.archivo}'.")

        except FileNotFoundError:
            # Requisito 3: Manejo si el archivo no existe
            print(f"[Aviso] No se encontró el archivo '{self.archivo}'. Se creará uno nuevo automáticamente.")
            # Creamos el archivo vacío
            try:
                open(self.archivo, 'a').close()
            except PermissionError:
                print(f"[Error] No hay permisos para crear el archivo '{self.archivo}' en este directorio.")

        except PermissionError:
            # Requisito 3: Manejo de permisos
            print(f"[Error] Permisos denegados para leer el archivo '{self.archivo}'.")

        except Exception as e:
            print(f"[Error] Ocurrió un problema inesperado al cargar el archivo: {e} (Posible archivo corrupto).")

    def guardar_en_archivo(self):
        """Sobrescribe el archivo de texto con el estado actual del inventario."""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.inventario.values():
                    f.write(producto.to_linea_archivo())
            # Requisito 4: Notificar al usuario sobre el éxito
            print(f"[Éxito] Los cambios han sido guardados en '{self.archivo}'.")

        except PermissionError:
            print(f"[Error crítico] Permiso denegado para escribir en '{self.archivo}'. Los cambios no se guardaron.")
        except Exception as e:
            print(f"[Error crítico] No se pudo guardar el archivo: {e}")

    # --- MODIFICACIONES EN LAS FUNCIONES EXISTENTES ---

    def agregar_item(self, p):
        if p.get_id() in self.inventario:
            print("¡Error! Ya existe un producto con el ID:", p.get_id())
        else:
            self.inventario[p.get_id()] = p
            print("Producto registrado con éxito.")
            # Requisito 1: Reflejar modificación en el archivo
            self.guardar_en_archivo()

    def borrar_item(self, id_producto):
        if id_producto in self.inventario:
            del self.inventario[id_producto]
            print(f"El producto {id_producto} fue eliminado.")
            # Requisito 1: Reflejar modificación en el archivo
            self.guardar_en_archivo()
        else:
            print("No se encontró ese ID para eliminar.")

    def modificar_item(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.inventario:
            producto = self.inventario[id_producto]
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print("Información actualizada correctamente.")
            # Requisito 1: Reflejar modificación en el archivo
            self.guardar_en_archivo()
        else:
            print("ID no encontrado en el sistema.")

    def buscar_nombre(self, texto_busqueda):
        print(f"--- Resultados para '{texto_busqueda}' ---")
        encontrados = False
        for prod in self.inventario.values():
            if texto_busqueda.lower() in prod.get_nombre().lower():
                print(prod.to_string())
                encontrados = True
        if not encontrados:
            print("No hay coincidencias.")

    def listar_todo(self):
        print("\n--- Listado Completo ---")
        if not self.inventario:
            print("Inventario vacío.")
        else:
            for prod in self.inventario.values():
                print(prod.to_string())


def ejecutar_sistema():
    sistema = GestionInventario()

    while True:
        print("\n=== SISTEMA DE TIENDA ===")
        print("1. Registrar nuevo producto")
        print("2. Eliminar producto existente")
        print("3. Actualizar stock o precio")
        print("4. Buscar productos")
        print("5. Ver reporte total")
        print("6. Salir")

        seleccion = input(">>> ")

        if seleccion == '1':
            uid = input("ID: ")
            nom = input("Nombre: ")
            try:
                q = int(input("Cantidad: "))
                p = float(input("Precio: "))
                sistema.agregar_item(Producto(uid, nom, q, p))
            except ValueError:
                print("[Error] Ingrese números válidos para cantidad y precio.")

        elif seleccion == '2':
            uid = input("Ingrese ID a borrar: ")
            sistema.borrar_item(uid)

        elif seleccion == '3':
            uid = input("ID del producto: ")
            print("Deje vacío si no desea cambiar el valor.")
            q_str = input("Nueva Cantidad: ")
            p_str = input("Nuevo Precio: ")

            try:
                q_val = int(q_str) if q_str.strip() else None
                p_val = float(p_str) if p_str.strip() else None
                sistema.modificar_item(uid, q_val, p_val)
            except ValueError:
                print("[Error] Debe ingresar valores numéricos válidos.")

        elif seleccion == '4':
            txt = input("Nombre a buscar: ")
            sistema.buscar_nombre(txt)

        elif seleccion == '5':
            sistema.listar_todo()

        elif seleccion == '6':
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    ejecutar_sistema()