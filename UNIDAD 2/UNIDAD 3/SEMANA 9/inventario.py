
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



# ARCHIVO: sistema_gestion.py (Lógica Principal)

# from items_inventario import Producto

class GestionInventario:
    def __init__(self):
        # Usamos un diccionario para acceso rápido por ID
        # Clave: ID, Valor: Objeto Producto
        self.inventario = {}

    def agregar_item(self, p):
        if p.get_id() in self.inventario:
            print("¡Error! Ya existe un producto con el ID:", p.get_id())
        else:
            self.inventario[p.get_id()] = p
            print("Producto registrado con éxito.")

    def borrar_item(self, id_producto):
        if id_producto in self.inventario:
            del self.inventario[id_producto]
            print(f"El producto {id_producto} fue eliminado.")
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
        else:
            print("ID no encontrado en el sistema.")

    def buscar_nombre(self, texto_busqueda):
        print(f"--- Resultados para '{texto_busqueda}' ---")
        encontrados = False
        # Recorremos los valores del diccionario
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
        print("\n=== SISTEMA DE TIENDA  ===")
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
                print("Error: Ingrese números válidos para cantidad y precio.")

        elif seleccion == '2':
            uid = input("Ingrese ID a borrar: ")
            sistema.borrar_item(uid)

        elif seleccion == '3':
            uid = input("ID del producto: ")
            print("Deje vacío si no desea cambiar el valor.")
            q_str = input("Nueva Cantidad: ")
            p_str = input("Nuevo Precio: ")

            q_val = int(q_str) if q_str.strip() else None
            p_val = float(p_str) if p_str.strip() else None

            sistema.modificar_item(uid, q_val, p_val)

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