# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Alan Arias · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `3d417e9`

Excelente trabajo, muy completo y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **96 / 100** |
| **Nota (0–5)** | **4.80** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identificó que divide y vencerás empieza a ganar entre n = 10 y n = 50, y explicó por qué en tamaños pequeños el costo de las llamadas recursivas pesa más.
- Comparó correctamente con hallar el máximo de un arreglo: combinar cuesta poco, la recurrencia da `Θ(n)` y dividir no mejora nada.
- Recomendó divide y vencerás, estimó el tiempo para 1.000.000 de registros (unas 6.9 horas contra unos 2.3 segundos) y lo declaró como estimación sin usar regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 3 pudo medir un tamaño intermedio (por ejemplo 20 o 30) para ubicar mejor el punto donde cambia el ganador.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Planteó `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término y la resolvió con el método maestro (caso 2, `Θ(n log n)`).
- Justificó el `Θ(n²)` de la fuerza bruta con la suma `n + (n-1) + ... + 1`.

**Lo que puede mejorar:**
- Al aplicar el método maestro, diga de forma explícita que se cumple la condición del caso 2 (que `f(n)` crece igual que `n^(log_b a)`), no solo que "tiene el mismo orden".

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en las veinte listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos y no llama a la fuerza bruta; ninguna función cambia la lista recibida.
- Tiene *type hints* y *docstrings* estilo Google en todas las funciones.

**Lo que puede mejorar:**
- En `subarreglo.py` falta una línea en blanco más antes de `suma_cruzada` y antes de `subarreglo_maximo` (PEP 8 pide dos entre funciones).

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con siete tamaños.
- Calculó los factores de crecimiento al duplicar n (≈3.96 y ≈2.09) y los comparó con `Θ(n²)` y `Θ(n log n)`; coinciden con lo que se ve en la gráfica (fuerza bruta cerca de 0.40 s en n = 4000, divide y vencerás pegada al eje).

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `lab2-divide-y-vencer/` y sus archivos siguen la estructura pedida.
- El informe sigue el orden pedido, enlaza el código en cada parte, la gráfica se ve y hay instrucciones claras de reproducción.
- Entregó seis commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan y la medición corre sin errores, verifica que ambos algoritmos den la misma suma y genera la gráfica.

## Para el próximo laboratorio
- Deje dos líneas en blanco entre todas las funciones, y mantenga docstrings y type hints.
- Al aplicar el método maestro, escriba la verificación de la condición del caso.
- Mida más tamaños pequeños o intermedios para ubicar mejor los puntos de cruce.
- Conserve la costumbre de repetir las mediciones y usar la mediana.
