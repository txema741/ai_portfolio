# 🧠 Proyecto 1 – Health Data Guardian (V3 AI Analyst)

Esta versión añade una capa **analítica e interpretativa** sobre los resultados de auditoría.  
El sistema no solo detecta y limpia errores (V1, V2), sino que ahora **resume y explica los hallazgos** en un informe ejecutivo, con recomendaciones prácticas.

---

## 🚀 Novedades de V3
- Nuevo módulo **AI Analyst (heurístico)** en `apps/ai_analyst/analyst.py`.
- Lee los archivos generados por V1/V2:
  - `results/issues_detectados.csv`
  - `results/profile.json`
- Genera un **informe ejecutivo en Markdown** (`results/analyst_summary.md`) con:
  1. **Visión general** del dataset.
  2. **Incidencias detectadas** (conteos por tipo y por campo).
  3. **Recomendaciones rápidas** basadas en reglas heurísticas.
  4. **Ejemplos concretos de errores** para ilustrar los hallazgos.

---

## 📂 Estructura del proyecto (añadidos en V3)

proyecto-1-health-data-guardian/
├─ apps/
│ └─ ai_analyst/
│ └─ analyst.py # script del analista heurístico
├─ results/
│ ├─ issues_detectados.csv # generado por V1 o V2
│ ├─ profile.json # generado por V1 o V2
│ └─ analyst_summary.md # salida de V3
├─ requirements_v3.txt # dependencias mínimas
└─ README_V3.md


---

## 🔧 Requisitos

Instalar dependencias de V3:

```bash
pip install -r requirements_v3.txt
---
Contenido de requirements_v3.txt:
pandas

▶️ Ejecución del analista

Asegúrate de haber ejecutado antes V1 o V2 para generar:

results/issues_detectados.csv

results/profile.json

Lanza el analista:

python apps/ai_analyst/analyst.py \
  --issues results/issues_detectados.csv \
  --profile results/profile.json \
  --out results/analyst_summary.md


Abre el informe generado:

results/analyst_summary.md
