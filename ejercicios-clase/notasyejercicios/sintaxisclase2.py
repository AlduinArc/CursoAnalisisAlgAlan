def contar_comparaciones(lista: list) -> int:
    """Cuenta cuantas comparaciones hace insertion sort sobre 'lista'.
 
    Args:
        lista: lista de numeros a ordenar.
 
    Returns:
        El numero total de comparaciones realizadas.
    """
    comparaciones = 0
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j - 1] > lista[j]:
            comparaciones = comparaciones + 1
            lista[j - 1], lista[j] = lista[j], lista[j - 1]
            j = j - 1
    return comparaciones

def contar():
    tiempo = 0.005
    if tiempo < 0.001:
        categoria = "rapido"
    elif tiempo < 0.01:
        categoria = "moderado"
    else:
        categoria = "lento"
    return categoria

def cuadrados():
    tamanos = [100, 1000, 10000]
    cuadrados = []
    for t in tamanos:
        cuadrados.append(t ** 2)
    return cuadrados

total = contar_comparaciones([5, 2, 9, 1])
total2 = contar()
total3 = cuadrados()
print(total3)