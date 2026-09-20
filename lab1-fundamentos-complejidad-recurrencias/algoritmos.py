"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arreglo = datos.copy()
    comparaciones = 0

    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if arreglo[j] < clave:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            else:
                break

        arreglo[j + 1] = clave

    return arreglo, comparaciones


def _merge(
    izquierda: list[int],
    derecha: list[int],
) -> tuple[list[int], int]:
    """Combina dos listas ordenadas de mayor a menor.

    Args:
        izquierda: primera lista ordenada.
        derecha: segunda lista ordenada.

    Returns:
        Una tupla con la lista combinada y el numero de comparaciones.
    """
    resultado: list[int] = []
    i = 0
    j = 0
    comparaciones = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1

        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones


def _merge_sort_recursivo(
    datos: list[int],
) -> tuple[list[int], int]:
    """Ordena recursivamente una lista y cuenta comparaciones.

    Args:
        datos: lista que se desea ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero de comparaciones.
    """
    if len(datos) <= 1:
        return datos, 0

    mitad = len(datos) // 2

    izquierda, comparaciones_izquierda = _merge_sort_recursivo(
        datos[:mitad]
    )

    derecha, comparaciones_derecha = _merge_sort_recursivo(
        datos[mitad:]
    )

    resultado, comparaciones_merge = _merge(
        izquierda,
        derecha,
    )

    comparaciones_total = (
        comparaciones_izquierda
        + comparaciones_derecha
        + comparaciones_merge
    )

    return resultado, comparaciones_total


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    copia = datos.copy()
    return _merge_sort_recursivo(copia)