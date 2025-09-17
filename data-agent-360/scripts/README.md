# 📂 Carpeta de scripts – Data Agent 360

## 📘 Descripción
En esta carpeta se encuentran los **scripts en Python** que implementan los ejercicios del proyecto **Data Agent 360 – Auditoría y Calidad de Datos Empresariales con IA**.  

Cada script está **100% comentado en español** y genera automáticamente sus informes en la carpeta `results/`, trabajando con datasets almacenados en `data_sample/`.  

La estructura común de cada ejercicio es:  
- **Dataset de entrada** → `data_sample/`  
- **Script de auditoría** → `scripts/`  
- **Informe en Markdown** → `results/`  
- **Dataset limpio o corregido** → `results/`  

---

## 📂 Índice de scripts

### 🔹 Ejercicio 1 – Auditoría de clientes (DSP)
- **Archivo:** `scripts/audit_clientes.py`  
- **Metodología aplicada:** *Directional Stimulus Prompting (DSP)*  
- **Dataset:** `data_sample/clientes.xlsx`  
- **Informe generado:** `results/01_auditoria_clientes_result.md`  
- **Descripción:** Detecta duplicados, nulos, ventas negativas, ventas a cero y outliers en los datos de clientes.  
- **Sector aplicado:** PYMEs, consultoría de negocio.  

---

### 🔹 Ejercicio 2 – Riesgo País (España, CFS)
- **Archivo:** `scripts/audit_riesgo_pais.py`  
- **Metodología aplicada:** *Contrastive Few-Shot (CFS)*  
- **Dataset:** `data_sample/riesgo_pais_spain_real.xlsx`  
- **Informe generado:** `results/02_riesgo_pais_result.md`  
- **Descripción:** Evalúa el riesgo país de España con indicadores oficiales (Eurostat, OCDE, IMF), clasificando en Bajo / Medio / Alto.  
- **Sector aplicado:** Comercio exterior y riesgo país.  

---

### 🔹 Ejercicio 3 – Control de registros educativos (DtR)
- **Archivo:** `scripts/control_registros.py`  
- **Metodología aplicada:** *Draft-then-Revise (DtR)*  
- **Dataset:** `data_sample/registros_educativos.xlsx`  
- **Informes generados:**  
  - `results/03_control_registros_result.md`  
  - `results/03_registros_educativos_limpio.xlsx`  
- **Descripción:** Detecta duplicados, valores nulos, notas fuera de rango y fechas inconsistentes, aplicando una doble revisión (*borrador y mejora*).  
- **Sector aplicado:** Educación y gestión académica.  

---

### 🔹 Ejercicio 4 – Auditoría de padrones municipales (Self-Consistency)
- **Archivo:** `scripts/auditoria_padron.py`  
- **Metodología aplicada:** *Self-Consistency (Auto-consistencia)*  
- **Dataset:** `data_sample/municipal_padron.xlsx`  
- **Informes generados:**  
  - `results/04_auditoria_padron_result.md`  
  - `results/04_padron_limpio.xlsx`  
- **Descripción:** Valida DNIs, edades, CP–Provincia–Municipio, altas y bajas incoherentes y duplicados. Combina múltiples rutas de validación por vota
