"""Comparacion experimental de insertion sort y merge sort."""

import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 300, 500, 700, 1400, 3500, 6000]


def medir_algoritmo(
    algoritmo,
    tamanos: list[int],
) -> list[float]:
    """Mide el tiempo de un algoritmo de ordenamiento.

    Args:
        algoritmo: funcion de ordenamiento a medir.
        tamanos: tamaños de entrada.

    Returns:
        Lista de tiempos de ejecución en segundos.
    """
    tiempos = []

    for n in tamanos:
        datos = generar_aleatorio(n)

        inicio = time.perf_counter()
        algoritmo(datos)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return tiempos


def crear_grafica(
    tiempos_insertion: list[float],
    tiempos_merge: list[float],
) -> None:
    """Genera la gráfica comparativa de tiempos.

    Args:
        tiempos_insertion: tiempos de insertion sort.
        tiempos_merge: tiempos de merge sort.
    """
    carpeta = Path("graficas")
    carpeta.mkdir(exist_ok=True)

    plt.figure()

    plt.plot(
        TAMANOS,
        tiempos_insertion,
        marker="o",
        label="Insertion sort",
    )

    plt.plot(
        TAMANOS,
        tiempos_merge,
        marker="o",
        label="Merge sort",
    )

    plt.title("Comparación de insertion sort y merge sort")
    plt.xlabel("Tamaño de entrada (registros)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(carpeta / "parte4_tiempo.png")
    plt.close()


def estimar_para_tamiza(
    tiempo: float,
    n_medido: int,
    n_objetivo: int,
    tipo: str,
) -> float:
    """Estima el tiempo para 1.200.000 registros.

    Args:
        tiempo: tiempo medido para n_medido.
        n_medido: tamaño utilizado en la medición.
        n_objetivo: tamaño que se quiere estimar.
        tipo: 'cuadratico' o 'nlogn'.

    Returns:
        Tiempo estimado en segundos.
    """
    if tipo == "cuadratico":
        factor = (n_objetivo / n_medido) ** 2
    else:
        factor = (
            n_objetivo * __import__("math").log2(n_objetivo)
        ) / (
            n_medido * __import__("math").log2(n_medido)
        )

    return tiempo * factor


def main() -> None:
    """Ejecuta la comparación entre los dos algoritmos."""
    tiempos_insertion = medir_algoritmo(
        insertion_sort,
        TAMANOS,
    )

    tiempos_merge = medir_algoritmo(
        merge_sort,
        TAMANOS,
    )

    print("\nResultados:")

    for n, insertion, merge in zip(
        TAMANOS,
        tiempos_insertion,
        tiempos_merge,
    ):
        print(
            f"n={n:5d} | "
            f"insertion={insertion:.6f} s | "
            f"merge={merge:.6f} s"
        )

    crear_grafica(
        tiempos_insertion,
        tiempos_merge,
    )

    n_medido = TAMANOS[-1]
    n_objetivo = 1_200_000

    estimacion_insertion = estimar_para_tamiza(
        tiempos_insertion[-1],
        n_medido,
        n_objetivo,
        "cuadratico",
    )

    estimacion_merge = estimar_para_tamiza(
        tiempos_merge[-1],
        n_medido,
        n_objetivo,
        "nlogn",
    )

    print("\nEstimaciones para 1.200.000 registros:")
    print(
        f"Insertion sort: "
        f"{estimacion_insertion:.2f} segundos"
    )
    print(
        f"Merge sort: "
        f"{estimacion_merge:.2f} segundos"
    )

    print("\nEstimación en horas:")
    print(
        f"Insertion sort: "
        f"{estimacion_insertion / 3600:.2f} horas"
    )
    print(
        f"Merge sort: "
        f"{estimacion_merge / 3600:.2f} horas"
    )


if __name__ == "__main__":
    main()