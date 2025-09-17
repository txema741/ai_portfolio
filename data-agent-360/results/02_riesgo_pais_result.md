# Ejercicio 2 – Evaluación de Riesgo País (España)

**Dataset:** `data_sample\riesgo_pais_spain_real.xlsx`

## Perfil de calidad del dataset
- Filas totales: 3
- Nulos por columna: `{'año': 0, 'deuda_publica_pct_pib': 1, 'deuda_externa_pct_pib': 3, 'balanza_comercial_musd': 1, 'inflacion_anual_pct': 1, 'crecimiento_pib_pct': 1}`

## Umbrales de riesgo aplicados
- deuda_publica_pct_pib > 95.0
- deuda_externa_pct_pib > 110.0 (si N/D, no puntúa)
- balanza_comercial_musd < 0 (déficit)
- inflacion_anual_pct > 4.0
- crecimiento_pib_pct < 0

## Resultado por año
|   año | deuda_publica_pct_pib   | deuda_externa_pct_pib   | balanza_comercial_musd   | inflacion_anual_pct   | crecimiento_pib_pct   | flags_activas                         |   score_riesgo | nivel_riesgo   |
|------:|:------------------------|:------------------------|:-------------------------|:----------------------|:----------------------|:--------------------------------------|---------------:|:---------------|
|  2023 | 107.7                   | N/D                     | -37200.0                 | 3.1                   | 2.5                   | deuda_publica_alta, deficit_comercial |              2 | Medio          |
|  2024 | 106.5                   | N/D                     | -18000.0                 | 3.4                   | 1.9                   | deuda_publica_alta, deficit_comercial |              2 | Medio          |
|  2025 | N/D                     | N/D                     | N/D                      | N/D                   | N/D                   | -                                     |              0 | Bajo           |

## Interpretación (ejemplo consultivo)
- *Bajo*: situación controlada; mantener vigilancia macro habitual.
- *Medio*: hay tensiones (p. ej., deuda/deflactor o déficit externo) → revisar liquidez y cobertura.
- *Alto*: multiplicidad de riesgos; activar planes de contingencia (hedging, diversificación de mercados/proveedores, seguros de crédito a la exportación).

## Fuentes (debes completar con tus URLs oficiales)
- Eurostat (deuda pública, balanza comercial)
- OCDE (crecimiento PIB)
- IMF SDDS (deuda externa)


## Validación
- Nivel de confianza: Alta (reglas reproducibles; datos de fuentes oficiales).
- Limitaciones: si algún valor es N/D, la regla asociada no puntúa; el análisis depende de la cobertura de la fuente.
