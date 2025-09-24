# 🏥 Proyecto 1 – Health Data Guardian

Este proyecto forma parte del portfolio **Data Agent 360** y aplica técnicas de **auditoría y calidad de datos** en el sector sanitario.

## 🎯 Objetivo
Construir un agente de IA para auditar registros clínicos, capaz de:
- Detectar valores faltantes en datos médicos.
- Identificar inconsistencias en diagnósticos, edades o géneros.
- Localizar duplicados en registros de pacientes.
- Evaluar riesgos asociados a la baja calidad de los datos clínicos.

La metodología aplicada es **Health Data Guardian (HDG)**, un **MVP (*Minimum Viable Product – Producto Mínimo Viable*)** diseñado para mostrar la utilidad de la auditoría automatizada en salud.

## 📂 Estructura del proyecto

proyecto-1-health-data-guardian/

│── data_sample/ # Datos clínicos sintéticos

│── scripts/ # Scripts de auditoría

│── results/ # Resultados de la auditoría

│── docs/ # Documentación técnica

│── images/ # Visualizaciones y diagramas

│── clean/ # Datos corregidos


## 🚀 Uso
Ejecutar el script principal sobre el dataset de ejemplo:

```bash
python scripts/health_audit.py --input data_sample/pacientes_sinteticos.csv --outdir results

📊 Resultados

results/issues_detectados.csv: errores de calidad encontrados.

results/reporte_health_audit.md: informe con métricas e interpretación.

clean/pacientes_limpios.csv: dataset depurado.

🛠️ Requisitos

Instalar dependencias con:

pip install -r requirements.txt

📚 Documentación

En la carpeta docs/ se incluye la descripción del MVP y su alcance.

📌 Notas

Los datos son sintéticos y no representan pacientes reales.

Proyecto orientado a fines educativos y de portfolio profesional.
