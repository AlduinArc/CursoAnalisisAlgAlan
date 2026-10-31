"""Mediciones experimentales de ListaEnlazada y TablaHash.

El módulo realiza los experimentos A y B del laboratorio. Solamente las
operaciones de búsqueda se incluyen dentro de las regiones cronometradas.
"""

import math
import random
import statistics
import time
from pathlib import Path
from typing import Callable, List, Tuple

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

SEMILLA = 2026
GUIA_MINIMA = 1_000_000_000
GUIA_MAXIMA = 9_999_999_999
BUSQUEDAS_POR_REPETICION = 200
REPETICIONES = 7
TAMANOS = [100, 500, 1000, 5000, 20000, 50000]
ALFAS = [0.5, 1.0, 4.0, 10.0]
N_EXPERIMENTO_B = 20000
CARPETA_GRAFICAS = Path("graficas")


def es_primo(numero: int) -> bool:
    """Determina si un número entero es primo.

    Args:
        numero: Número que se desea evaluar.

    Returns:
        True si el número es primo; False en caso contrario.
    """
    if numero < 2:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    limite = math.isqrt(numero)

    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            return False

    return True


def primo_cercano(numero: int) -> int:
    """Encuentra un número primo cercano al valor recibido.

    Se busca simétricamente hacia abajo y hacia arriba hasta encontrar
    candidatos primos. Si ambos están a igual distancia, se escoge el
    menor.

    Args:
        numero: Valor alrededor del cual se busca un primo.

    Returns:
        Número primo cercano al valor solicitado.
    """
    if numero <= 2:
        return 2

    distancia = 0

    while True:
        inferior = numero - distancia
        superior = numero + distancia

        if inferior >= 2 and es_primo(inferior):
            return inferior

        if es_primo(superior):
            return superior

        distancia += 1


def generar_guias(
    cantidad: int,
    generador: random.Random,
) -> List[int]:
    """Genera guías únicas de diez dígitos.

    Args:
        cantidad: Número de guías requeridas.
        generador: Generador pseudoaleatorio reproducible.

    Returns:
        Lista de claves únicas de diez dígitos.
    """
    return generador.sample(
        range(GUIA_MINIMA, GUIA_MAXIMA + 1),
        cantidad,
    )


def generar_inexistentes(
    cantidad: int,
    ocupadas: set[int],
    generador: random.Random,
) -> List[int]:
    """Genera claves que no pertenecen a la colección almacenada.

    Args:
        cantidad: Número de claves inexistentes requeridas.
        ocupadas: Conjunto de claves que ya están almacenadas.
        generador: Generador pseudoaleatorio reproducible.

    Returns:
        Lista de claves que no pertenecen al conjunto de ocupadas.
    """
    resultado: List[int] = []

    while len(resultado) < cantidad:
        candidata = generador.randint(
            GUIA_MINIMA,
            GUIA_MAXIMA,
        )

        if candidata not in ocupadas:
            resultado.append(candidata)

    return resultado


def construir_estructuras(
    guias: List[int],
    capacidad: int,
) -> Tuple[ListaEnlazada, TablaHash]:
    """Construye las dos estructuras con exactamente los mismos datos.

    Args:
        guias: Claves que se almacenarán.
        capacidad: Número de cajones de la tabla hash.

    Returns:
        Tupla con la lista enlazada y la tabla hash construidas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(capacidad)

    for guia in guias:
        lista.insertar(guia, "en reparto")
        tabla.insertar(guia, "en reparto")

    return lista, tabla


def medir_busquedas(
    funcion_busqueda: Callable[[int], object],
    claves: List[int],
) -> float:
    """Mide el tiempo medio de un grupo de búsquedas.

    El cronómetro comienza inmediatamente antes de las búsquedas y
    termina inmediatamente después. La preparación de datos no forma
    parte de la medición.

    Args:
        funcion_busqueda: Función que realiza una búsqueda individual.
        claves: Claves que serán consultadas.

    Returns:
        Tiempo medio por búsqueda expresado en segundos.
    """
    inicio = time.perf_counter()

    for clave in claves:
        funcion_busqueda(clave)

    fin = time.perf_counter()

    return (fin - inicio) / len(claves)


def medir_con_repeticiones(
    funcion_busqueda: Callable[[int], object],
    claves: List[int],
) -> float:
    """Obtiene una medición robusta mediante repeticiones.

    Cada repetición mide el tiempo medio de todas las búsquedas. Como
    medida final se utiliza la mediana de siete repeticiones para
    reducir el efecto de interrupciones y ruido del sistema operativo.

    Args:
        funcion_busqueda: Función de búsqueda que se desea medir.
        claves: Claves consultadas en cada repetición.

    Returns:
        Mediana del tiempo medio por búsqueda, en segundos.
    """
    mediciones: List[float] = []

    for _ in range(REPETICIONES):
        tiempo = medir_busquedas(funcion_busqueda, claves)
        mediciones.append(tiempo)

    return statistics.median(mediciones)


def experimento_a() -> Tuple[List[float], List[float]]:
    """Ejecuta el experimento de crecimiento respecto a n.

    Para cada tamaño se utiliza un número primo de cajones cercano a
    n / 2, por lo que el factor de carga se mantiene aproximadamente
    en 2.

    Args:
        No recibe argumentos.

    Returns:
        Dos listas con los tiempos de ListaEnlazada y TablaHash.
    """
    generador = random.Random(SEMILLA)
    tiempos_lista: List[float] = []
    tiempos_tabla: List[float] = []

    print("\nEXPERIMENTO A")
    print(
        f"{'n':>8} {'m':>8} {'alfa':>8} "
        f"{'lista (us)':>14} {'hash (us)':>14}"
    )

    for n in TAMANOS:
        capacidad = primo_cercano(max(2, round(n / 2)))
        guias = generar_guias(n, generador)
        ocupadas = set(guias)

        inexistentes = generar_inexistentes(
            BUSQUEDAS_POR_REPETICION,
            ocupadas,
            generador,
        )

        lista, tabla = construir_estructuras(
            guias,
            capacidad,
        )

        tiempo_lista = medir_con_repeticiones(
            lista.buscar,
            inexistentes,
        )
        tiempo_tabla = medir_con_repeticiones(
            tabla.buscar,
            inexistentes,
        )

        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"{n:8d} "
            f"{capacidad:8d} "
            f"{tabla.factor_carga():8.3f} "
            f"{tiempo_lista * 1_000_000:14.3f} "
            f"{tiempo_tabla * 1_000_000:14.3f}"
        )

    return tiempos_lista, tiempos_tabla


def graficar_experimento_a(
    tiempos_lista: List[float],
    tiempos_tabla: List[float],
) -> None:
    """Genera la gráfica comparativa del experimento A.

    Args:
        tiempos_lista: Tiempos medidos para la lista enlazada.
        tiempos_tabla: Tiempos medidos para la tabla hash.

    Returns:
        None.
    """
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    tiempos_lista_us = [
        tiempo * 1_000_000 for tiempo in tiempos_lista
    ]
    tiempos_tabla_us = [
        tiempo * 1_000_000 for tiempo in tiempos_tabla
    ]

    plt.figure(figsize=(9, 6))
    plt.plot(
        TAMANOS,
        tiempos_lista_us,
        marker="o",
        label="Lista enlazada",
    )
    plt.plot(
        TAMANOS,
        tiempos_tabla_us,
        marker="o",
        label="Tabla hash",
    )
    plt.xlabel("Número de envíos (n)")
    plt.ylabel("Tiempo mediano por búsqueda (µs)")
    plt.title("Búsqueda infructuosa: lista enlazada vs. tabla hash")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(
        CARPETA_GRAFICAS / "lista_vs_tabla.png",
        dpi=150,
    )
    plt.close()


def experimento_b() -> Tuple[List[float], List[float]]:
    """Ejecuta el experimento sobre el factor de carga.

    Se mantiene n fijo y se modifica el número de cajones para producir
    distintos factores de carga.

    Args:
        No recibe argumentos.

    Returns:
        Tupla con los factores de carga reales y sus tiempos medidos.
    """
    generador = random.Random(SEMILLA + 1)
    guias = generar_guias(N_EXPERIMENTO_B, generador)
    ocupadas = set(guias)

    inexistentes = generar_inexistentes(
        BUSQUEDAS_POR_REPETICION,
        ocupadas,
        generador,
    )

    alfas_reales: List[float] = []
    tiempos: List[float] = []

    print("\nEXPERIMENTO B")
    print(
        f"{'alfa objetivo':>15} {'m':>8} "
        f"{'alfa real':>12} {'hash (us)':>14}"
    )

    for alfa_objetivo in ALFAS:
        capacidad_objetivo = round(
            N_EXPERIMENTO_B / alfa_objetivo
        )
        capacidad = primo_cercano(
            max(2, capacidad_objetivo)
        )

        tabla = TablaHash(capacidad)

        for guia in guias:
            tabla.insertar(guia, "en reparto")

        tiempo = medir_con_repeticiones(
            tabla.buscar,
            inexistentes,
        )

        alfa_real = tabla.factor_carga()

        alfas_reales.append(alfa_real)
        tiempos.append(tiempo)

        print(
            f"{alfa_objetivo:15.3f} "
            f"{capacidad:8d} "
            f"{alfa_real:12.3f} "
            f"{tiempo * 1_000_000:14.3f}"
        )

    return alfas_reales, tiempos


def graficar_experimento_b(
    alfas: List[float],
    tiempos: List[float],
) -> None:
    """Genera la gráfica de tiempo frente al factor de carga.

    Args:
        alfas: Factores de carga reales obtenidos.
        tiempos: Tiempos medidos para cada factor de carga.

    Returns:
        None.
    """
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    tiempos_us = [
        tiempo * 1_000_000 for tiempo in tiempos
    ]

    plt.figure(figsize=(9, 6))
    plt.plot(
        alfas,
        tiempos_us,
        marker="o",
    )
    plt.xlabel("Factor de carga (α = n / m)")
    plt.ylabel("Tiempo mediano por búsqueda (µs)")
    plt.title("Efecto del factor de carga en la tabla hash")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(
        CARPETA_GRAFICAS / "tiempo_vs_alfa.png",
        dpi=150,
    )
    plt.close()


def analizar_factores_crecimiento(
    tiempos_lista: List[float],
    tiempos_tabla: List[float],
) -> None:
    """Muestra factores empíricos de crecimiento consecutivos.

    Args:
        tiempos_lista: Mediciones obtenidas para ListaEnlazada.
        tiempos_tabla: Mediciones obtenidas para TablaHash.

    Returns:
        None.
    """
    print("\nFACTORES DE CRECIMIENTO DEL EXPERIMENTO A")
    print(
        f"{'intervalo':>18} {'factor n':>12} "
        f"{'factor lista':>14} {'factor hash':>14}"
    )

    for indice in range(1, len(TAMANOS)):
        factor_n = TAMANOS[indice] / TAMANOS[indice - 1]
        factor_lista = (
            tiempos_lista[indice] / tiempos_lista[indice - 1]
        )
        factor_tabla = (
            tiempos_tabla[indice] / tiempos_tabla[indice - 1]
        )

        intervalo = (
            f"{TAMANOS[indice - 1]}->{TAMANOS[indice]}"
        )

        print(
            f"{intervalo:>18} "
            f"{factor_n:12.3f} "
            f"{factor_lista:14.3f} "
            f"{factor_tabla:14.3f}"
        )


def main() -> None:
    """Ejecuta todos los experimentos y genera las gráficas.

    Args:
        No recibe argumentos.

    Returns:
        None.
    """
    tiempos_lista, tiempos_tabla = experimento_a()

    graficar_experimento_a(
        tiempos_lista,
        tiempos_tabla,
    )

    analizar_factores_crecimiento(
        tiempos_lista,
        tiempos_tabla,
    )

    alfas, tiempos_alfa = experimento_b()

    graficar_experimento_b(
        alfas,
        tiempos_alfa,
    )

    print("\nGráficas generadas correctamente:")
    print("graficas/lista_vs_tabla.png")
    print("graficas/tiempo_vs_alfa.png")


if __name__ == "__main__":
    main()