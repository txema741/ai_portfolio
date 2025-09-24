
---

# 📄 README v2 – Auditoría de Clientes (DSP)  

```markdown
# 🧾 Proyecto 2 – Auditoría de Clientes (DSP)

Este proyecto forma parte del portfolio **Data Agent 360** y aplica técnicas de **auditoría y calidad de datos** en el sector empresarial.

## 🎯 Objetivo
Desarrollar un agente de IA que audite bases de clientes, detectando:
- Duplicados en identificadores de cliente.
- Errores en direcciones de correo y teléfono.
- Campos obligatorios vacíos.
- Inconsistencias en la segmentación de clientes.

La metodología aplicada es **DSP (*Directional Stimulus Prompting – Estímulo Direccional de Prompting*)**, que guía a la IA para focalizar la detección de errores en áreas clave.

## 📂 Estructura del proyecto

proyecto-2-auditoria-clientes/

│── data_sample/ # Datos de clientes sintéticos

│── scripts/ # Scripts de auditoría

│── results/ # Resultados de la auditoría

│── docs/ # Documentación técnica

│── images/ # Visualizaciones y diagramas

│── clean/ # Datos corregidos


## 🚀 Uso
Ejecutar el script principal sobre el dataset de ejemplo:

```bash
python scripts/audit_clientes.py --input data_sample/clientes_sinteticos.csv --outdir results

Resultados

results/issues_detectados.csv: inconsistencias detectadas.

results/reporte_clientes.md: resumen en lenguaje natural.

clean/clientes_limpios.csv: dataset corregido.

🛠️ Requisitos

Instalar dependencias con:

pip install -r requirements.txt

📚 Documentación

En la carpeta docs/ se incluye la explicación de la metodología DSP aplicada en el contexto empresarial.

📌 Notas

Los datos son sintéticos y no representan clientes reales.

Proyecto orientado a fines educativos y de portfolio profesional.
