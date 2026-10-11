"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(
    valores: list[float],
) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).

    Args:
        valores: Variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    mejor_suma = float("-inf")
    mejor_inicio = 0
    mejor_fin = 0

    for inicio in range(len(valores)):
        suma_actual = 0.0

        for fin in range(inicio, len(valores)):
            suma_actual += valores[fin]

            if suma_actual > mejor_suma:
                mejor_suma = suma_actual
                mejor_inicio = inicio
                mejor_fin = fin

    return mejor_inicio, mejor_fin, mejor_suma