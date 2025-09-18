# 📂 Índice de Scripts – Data Agent 360

Scripts en Python que implementan la auditoría de datos en cada ejercicio.  
Cada script toma un dataset de `data_sample/` y genera informes en `results/`.

---

🔹 **Ejercicio 1 – Auditoría de Clientes (DSP)**  
- **Archivo:** `scripts/audit_clientes.py`  
- **Metodología:** Directional Stimulus Prompting (DSP)  
- **Dataset:** `data_sample/clientes.xlsx`  
- **Informe:** `results/01_auditoria_clientes_result.md`  
- **Descripción:** Detección de duplicados, valores nulos, ventas negativas/cero y outliers.  

---

🔹 **Ejercicio 2 – Riesgo País (España, CFS)**  
- **Archivo:** `scripts/audit_riesgo_pais.py`  
- **Metodología:** Contrastive Few-Shot (CFS)  
- **Dataset:** `data_sample/riesgo_pais_spain_real.xlsx`  
- **Informe:** `results/02_riesgo_pais_result.md`  
- **Descripción:** Evaluación de riesgo país con indicadores macroeconómicos oficiales.  

---

🔹 **Ejercicio 3 – Control de Registros Educativos (DtR)**  
- **Archivo:** `scripts/control_registros.py`  
- **Metodología:** Draft-then-Revise (DtR)  
- **Dataset:** `data_sample/registros_educativos.xlsx`  
- **Informes:**  
  - `results/03_control_registros_result.md`  
  - `results/03_registros_educativos_limpio.xlsx`  
- **Descripción:** Validación académica: duplicados, notas fuera de rango, fechas inválidas y campos vacíos.  

---

🔹 **Ejercicio 4 – Auditoría de Padrones Municipales (Self-Consistency)**  
- **Archivo:** `scripts/auditoria_padron.py`  
- **Metodología:** Self-Consistency (Auto-consistencia)  
- **Dataset:** `data_sample/municipal_padron.xlsx`  
- **Informes:**  
  - `results/04_auditoria_padron_result.md`  
  - `results/04_padron_limpio.xlsx`  
- **Descripción:** Validación de DNIs, edades, CP–Provincia–Municipio, altas/bajas incoherentes y duplicados.  

---

🔹 **Ejercicio 5 – Auditoría de Historias Clínicas (EHR, CoT)**  
- **Archivo:** `scripts/auditoria_ehr.py`  
- **Metodología:** Chain-of-Thought (CoT)  
- **Dataset:** `data_sample/historias_clinicas.xlsx`  
- **Informes:**  
  - `results/05_auditoria_ehr_result.md`  
  - `results/05_historias_clinicas_limpio.xlsx`  
- **Descripción:** Auditoría clínica: duplicados, fechas incoherentes (alta < ingreso), ICD-10 inválidos, edades imposibles y campos vacíos.  

---

🔹 **Ejercicio 6 – Auditoría de Transacciones Bancarias (CoT vectorizado)**  
- **Archivo:** `scripts/auditoria_transacciones.py`  
- **Metodología:** Chain-of-Thought vectorizado + reglas agrupadas  
- **Dataset:** `data_sample/transacciones_bancarias.xlsx`  
- **Informes:**  
  - `results/06_auditoria_transacciones_result.md`  
  - `results/06_transacciones_limpio.xlsx`  
- **Descripción:** Detecta duplicados, fechas incoherentes, monedas inválidas, IBAN incorrectos, importes incoherentes y campos vacíos.  

---

🔹 **Ejercicio 7 – Auditoría de Envíos y Trazabilidad Logística (Self-Consistency + CoT)**  
- **Archivo:** `scripts/auditoria_envios.py`  
- **Metodología:** Self-Consistency + Chain-of-Thought (CoT) vectorizado  
- **Dataset:** `data_sample/envios_logistica.xlsx`  
- **Informes:**  
  - `results/07_auditoria_envios_result.md`  
  - `results/07_envios_limpio.xlsx`  
- **Descripción:** Auditoría logística: duplicados, fechas incoherentes, CP–Ciudad inconsistentes, transportistas inválidos, pesos/volúmenes imposibles y registros incompletos.  

---

🔹 **Ejercicio 8 – Auditoría de Pólizas y Siniestros de Seguros (Self-Consistency + CoT vectorizado)**  
- **Archivo:** `scripts/auditoria_seguro.py`  
- **Metodología:** Self-Consistency + CoT vectorizado  
- **Dataset:** `data_sample/polizas_siniestros.xlsx`  
- **Informes:**  
  - `results/08_auditoria_seguro_result.md`  
  - `results/08_polizas_siniestros_limpio.xlsx`  
- **Descripción:** Auditoría de pólizas y siniestros: duplicados, fechas incoherentes, montos fuera de rango, tipos de póliza inválidos y campos vacíos.

- 🔹 Ejercicio 9 – Auditoría de Consumos Energéticos (CoT + Reglas Vectorizadas)

Archivo: scripts/auditoria_energia.py  
Metodología: Chain-of-Thought (CoT) + reglas vectorizadas  
Dataset: data_sample/consumos_energia.xlsx  
Informes:  
results/09_auditoria_energia_result.md  
results/09_consumos_energia_limpio.xlsx  
Descripción: Auditoría energética: duplicados por cliente/periodo, periodos inválidos, consumos negativos o fuera de rango, costes incoherentes, tarifas inválidas y clientes vacíos.  

---

🔹 Ejercicio 10 – Auditoría de Inventarios y Cadenas de Suministro (ReAct)

Archivo: scripts/auditoria_inventarios.py  
Metodología: ReAct (Reason + Act)  
Dataset: data_sample/inventarios.xlsx  
Informes:  
results/10_auditoria_inventarios_result.md  
results/10_inventarios_limpio.xlsx  
Descripción: Auditoría de inventarios: duplicados por clave, fechas incoherentes o fuera de rango, cantidades negativas o excesivas, precios inválidos, códigos de producto y almacenes no registrados.  

