# Proyecto 2 — Auditoría de Clientes con IA

**Metodología:** DSP (*Directional Stimulus Prompting – Estímulo Direccional de Prompting*)  

Este proyecto implementa una **auditoría de calidad de datos** sobre una base de clientes, detectando:

- Valores faltantes, **duplicados**, **inconsistencias** y **formatos inválidos**.  
- Problemas típicos en **PII (*Personally Identifiable Information – Información de Identificación Personal*)** como emails y teléfonos.  
- Reglas de negocio (fechas imposibles, códigos de país inválidos, etc.).  

---

## 🎯 Objetivos
1. Generar un **informe reproducible** con incidencias: `results/issues_detectados.csv`.  
2. Producir un **reporte narrativo**: `results/reporte_clientes.md` con **KPIs (*Key Performance Indicators – Indicadores Clave de Desempeño*)** de calidad.  
3. Documentar el uso de **DSP** como técnica conceptual para guiar validaciones semánticas.

---

## 📂 Estructura del proyecto
proyecto-2-auditoria-clientes/
├─ data_sample/
│ └─ clientes_sinteticos.csv
├─ scripts/
│ └─ audit_clientes.py
├─ results/
│ ├─ issues_detectados.csv
│ └─ reporte_clientes.md
├─ docs/
│ └─ metodologia_dsp.md
├─ images/ # (opcional para gráficos)
├─ clean/ # (datasets limpios post-ETL)
├─ README.md
├─ requirements.txt
└─ .gitignore


---

## ▶️ Ejecución rápida
```bash
python scripts/audit_clientes.py \
  --input data_sample/clientes_sinteticos.csv \
  --outdir results

Entradas y salidas

Entrada:
data_sample/clientes_sinteticos.csv (CSV – Comma-Separated Values – Valores Separados por Comas).

Salidas:

results/issues_detectados.csv — registro fila a fila de todas las incidencias.

results/reporte_clientes.md — resumen ejecutivo + métricas de calidad.

🔍 Validaciones implementadas

Campos obligatorios: id_cliente, nombre, email, telefono, pais, fecha_alta.

Email (regex); Teléfono (longitud mínima configurable).

País (lista ISO – International Organization for Standardization – Organización Internacional de Normalización básica ampliable).

Fechas (formato ISO YYYY-MM-DD).

Duplicados por email y telefono.

Reglas de plausibilidad (ej. fecha_alta no futura).

⚙️ Requisitos

Instala dependencias con:

pip install -r requirements.txt

🧠 Nota sobre DSP

Se usa DSP (Directional Stimulus Prompting – Estímulo Direccional de Prompting) como guía conceptual para:

Diseñar ejemplares positivos/negativos que inspiran reglas.

Traducir heurísticas en comprobaciones programáticas (ver docs/metodologia_dsp.md).

📜 Glosario de siglas

DSP — Directional Stimulus Prompting – Estímulo Direccional de Prompting

KPI — Key Performance Indicator – Indicador Clave de Desempeño

PII — Personally Identifiable Information – Información de Identificación Personal

GDPR — General Data Protection Regulation – Reglamento General de Protección de Datos

ISO — International Organization for Standardization – Organización Internacional de Normalización

CSV — Comma-Separated Values – Valores Separados por Comas

ETL — Extract, Transform, Load – Extraer, Transformar y Cargar
