#Antes
"""def CalcularPromedio(Lista):
    s=0
    for x in Lista:
     s=s+x
    return s/len(Lista)
 
l=[1,2,3,4,5]
print(CalcularPromedio(l))"""

#despues
def calcular_promedio(lista: list[int]) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        lista: lista de números cuyo promedio se desea calcular.

    Returns:
        El promedio de los números de la lista.
    """
    suma = 0

    for numero in lista:
        suma = suma + numero

    return suma / len(lista)


def main() -> None:
    """Ejecuta el ejemplo de cálculo del promedio."""
    lista = [1, 2, 3, 4, 5]
    print(calcular_promedio(lista))


if __name__ == "__main__":
    main()