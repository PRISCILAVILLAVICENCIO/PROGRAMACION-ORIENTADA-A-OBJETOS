class ClimaSemanal:
    """Clase para gestionar los registros meteorológicos de una semana."""

    def __init__(self):
        # Encapsulamiento: El atributo __temperaturas es privado
        self.__temperaturas = []

    def agregar_temperatura(self, valor):
        """Agrega una nueva temperatura a la lista privada."""
        self.__temperaturas.append(valor)

    def calcular_promedio(self):
        """Lógica interna para promediar los datos almacenados."""
        if not self.__temperaturas:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)


class ClimaDetallado(ClimaSemanal):
    """Subclase que añade un reporte visual más completo."""

    def mostrar_reporte(self):
        promedio = self.calcular_promedio()
        print("\n--- INFORME METEOROLÓGICO ---")
        print(f"Estado: Procesado con éxito")
        print(f"Promedio de la semana: {promedio:.2f} grados")


def app_clima():

    gestor = ClimaDetallado()
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias:
        while True:
            try:
                t = float(input(f"Clima del {dia}: "))
                gestor.agregar_temperatura(t)
                break
            except ValueError:
                print("Error: El dato debe ser un número.")

    gestor.mostrar_reporte()


if __name__ == "__main__":
    app_clima()