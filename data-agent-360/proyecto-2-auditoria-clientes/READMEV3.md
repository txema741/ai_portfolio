
---

# 📄 README v3 – Control de Registros Educativos (DtR)  

```markdown
# 📘 Proyecto 3 – Control de Registros Educativos (DtR)

Este proyecto forma parte del portfolio **Data Agent 360** y aplica técnicas de **auditoría y calidad de datos** en el sector educativo.

## 🎯 Objetivo
Desarrollar un agente de IA que audite registros de estudiantes, detectando:
- Errores en calificaciones.
- Duplicados en matrículas.
- Inconsistencias entre asignaturas y alumnos.
- Faltas de datos obligatorios.

La metodología aplicada es **DtR (*Draft-then-Revise – Borrador-Luego-Revisión*)**, que permite:
1. Generar una primera versión del análisis.
2. Revisar y mejorar iterativamente los resultados.

## 📂 Estructura del proyecto
proyecto-3-control-educativo/
│── data_sample/ # Datos de estudiantes sintéticos
│── scripts/ # Scripts de auditoría
│── results/ # Resultados de la auditoría
│── docs/ # Documentación técnica
│── images/ # Visualizaciones y diagramas
│── clean/ # Datos corregidos


## 🚀 Uso
Ejecutar el script de auditoría sobre el dataset de ejemplo:

```bash
python scripts/audit_educativo.py --input data_sample/alumnos_sinteticos.csv --outdir results

Resultados

results/issues_detectados.csv: inconsistencias detectadas.

results/reporte_educativo.md: informe en lenguaje natural con resumen y métricas.

clean/alumnos_limpios.csv: dataset corregido y depurado.

🛠️ Requisitos

Instalar dependencias con:

pip install -r requirements.txt

📚 Documentación

En la carpeta docs/ se incluye:

metodologia_dtr.md: explicación de la metodología DtR aplicada en el sector educativo.

📌 Notas

Los datos son sintéticos y no representan información real de estudiantes.

Proyecto orientado a fines educativos y de portfolio profesional.
