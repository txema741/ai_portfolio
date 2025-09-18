# Ejercicio 10 – Auditoría de Inventarios y Cadenas de Suministro
**Ejecución:** 2025-09-18 17:28  
**Filas totales (entrada):** 334

## 📊 Resumen de incidencias
- Duplicados (ID_Producto, ID_Almacén, Fecha_Entrada): **28**
- Fechas incoherentes / fuera de rango: **19**
- Cantidades inválidas: **17**
- Precios inválidos: **12**
- Códigos de producto inválidos: **17**
- Almacenes inválidos: **25**

## 📑 Ejemplos
**Duplicados por clave**
| ID_Producto   | ID_Almacén   | Fecha_Entrada   |   Cantidad |   Precio_Unitario |
|:--------------|:-------------|:----------------|-----------:|------------------:|
| PRD-00004     | ALM-0        | 2024-03-03      |        109 |             15.23 |
| PRD-00013     | ALM-99X      | 2020-08-30      |         39 |             20.95 |
| PRD-00031     | ALM-03       | 2018-02-16      |        151 |             31.63 |
| PRD-00095     | ALM-0        | 2023-12-16      |         66 |             35.87 |
| PRD-00098     | ALM-02       | 2025-08-23      |         61 |             29.44 |
| PRD-00109     | ALM-01       | 2020-08-21      |         93 |             12.74 |
| PRD-00110     | ALM-01       | 2020-02-11      |        132 |             22.35 |
| PRD-00143     | ALM-02       | 2025-07-01      |        -39 |             37.93 |
| PRD-00165     | ALM-02       | 2018-07-27      |         62 |             17.77 |
| PRD-00166     | ALM-04       | 2018-12-14      |         69 |             31.24 |
| PRD-00196     | ALM-02       | 2018-03-01      |         40 |             24.97 |
| PRD-00233     | ALM-04       | 2023-05-23      |         21 |             25.92 |
**Fechas incoherentes / fuera de rango**
| ID_Producto   | Fecha_Entrada   | Fecha_Salida   | ID_Almacén   |
|:--------------|:----------------|:---------------|:-------------|
| PRD-00015     | 2019-11-30      | 2019-11-29     | ALM-02       |
| PRD-00021     | 2021-12-16      | 2021-12-02     | ALM-05       |
| PRD-00035     | 2018-12-23      | 2018-12-20     | ALM-01       |
| PRDX-12345    | 2055-02-19      | 2023-12-09     | ALM-03       |
| PRD-00088     | 2022-01-21      | 2022-01-09     | ALM-02       |
| PRD-00117     | 2055-11-21      | 2024-04-05     | ALM-04       |
| nan           | 2019-12-05      | 2019-11-24     | ALM-03       |
| PRD-00125     | 2020-09-11      | 2020-08-29     | ALM-05       |
| PRD-00127     | 2021-09-29      | 2021-09-27     | ALM-03       |
| PRD-00194     | 2023-01-03      | 2022-12-28     | ALM-01       |
| PRD-00215     | 2055-09-03      | 2021-08-03     | ALM-01       |
| PRD-00223     | 2022-03-11      | 2022-03-05     | ALM-01       |
**Códigos de producto inválidos**
| ID_Producto   | ID_Almacén   |
|:--------------|:-------------|
| PRDX-12345    | ALM-03       |
| 12345         | ALM-01       |
| 12345         | ALM-02       |
| nan           | ALM-04       |
| PROD-00001    | ALM-02       |
| nan           | ALM-03       |
| PRDX-12345    | ALM-02       |
| 12345         | ALM-03       |
| PROD-00001    | ALM-04       |
| PRD-123       | ALM-02       |
| PRD-123       | ALM-05       |
| PROD-00001    | ALM-05       |

---
## ✅ Conclusiones
- Reglas vectorizadas y `flags_total` para priorizar correcciones.
- Recomendación: integrar maestro de productos y catálogo de almacenes de ERP/WMS.