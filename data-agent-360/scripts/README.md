# 📂 Índice de Scripts – Data Agent 360

Scripts en Python que implementan la auditoría de datos en cada ejercicio.  
Cada script toma un dataset de `data_sample/` y genera informes en `results/`.

---

## 🔹 Ejercicio 1 – Auditoría de Clientes (DSP)
- **Archivo:** `scripts/audit_clientes.py`  
- **Metodología:** Directional Stimulus Prompting (DSP)  
- **Dataset:** `data_sample/clientes.xlsx`  
- **Informe:** `results/01_auditoria_clientes_result.md`  
- **Descripción:** Detección de duplicados, valores nulos, ventas negativas/cero y outliers.  

---

## 🔹 Ejercicio 2 – Riesgo País (España, CFS)
- **Archivo:** `scripts/audit_riesgo_pais.py`  
- **Metodología:** Contrastive Few-Shot (CFS)  
- **Dataset:** `data_sample/riesgo_pais_spain_real.xlsx`  
- **Informe:** `results/02_riesgo_pais_result.md`  
- **Descripción:** Evaluación de riesgo país con indicadores macroeconómicos oficiales.  

---

## 🔹 Ejercicio 3 – Control de Registros Educativos (DtR)
- **Archivo:** `scripts/control_registros.py`  
- **Metodología:** Draft-then-Revise (DtR)  
- **Dataset:** `data_sample/registros_educativos.xlsx`  
- **Informes:**  
  - `results/03_control_registros_result.md`  
  - `results/03_registros_educativos_limpio.xlsx`  
- **Descripción:** Validación académica: duplicados, notas fuera de rango, fechas inválidas y campos vacíos.  

---

## 🔹 Ejercicio 4 – Auditoría de Padrones Municipales (Self-Consistency)
- **Archivo:** `scripts/auditoria_padron.py`  
- **Metodología:** Self-Consistency (Auto-consistencia)  
- **Dataset:** `data_sample/municipal_padron.xlsx`  
- **Informes:**  
  - `results/04_auditoria_padron_result.md`  
  - `results/04_padron_limpio.xlsx`  
- **Descripción:** Validación de DNIs, edades, CP–Provincia–Municipio, altas/bajas incoherentes y duplicados.  

---

## 🔹 Ejercicio 5 – Auditoría de Historias Clínicas (EHR, CoT)
- **Archivo:** `scripts/auditoria_ehr.py`  
- **Metodología:** Chain-of-Thought (CoT)  
- **Dataset:** `data_sample/historias_clinicas.xlsx`  
- **Informes:**  
  - `results/05_auditoria_ehr_result.md`  
  - `results/05_historias_clinicas_limpio.xlsx`  
- **Descripción:** Auditoría clínica: duplicados, fechas incoherentes (alta < ingreso), ICD-10 inválidos, edades imposibles y campos vacíos.  
