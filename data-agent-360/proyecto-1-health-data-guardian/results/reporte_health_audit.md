# 🩺 Reporte de Auditoría (V2 Dashboard)

- Filas: 16
- Columnas: 18
- Nulos por columna: {'patient_id': 0, 'nombre': 0, 'edad': 1, 'sexo': 0, 'altura_cm': 0, 'peso_kg': 0, 'imc': 1, 'tension_sistolica': 0, 'tension_diastolica': 0, 'frecuencia_cardiaca': 0, 'glucosa_mg_dl': 0, 'colesterol_total': 0, 'diagnosticos': 6, 'medicacion': 2, 'fecha_ultima_visita': 0, 'correo': 0, 'telefono': 0, 'codigo_postal': 0}

## Resumen de incidencias (campo, tipo, conteo)

| campo               | tipo          |   conteo |
|:--------------------|:--------------|---------:|
| diagnosticos        | nulo          |        6 |
| correo              | formato       |        3 |
| fecha_ultima_visita | fecha_futura  |        2 |
| telefono            | formato       |        2 |
| medicacion          | nulo          |        2 |
| altura_cm           | rango         |        1 |
| codigo_postal       | formato       |        1 |
| colesterol_total    | rango         |        1 |
| fecha_ultima_visita | formato_fecha |        1 |
| edad                | rango         |        1 |
| edad                | nulo          |        1 |
| glucosa_mg_dl       | rango         |        1 |
| frecuencia_cardiaca | rango         |        1 |
| imc                 | nulo          |        1 |
| imc                 | consistencia  |        1 |
| patient_id          | duplicado     |        1 |
| peso_kg             | rango         |        1 |
| tension_diastolica  | rango         |        1 |
| tension_sistolica   | rango         |        1 |
