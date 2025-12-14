def recolectar_datos_clima():
    """Solicita al usuario las temperaturas de los 7 días."""
    lista_temperaturas = []
    print(">>> Registro de Temperaturas Semanales <<<")

    contador = 1
    while contador <= 7:
        try:
            valor = float(input(f"Día {contador} - Ingrese la temperatura: "))
            lista_temperaturas.append(valor)
            contador += 1
        except ValueError:
            print("Entrada no válida. Por favor, use números.")

    return lista_temperaturas


def obtener_media(lista):
    """Calcula el promedio aritmético de una lista de números."""
    if len(lista) == 0:
        return 0
    suma_total = sum(lista)
    return suma_total / len(lista)


def ejecutar_sistema():
    """Coordina la ejecución de las funciones."""
    datos = recolectar_datos_clima()
    resultado = obtener_media(datos)

    print("\n--------------------------------")
    print(f"Resultado Final: El promedio es {resultado:.1f}°C")
    print("--------------------------------")


if __name__ == "__main__":
    ejecutar_sistema()