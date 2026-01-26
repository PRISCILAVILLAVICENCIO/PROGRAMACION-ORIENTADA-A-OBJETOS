
class Personaje:
    def __init__(self, nombre, vida):
        """
        Constructor (__init__): Configura el estado inicial del objeto.
        Establece el nombre y los puntos de vida del personaje.
        """
        self.nombre = nombre
        self.vida = vida
        print(f"+++ Constructor: ¡Ha nacido {self.nombre} con {self.vida} puntos de vida!")

    def atacar(self, objetivo):
        """
        Método de acción del personaje.
        """
        print(f"    [Acción]: {self.nombre} está atacando a {objetivo}.")

    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        print(f"    [Estado]: {self.nombre} recibió daño. Vida restante: {self.vida}")

    def __del__(self):
        """
        Destructor (__del__): Realiza tareas de limpieza.
        En este contexto, anuncia que el personaje ha sido eliminado de la memoria del juego.
        """
        print(f"--- Destructor: {self.nombre} ha sido eliminado de la partida (Memoria liberada).")


# Bloque principal de ejecución
if __name__ == "__main__":
    print("=== Iniciando Simulación del Juego ===")

    # 1. Instanciamos (creamos) los objetos. Aquí se activa __init__
    heroe = Personaje("Aragorn", 100)
    villano = Personaje("Orco", 50)

    # 2. Interactuamos con los objetos
    heroe.atacar("Orco")
    villano.recibir_daño(50)

    print("=== El villano ha sido derrotado ===")

    # 3. Eliminamos el objeto villano manualmente. Aquí se activa __del__
    del villano

    print("=== El héroe termina su misión ===")

    # Al finalizar el programa, Python eliminará automáticamente a 'heroe',
    # activando su destructor también.