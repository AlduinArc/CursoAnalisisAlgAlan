# Laboratorio de Tabla Hash — Rutas del Caribe

**Estudiante:** Alan Arias Ruiz

---

# Reproducción del experimento

El laboratorio fue desarrollado utilizando **Python 3**. Para reproducir las pruebas funcionales y las mediciones experimentales se debe ingresar a la carpeta del proyecto, crear y activar un entorno virtual e instalar la dependencia utilizada para generar las gráficas.

## 1. Crear el entorno virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Instalar la dependencia

Con el entorno virtual activado:

```bash
pip install matplotlib
```

## 3. Ejecutar las pruebas

Las pruebas de la Parte 1 se ejecutan mediante:

```bash
python pruebas.py
```

Si todas las pruebas son correctas, se muestra:

```text
Todas las pruebas finalizaron correctamente.
```

## 4. Ejecutar las mediciones

Los experimentos de la Parte 2 y la generación de las dos gráficas se ejecutan mediante:

```bash
python medicion.py
```

El programa genera:

```text
graficas/
├── lista_vs_tabla.png
└── tiempo_vs_alfa.png
```

Los datos aleatorios se generan utilizando una semilla fija (`2026`) para facilitar la reproducción del experimento.

---

# Parte 1 — Implementación y verificación de las estructuras

**Código de las estructuras:** [estructuras.py](estructuras.py)  
**Código de las pruebas:** [pruebas.py](pruebas.py)

Se implementaron tres componentes principales:

- `Nodo`: representa cada elemento de una lista enlazada.
- `ListaEnlazada`: almacena los códigos de guía mediante nodos enlazados.
- `TablaHash`: utiliza una tabla de casillas y una lista enlazada en cada casilla para resolver colisiones mediante **encadenamiento separado**.

La función hash utilizada es la función de división:

\[
h(k)=k\bmod m
\]

donde \(k\) es el código de guía y \(m\) es el número de casillas de la tabla.

## Casos verificados

Las pruebas cubren:

1. Creación de nodos.
2. Inserción en la lista enlazada.
3. Búsqueda exitosa en la lista.
4. Búsqueda no exitosa en la lista.
5. Inserción en la tabla hash.
6. Búsqueda exitosa en la tabla hash.
7. Búsqueda no exitosa en la tabla hash.
8. Verificación del tamaño de las estructuras.
9. Cálculo del factor de carga.
10. Manejo de colisiones mediante encadenamiento.
11. Comparación de los resultados de la lista y la tabla hash sobre colecciones aleatorias.

### Colisión controlada

Para comprobar directamente el manejo de colisiones se utilizó una tabla con:

\[
m=7
\]

y las claves:

\[
10,\;24,\;17
\]

Las tres claves producen el mismo índice:

\[
10\bmod7=3
\]

\[
24\bmod7=3
\]

\[
17\bmod7=3
\]

Por lo tanto, las tres claves se almacenan en la misma casilla:

```text
casilla 3 → 10 → 24 → 17 → None
```

Las pruebas verifican que las tres claves puedan insertarse y que posteriormente cada una pueda encontrarse correctamente.

### Colecciones aleatorias

Además de los casos controlados, se probaron **25 colecciones aleatorias** utilizando una semilla fija.

Para cada colección se realizaron búsquedas de claves presentes y ausentes. Los resultados obtenidos mediante la lista enlazada y la tabla hash se compararon para comprobar que ambas estructuras entregaran la misma respuesta.

Esto permite comprobar no solamente los casos específicos de colisión, sino también el comportamiento de las estructuras sobre diferentes distribuciones de códigos de guía.

---

# Parte 2 — Medición experimental

**Código utilizado para las mediciones:** [medicion.py](medicion.py)

Las mediciones se realizaron exclusivamente sobre las operaciones de búsqueda utilizando:

```python
time.perf_counter()
```

La construcción de las estructuras, la generación de los datos y la generación de las gráficas no forman parte del intervalo cronometrado.

Para disminuir la influencia del ruido producido por el sistema operativo y otros procesos en segundo plano, cada configuración se ejecutó **7 veces** y se utilizó la **mediana** como resultado representativo.

Cada medición realizó **200 búsquedas no exitosas**.

---

## Experimento A — Lista enlazada frente a tabla hash

Se utilizaron los siguientes tamaños de colección:

\[
n\in\{100,\;500,\;1000,\;5000,\;20000,\;50000\}
\]

Para cada valor de \(n\), el tamaño \(m\) de la tabla hash se seleccionó como un número primo cercano a:

\[
m\approx\frac{n}{2}
\]

De esta forma se mantuvo un factor de carga aproximadamente igual a:

\[
\alpha=\frac{n}{m}\approx2
\]

Los valores utilizados fueron:

| \(n\) | \(m\) | \(\alpha\) aproximado |
|---:|---:|---:|
| 100 | 53 | 1.887 |
| 500 | 251 | 1.992 |
| 1.000 | 503 | 1.988 |
| 5.000 | 2.503 | 1.998 |
| 20.000 | 10.007 | 1.999 |
| 50.000 | 25.007 | 2.000 |

Las búsquedas fueron no exitosas, es decir, se utilizaron códigos que no estaban almacenados en las estructuras.

Esta elección permite observar dos comportamientos teóricos diferentes.

Para la lista enlazada, una búsqueda no exitosa debe recorrer todos los elementos:

\[
T_{\text{lista}}(n)=\Theta(n)
\]

Para la tabla hash con encadenamiento, bajo el supuesto de una distribución aproximadamente uniforme:

\[
T_{\text{hash}}(n)=\Theta(1+\alpha)
\]

Como \(\alpha\) se mantiene aproximadamente constante alrededor de 2, el costo esperado de búsqueda de la tabla hash no crece proporcionalmente con \(n\).

### Gráfica

![Comparación del tiempo de búsqueda entre lista enlazada y tabla hash](graficas/lista_vs_tabla.png)

La gráfica permite observar la diferencia entre ambas estructuras a medida que aumenta el número de elementos. El crecimiento de la lista está asociado directamente con \(n\), mientras que la tabla hash mantiene un comportamiento mucho más estable debido a que su factor de carga se conserva aproximadamente constante.

---

## Experimento B — Efecto del factor de carga

En este experimento se mantuvo constante:

\[
n=20\,000
\]

y se modificó el tamaño de la tabla para obtener cuatro valores objetivo del factor de carga:

\[
\alpha\in\{0.5,\;1,\;4,\;10\}
\]

El tamaño de la tabla se determinó aproximadamente mediante:

\[
m\approx\frac{n}{\alpha}
\]

y se seleccionó un número primo cercano.

Se obtuvieron los siguientes resultados:

| Alfa objetivo | \(m\) (casillas) | Alfa real | Tiempo de búsqueda Hash (μs) |
|---:|---:|---:|---:|
| 0.500 | 40.009 | 0.500 | 0.127 |
| 1.000 | 19.997 | 1.000 | 0.144 |
| 4.000 | 4.999 | 4.001 | 0.256 |
| 10.000 | 1.999 | 10.005 | 0.509 |

Los resultados muestran que el tiempo aumenta conforme aumenta el factor de carga.

Entre los extremos del experimento, el tiempo pasó de:

\[
0.127\ \mu s
\]

con:

\[
\alpha=0.500
\]

a:

\[
0.509\ \mu s
\]

con:

\[
\alpha=10.005
\]

Por tanto, el tiempo medido en el último caso fue aproximadamente **4.0 veces** el del primer caso.

Esto coincide con la predicción teórica:

\[
T(\alpha)=\Theta(1+\alpha)
\]

porque al aumentar \(\alpha\), aumenta la cantidad promedio de elementos almacenados en cada cadena.

El crecimiento no es perfectamente lineal entre los cuatro puntos porque el tiempo medido también contiene constantes de implementación y efectos propios del entorno de ejecución de Python. Sin embargo, la tendencia experimental coincide con el comportamiento esperado.

### Gráfica

![Tiempo de búsqueda de la tabla hash según el factor de carga](graficas/tiempo_vs_alfa.png)

---

# Parte 3 — Análisis

## 1. ¿Cuál es el costo teórico de buscar en una lista enlazada frente a una tabla hash?

En una lista enlazada la búsqueda es secuencial. Para una búsqueda no exitosa se deben recorrer todos los elementos, por lo que:

\[
T_{\text{lista}}(n)=\Theta(n)
\]

En el peor caso de una búsqueda exitosa también puede ser necesario recorrer prácticamente toda la estructura.

En una tabla hash con encadenamiento, el índice se obtiene directamente mediante:

\[
h(k)=k\bmod m
\]

y posteriormente se busca dentro de la cadena correspondiente.

Si las claves se distribuyen aproximadamente de manera uniforme, la longitud esperada de una cadena está relacionada con el factor de carga:

\[
\alpha=\frac{n}{m}
\]

Por ello, el costo esperado de una búsqueda es:

\[
T_{\text{hash}}=\Theta(1+\alpha)
\]

Si se mantiene \(\alpha=\Theta(1)\), entonces:

\[
T_{\text{hash}}=\Theta(1)
\]

Por tanto, para búsquedas exactas por código de guía, la tabla hash presenta una ventaja teórica importante frente a la lista enlazada cuando el número de registros aumenta.

---

## 2. ¿Cómo se relacionan los factores de crecimiento teóricos con los tiempos medidos?

El Experimento A mantiene aproximadamente:

\[
\alpha\approx2
\]

mientras aumenta \(n\).

Para la lista enlazada, el costo de una búsqueda no exitosa es:

\[
\Theta(n)
\]

por lo que duplicar aproximadamente la cantidad de elementos implica aumentar también la cantidad de elementos que deben revisarse.

En la tabla hash, en cambio:

\[
T_{\text{hash}}=\Theta(1+\alpha)
\]

y como \(\alpha\) se mantiene aproximadamente constante, la cantidad esperada de elementos revisados dentro de una cadena no crece proporcionalmente con \(n\).

Por eso las dos curvas de la gráfica del Experimento A presentan comportamientos diferentes: la curva de la lista aumenta conforme crece el tamaño de la colección, mientras que la curva de la tabla hash permanece mucho más estable.

La diferencia es especialmente relevante en los tamaños grandes utilizados en el experimento. La interpretación no se basa únicamente en la forma de la gráfica, sino en que los parámetros utilizados mantienen aproximadamente constante el factor de carga y, por tanto, permiten comparar directamente el crecimiento de la lista con el comportamiento esperado de la tabla hash.

---

## 3. ¿Por qué las colisiones afectan el rendimiento de una tabla hash?

Una colisión ocurre cuando diferentes claves producen el mismo índice:

\[
h(k_1)=h(k_2)
\]

Con el método de encadenamiento, las claves que colisionan se almacenan en una misma lista:

```text
casilla 3 → k1 → k2 → k3 → None
```

Una búsqueda primero calcula el índice y después debe recorrer la cadena hasta encontrar la clave o determinar que no existe.

Por tanto, si las colisiones aumentan, también aumenta la longitud de las cadenas y el número esperado de comparaciones.

El factor de carga permite expresar este comportamiento:

\[
\alpha=\frac{n}{m}
\]

Con \(\alpha=0.5\), el experimento obtuvo:

\[
0.127\ \mu s
\]

por búsqueda, mientras que con:

\[
\alpha=10.005
\]

obtuvo:

\[
0.509\ \mu s
\]

Es decir, el tiempo medido aumentó aproximadamente cuatro veces al pasar del menor al mayor factor de carga utilizado.

Esto proporciona evidencia experimental de que una mayor concentración de elementos por casilla incrementa el costo de búsqueda.

---

## 4. ¿Cuándo sería preferible un árbol de búsqueda binaria?

La tabla hash es especialmente adecuada cuando la operación principal es una búsqueda exacta:

```text
¿Existe la guía 1234567890?
```

Sin embargo, una tabla hash no mantiene las claves ordenadas.

Por ejemplo, una operación como:

```text
Mostrar todas las guías entre 1000000000 y 2000000000.
```

requiere una consulta por rango.

En este escenario sería preferible un árbol de búsqueda binaria balanceado, porque mantiene los elementos ordenados y permite buscar en:

\[
\Theta(\log n)
\]

Una consulta de rango puede realizarse en:

\[
\Theta(\log n+k)
\]

donde \(k\) es la cantidad de elementos que pertenecen al rango.

Por lo tanto, la selección depende de la operación requerida:

- **Búsqueda exacta por código:** tabla hash.
- **Consultas por rango:** árbol de búsqueda balanceado.
- **Recorrido ordenado:** árbol de búsqueda balanceado.

La tabla hash no debe considerarse superior para cualquier tipo de consulta; su principal ventaja está en las búsquedas por igualdad.

---

## 5. ¿Qué ocurriría si Rutas del Caribe tuviera 5.000.000 de envíos?

Con una lista enlazada, una búsqueda no exitosa podría recorrer los:

\[
5\,000\,000
\]

elementos, por lo que su costo seguiría siendo:

\[
\Theta(n)
\]

La tabla hash permite analizar el problema de una manera diferente porque el costo depende del factor de carga:

\[
\alpha=\frac{n}{m}
\]

Si se desea mantener:

\[
\alpha\approx2
\]

para:

\[
n=5\,000\,000
\]

se necesita aproximadamente:

\[
m=\frac{5\,000\,000}{2}=2\,500\,000
\]

casillas.

En ese escenario:

\[
T_{\text{hash}}
=
\Theta(1+\alpha)
=
\Theta(1+2)
=
\Theta(1)
\]

Por lo tanto, el crecimiento del número de envíos no implica que una búsqueda deba recorrer proporcionalmente los cinco millones de registros, siempre que la tabla se dimensione para conservar un factor de carga razonable.

Como contraste, si se mantuviera una tabla de solamente:

\[
m=200\,000
\]

casillas, el factor de carga sería:

\[
\alpha=
\frac{5\,000\,000}{200\,000}
=25
\]

y el costo esperado sería:

\[
\Theta(1+25)
\]

Las cadenas serían mucho más largas y el rendimiento disminuiría.

Por esta razón, para un sistema con cinco millones de envíos no basta con elegir una tabla hash: también es necesario controlar su factor de carga. En una implementación real, esto se resolvería redimensionando la tabla cuando el factor de carga supere un umbral determinado.

La tabla hash sería, por tanto, una buena elección para búsquedas exactas de códigos de guía a gran escala, mientras que para consultas por rangos o que requieran mantener los envíos ordenados sería más conveniente una estructura de búsqueda balanceada.