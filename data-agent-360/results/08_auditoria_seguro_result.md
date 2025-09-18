# Ejercicio 8 – Auditoría de Pólizas y Siniestros de Seguros
**Metodología:** Self-Consistency + CoT vectorizado  
**Sector:** Seguros y gestión de riesgos

---

## 🗓️ Ejecución
- Fecha y hora: **2025-09-18 11:54**
- Filas totales (entrada): **322**

## 📊 Resumen de incidencias
- Duplicados por ID: **44**
- Duplicados por clave: **20**
- Fecha póliza nula: **0**
- Fecha siniestro nula: **0**
- Siniestro antes de póliza: **33**
- Fecha póliza fuera de rango: **0**
- Monto póliza inválido: **0**
- Monto siniestro negativo: **15**
- Monto siniestro > póliza: **0**
- Tipo de póliza inválido: **20**
- Asegurado vacío: **0**
- Beneficiario vacío: **0**
- Descripción vacía: **0**

## 📑 Ejemplos
**Duplicados por ID_Poliza**
|   ID_Poliza | Asegurado      | Tipo_Poliza   | Fecha_Poliza   |   Monto_Poliza |
|------------:|:---------------|:--------------|:---------------|---------------:|
|      800031 | Alberto Romero | Vida          | 2008-02-23     |        61129.2 |
|      800037 | Sara Morales   | Auto          | 2009-10-24     |        42857.9 |
|      800038 | Pedro López    | Vida          | 2008-09-10     |        63505.9 |
|      800039 | Pedro López    | Hogar         | 2009-04-18     |        82064.4 |
|      800044 | Lucía Vázquez  | Viaje         | 2020-09-10     |        96061.4 |
|      800053 | Lucía Vázquez  | Auto          | 2008-09-15     |        10497.1 |
|      800057 | Ana Martínez   | Auto          | 2050-07-06     |        11033.6 |
|      800066 | Ana Martínez   | Hogar         | 2011-07-22     |        39605.6 |
|      800095 | Sara Morales   | Auto          | 2018-05-28     |        30720.7 |
|      800114 | Miguel Navarro | Invalida      | 2050-02-03     |        44663.1 |
|      800149 | Lucía Vázquez  | Auto          | 2022-09-26     |        22192.8 |
|      800150 | Carlos Ruiz    | Viaje         | 2005-05-10     |        20534.8 |
**Duplicados por clave (Asegurado, Tipo_Poliza, Fecha_Poliza)**
|   ID_Poliza | Asegurado       | Tipo_Poliza   | Fecha_Poliza   |   Monto_Poliza |
|------------:|:----------------|:--------------|:---------------|---------------:|
|      800037 | Sara Morales    | Auto          | 2009-10-24     |        42857.9 |
|      800057 | Ana Martínez    | Auto          | 2050-07-06     |        11033.6 |
|      800066 | Ana Martínez    | Hogar         | 2011-07-22     |        39605.6 |
|      800114 | Miguel Navarro  | Invalida      | 2050-02-03     |        44663.1 |
|      800150 | Carlos Ruiz     | Viaje         | 2005-05-10     |        20534.8 |
|      800177 | Marta Fernández | Auto          | 2014-03-29     |        55903.6 |
|      800204 | Lucía Vázquez   | Salud         | 2015-01-27     |        53056   |
|      800249 | Juan Pérez      | Vida          | 2023-05-23     |        62386.8 |
|      800254 | Marta Fernández | Auto          | 2005-06-23     |        73169.4 |
|      800280 | Juan Pérez      | Salud         | 2019-10-24     |        43124.1 |
|      800254 | Marta Fernández | Auto          | 2005-06-23     |        73169.4 |
|      800057 | Ana Martínez    | Auto          | 2050-07-06     |        11033.6 |
**Siniestro antes de póliza**
|   ID_Poliza | Fecha_Poliza   | Fecha_Siniestro   | Asegurado      |
|------------:|:---------------|:------------------|:---------------|
|      800001 | 2050-12-21     | 2007-03-03        | Ana Martínez   |
|      800003 | 2050-09-14     | 2009-07-17        | Alberto Romero |
|      800004 | 2020-01-09     | 2020-01-08        | Laura Gómez    |
|      800007 | 2050-11-19     | 2007-07-10        | Ana Martínez   |
|      800015 | 2014-06-20     | 2014-06-19        | Alberto Romero |
|      800030 | 2023-03-23     | 2023-03-21        | Pedro López    |
|      800031 | 2008-02-23     | 2008-02-17        | Alberto Romero |
|      800057 | 2050-07-06     | 2019-05-12        | Ana Martínez   |
|      800073 | 2050-05-04     | 2013-03-23        | Carlos Ruiz    |
|      800077 | 2019-06-24     | 2019-06-15        | Juan Pérez     |
|      800096 | 2012-09-07     | 2012-09-01        | Pedro López    |
|      800098 | 2021-11-03     | 2021-10-31        | Carlos Ruiz    |
**Tipo de póliza inválido**
|   ID_Poliza | Asegurado       | Tipo_Poliza   |
|------------:|:----------------|:--------------|
|      800114 | Miguel Navarro  | Invalida      |
|      800130 | Marta Fernández | Invalida      |
|      800168 | Sofía Torres    | Invalida      |
|      800182 | Carlos Ruiz     | Invalida      |
|      800205 | David Hernández | Invalida      |
|      800278 | David Hernández | Invalida      |
|      800293 | Sara Morales    | Invalida      |
|      800114 | Miguel Navarro  | Invalida      |
|      800273 | Pedro López     | Duplicada     |
|      800039 | Pedro López     | Duplicada     |
|      800044 | Lucía Vázquez   | Duplicada     |
|      800053 | Lucía Vázquez   | Duplicada     |
**Montos anómalos**
|   ID_Poliza |   Monto_Poliza |   Monto_Siniestro | Asegurado      |
|------------:|---------------:|------------------:|:---------------|
|      800033 |        80542.7 |         -21813.6  | Juan Pérez     |
|      800145 |        66780.9 |         -13325.6  | Miguel Navarro |
|      800152 |        63628.8 |         -44971.4  | Miguel Navarro |
|      800195 |        88833.6 |          -9389.14 | Sofía Torres   |
|      800198 |        79336.1 |         -18076.1  | Alberto Romero |
|      800207 |        79460.2 |         -44039    | Sara Morales   |
|      800236 |        75116.6 |         -60558.7  | Juan Pérez     |
|      800240 |        44212.3 |         -35473.9  | Sara Morales   |
|      800242 |        25752.1 |          -3096.62 | Alberto Romero |
|      800250 |        50057.4 |         -29577.3  | Juan Pérez     |
|      800273 |        81626   |         -38893.4  | Pedro López    |
|      800280 |        43124.1 |         -12614.4  | Juan Pérez     |

---
## ✅ Conclusiones
- Auditoría vectorizada y escalable con banderas por registro y `flags_total` para priorizar correcciones.
- Para producción: integrar reglas antifraude y catálogos ampliados de productos/ramas.