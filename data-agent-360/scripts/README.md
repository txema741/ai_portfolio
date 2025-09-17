# 📂 Índice de Scripts – Data Agent 360

---

## 🔹 Ejercicio 1 – Auditoría de Clientes (DSP)
- **Archivo:** `scripts/audit_clientes.py`  
- **Metodología:** *Directional Stimulus Prompting (DSP)*  
- **Dataset:** `data_sample/clientes.xlsx`  
- **Informes generados:**  
  - `results/01_auditoria_clientes_result.md`  
- **Descripción:** Detección de **duplicados**, **valores nulos**, **ventas negativas/cero** y **outliers** en importes de clientes.  

---

## 🔹 Ejercicio 2 – Riesgo País (España, CFS)
- **Archivo:** `scripts/audit_riesgo_pais.py`  
- **Metodología:** *Contrastive Few-Shot (CFS)*  
- **Dataset:** `data_sample/riesgo_pais_spain_real.xlsx`  
- **Informes generados:**  
  - `results/02_riesgo_pais_result.md`  
- **Descripción:** Evaluación del **riesgo país de España** con indicadores oficiales (Eurostat, OCDE, IMF).  
  Reglas aplicadas: **deuda pública/PIB, déficit comercial, inflación, crecimiento del PIB, deuda externa**.  
  **Salida:** clasificación en **Bajo / Medio / Alto**.  

---

## 🔹 Ejercicio 3 – Control de Registros Educativos (DtR)
- **Archivo:** `scripts/control_registros.py`  
- **Metodología:** *Draft-then-Revise (DtR)*  
- **Dataset:** `data_sample/registros_educativos.xlsx`  
- **Informes generados:**  
  - `results/03_control_registros_result.md`  
  - `results/03_registros_educativos_limpio.xlsx`  
- **Descripción:** Validación de registros académicos mediante dos iteraciones (*borrador y revisión*).  
  Detección de **duplicados, notas fuera de rango, valores nulos y fechas inválidas** en matrículas.  

---

## 🔹 Ejercicio 4 – Auditoría de Padrones Municipales (Self-Consistency)
- **Archivo:** `scripts/auditoria_padron.py`  
- **Metodología:** *Self-Consistency (Auto-consistencia)*  
- **Dataset:** `data_sample/municipal_padron.xlsx`  
- **Informes generados:**  
  - `results/04_auditoria_padron_result.md`  
  - `results/04_padron_limpio.xlsx`  
- **Descripción:** Validación de **DNIs, edades, coherencia CP–Provincia–Municipio, altas y bajas incoherentes** y **duplicados**.  
  Se combinan múltiples rutas de validación con votación mayoritaria para reducir falsos positivos.  

---

## 🔹 Ejercicio 5 – Auditoría de Historias Clínicas (EHR, CoT)
- **Archivo:** `scripts/auditoria_ehr.py`  
- **Metodología:** *Chain-of-Thought (CoT)*  
- **Dataset:** `data_sample/historias_clinicas.xlsx`  
- **Informes generados:**  
  - `results/05_auditoria_ehr_result.md`  
  - `results/05_historias_clinicas_limpio.xlsx`  
- **Descripción:** Auditoría de EHR para detectar **duplicados, fechas incoherentes (alta < ingreso), códigos ICD-10 inválidos, edades imposibles y campos vacíos** (diagnóstico, tratamiento).  
  Aplica razonamiento encadenado paso a paso, imitando la lógica de revisión de un auditor humano.  

---
