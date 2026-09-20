"""Experimento de peor, mejor y caso promedio para insertion sort."""

import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir_escenario(
    generador,
    tamanos: list[int],
) -> tuple[list[float], list[int]]:
    """Mide tiempo y comparaciones para un generador.

    Args:
        generador: funcion que genera un escenario de entrada.
        tamanos: tamaños que se desean medir.

    Returns:
        Tupla con tiempos y cantidades de comparaciones.
    """
    tiempos = []
    comparaciones = []

    for n in tamanos:
        datos = generador(n)

        inicio = time.perf_counter()
        _, cantidad_comparaciones = insertion_sort(datos)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)
        comparaciones.append(cantidad_comparaciones)

    return tiempos, comparaciones


def crear_graficas(
    resultados: dict[str, tuple[list[float], list[int]]],
) -> None:
    """Genera las gráficas de comparaciones y tiempos.

    Args:
        resultados: resultados de los tres escenarios.
    """
    carpeta = Path("graficas")
    carpeta.mkdir(exist_ok=True)

    plt.figure()

    for escenario, (_, comparaciones) in resultados.items():
        plt.plot(
            TAMANOS,
            comparaciones,
            marker="o",
            label=escenario,
        )

    plt.title("Insertion sort: comparaciones por escenario")
    plt.xlabel("Tamaño de entrada (registros)")
    plt.ylabel("Comparaciones entre elementos")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(carpeta / "parte3_comparaciones.png")
    plt.close()

    plt.figure()

    for escenario, (tiempos, _) in resultados.items():
        plt.plot(
            TAMANOS,
            tiempos,
            marker="o",
            label=escenario,
        )

    plt.title("Insertion sort: tiempo por escenario")
    plt.xlabel("Tamaño de entrada (registros)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(carpeta / "parte3_tiempo.png")
    plt.close()


def main() -> None:
    """Ejecuta el experimento de la Parte 3."""
    escenarios = {
        "A - Aleatorio": generar_aleatorio,
        "B - Casi ordenado": generar_casi_ordenado,
        "C - Inverso": generar_inverso,
    }

    resultados = {}

    for nombre, generador in escenarios.items():
        tiempos, comparaciones = medir_escenario(
            generador,
            TAMANOS,
        )

        resultados[nombre] = (
            tiempos,
            comparaciones,
        )

        print(f"\n{nombre}")

        for n, tiempo, cantidad in zip(
            TAMANOS,
            tiempos,
            comparaciones,
        ):
            print(
                f"n={n:5d} | "
                f"tiempo={tiempo:.6f} s | "
                f"comparaciones={cantidad}"
            )

    crear_graficas(resultados)

    print("\nGráficas creadas en la carpeta 'graficas/'.")


if __name__ == "__main__":
    main()