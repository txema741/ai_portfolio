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

