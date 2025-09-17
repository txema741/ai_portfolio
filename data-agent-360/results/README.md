# Resultados del proyecto Data Agent 360

En esta carpeta se guardan los **informes generados automáticamente** por los scripts del proyecto.  
Cada informe está en formato **Markdown (.md)**, pensado para que se pueda visualizar en GitHub directamente y también exportar a PDF si se requiere.

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

### ✅ Ejercicio 3 – Control de registros educativos (Draft-then-Revise, DtR)
- **Script:** `scripts/control_registros.py`  
- **Dataset:** `data_sample/registros_educativos.xlsx`  
- **Informe generado:** `results/03_control_registros_result.md`  
- **Contenido:**  
  - Primera iteración (*Draft*): detección de duplicados, notas fuera de rango y valores nulos.  
  - Segunda iteración (*Revise*): validación de fechas de matrícula, normalización de nombres y limpieza definitiva de registros.  
- **Metodología aplicada:** *Draft-then-Revise (DtR)* – Borrador y Revisión.  
- **Sector aplicado:** Educación, gestión académica y control de calidad de datos.  

---

## 🎯 Objetivo de esta carpeta
Centralizar todos los **informes de salida** de los ejercicios y prácticas, mostrando cómo los **scripts Python** se convierten en **herramientas de consultoría y docencia listas para usarse**.  
