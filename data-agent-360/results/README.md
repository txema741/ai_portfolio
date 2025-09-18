# 📂 Carpeta de resultados – Data Agent 360

En esta carpeta se guardan los **informes y datasets generados automáticamente** por los scripts del proyecto.  
Todos los informes están en formato Markdown (`.md`), listos para verse en GitHub y exportarse a PDF si es necesario.  
Los datasets corregidos se exportan en Excel (`.xlsx`) con banderas de error para cada registro.

---

## ✅ Ejercicio 1 – Auditoría de Clientes (DSP)
- **Script:** `scripts/audit_clientes.py`  
- **Dataset:** `data_sample/clientes.xlsx`  
- **Informe:** `results/01_auditoria_clientes_result.md`  
- **Contenido:** Detección de duplicados, nulos, ventas negativas, ventas a cero y outliers en datos de clientes.  
- **Sector aplicado:** PYMEs, consultoría de negocio.  

---

## ✅ Ejercicio 2 – Riesgo País (España, CFS)
- **Script:** `scripts/audit_riesgo_pais.py`  
- **Dataset:** `data_sample/riesgo_pais_spain_real.xlsx`  
- **Informe:** `results/02_riesgo_pais_result.md`  
- **Contenido:** Evaluación del riesgo país de España usando indicadores oficiales (Eurostat, OCDE, IMF).  
- **Reglas aplicadas:** deuda pública, deuda externa, déficit comercial, inflación, crecimiento del PIB.  
- **Salida:** Clasificación de riesgo **Bajo / Medio / Alto**.  
- **Sector aplicado:** Comercio exterior y geopolítica económica.  

---

## ✅ Ejercicio 3 – Control de Registros Educativos (DtR)
- **Script:** `scripts/control_registros.py`  
- **Dataset:** `data_sample/registros_educativos.xlsx`  
- **Informes:**  
  - `results/03_control_registros_result.md`  
  - `results/03_registros_educativos_limpio.xlsx`  
- **Contenido:** Auditoría de registros académicos: duplicados, notas fuera de rango, fechas inválidas y campos vacíos.  
- **Metodología:** Draft-then-Revise (dos iteraciones: borrador + revisión).  
- **Sector aplicado:** Educación y gestión académica.  

---

## ✅ Ejercicio 4 – Auditoría de Padrones Municipales (Self-Consistency)
- **Script:** `scripts/auditoria_padron.py`  
- **Dataset:** `data_sample/municipal_padron.xlsx`  
- **Informes:**  
  - `results/04_auditoria_padron_result.md`  
  - `results/04_padron_limpio.xlsx`  
- **Contenido:** Validación de DNIs, edades, coherencia CP–Provincia–Municipio, fechas de alta/baja incoherentes y duplicados.  
- **Metodología:** Self-Consistency (varias rutas de validación y votación mayoritaria).  
- **Sector aplicado:** Administración pública y gestión municipal.  

---

## ✅ Ejercicio 5 – Auditoría de Historias Clínicas (EHR, CoT)
- **Script:** `scripts/auditoria_ehr.py`  
- **Dataset:** `data_sample/historias_clinicas.xlsx`  
- **Informes:**  
  - `results/05_auditoria_ehr_result.md`  
  - `results/05_historias_clinicas_limpio.xlsx`  
- **Contenido:** Detección de duplicados, fechas incoherentes (alta < ingreso), códigos ICD-10 inválidos, edades imposibles y campos vacíos (diagnóstico, tratamiento).  
- **Metodología:** Chain-of-Thought (CoT) – razonamiento paso a paso.  
- **Sector aplicado:** Sanidad pública/privada y proyectos de salud digital.

- ## ✅ Ejercicio 6 – Auditoría de Transacciones Bancarias (CoT vectorizado)
Informes:  
- `results/06_auditoria_transacciones_result.md`  
- `results/06_transacciones_limpio.xlsx`  
Contenido: detección de duplicados, fechas incoherentes, monedas inválidas, IBAN incorrectos, importes incoherentes y campos vacíos.

---

## 🎯 Objetivo de esta carpeta
Centralizar todos los informes y datasets de salida de los ejercicios, mostrando cómo los **scripts Python** se convierten en herramientas de **consultoría y docencia** listas para usarse en diferentes sectores.
