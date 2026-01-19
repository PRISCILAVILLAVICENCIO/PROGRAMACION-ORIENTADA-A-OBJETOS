# Definición de la Clase Base
class Producto:
    def __init__(self, nombre, precio, stock_inicial):
        self.nombre = nombre
        self.precio = precio
        # ENCAPSULACIÓN: Protegemos el stock para controlarlo internamente
        self.__stock = stock_inicial

    # Método para intentar realizar una venta
    def vender(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            print(f"Venta exitosa: {cantidad} unidades de {self.nombre}.")
        else:
            print(f"Error: No hay suficiente stock de {self.nombre}.")

    # Getter para consultar stock (Encapsulación)
    def consultar_stock(self):
        return self.__stock

    # Método base para precio (sin impuestos especiales)
    def obtener_precio_final(self):
        return self.precio

    def describir(self):
        return f"Producto: {self.nombre} | Precio Base: ${self.precio}"


# HERENCIA: ProductoElectronico extiende la funcionalidad de Producto
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, stock_inicial, garantia_meses):
        # Inicializamos la clase padre
        super().__init__(nombre, precio, stock_inicial)
        self.garantia_meses = garantia_meses

    # POLIMORFISMO: Sobreescritura de método
    # Los electrónicos agregan un 10% de impuesto tecnológico al precio final
    def obtener_precio_final(self):
        return self.precio * 1.10

    # POLIMORFISMO: Modificamos la descripción para agregar la garantía
    def describir(self):
        base = super().describir()
        return f"{base} | Garantía: {self.garantia_meses} meses"


# --- Bloque Principal de Ejecución ---
if __name__ == "__main__":
    print("--- SISTEMA DE INVENTARIO ---\n")

    # Instanciación de objetos
    camisa = Producto("Camisa de Algodón", 25.00, 50)
    laptop = ProductoElectronico("Laptop Gamer", 1200.00, 10, 24)

    # Demostración de Polimorfismo
    inventario = [camisa, laptop]

    for item in inventario:
        print("." * 40)
        print(item.describir())
        # Aquí vemos polimorfismo: el cálculo del precio varía según la clase
        print(f"Precio Final al cliente: ${item.obtener_precio_final():.2f}")

    print("\n--- Demostración de Encapsulación ---")
    # Intentamos modificar stock directamente (esto fallaría si descomentamos la línea de abajo)
    # laptop.__stock = -5

    # Usamos los métodos públicos para interactuar con los datos privados
    print(f"Stock inicial de Laptop: {laptop.consultar_stock()}")
    laptop.vender(2)
    print(f"Stock actual de Laptop: {laptop.consultar_stock()}")
