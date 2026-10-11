"""Pruebas para los algoritmos de subarreglo maximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def probar_serie_ejemplo() -> None:
    """Verifica la serie propuesta en el enunciado."""
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]

    fuerza_bruta = subarreglo_fuerza_bruta(serie)
    divide_venceras = subarreglo_maximo(serie, 0, len(serie) - 1)

    assert fuerza_bruta[2] == 17
    assert divide_venceras[2] == 17


def probar_un_elemento() -> None:
    """Verifica una serie con un solo elemento."""
    serie = [8]

    assert subarreglo_fuerza_bruta(serie)[2] == 8
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 8


def probar_todos_negativos() -> None:
    """Verifica una serie compuesta solamente por valores negativos."""
    serie = [-8, -3, -10, -2, -7]

    assert subarreglo_fuerza_bruta(serie)[2] == -2
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -2


def probar_todos_positivos() -> None:
    """Verifica una serie compuesta solamente por valores positivos."""
    serie = [2, 4, 1, 6, 3]

    suma_esperada = 16

    assert subarreglo_fuerza_bruta(serie)[2] == suma_esperada
    assert (
        subarreglo_maximo(serie, 0, len(serie) - 1)[2]
        == suma_esperada
    )


def probar_caso_cruzado() -> None:
    """Verifica un caso cuyo mejor tramo cruza el punto medio."""
    serie = [-5, 4, 3, -1, 2, 1, -8, -2]

    fuerza_bruta = subarreglo_fuerza_bruta(serie)
    divide_venceras = subarreglo_maximo(serie, 0, len(serie) - 1)

    assert fuerza_bruta[2] == 9
    assert divide_venceras[2] == 9


def probar_listas_aleatorias() -> None:
    """Compara ambos algoritmos en al menos veinte listas aleatorias."""
    random.seed(42)

    for _ in range(20):
        tamano = random.randint(1, 50)
        serie = [random.randint(-100, 100) for _ in range(tamano)]

        fuerza_bruta = subarreglo_fuerza_bruta(serie)
        divide_venceras = subarreglo_maximo(
            serie, 0, len(serie) - 1
        )

        assert fuerza_bruta[2] == divide_venceras[2]


def ejecutar_pruebas() -> None:
    """Ejecuta todas las pruebas del laboratorio."""
    probar_serie_ejemplo()
    probar_un_elemento()
    probar_todos_negativos()
    probar_todos_positivos()
    probar_caso_cruzado()
    probar_listas_aleatorias()

    print("Todas las pruebas fueron superadas correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()