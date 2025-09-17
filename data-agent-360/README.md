# 🤖 Data Agent 360 – Auditoría y Calidad de Datos Empresariales con IA

**Autor:** Txema Ríos ([@txema741](https://github.com/txema741))  
**Estado:** 🚧 En desarrollo (primeros módulos del portfolio de IA)

---

## 🎯 Objetivo del proyecto
Este repositorio forma parte de mi **portfolio profesional en Inteligencia Artificial aplicada a empresa y docencia**.  
Su meta es construir un **Agente de IA para la auditoría de datos de negocio**, capaz de:

- 🔎 Detectar errores de calidad (duplicados, nulos, inconsistencias).  
- ⚠️ Señalar riesgos financieros y operativos (ventas negativas, ventas a cero, valores atípicos).  
- 📝 Generar informes ejecutivos automáticos en **Markdown**, listos para consultoría o presentación a directivos.  
- 🎓 Servir de caso docente en clases de IA aplicada a **gestión empresarial, comercio exterior o administración pública**.  

---

## 🏗️ Estructura del repositorio

data-agent-360/
├─ data_sample/                 # Datasets de ejemplo (Excel)
│   ├─ clientes.xlsx
│   ├─ comercio_exterior.xlsx          (Ej. 2)
│   └─ riesgo_pais_spain_real.xlsx     (Ej. 2)
│
├─ scripts/                    # Scripts en Python
│   ├─ audit_clientes.py              (Ej. 1)
│   └─ audit_riesgo_pais.py           (Ej. 2)
│
├─ results/                    # Resultados de auditorías en Markdown
│   ├─ 01_auditoria_clientes_result.md
│   └─ 02_riesgo_pais_result.md
│
├─ docs/                       # Documentación adicional (en desarrollo)
├─ exercises/                  # Ejercicios de prompting y metodologías
├─ images/                     # Gráficos y visualizaciones
└─ README.md                   # Este archivo

---

## 📂 Ejercicios completados

### ✅ Ejercicio 1 – Auditoría de clientes (DSP)
- **Script:** [`scripts/audit_clientes.py`](scripts/audit_clientes.py)  
- **Dataset:** [`data_sample/clientes.xlsx`](data_sample/clientes.xlsx)  
- **Informe:** [`results/01_auditoria_clientes_result.md`](results/01_auditoria_clientes_result.md)  
- **Metodología:** Directional Stimulus Prompting (DSP).  
- **Sector aplicado:** PYMEs / consultoría de negocio.  

---

### ✅ Ejercicio 2 – Riesgo País (España, CFS)
- **Script:** [`scripts/audit_riesgo_pais.py`](scripts/audit_riesgo_pais.py)  
- **Dataset:** [`data_sample/riesgo_pais_spain_real.xlsx`](data_sample/riesgo_pais_spain_real.xlsx)  
- **Informe:** [`results/02_riesgo_pais_result.md`](results/02_riesgo_pais_result.md)  
- **Metodología:** Contrastive Few-Shot (CFS).  
- **Sector aplicado:** Comercio exterior y riesgo país.  

---

## 📅 Próximos ejercicios

- Ejercicio 3 → Control de registros educativos (Draft-then-Revise, DtR).  
- Ejercicio 4 → Auditoría de padrones municipales (Self-Consistency).  
- Ejercicio 5 → Transacciones sanitarias (Zero-shot + Chain-of-Thought).  

---

## 📌 Estado del portfolio
- ✔️ **Base de datos de clientes auditada**.  
- ✔️ **Indicadores de riesgo país (España) evaluados**.  
- ⏳ Próximos módulos incluirán **educación, administración pública, salud y visualizaciones gráficas**.  

---

## 📜 Licencia
Uso abierto con fines de **aprendizaje, docencia y consultoría empresarial**.  


