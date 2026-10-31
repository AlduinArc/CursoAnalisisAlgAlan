"""Pruebas para las estructuras implementadas en estructuras.py."""

import random
from typing import List

from estructuras import ListaEnlazada, TablaHash

SEMILLA = 2026
PRUEBAS_ALEATORIAS = 25
GUIA_MINIMA = 1_000_000_000
GUIA_MAXIMA = 9_999_999_999


def probar_lista_enlazada() -> None:
    """Verifica las operaciones fundamentales de ListaEnlazada.

    Args:
        No recibe argumentos.

    Returns:
        None.
    """
    lista = ListaEnlazada()

    assert lista.longitud() == 0
    assert lista.buscar(1234567890) is None

    lista.insertar(1234567890, "en bodega")
    lista.insertar(2234567890, "en reparto")

    assert lista.longitud() == 2
    assert lista.buscar(1234567890) == "en bodega"
    assert lista.buscar(2234567890) == "en reparto"
    assert lista.buscar(9999999999) is None

    lista.insertar(1234567890, "entregado")

    assert lista.longitud() == 2
    assert lista.buscar(1234567890) == "entregado"


def probar_tabla_hash() -> None:
    """Verifica búsquedas exitosas e infructuosas en TablaHash.

    Args:
        No recibe argumentos.

    Returns:
        None.
    """
    tabla = TablaHash(11)

    tabla.insertar(125, "en bodega")
    tabla.insertar(136, "en reparto")

    assert tabla.buscar(125) == "en bodega"
    assert tabla.buscar(136) == "en reparto"
    assert tabla.buscar(999) is None

    tabla.insertar(125, "entregado")

    assert tabla.buscar(125) == "entregado"
    assert tabla.tamano == 2


def probar_colisiones_exactas() -> None:
    """Verifica las colisiones exigidas por el enunciado.

    Con m = 7, las claves 10, 24 y 17 deben caer exactamente en el
    cajón 3 porque todas producen resto 3 al dividirlas entre 7.

    Args:
        No recibe argumentos.

    Returns:
        None.
    """
    tabla = TablaHash(7)

    assert 10 % 7 == 3
    assert 24 % 7 == 3
    assert 17 % 7 == 3

    tabla.insertar(10, "en bodega")
    tabla.insertar(24, "en reparto")
    tabla.insertar(17, "entregado")

    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en reparto"
    assert tabla.buscar(17) == "entregado"

    assert tabla.longitud_cajon(3) == 3
    assert tabla.tamano == 3


def probar_factor_carga() -> None:
    """Verifica el cálculo del factor de carga alfa = n / m.

    Args:
        No recibe argumentos.

    Returns:
        None.
    """
    tabla = TablaHash(7)

    assert tabla.factor_carga() == 0.0

    tabla.insertar(10, "en bodega")
    tabla.insertar(24, "en reparto")
    tabla.insertar(17, "entregado")

    esperado = 3 / 7

    assert abs(tabla.factor_carga() - esperado) < 1e-12

    tabla.insertar(10, "entregado")

    assert tabla.tamano == 3
    assert abs(tabla.factor_carga() - esperado) < 1e-12


def generar_guias_aleatorias(
    cantidad: int,
    generador: random.Random,
) -> List[int]:
    """Genera guías únicas de diez dígitos.

    Args:
        cantidad: Número de guías que se deben generar.
        generador: Generador pseudoaleatorio con semilla controlada.

    Returns:
        Lista con guías enteras únicas de diez dígitos.
    """
    return generador.sample(
        range(GUIA_MINIMA, GUIA_MAXIMA + 1),
        cantidad,
    )


def probar_colecciones_aleatorias() -> None:
    """Compara ListaEnlazada y TablaHash en colecciones aleatorias.

    Se realizan más de veinte experimentos reproducibles. En cada uno
    se insertan las mismas claves y valores en ambas estructuras y se
    comprueba que las búsquedas exitosas e infructuosas coincidan.

    Args:
        No recibe argumentos.

    Returns:
        None.
    """
    generador = random.Random(SEMILLA)

    for numero_prueba in range(PRUEBAS_ALEATORIAS):
        cantidad = generador.randint(20, 100)
        guias = generar_guias_aleatorias(cantidad, generador)

        lista = ListaEnlazada()
        tabla = TablaHash(101)

        for indice, guia in enumerate(guias):
            estado = f"estado-{numero_prueba}-{indice}"
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia in guias:
            assert lista.buscar(guia) == tabla.buscar(guia)

        inexistentes = generar_guias_aleatorias(10, generador)

        for guia in inexistentes:
            while lista.buscar(guia) is not None:
                guia = generador.randint(
                    GUIA_MINIMA,
                    GUIA_MAXIMA,
                )

            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None

        assert lista.longitud() == cantidad
        assert tabla.tamano == cantidad


def probar_errores() -> None:
    """Verifica el manejo de argumentos inválidos.

    Args:
        No recibe argumentos.

    Returns:
        None.
    """
    error_capacidad = False

    try:
        TablaHash(0)
    except ValueError:
        error_capacidad = True

    assert error_capacidad

    tabla = TablaHash(7)
    error_indice = False

    try:
        tabla.longitud_cajon(7)
    except IndexError:
        error_indice = True

    assert error_indice


def ejecutar_pruebas() -> None:
    """Ejecuta todas las pruebas del laboratorio.

    Args:
        No recibe argumentos.

    Returns:
        None.
    """
    probar_lista_enlazada()
    probar_tabla_hash()
    probar_colisiones_exactas()
    probar_factor_carga()
    probar_colecciones_aleatorias()
    probar_errores()

    print("Todas las pruebas finalizaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()