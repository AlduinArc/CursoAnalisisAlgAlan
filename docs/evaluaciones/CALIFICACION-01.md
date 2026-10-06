# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Alan Arias Ruiz · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `3085dd2`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 25 |
| Calidad de la explicación teórica | 17 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 15 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **73 / 100** |
| **Nota (0–5)** | **3.65** |

## 1. Corrección conceptual (16 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el algoritmo sea correcto y que quepa en la ventana de cuatro horas.
- Explica que duplicar la velocidad del servidor no cambia el crecimiento cuadrático del algoritmo.
- En la Parte 2 identifica dos perjuicios (el paciente y los operadores) e indica quién asume el costo, y habla de que el orden decide a quién se llama primero.

**Lo que puede mejorar:**
- El segundo ejemplo de la Parte 1 es genérico: no dice qué sistema es, cuántos datos tiene ni qué restricción concreta se incumple. Debía ser un caso propio, con cifras.
- La relación entre tiempo de ejecución y consumo de energía se queda en lo general: faltó un cálculo o una estimación del consumo acumulado de todas las madrugadas durante años.
- Los dos perjuicios de la Parte 2 son muy parecidos entre sí; el segundo (los operadores) no es tan claro como perjuicio individual.

## 2. Calidad de la explicación teórica (17 / 25)
**Lo que hizo bien:**
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro, verificando la condición del caso 2.
- Incluye la predicción antes del experimento y justifica que usaría el peor caso para decidir si entra en producción.
- La tabla de complejidades está completa.

**Lo que puede mejorar:**
- Al definir los tres casos no dice sobre qué conjunto de entradas (de tamaño fijo n) se toma el máximo, el mínimo o el promedio.
- El cálculo de insertion sort no es "línea a línea": solo cuenta comparaciones. Faltó indicar cuántas veces se ejecuta cada línea del código y sumar sus costos.
- La tabla del escenario A en la Parte 3.2 tiene casillas de comparaciones vacías ("—").

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista original y cuentan las comparaciones entre elementos (el conteo da n − 1 en una lista ya ordenada). No usan `sorted()` ni `sort()`.
- `merge_sort` tiene su propia mezcla recursiva. Los generadores dan listas del tamaño pedido, sin repetidos y con semilla.

**Lo que puede mejorar:**
- En `generar_inverso` el texto de ayuda quedó mal armado (la parte de "Returns" quedó pegada a "Args").
- Algunos parámetros (`generador`, `algoritmo`) no tienen tipo, y se usó `__import__("math")` en lugar de un import normal.
- Los cuatro archivos `.py` terminan sin salto de línea final.

## 4. Calidad del análisis de las gráficas (15 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes con unidades y leyenda. Las de la Parte 3 muestran los tres escenarios en los mismos ejes.
- Identifica el escenario inverso como peor caso, el casi ordenado como mejor y el aleatorio como intermedio, y la conclusión de la Parte 4 coincide con lo que muestra la curva.
- El concepto técnico recomienda merge sort, declara la extrapolación como estimación y menciona memoria y cambio del escenario B.

**Lo que puede mejorar:**
- Las gráficas publicadas usan tamaños (hasta 6400) distintos a los que dice el informe (hasta 6000).
- No explica qué pasa con los tamaños pequeños, donde las dos curvas casi se juntan.
- En el concepto para la Secretaría falta decir con claridad si cada algoritmo cabe en las cuatro horas, y la respuesta sobre el servidor del doble de velocidad no cita la gráfica ni el tamaño de donde sale el dato.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Estructura de carpetas correcta, imágenes visibles, enlaces al código en las Partes 3 y 4 y siete commits descriptivos.

**Lo que puede mejorar:**
- Las instrucciones para reproducir solo sirven para Windows y no explican cómo crear el entorno virtual.

## ¿El código funciona?
Sí. Los scripts corren sin errores, ordenan bien y generan las gráficas.

## Para el próximo laboratorio
- Dar ejemplos propios con datos (qué se procesa, cuántos datos, qué límite se incumple).
- Cuando se pida un cálculo línea a línea, escribir cuántas veces se ejecuta cada línea y sumar.
- Dejar las tablas completas y las gráficas publicadas generadas con los mismos parámetros que describe el informe.
- Responder cada propuesta con el dato medido y citar la gráfica y el tamaño de donde sale.
- Revisar los textos de ayuda de las funciones y poner tipos a todos los parámetros.
