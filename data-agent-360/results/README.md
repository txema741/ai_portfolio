# 📂 Carpeta de resultados – Data Agent 360

## 📘 Descripción
En esta carpeta se guardan los **informes generados automáticamente** por los scripts del proyecto.  
Cada informe está en formato **Markdown (.md)**, pensado para visualizarse directamente en GitHub y exportarse a PDF si se requiere.  
En algunos ejercicios también se generan datasets **limpios o corregidos** en formato Excel (.xlsx).  

---

## 📂 Índice de resultados

### ✅ Ejercicio 1 – Auditoría de clientes (DSP)
- **Script:** `scripts/audit_clientes.py`  
- **Dataset:** `data_sample/clientes.xlsx`  
- **Informe generado:** `results/01_auditoria_clientes_result.md`  
- **Contenido:** Detección de duplicados, nulos, ventas negativas, ventas a cero y outliers en datos de clientes.  
- **Sector aplicado:** PYMEs, consultoría de negocio.  

---

### ✅ Ejercicio 2 – Riesgo País (España, CFS)
- **Script:** `scripts/audit_riesgo_pais.py`  
- **Dataset:** `data_sample/riesgo_pais_spain_real.xlsx`  
- **Informe generado:** `results/02_riesgo_pais_result.md`  
- **Contenido:** Evaluación de riesgo país de España usando indicadores oficiales (Eurostat, OCDE, IMF).  
- **Reglas aplicadas:** deuda pública, deuda externa, déficit comercial, inflación, crecimiento del PIB.  
- **Etiquetado de riesgo:** Bajo / Medio / Alto.  
- **Sector aplicado:** Comercio exterior y riesgo país.  

---

### ✅ Ejercicio 3 – Control de registros educativos (DtR)
- **Script:** `scripts/control_registros.py`  
- **Dataset:** `data_sample/registros_educativos.xlsx`  
- **Informes generados:**  
  - `results/03_control_registros_result.md`  
  - `results/03_registros_educativos_limpio.xlsx`  
- **Contenido:**  
  - Fase *Draft*: detección de duplicados, notas fuera de rango y valores nulos.  
  - Fase *Revise*: validación de fechas de matrícula, normalización de nombres y limpieza definitiva de registros.  
- **Metodología aplicada:** *Draft-then-Revise (DtR)* – Borrador y Revisión.  
- **Sector aplicado:** Educación y gestión académica.  

---

### ✅ Ejercicio 4 – Auditoría de padrones municipales (Self-Consistency)
- **Script:** `scripts/auditoria_padron.py`  
- **Dataset:** `data_sample/municipal_padron.xlsx`  
- **Informes generados:**  
  - `results/04_auditoria_padron_result.md`  
  - `results/04_padron_limpio.xlsx`  
- **Contenido:**  
  - Validación de DNIs, edades y fechas de nacimiento.  
  - Coherencia CP–Provincia–Municipio.  
  - Revisión de altas y bajas incoherentes.  
  - Date
