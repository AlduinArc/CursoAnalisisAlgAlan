"""Medicion de los algoritmos de subarreglo maximo."""

import random
import statistics
import time

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000]
SEMILLA = 42
REPETICIONES = 3


def medir_fuerza_bruta(valores: list[float]) -> tuple[float, float]:
    """Mide el tiempo de ejecucion del algoritmo de fuerza bruta.

    Args:
        valores: Lista de valores sobre la cual ejecutar el algoritmo.

    Returns:
        Una tupla con la mediana del tiempo y la suma maxima encontrada.
    """
    tiempos = []
    resultado = 0.0

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        solucion = subarreglo_fuerza_bruta(valores)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)
        resultado = solucion[2]

    return statistics.median(tiempos), resultado


def medir_divide_venceras(
    valores: list[float],
) -> tuple[float, float]:
    """Mide el tiempo de ejecucion de divide y venceras.

    Args:
        valores: Lista de valores sobre la cual ejecutar el algoritmo.

    Returns:
        Una tupla con la mediana del tiempo y la suma maxima encontrada.
    """
    tiempos = []
    resultado = 0.0

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        solucion = subarreglo_maximo(valores, 0, len(valores) - 1)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)
        resultado = solucion[2]

    return statistics.median(tiempos), resultado


def ejecutar_experimento() -> None:
    """Ejecuta las mediciones y genera la grafica comparativa."""
    random.seed(SEMILLA)

    tiempos_fuerza_bruta = []
    tiempos_divide_venceras = []

    print("Resultados del experimento")
    print("-" * 65)

    for tamano in TAMANOS:
        valores = [
            random.randint(-100, 100)
            for _ in range(tamano)
        ]

        tiempo_fb, suma_fb = medir_fuerza_bruta(valores)
        tiempo_dv, suma_dv = medir_divide_venceras(valores)

        assert suma_fb == suma_dv

        tiempos_fuerza_bruta.append(tiempo_fb)
        tiempos_divide_venceras.append(tiempo_dv)

        print(
            f"n={tamano:5d} | "
            f"Fuerza bruta={tiempo_fb:.6f} s | "
            f"Divide y venceras={tiempo_dv:.6f} s"
        )

    plt.figure(figsize=(10, 6))

    plt.plot(
        TAMANOS,
        tiempos_fuerza_bruta,
        marker="o",
        label="Fuerza bruta",
    )

    plt.plot(
        TAMANOS,
        tiempos_divide_venceras,
        marker="o",
        label="Divide y venceras",
    )

    plt.title("Tiempo de ejecucion vs. tamano de entrada")
    plt.xlabel("Tamano de entrada n (elementos)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("graficas/tiempo_vs_n.png")
    plt.close()

    print("-" * 65)
    print("Grafica guardada en graficas/tiempo_vs_n.png")


if __name__ == "__main__":
    ejecutar_experimento()