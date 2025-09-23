# 🧠 Health Data Guardian – Resumen Ejecutivo (V3)

## 1) Visión general del dataset
- Filas: **16**
- Columnas: **18**
- Top columnas con nulos:
  - `diagnosticos` → 6 nulos
  - `medicacion` → 2 nulos
  - `edad` → 1 nulos
  - `imc` → 1 nulos
  - `patient_id` → 0 nulos

## 2) Incidencias detectadas
- Total de incidencias: **29**
- Por tipo:
  - **nulo** → 10
  - **rango** → 8
  - **formato** → 6
  - **fecha_futura** → 2
  - **consistencia** → 1
  - **duplicado** → 1
  - **formato_fecha** → 1
- Por campo:
  - `diagnosticos` → 6
  - `correo` → 3
  - `fecha_ultima_visita` → 3
  - `edad` → 2
  - `medicacion` → 2
  - `telefono` → 2
  - `imc` → 2
  - `colesterol_total` → 1
  - `frecuencia_cardiaca` → 1
  - `altura_cm` → 1

## 3) Recomendaciones rápidas (accionables)
- Completar valores nulos en campos clínicos críticos (edad, tensión, IMC) con reglas y/o imputación controlada.
- Normalizar formatos de email/teléfono/código postal con expresiones regulares y plantillas.
- Validar umbrales fisiológicos con comité clínico y rechazar valores fuera de rango.
- Desduplicar por `patient_id` y establecer clave única en el origen.
- Recalcular IMC desde peso/altura y bloquear escritura directa del campo.
- Estandarizar fecha `YYYY-MM-DD` y bloquear fechas futuras en admisión/visitas.
- Priorizar limpieza en campos más problemáticos: diagnosticos, correo, fecha_ultima_visita, edad, medicacion.

## 4) Muestras de incidencias
| fila | campo | tipo | detalle |
|-----:|:------|:-----|:--------|
| 8 | patient_id | duplicado |  |
| 2 | edad | nulo |  |
| 2 | imc | nulo |  |
| 2 | diagnosticos | nulo |  |
| 9 | diagnosticos | nulo |  |
| 12 | diagnosticos | nulo |  |
| 13 | diagnosticos | nulo |  |
| 14 | diagnosticos | nulo |  |
| 15 | diagnosticos | nulo |  |
| 6 | medicacion | nulo |  |