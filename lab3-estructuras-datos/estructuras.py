"""Estructuras de datos para el laboratorio de tablas hash.

Este módulo implementa una lista enlazada simple y una tabla hash con
encadenamiento separado. La implementación de la tabla hash no utiliza
dict, set ni la función hash() de Python.
"""

from typing import Optional


class Nodo:
    """Representa un nodo de una lista enlazada simple."""

    def __init__(self, clave: int, valor: str) -> None:
        """Inicializa un nodo.

        Args:
            clave: Clave entera almacenada en el nodo.
            valor: Valor asociado con la clave.

        Returns:
            None.
        """
        self.clave = clave
        self.valor = valor
        self.siguiente: Optional["Nodo"] = None


class ListaEnlazada:
    """Implementa una lista enlazada simple con inserción al inicio."""

    def __init__(self) -> None:
        """Inicializa una lista enlazada vacía.

        Args:
            No recibe argumentos.

        Returns:
            None.
        """
        self.cabeza: Optional[Nodo] = None
        self.tamano = 0


    def insertar(self, clave: int, valor: str) -> None:
        """Inserta o actualiza un elemento de la lista.

        Si la clave ya existe, actualiza su valor. En caso contrario,
        crea un nuevo nodo al inicio de la lista.

        Args:
            clave: Clave entera que identifica el elemento.
            valor: Valor asociado con la clave.

        Returns:
            None.
        """
        actual = self.cabeza

        while actual is not None:
            if actual.clave == clave:
                actual.valor = valor
                return
            actual = actual.siguiente

        nuevo = Nodo(clave, valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1


    def buscar(self, clave: int) -> Optional[str]:
        """Busca una clave recorriendo secuencialmente la lista.

        Args:
            clave: Clave entera que se desea localizar.

        Returns:
            El valor asociado con la clave si existe; de lo contrario,
            None.
        """
        actual = self.cabeza

        while actual is not None:
            if actual.clave == clave:
                return actual.valor
            actual = actual.siguiente

        return None


    def longitud(self) -> int:
        """Obtiene la cantidad de elementos almacenados.

        Args:
            No recibe argumentos.

        Returns:
            Número de nodos almacenados en la lista.
        """
        return self.tamano


class TablaHash:
    """Implementa una tabla hash con encadenamiento separado.

    La función utilizada es el método de la división:

        h(k) = k mod m

    Cada cajón contiene una ListaEnlazada.
    """

    def __init__(self, capacidad: int) -> None:
        """Inicializa una tabla hash vacía.

        Args:
            capacidad: Número de cajones de la tabla hash.

        Returns:
            None.

        Raises:
            ValueError: Si la capacidad no es un entero positivo.
        """
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")

        self.capacidad = capacidad
        self.tabla = [
            ListaEnlazada() for _ in range(capacidad)
        ]
        self.tamano = 0


    def _indice(self, clave: int) -> int:
        """Calcula el cajón correspondiente a una clave.

        Args:
            clave: Clave entera que se desea transformar.

        Returns:
            Índice del cajón calculado mediante k mod m.
        """
        return clave % self.capacidad


    def insertar(self, clave: int, valor: str) -> None:
        """Inserta o actualiza una clave en la tabla hash.

        Las colisiones se resuelven mediante encadenamiento separado.

        Args:
            clave: Clave entera que identifica el elemento.
            valor: Valor asociado con la clave.

        Returns:
            None.
        """
        indice = self._indice(clave)
        lista = self.tabla[indice]

        if lista.buscar(clave) is None:
            self.tamano += 1

        lista.insertar(clave, valor)


    def buscar(self, clave: int) -> Optional[str]:
        """Busca una clave dentro de la tabla hash.

        Args:
            clave: Clave entera que se desea localizar.

        Returns:
            El valor asociado con la clave si existe; de lo contrario,
            None.
        """
        indice = self._indice(clave)
        return self.tabla[indice].buscar(clave)


    def factor_carga(self) -> float:
        """Calcula el factor de carga de la tabla.

        El factor de carga se define como alfa = n / m.

        Args:
            No recibe argumentos.

        Returns:
            Factor de carga actual de la tabla hash.
        """
        return self.tamano / self.capacidad


    def longitud_cajon(self, indice: int) -> int:
        """Obtiene la cantidad de elementos de un cajón.

        Este método se utiliza principalmente para verificar colisiones
        durante las pruebas.

        Args:
            indice: Índice del cajón que se desea consultar.

        Returns:
            Número de elementos almacenados en el cajón.

        Raises:
            IndexError: Si el índice está fuera de los límites.
        """
        if indice < 0 or indice >= self.capacidad:
            raise IndexError("Índice de cajón fuera de rango.")

        return self.tabla[indice].longitud()