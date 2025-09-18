# Ejercicio 6 – Auditoría de Transacciones Bancarias
**Metodología:** CoT vectorizado + reglas agrupadas  
**Sector:** Banca, seguros y consultoría financiera

---

## 🗓️ Ejecución
- Fecha y hora: **2025-09-18 10:07**
- Filas totales (entrada): **326**

## 📊 Resumen de incidencias
- Duplicados por ID: **51**
- Duplicados por clave: **51**
- Fecha nula: **0**
- Fecha fuera de rango: **15**
- Moneda inválida: **71**
- IBAN inválido: **48**
- Beneficiario vacío: **11**
- Concepto vacío: **15**
- Importe incoherente (ingreso negativo): **22**

## 📑 Ejemplos
**Duplicados por ID_Transaccion**
|   ID_Transaccion | Cuenta_IBAN              | Fecha      |   Importe | Moneda   | Beneficiario        | Concepto          |
|-----------------:|:-------------------------|:-----------|----------:|:---------|:--------------------|:------------------|
|           700024 | ES3361152050341385421331 | 2024-03-13 |   6578.94 | USD      | Viajes Castro       | Bizum             |
|           700030 | ES3543815199129600860015 | 2020-03-29 |   9653.39 | GBP      | Servicios López     | Devolución recibo |
|           700051 | ES2162582108161059622679 | 2025-04-18 |  -1189.45 | EUR      | Energía Torres      | Ingreso cajero    |
|           700055 | ES4449435668367714292019 | 2000-01-15 |   8085.74 | USD      | Aseguradora Vázquez | Factura           |
|           700058 | ES095804173699380454     | 2015-04-22 |  -3221.24 | EUR      | Farmacia Navarro    | Pago proveedor    |
|           700059 | ES8320590314631054123875 | 2005-06-30 |    751.81 | EUR      | Comercial Álvarez   | nan               |
|           700061 | ES7881101670611090347771 | 2026-04-06 |    905.21 | USD      | Viajes Castro       | Ingreso cajero    |
|           700080 | ES8231679754299385581166 | 2004-05-16 |   1196.78 | EUR      | Consulting García   | Bizum             |
|           700082 | ES5429337094032021438123 | 2016-08-18 |   2263.54 | USD      | Distribuciones Díaz | Bizum             |
|           700091 | ES0243002132088852991804 | 2025-01-30 |  12619.9  | EUR      | TechNova SL         | Transferencia     |
|           700099 | ES6745912526679838694    | 2002-03-30 |   2566.17 | EUR      | Ferretería Romero   | Domiciliación     |
|           700104 | E7597589075763468555542  | 2025-05-10 |  -4969.69 | GBP      | Viajes Castro       | Domiciliación     |
**Duplicados por clave (IBAN, Fecha, Importe, Beneficiario)**
| Cuenta_IBAN              | Fecha      |   Importe | Beneficiario        | Concepto          |
|:-------------------------|:-----------|----------:|:--------------------|:------------------|
| ES3361152050341385421331 | 2024-03-13 |   6578.94 | Viajes Castro       | Bizum             |
| ES3543815199129600860015 | 2020-03-29 |   9653.39 | Servicios López     | Devolución recibo |
| ES2162582108161059622679 | 2025-04-18 |  -1189.45 | Energía Torres      | Ingreso cajero    |
| ES4449435668367714292019 | 2000-01-15 |   8085.74 | Aseguradora Vázquez | Factura           |
| ES095804173699380454     | 2015-04-22 |  -3221.24 | Farmacia Navarro    | Pago proveedor    |
| ES8320590314631054123875 | 2005-06-30 |    751.81 | Comercial Álvarez   | nan               |
| ES7881101670611090347771 | 2026-04-06 |    905.21 | Viajes Castro       | Ingreso cajero    |
| ES8231679754299385581166 | 2004-05-16 |   1196.78 | Consulting García   | Bizum             |
| ES5429337094032021438123 | 2016-08-18 |   2263.54 | Distribuciones Díaz | Bizum             |
| ES0243002132088852991804 | 2025-01-30 |  12619.9  | TechNova SL         | Transferencia     |
| ES6745912526679838694    | 2002-03-30 |   2566.17 | Ferretería Romero   | Domiciliación     |
| E7597589075763468555542  | 2025-05-10 |  -4969.69 | Viajes Castro       | Domiciliación     |
**Fechas fuera de rango (futuras o < 2000-01-01)**
|   ID_Transaccion | Fecha      |   Importe | Beneficiario        |
|-----------------:|:-----------|----------:|:--------------------|
|           700005 | 2026-02-15 |   -141.95 | Aseguradora Vázquez |
|           700013 | 2026-10-15 |    314.01 | Restaurante Moreno  |
|           700036 | 2026-04-01 |  -2608.7  | Hostelería Gómez    |
|           700047 | 2026-05-15 |  -4101.37 | Aseguradora Vázquez |
|           700048 | 2026-01-17 |   8542.71 | Comercial Álvarez   |
|           700061 | 2026-04-06 |    905.21 | Viajes Castro       |
|           700085 | 2026-04-11 |  -1867.53 | Servicios López     |
|           700097 | 2026-09-08 |   9138.63 | TechNova SL         |
|           700226 | 2026-03-07 |   3269.22 | Servicios López     |
|           700250 | 2026-10-03 |  -2846.32 | Viajes Castro       |
|           700253 | 2026-05-01 |   5149.85 | Academia Hernández  |
|           700263 | 2026-10-10 |   7145.2  | Consulting García   |
**IBAN inválido**
|   ID_Transaccion | Cuenta_IBAN             | Beneficiario       |   Importe |
|-----------------:|:------------------------|:-------------------|----------:|
|           700000 | nan                     | Academia Hernández |     97.88 |
|           700014 | E2225141495358708540470 | Consulting García  |   1987.17 |
|           700023 | nan                     | Logística Pérez    |    298.35 |
|           700029 | nan                     | Academia Hernández |   1910.16 |
|           700037 | ES47430101615948339771  | Ferretería Romero  |   -169.25 |
|           700041 | E7533969472780282207735 | Viajes Castro      |   6648.57 |
|           700043 | nan                     | Servicios López    |  14696.5  |
|           700048 | ES291764637262652473    | Comercial Álvarez  |   8542.71 |
|           700053 | ES5623823364107796638   | Consulting García  |   2446.48 |
|           700058 | ES095804173699380454    | Farmacia Navarro   |  -3221.24 |
|           700069 | nan                     | Viajes Castro      |  -2035.71 |
|           700099 | ES6745912526679838694   | Ferretería Romero  |   2566.17 |
**Moneda inválida**
|   ID_Transaccion | Moneda   |   Importe | Beneficiario        |
|-----------------:|:---------|----------:|:--------------------|
|           700001 | nan      |   3375.14 | Restaurante Moreno  |
|           700002 | XXX      |   5038.47 | Hostelería Gómez    |
|           700003 | XXX      |   9755.99 | Hostelería Gómez    |
|           700004 | XXX      |  13199.5  | Farmacia Navarro    |
|           700014 | nan      |   1987.17 | Consulting García   |
|           700016 | XXX      |   2347.11 | Ferretería Romero   |
|           700018 | XXX      |   2135.89 | Aseguradora Vázquez |
|           700019 | nan      |   9050.05 | Academia Hernández  |
|           700023 | nan      |    298.35 | Logística Pérez     |
|           700031 | nan      |   4045.53 | Ferretería Romero   |
|           700038 | nan      |   1053.04 | Comercial Álvarez   |
|           700042 | nan      |   8451.39 | Academia Hernández  |
**Importe incoherente (ingreso negativo)**
|   ID_Transaccion | Concepto           |   Importe | Beneficiario       | Fecha      |
|-----------------:|:-------------------|----------:|:-------------------|:-----------|
|           700007 | Ingreso ventanilla |  -3161.9  | Energía Torres     | 2005-04-25 |
|           700010 | Nómina             |  -8970.16 | TechNova SL        | 2018-08-28 |
|           700020 | Ingreso ventanilla | -14506.5  | Comercial Álvarez  | 2008-09-28 |
|           700032 | Nómina             | -11582.6  | Consulting García  | 2021-09-21 |
|           700045 | Ingreso ventanilla | -10605.6  | Ferretería Romero  | 2011-01-26 |
|           700051 | Ingreso cajero     |  -1189.45 | Energía Torres     | 2025-04-18 |
|           700081 | Ingreso cajero     |  -2356.45 | Comercial Álvarez  | 2009-01-20 |
|           700085 | Ingreso ventanilla |  -1867.53 | Servicios López    | 2026-04-11 |
|           700093 | Ingreso cajero     |  -2530.55 | Consulting García  | 2013-03-06 |
|           700102 | Nómina             |  -2766.68 | Academia Hernández | 2004-02-04 |
|           700131 | Nómina             |  -2909.99 | Restaurante Moreno | 2002-11-18 |
|           700189 | Nómina             |  -8379.68 | nan                | 2024-01-24 |

---
## ✅ Conclusiones
- Auditoría vectorizada lista para escalar a millones de filas.
- El Excel de salida incluye **banderas por fila** y `flags_total` para priorizar limpieza.
- Para producción: validación IBAN con checksum, catálogo ISO 4217 completo y reglas AML/KYC específicas.