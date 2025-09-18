# Ejercicio 7 – Auditoría de Envíos y Trazabilidad Logística
**Metodología:** Self-Consistency + CoT vectorizado  
**Sector:** Logística y transporte

---

## 🗓️ Ejecución
- Fecha y hora: **2025-09-18 11:25**
- Filas totales (entrada): **322**

## 📊 Resumen de incidencias
- Duplicados por ID: **44**
- Duplicados por clave: **44**
- Fecha envío nula: **0**
- Fecha entrega nula: **0**
- Entrega antes de envío: **29**
- Fecha fuera de rango: **0**
- CP–Ciudad incoherente: **22**
- Transportista inválido: **41**
- Peso nulo: **0**
- Peso negativo: **21**
- Peso excesivo: **0**
- Volumen nulo: **0**
- Volumen negativo: **0**
- Volumen excesivo: **12**
- Destinatario vacío: **0**
- Dirección vacía: **0**

## 📑 Ejemplos
**Duplicados por ID_Envio**
|   ID_Envio | Fecha_Envio   | Fecha_Entrega   |    CP | Ciudad    | Transportista   |   Peso_kg |   Volumen_m3 | Destinatario        | Dirección                      |
|-----------:|:--------------|:----------------|------:|:----------|:----------------|----------:|-------------:|:--------------------|:-------------------------------|
|     900031 | 2023-04-06    | 2023-04-15      | 48002 | Bilbao    | Correos         |    -69.73 |         4.68 | Comercial Álvarez   | Avenida de la Constitución 164 |
|     900037 | 2018-03-01    | 2018-03-04      | 46002 | Valencia  | UPS             |     84.9  |         4.53 | Hostelería Gómez    | Avenida de la Constitución 141 |
|     900038 | 2019-08-11    | 2019-08-18      |  8002 | Barcelona | DHL             |    192.44 |         1.88 | Consulting García   | Calle Mayor 166                |
|     900039 | 2016-11-15    | 2016-11-14      | 48001 | Bilbao    | UPS             |    193.86 |         2.62 | Ferretería Romero   | Calle Mayor 159                |
|     900044 | 2018-12-31    | 2019-01-06      | 46002 | Valencia  | Correos         |     90.16 |         0.65 | Hostelería Gómez    | Calle Mayor 190                |
|     900053 | 2016-12-14    | 2016-12-20      |  8002 | Barcelona | MRW             |    178.12 |         2.97 | Ferretería Romero   | Calle Mayor 109                |
|     900057 | 2023-06-25    | 2023-06-27      |  8004 | Barcelona | DHL             |     39.98 |         3.68 | Energía Torres      | Gran Vía 142                   |
|     900066 | 2025-02-11    | 2025-02-18      | 48002 | Bilbao    | GLS             |    184.51 |         3.54 | Servicios López     | Plaza España 122               |
|     900095 | 2022-07-08    | 2022-07-10      | 41002 | Sevilla   | Correos         |    175.74 |         3.99 | Aseguradora Vázquez | Gran Vía 59                    |
|     900114 | 2017-03-04    | 2017-03-11      | 48002 | Bilbao    | Correos         |    102.57 |         2.07 | Comercial Álvarez   | Gran Vía 60                    |
|     900149 | 2021-03-29    | 2021-04-02      | 48002 | Bilbao    | MRW             |     45.47 |         4.45 | Restaurante Moreno  | Rambla Cataluña 69             |
|     900150 | 2020-11-18    | 2020-11-17      | 46002 | Valencia  | MRW             |     21.16 |         0.19 | Ferretería Romero   | Avenida de la Constitución 159 |
**Duplicados por clave (Fecha_Envio, Destinatario, Dirección, CP)**
|   ID_Envio | Fecha_Envio   | Destinatario        | Dirección                      |    CP |
|-----------:|:--------------|:--------------------|:-------------------------------|------:|
|     900031 | 2023-04-06    | Comercial Álvarez   | Avenida de la Constitución 164 | 48002 |
|     900037 | 2018-03-01    | Hostelería Gómez    | Avenida de la Constitución 141 | 46002 |
|     900038 | 2019-08-11    | Consulting García   | Calle Mayor 166                |  8002 |
|     900039 | 2016-11-15    | Ferretería Romero   | Calle Mayor 159                | 48001 |
|     900044 | 2018-12-31    | Hostelería Gómez    | Calle Mayor 190                | 46002 |
|     900053 | 2016-12-14    | Ferretería Romero   | Calle Mayor 109                |  8002 |
|     900057 | 2023-06-25    | Energía Torres      | Gran Vía 142                   |  8004 |
|     900066 | 2025-02-11    | Servicios López     | Plaza España 122               | 48002 |
|     900095 | 2022-07-08    | Aseguradora Vázquez | Gran Vía 59                    | 41002 |
|     900114 | 2017-03-04    | Comercial Álvarez   | Gran Vía 60                    | 48002 |
|     900149 | 2021-03-29    | Restaurante Moreno  | Rambla Cataluña 69             | 48002 |
|     900150 | 2020-11-18    | Ferretería Romero   | Avenida de la Constitución 159 | 46002 |
**Entregas antes de envío**
|   ID_Envio | Fecha_Envio   | Fecha_Entrega   | Destinatario        | Dirección                      |    CP |
|-----------:|:--------------|:----------------|:--------------------|:-------------------------------|------:|
|     900001 | 2021-07-19    | 2021-07-15      | Servicios López     | Avenida de la Constitución 188 |  8002 |
|     900004 | 2025-07-10    | 2025-07-08      | Aseguradora Vázquez | Paseo de la Castellana 190     | 48001 |
|     900008 | 2017-11-04    | 2017-11-03      | Energía Torres      | Calle Real 143                 | 28003 |
|     900017 | 2050-02-02    | 2024-01-20      | Comercial Álvarez   | Calle del Sol 148              | 46001 |
|     900027 | 2022-10-08    | 2022-10-06      | Hostelería Gómez    | Calle Mayor 197                | 46002 |
|     900039 | 2016-11-15    | 2016-11-14      | Ferretería Romero   | Calle Mayor 159                | 48001 |
|     900040 | 2024-02-13    | 2024-02-09      | Consulting García   | Avenida de la Constitución 136 | 46001 |
|     900045 | 2020-09-12    | 2020-09-10      | Restaurante Moreno  | Calle del Sol 57               | 28001 |
|     900071 | 2022-06-10    | 2022-06-08      | Distribuciones Díaz | Calle Real 166                 | 28001 |
|     900087 | 2018-12-20    | 2018-12-18      | Restaurante Moreno  | Paseo de la Castellana 29      |  8003 |
|     900091 | 2018-10-21    | 2018-10-20      | Farmacia Navarro    | Plaza España 99                | 41003 |
|     900107 | 2016-12-14    | 2016-12-10      | Restaurante Moreno  | Rambla Cataluña 166            | 48002 |
**CP–Ciudad incoherente**
|   ID_Envio |    CP | Ciudad    |
|-----------:|------:|:----------|
|     900040 | 46001 | Madrid    |
|     900043 | 48001 | Barcelona |
|     900084 | 48002 | Valencia  |
|     900089 | 41003 | Valencia  |
|     900129 | 48002 | Madrid    |
|     900132 | 46001 | Barcelona |
|     900143 | 41003 | Valencia  |
|     900162 | 48001 | Barcelona |
|     900163 | 48002 | Sevilla   |
|     900167 | 48002 | Sevilla   |
|     900168 | 48001 | Valencia  |
|     900182 | 41001 | Bilbao    |
**Transportista inválido**
|   ID_Envio | Transportista   | Destinatario      |
|-----------:|:----------------|:------------------|
|     900006 |                 | Market Ruiz       |
|     900012 | XXX Transportes | Ferretería Romero |
|     900021 |                 | Logística Pérez   |
|     900025 |                 | Market Ruiz       |
|     900027 | XXX Transportes | Hostelería Gómez  |
|     900036 |                 | Market Ruiz       |
|     900043 | XXX Transportes | Servicios López   |
|     900069 |                 | Hostelería Gómez  |
|     900082 | XXX Transportes | Ferretería Romero |
|     900088 |                 | Logística Pérez   |
|     900098 |                 | Market Ruiz       |
|     900099 | XXX Transportes | Comercial Álvarez |
**Peso/Volumen anómalos (ejemplos)**
|   ID_Envio |   Peso_kg |   Volumen_m3 | Destinatario        |    CP |
|-----------:|----------:|-------------:|:--------------------|------:|
|     900002 |   -136.09 |         2.26 | Comercial Álvarez   | 48002 |
|     900005 |    -59.33 |         0.83 | Market Ruiz         |  8004 |
|     900010 |   -163.62 |         4.31 | Energía Torres      | 28003 |
|     900027 |    -23.3  |         0.24 | Hostelería Gómez    | 46002 |
|     900028 |   -123.21 |         3.18 | Farmacia Navarro    | 46003 |
|     900030 |    -43    |         1.89 | Farmacia Navarro    |  8003 |
|     900031 |    -69.73 |         4.68 | Comercial Álvarez   | 48002 |
|     900064 |     97.32 |      1000    | Distribuciones Díaz |  8003 |
|     900077 |    105.19 |      1000    | Logística Pérez     | 28003 |
|     900087 |     76.85 |      1000    | Restaurante Moreno  |  8003 |
|     900088 |     67.34 |      1000    | Logística Pérez     | 28002 |
|     900106 |     29.27 |      1000    | Farmacia Navarro    | 41003 |

---
## ✅ Conclusiones
- Validación híbrida y vectorizada: alto rendimiento con múltiples rutas de control.
- El Excel de salida contiene `flag_*`, `flags_total` y `registro_valido` para priorizar limpieza.
- Próximos pasos: ampliar CP→Ciudad, validar direcciones (geocoding) y reglas según tipología de carga.