import json
import os


class MaterialLectura:
    def __init__(self, nombre_libro, creador, genero, codigo_isbn):
        self.nombre_libro = nombre_libro
        self.creador = creador
        self.genero = genero
        self.codigo_isbn = codigo_isbn

    def empaquetar_datos(self):
        return {
            "nombre": self.nombre_libro,
            "creador": self.creador,
            "genero": self.genero,
            "codigo": self.codigo_isbn
        }

    def __str__(self):
        return f"Obra: {self.nombre_libro} | Escrito por: {self.creador} | [{self.genero}] - Código: {self.codigo_isbn}"


class Lector:
    def __init__(self, nombre_completo, identificacion):
        self.nombre_completo = nombre_completo
        self.identificacion = identificacion
        self.materiales_retirados = []

    def empaquetar_datos(self):
        return {
            "nombre_completo": self.nombre_completo,
            "identificacion": self.identificacion,
            "materiales_retirados": [material.empaquetar_datos() for material in self.materiales_retirados]
        }

    def __str__(self):
        return f"Lector: {self.nombre_completo} (ID: {self.identificacion})"


class GestorBiblioteca:
    def __init__(self):
        self.catalogo = {}
        self.lectores_activos = {}
        self.archivo_respaldo = "registro_biblioteca.txt"
        self.restaurar_estado()

    def cargar_datos_base(self):
        print("📦 Iniciando con el inventario base...")
        self.ingresar_material(MaterialLectura("Orgullo y Prejuicio", "Jane Austen", "Romance", "LIT001"),
                               silencioso=True)
        self.ingresar_material(MaterialLectura("Hábitos Atómicos", "James Clear", "Desarrollo Personal", "HAB002"), silencioso=True)
        self.ingresar_material(
            MaterialLectura("El Código Da Vinci", "Dan Brown", "Misterio", "MYS003"),
            silencioso=True)

        self.inscribir_lector(Lector("Priscila", "W100"), silencioso=True)
        self.inscribir_lector(Lector("Juan", "W200"), silencioso=True)
        print("✅ Inventario base configurado y listo para usar.")

    def ingresar_material(self, material, silencioso=False):
        if material.codigo_isbn not in self.catalogo:
            self.catalogo[material.codigo_isbn] = material
            if not silencioso:
                print(f"-> Operación exitosa: '{material.nombre_libro}' agregado al catálogo.")
            self.actualizar_archivo()
        else:
            if not silencioso:
                print("-> Alerta: Este código ya se encuentra en el registro.")

    def inscribir_lector(self, lector, silencioso=False):
        if lector.identificacion not in self.lectores_activos:
            self.lectores_activos[lector.identificacion] = lector
            if not silencioso:
                print(f"-> Lector inscrito correctamente: {lector.nombre_completo}")
            self.actualizar_archivo()
        else:
            if not silencioso:
                print("-> Alerta: La identificación ya pertenece a otro lector.")

    def buscar_obra(self, filtro, palabra_clave):
        encontrados = []
        palabra_clave = palabra_clave.lower()
        for mat in self.catalogo.values():
            if (filtro == 'titulo' and palabra_clave in mat.nombre_libro.lower()) or \
                    (filtro == 'autor' and palabra_clave in mat.creador.lower()) or \
                    (filtro == 'genero' and palabra_clave == mat.genero.lower()):
                encontrados.append(mat)
        return encontrados

    def asignar_prestamo(self, id_lector, codigo_isbn):
        if id_lector in self.lectores_activos and codigo_isbn in self.catalogo:
            lector = self.lectores_activos[id_lector]
            obra = self.catalogo.pop(codigo_isbn)
            lector.materiales_retirados.append(obra)
            print(f"-> Excelente: '{obra.nombre_libro}' ha sido prestado a {lector.nombre_completo}.")
            self.actualizar_archivo()
        else:
            print("-> Error: Lector no registrado u obra no disponible.")

    def procesar_devolucion(self, id_lector, codigo_isbn):
        if id_lector in self.lectores_activos:
            lector = self.lectores_activos[id_lector]
            for obra in lector.materiales_retirados:
                if obra.codigo_isbn == codigo_isbn:
                    lector.materiales_retirados.remove(obra)
                    self.catalogo[codigo_isbn] = obra
                    print(f"-> Listo: '{obra.nombre_libro}' devuelto por {lector.nombre_completo}.")
                    self.actualizar_archivo()
                    return
            print(f"-> Aviso: {lector.nombre_completo} no posee el material con código {codigo_isbn}.")
        else:
            print(f"-> Error: No existe un lector con la identificación {id_lector}.")

    def actualizar_archivo(self):
        estado_actual = {
            "inventario": {cod: mat.empaquetar_datos() for cod, mat in self.catalogo.items()},
            "clientes": {ident: lec.empaquetar_datos() for ident, lec in self.lectores_activos.items()}
        }
        with open(self.archivo_respaldo, 'w', encoding='utf-8') as f:
            json.dump(estado_actual, f, indent=4)

    def restaurar_estado(self):
        if os.path.exists(self.archivo_respaldo):
            with open(self.archivo_respaldo, 'r', encoding='utf-8') as f:
                try:
                    estado_actual = json.load(f)
                    for cod, datos in estado_actual.get("inventario", {}).items():
                        self.catalogo[cod] = MaterialLectura(datos['nombre'], datos['creador'], datos['genero'],
                                                             datos['codigo'])
                    for ident, datos in estado_actual.get("clientes", {}).items():
                        nuevo_lector = Lector(datos['nombre_completo'], datos['identificacion'])
                        for mat_ret in datos.get('materiales_retirados', []):
                            nuevo_lector.materiales_retirados.append(
                                MaterialLectura(mat_ret['nombre'], mat_ret['creador'], mat_ret['genero'],
                                                mat_ret['codigo']))
                        self.lectores_activos[ident] = nuevo_lector
                except json.JSONDecodeError:
                    print("-> Archivo vacío o con errores. Empezando limpio.")
                    self.cargar_datos_base()
        else:
            self.cargar_datos_base()


def iniciar_panel():
    gestor = GestorBiblioteca()

    while True:
        print("\n" + "=" * 45)
        print(" 🏛️  PANEL DE CONTROL - GESTOR LITERARIO 🏛️ ")
        print("=" * 45)
        print(" [A] Agregar Material Literario")
        print(" [B] Inscribir Nuevo Lector")
        print(" [C] Explorar Catálogo (Buscar)")
        print(" [D] Registrar Préstamo")
        print(" [E] Registrar Devolución")
        print(" [F] Mostrar Inventario Actual")
        print(" [G] Mostrar Lista de Lectores")
        print(" [S] Salir del Programa")

        seleccion = input("\nSeleccione una acción (A-S): ").upper()

        if seleccion == 'A':
            n = input("Título: ")
            c = input("Autor: ")
            g = input("Género: ")
            cod = input("Código ISBN: ")
            gestor.ingresar_material(MaterialLectura(n, c, g, cod))

        elif seleccion == 'B':
            nom = input("Nombre del lector: ")
            iden = input("Número de Identificación: ")
            gestor.inscribir_lector(Lector(nom, iden))

        elif seleccion == 'C':
            filtro = input("Criterio de búsqueda (titulo, autor, genero): ").lower()
            if filtro in ['titulo', 'autor', 'genero']:
                palabra = input(f"Ingrese la palabra clave para {filtro}: ")
                resultados = gestor.buscar_obra(filtro, palabra)
                print("\n--- RESULTADOS DE BÚSQUEDA ---")
                if resultados:
                    for r in resultados:
                        print(f"  => {r}")
                else:
                    print("  No hay coincidencias en el catálogo.")
            else:
                print("  Filtro incorrecto. Use 'titulo', 'autor' o 'genero'.")

        elif seleccion == 'D':
            iden = input("Identificación del lector: ")
            cod = input("Código ISBN de la obra: ")
            gestor.asignar_prestamo(iden, cod)

        elif seleccion == 'E':
            iden = input("Identificación del lector: ")
            cod = input("Código ISBN de la obra: ")
            gestor.procesar_devolucion(iden, cod)

        elif seleccion == 'F':
            print("\n--- INVENTARIO DISPONIBLE ---")
            if not gestor.catalogo:
                print(" El catálogo está vacío en este momento.")
            for mat in gestor.catalogo.values():
                print(mat)

        elif seleccion == 'G':
            print("\n--- LECTORES ACTIVOS ---")
            if not gestor.lectores_activos:
                print(" No hay lectores registrados.")
            for lec in gestor.lectores_activos.values():
                print(lec)
                if lec.materiales_retirados:
                    print("    [+] Obras bajo su cuidado:")
                    for obra in lec.materiales_retirados:
                        print(f"        - {obra.nombre_libro}")

        elif seleccion == 'S':
            print("Apagando sistema y respaldando información... ¡Hasta luego!")
            break
        else:
            print("-> Acción inválida. Intente nuevamente.")


if __name__ == "__main__":
    iniciar_panel()