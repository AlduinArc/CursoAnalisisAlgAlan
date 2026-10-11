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

def suma_cruzada(
    valores: list[float],
    inicio: int,
    medio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: Variacion diaria de caja.
        inicio: Indice inicial del rango considerado (inclusive).
        medio: Indice del ultimo elemento de la mitad izquierda.
        fin: Indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    mejor_suma_izquierda = float("-inf")
    suma_actual = 0.0
    mejor_inicio = medio

    for i in range(medio, inicio - 1, -1):
        suma_actual += valores[i]

        if suma_actual > mejor_suma_izquierda:
            mejor_suma_izquierda = suma_actual
            mejor_inicio = i

    mejor_suma_derecha = float("-inf")
    suma_actual = 0.0
    mejor_fin = medio + 1

    for j in range(medio + 1, fin + 1):
        suma_actual += valores[j]

        if suma_actual > mejor_suma_derecha:
            mejor_suma_derecha = suma_actual
            mejor_fin = j

    suma_total = mejor_suma_izquierda + mejor_suma_derecha

    return mejor_inicio, mejor_fin, suma_total

def subarreglo_maximo(
    valores: list[float],
    inicio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.

    Args:
        valores: Variacion diaria de caja.
        inicio: Indice inicial del rango a considerar (inclusive).
        fin: Indice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    izquierdo = subarreglo_maximo(valores, inicio, medio)
    derecho = subarreglo_maximo(valores, medio + 1, fin)
    cruzado = suma_cruzada(valores, inicio, medio, fin)

    mejor = izquierdo

    if derecho[2] > mejor[2]:
        mejor = derecho

    if cruzado[2] > mejor[2]:
        mejor = cruzado

    return mejor