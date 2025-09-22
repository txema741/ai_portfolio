# Metodología – Health Data Guardian (V2)

## Validaciones aplicadas
- Esquema mínimo (columnas obligatorias).
- Nulos por columna.
- Duplicados por `patient_id`.
- Rangos fisiológicos (edad, tensión, glucosa, colesterol…).
- Consistencia del IMC (`peso_kg` y `altura_cm`).
- Formatos: `correo`, `telefono`, `codigo_postal` (ES 5 dígitos).
- Fechas: inválidas o futuras en `fecha_ultima_visita`.

## Salidas
- Dataset limpio (descarga CSV desde la app).
- Incidencias (CSV), Perfil (JSON) y Reporte (Markdown) — todos descargables.

## Límites del MVP
- Reglas genéricas no validadas por comité clínico.
- No hay imputación avanzada (solo normalización básica).
- No guarda datos en servidor (todo en memoria).
