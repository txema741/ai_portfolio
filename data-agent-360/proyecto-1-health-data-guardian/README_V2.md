# 🩺 Proyecto 1 – Health Data Guardian (V2 Dashboard)

Esta versión extiende el MVP inicial (V1 CLI) y añade un **dashboard interactivo con Streamlit**.  
Ahora los usuarios pueden **subir un CSV clínico**, ver un **informe de calidad de datos en tiempo real** y **descargar los resultados limpios** directamente desde la interfaz web.

---

## 🚀 Novedades de V2
- Interfaz web construida con **Streamlit**.
- Subida de archivos CSV directamente desde el navegador.
- Ejecución de la auditoría en memoria (sin escribir en disco).
- Descarga directa de:
  - CSV limpio (`pacientes_clean.csv`)
  - Incidencias detectadas (`issues_detectados.csv`)
  - Perfil del dataset (`profile.json`)
  - Reporte resumido en Markdown (`reporte_health_audit.md`)
- Vista previa de:
  - Dataset original
  - Dataset limpio
  - Perfil del dataset
  - Incidencias detectadas

---

## 📂 Estructura del proyecto (añadidos en V2)

proyecto-1-health-data-guardian/
├─ apps/
│ └─ dashboard/
│ └─ app.py # aplicación Streamlit
├─ scripts/
│ ├─ audit_core.py # núcleo de validación y limpieza
│ └─ health_audit.py # CLI de V1
├─ data_sample/
│ └─ pacientes_sinteticos.csv
├─ docs/
│ └─ metodologia.md # explicación de reglas de validación
├─ requirements_v2.txt # dependencias de V2 (pandas, numpy, streamlit)
└─ README_V2.md


---

## 🔧 Requisitos

Instalar dependencias de V2:

```bash
pip install -r requirements_v2.txt
---
Contenido de requirements_v2.txt:
pandas
numpy
streamlit

▶️ Ejecución del dashboard

Lanzar desde la raíz del proyecto:

streamlit run apps/dashboard/app.py

Esto abrirá el dashboard en tu navegador en http://localhost:8501/.

Subir CSV clínico con columnas mínimas esperadas:

patient_id, nombre, edad, sexo, altura_cm, peso_kg, imc,
tension_sistolica, tension_diastolica, frecuencia_cardiaca,
glucosa_mg_dl, colesterol_total, diagnosticos, medicacion,
fecha_ultima_visita, correo, telefono, codigo_postal

Ejecutar auditoría con un clic.

Explorar resultados:

Perfil general

Incidencias detectadas

Dataset limpio

Descargar archivos listos para usar.

Documentación metodológica

En docs/metodologia.md se detallan:

Reglas de validación aplicadas

Tipos de incidencias detectadas

Limitaciones del MVP
