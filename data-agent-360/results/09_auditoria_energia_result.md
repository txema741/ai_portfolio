# Ejercicio 9 – Auditoría de Consumos Energéticos y Facturación
**Metodología:** Self-Consistency + CoT vectorizado  
**Sector:** Energía (utilities)

---

## 🗓️ Ejecución
- Fecha y hora: **2025-09-18 13:17**
- Filas totales (entrada): **352**

## 📊 Resumen de incidencias
- Duplicados por ID_Factura: **20**
- Duplicados por (ID_Contrato, Periodo): **46**
- Fecha de factura fuera de rango: **15**
- Periodo inválido: **0**
- CUPS mal formado: **13**
- CP–Provincia incoherente: **21**
- Tarifa inválida: **19**
- kWh inválidos: **10**
- kW contratada inválida: **6**
- Importe sospechoso vs kWh: **27**
- Outlier kWh (p99): **4**
- Outlier Importe (p99): **4**
- Cliente vacío: **0**
- Dirección vacía: **0**

## 📑 Ejemplos
**Duplicados por (ID_Contrato, Periodo)**
| ID_Contrato   | Periodo   | ID_Factura   |     kWh |   Importe_Factura |
|:--------------|:----------|:-------------|--------:|------------------:|
| C-100873      | 2022-03   | F-700031     |  1550.9 |            328.92 |
| C-100621      | 2024-03   | F-700072     |  1120.6 |            325.85 |
| C-100131      | 2024-07   | F-700074     |   549.5 |            141.02 |
| C-100430      | 2022-01   | F-700086     | -1284   |            302.58 |
| C-100825      | 2022-09   | F-700097     |   391.4 |             89.84 |
| C-100201      | 2021-05   | F-700099     |   831.3 |            220.76 |
| C-100511      | 2020-11   | F-700103     |  1208.8 |            319.51 |
| C-100625      | 2024-01   | F-700118     |  1572.4 |            412.22 |
| C-100385      | 2022-07   | F-700133     |   898   |            173.95 |
| C-100621      | 2024-03   | F-700138     |  1322.5 |            333.2  |
| C-100322      | 2022-02   | F-700143     |   590.9 |            168.62 |
| C-100835      | 2021-05   | F-700159     |  1099.7 |            328.31 |
**CUPS mal formado**
| CUPS       | Cliente             | Periodo   |
|:-----------|:--------------------|:----------|
| XX52C70M6F | Market Ruiz         | 2023-04   |
| XXRBMDZY3K | Hotel Sánchez       | 2022-12   |
| XXZU4YWX1U | Farmacia Navarro    | 2023-09   |
| XXCVD1L9EM | Servicios López     | 2025-01   |
| XX0BPB3T1Y | Distribuciones Díaz | 2020-12   |
| XXYLZ61ILE | Panadería Ortega    | 2022-07   |
| XXFSE5JI0M | Hotel Sánchez       | 2021-05   |
| XXX99D9RPR | Distribuciones Díaz | 2024-03   |
| XXIMOD6X9J | Comercial Álvarez   | 2025-03   |
| XXAICZIPXN | Farmacia Navarro    | 2023-06   |
| XXXIGPSFKL | Hotel Sánchez       | 2022-10   |
| XXPF6RPLT2 | Servicios López     | 2022-03   |
**Importe sospechoso vs kWh**
| ID_Factura   |     kWh |   Importe_Factura |
|:-------------|--------:|------------------:|
| F-700000     |   105.4 |             41.53 |
| F-700007     |  1522.5 |             45.67 |
| F-700034     |  2600.9 |           2340.81 |
| F-700039     | 50000   |            267.24 |
| F-700061     |  1070.8 |            963.72 |
| F-700071     |   339.3 |             10.18 |
| F-700075     |   373.7 |             11.21 |
| F-700085     |   126.9 |             47.51 |
| F-700107     |   354.5 |            319.05 |
| F-700110     |  2457.8 |           2212.02 |
| F-700126     | 50000   |             63.88 |
| F-700127     |   654.6 |             19.64 |
**CP–Provincia incoherente**
|    CP | Provincia   | Cliente             |
|------:|:------------|:--------------------|
| 28001 | Barcelona   | Distribuciones Díaz |
| 41002 | Valencia    | Hostelería Gómez    |
| 46003 | Barcelona   | Panadería Ortega    |
| 48001 | Barcelona   | Hotel Sánchez       |
| 28004 | Bizkaia     | Restaurante Moreno  |
| 28005 | Bizkaia     | Farmacia Navarro    |
| 48003 | Valencia    | Market Ruiz         |
| 48002 | Valencia    | Textiles Vega       |
| 28004 | Valencia    | Restaurante Moreno  |
| 46004 | Bizkaia     | Aseguradora Vázquez |
| 28005 | Valencia    | Aseguradora Vázquez |
| 28004 | Bizkaia     | Textiles Vega       |
**Outliers (kWh o Importe)**
| ID_Factura   |     kWh |   Importe_Factura |
|:-------------|--------:|------------------:|
| F-700025     |  3210.1 |            777.67 |
| F-700034     |  2600.9 |           2340.81 |
| F-700039     | 50000   |            267.24 |
| F-700061     |  1070.8 |            963.72 |
| F-700110     |  2457.8 |           2212.02 |
| F-700126     | 50000   |             63.88 |
| F-700327     | 50000   |            275.05 |

---
## ✅ Conclusiones
- Validaciones vectorizadas y combinadas por `flags_total` para priorizar correcciones.
- Recomendación: ampliar catálogo de tarifas, mapa CP–Provincia y añadir checksum real de CUPS.