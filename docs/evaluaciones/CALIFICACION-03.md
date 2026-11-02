# Retroalimentación — Laboratorio 03 Estructuras de datos

**Estudiante:** Alan Arias Ruiz · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `b342480`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 7 / 20 |
| Calidad de la explicación teórica | 13 / 20 |
| Corrección de la implementación | 20 / 25 |
| Calidad del análisis de las gráficas | 17 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **65 / 100** |
| **Nota (0–5)** | **3.25** |

## 1. Corrección conceptual (7 / 20)
**Lo que hizo bien:**
- Explica la colisión con el ejemplo de `10`, `24` y `17` con `m = 7` y dice que las tres van a la casilla 3.
- Reconoce que la tabla hash no sirve para consultas por rango y que el árbol balanceado sí.

**Lo que puede mejorar (y cómo corregirlo):**
- La pregunta 3 no explica por qué ocurre una colisión aunque haya más casillas que guías, ni compara el encadenamiento con el direccionamiento abierto (ventajas y costos).
  → *Cómo corregirlo:* responda dos cosas por separado: por qué dos guías distintas pueden dar el mismo resultado de `k mod m`, y qué hace cada método con la guía que encuentra su casilla ocupada.
- La pregunta 4 no dice qué pasa si las 400.000 guías llegan ordenadas y se insertan una a una en un árbol de búsqueda, ni estima la altura ni las comparaciones.
  → *Cómo corregirlo:* piense hacia qué lado se va cada guía nueva, cuántos niveles quedan, y compárelo con un árbol equilibrado de 400.000 elementos.
- La pregunta 5 no estima cuánto tardaría una búsqueda de guía inexistente con 5.000.000 de envíos en cada estructura, y no la declara como estimación. Además el texto termina cortado a mitad de una frase.
  → *Cómo corregirlo:* use sus mediciones y la forma de cada curva (lineal para la lista, casi plana para la tabla con `α` fija) para proyectar un tiempo, dígalo como estimación y termine la frase pendiente.

## 2. Calidad de la explicación teórica (13 / 20)
**Lo que hizo bien:**
- Explica que la búsqueda en la lista recorre los nodos y que en el peor caso, con todas las guías en una casilla, la tabla se comporta como una lista.

**Lo que puede mejorar (y cómo corregirlo):**
- No nombra el supuesto de hash uniforme; habla de una "distribución adecuada" sin precisarla.
  → *Cómo corregirlo:* diga con una frase qué debe cumplir la función hash al repartir las guías entre las casillas.
- Para la lista inexistente no se justifica el `Θ(n)` con claridad (menciona mejor caso, promedio y peor caso en general).
  → *Cómo corregirlo:* razone solo sobre la guía inexistente: cuántos nodos revisa siempre antes de poder responder.

## 3. Corrección de la implementación (20 / 25)
**Lo que hizo bien:**
- Las dos estructuras buscan bien (exitosas e infructuosas), la tabla reutiliza `ListaEnlazada` sin `dict`, `set` ni `hash()`, y `factor_carga` funciona.
- `pruebas.py` cubre la colisión forzada con `m = 7`, el factor de carga y 25 colecciones aleatorias. Las funciones tienen *docstrings* con `Args` y `Returns` y *type hints*.

**Lo que puede mejorar (y cómo corregirlo):**
- `ListaEnlazada.insertar` recorre toda la lista para revisar si la guía ya existe, así que ya no cuesta `Θ(1)` como pedía el enunciado (se asumía que las guías no se repiten). En la tabla, además, `insertar` busca antes de insertar.
  → *Cómo corregirlo:* quite la búsqueda previa y deje solo crear el nodo, enlazarlo con la cabeza y actualizar el tamaño.
- Las firmas cambiaron respecto a las pedidas (`clave`/`valor` en lugar de `guia`/`estado`, `capacidad` en lugar de `m`, `tabla` en lugar de `casillas`, y falta el método `hash`).
  → *Cómo corregirlo:* use los nombres del enunciado, incluido un método `hash(self, guia)` que devuelva `guia % m`.

## 4. Calidad del análisis de las gráficas (17 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda en la primera. La primera usa seis valores de `n` con las dos curvas en los mismos ejes, y la segunda cuatro valores de `α`.
- Presenta tablas con `m` y el `α` real, y dice que usó 200 búsquedas y la mediana de 7 repeticiones.

**Lo que puede mejorar (y cómo corregirlo):**
- La pregunta 2 no toma dos valores consecutivos de `n` para calcular cuánto se multiplicó el tiempo de cada estructura, así que no contrasta con `Θ(n)` y `Θ(1)`. Solo dice "sí coincide".
  → *Cómo corregirlo:* lea de la primera gráfica los tiempos de dos `n` consecutivos, divida los tiempos y compare esa razón con la razón de los `n`.
- Para la segunda gráfica compara solo los extremos (de `α = 0.5` a `α = 10`) y no lo relaciona con `Θ(1 + α)`.
  → *Cómo corregirlo:* revise si el aumento de tiempo acompaña al aumento de `α` en la forma que predice `1 + α`.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- Cumple la estructura de carpetas (`lab3-estructuras-datos/` con los cuatro archivos y las dos gráficas). El informe lleva su nombre, instrucciones de reproducción, enlaces al código en cada parte y las gráficas se ven con ruta relativa.
- Tiene siete commits con mensajes descriptivos.

**Lo que puede mejorar (y cómo corregirlo):**
- El informe termina cortado a mitad de la pregunta 5, y las preguntas 2 a 5 no responden lo que pide cada enunciado (la 3 trata del rendimiento y la 4 de "por qué tabla y no árbol").
  → *Cómo corregirlo:* revise que cada respuesta corresponda a la pregunta del laboratorio y complete el final del archivo.

## ¿El código funciona?
Sí. Las pruebas pasan y el programa de medición corre completo y genera las dos gráficas. Las estructuras devuelven resultados correctos.
