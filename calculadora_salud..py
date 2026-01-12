"""
Descripción del Programa:
Este programa gestiona un registro básico de salud. Calcula el Índice de
Masa Corporal (IMC) de una persona utilizando su peso y altura, y determina
si tiene un peso bajo basado en un umbral estándar.
"""


def main():
    # --- Datos del Usuario (Variables) ---

    # Tipo de dato: String - Nombre del usuario para el registro
    nombre_paciente = "PRISCILA"

    # Tipo de dato: Integer - Edad del paciente
    edad_paciente = 29

    # Tipo de dato: Float - Peso en kilogramos y altura en metros
    peso_kg = 60.5
    altura_m = 1.65

    # --- Lógica del Programa ---

    # Fórmula del IMC: Peso dividido por la altura al cuadrado
    indice_masa_corporal = peso_kg / (altura_m ** 2)

    # Tipo de dato: Boolean - Evaluamos una condición lógica
    # Consideramos 'bajo peso' si el IMC es menor a 18.5
    es_bajo_peso = indice_masa_corporal < 18.5

    # --- Mostrar Resultados ---
    print(f"--- Reporte de Salud de: {nombre_paciente} ---")
    print(f"Edad: {edad_paciente} años")
    print(f"Su IMC calculado es: {indice_masa_corporal:.2f}")

    # Uso del booleano para mostrar información
    print(f"¿Se considera bajo peso?: {es_bajo_peso}")


# Punto de entrada del script
if __name__ == "__main__":
    main()