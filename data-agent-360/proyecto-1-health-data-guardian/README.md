# 🩺 Proyecto 1 – Health Data Guardian  

**MVP (Producto Mínimo Viable) de un sistema de auditoría y limpieza de datos clínicos**.  
Este proyecto forma parte de un portfolio profesional en Inteligencia Artificial aplicada a **empresa** y **docencia**.  

Su objetivo es demostrar cómo la IA y la programación pueden ayudar a garantizar la **calidad, coherencia y confiabilidad de datos de salud** antes de usarlos en análisis, informes o modelos predictivos.  

---

## 🎯 Objetivos del proyecto
- Detectar errores de **calidad de datos** (valores nulos, duplicados, inconsistencias, outliers).  
- Validar **rangos fisiológicos plausibles** (ej. edad, tensión arterial, glucosa, colesterol).  
- Revisar **formatos** (emails, teléfonos, fechas, códigos postales).  
- Generar automáticamente:
  - 📄 Informe legible en **Markdown**.  
  - 📊 Dataset limpio y depurado.  
  - 📑 Listado detallado de incidencias.  

---

## 📂 Estructura del proyecto
```bash
proyecto-1-health-data-guardian/
├─ data_sample/        → datasets sintéticos con errores intencionados
│   └─ pacientes_sinteticos.csv
├─ docs/               → documentación metodológica
├─ results/            → informes generados automáticamente
│   └─ clean/          → datasets limpios depurados
├─ scripts/            → scripts de auditoría y limpieza
│   └─ health_audit.py
├─ .gitignore          → exclusiones para Git
├─ README.md           → documentación principal
└─ requirements.txt    → dependencias mínimas (pandas, numpy)



## ▶️ Ejecución

Ejecutar desde la raíz del proyecto:

python scripts/health_audit.py --input data_sample/pacientes_sinteticos.csv --outdir results

Esto generará:
- results/reporte_health_audit.md → resumen de la auditoría.
- results/issues_detectados.csv → listado detallado de problemas.
- results/profile.json → perfil estadístico del dataset.
- results/clean/pacientes_clean.csv → dataset limpio.

---

## 🔧 Requisitos

Instalar las dependencias necesarias:

pip install -r requirements.txt

Contenido de requirements.txt:
pandas
numpy

Dependencias incluidas:
- pandas → manipulación y validación de datos.
- numpy → operaciones numéricas básicas.

---

## 🚀 ¿Qué es un MVP?

Un MVP (Producto Mínimo Viable) es una primera versión funcional que incluye lo mínimo necesario para probar, demostrar y enseñar el valor de una idea.

En este proyecto:
- Se trabaja con un dataset clínico sintético lleno de errores intencionados.
- El script health_audit.py los detecta y corrige parcialmente.
- Los informes permiten mostrar cómo un sistema automático puede mejorar la calidad de los datos médicos.

El objetivo es mostrar impacto inmediato y servir como base para desarrollos más avanzados (ej. dashboards, agentes de IA, integración en sistemas hospitalarios).

---

## 📑 Archivos clave

- data_sample/pacientes_sinteticos.csv → dataset sintético con errores intencionales.
- scripts/health_audit.py → script en Python que realiza la auditoría y limpieza.
- results/ → carpeta con ejemplos de informes generados automáticamente.
- docs/metodologia.md → explicación de la metodología aplicada (opcional, en desarrollo).
- .gitignore → exclusión de archivos no relevantes para GitHub.
- requirements.txt → dependencias mínimas del proyecto.
