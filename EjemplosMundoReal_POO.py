
# Tienda de Tecnología
#Este programa demuestra el uso de Herencia y Polimorfismo.
#Modela productos genéricos y específicos, interactuando con un proceso de venta.
class Producto:
    """Clase padre que representa un producto genérico."""

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        """Reduce el stock disponible si es posible."""
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        return False

    def obtener_info(self):
        return f"{self.nombre} - ${self.precio}"


# Herencia: Telefono hereda de Producto
class Telefono(Producto):
    """Subclase para teléfonos, añade atributos específicos."""

    def __init__(self, nombre, precio, stock, camara_mp):
        super().__init__(nombre, precio, stock)  # Llama al constructor del padre
        self.camara_mp = camara_mp

    # Polimorfismo: Sobreescribe el MEtodo obtener_info
    def obtener_info(self):
        return f"[Teléfono] {self.nombre} (Cámara: {self.camara_mp}MP) - ${self.precio}"


# Herencia: Laptop hereda de Producto
class Laptop(Producto):
    """Subclase para laptops, añade atributos específicos."""

    def __init__(self, nombre, precio, stock, ram_gb):
        super().__init__(nombre, precio, stock)
        self.ram_gb = ram_gb

    def obtener_info(self):
        return f"[Laptop] {self.nombre} (RAM: {self.ram_gb}GB) - ${self.precio}"


class CarritoDeCompras:
    """Clase que gestiona la compra de múltiples productos."""

    def __init__(self):
        self.lista_productos = []
        self.total = 0.0

    def agregar_producto(self, producto, cantidad=1):
        """Interacción: El carrito verifica stock del objeto Producto."""
        if producto.reducir_stock(cantidad):
            self.lista_productos.append(producto)
            self.total += producto.precio * cantidad
            print(f"Añadido: {producto.nombre}")
        else:
            print(f"Stock insuficiente para: {producto.nombre}")

    def mostrar_detalle(self):
        """Muestra el resumen de la compra."""
        print("\n--- Detalle del Carrito ---")
        for prod in self.lista_productos:
            print(prod.obtener_info())
        print(f"Total a Pagar: ${self.total:.2f}")


# --- Bloque Principal de Ejecución ---
if __name__ == "__main__":
    # 1. Crear inventario (Objetos de diferentes clases)
    iphone = Telefono("iPhone 14", 999.00, 5, 48)
    macbook = Laptop("MacBook Air", 1200.00, 2, 16)

    # 2. Crear el carrito
    mi_carrito = CarritoDeCompras()

    # 3. Interacción: Agregar productos al carrito
    print("--- Iniciando Compras ---")
    mi_carrito.agregar_producto(iphone)
    mi_carrito.agregar_producto(macbook)

    # Intentar comprar más stock del que existe para probar lógica
    # Creamos un producto con poco stock
    mouse = Producto("Mouse Genérico", 20.00, 0)
    mi_carrito.agregar_producto(mouse)  # Debería fallar

    # 4. Finalizar
    mi_carrito.mostrar_detalle()