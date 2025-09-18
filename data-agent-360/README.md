# 🤖 Data Agent 360 – Auditoría Inteligente de Datos

**Autor:** Txema Ríos (@txema741)  
**Repositorio:** [ai_portfolio/data-agent-360](https://github.com/txema741/ai_portfolio/tree/main/data-agent-360)  

---

## 📌 Sobre el proyecto
**Data Agent 360** es un entorno de **auditoría de datos con Inteligencia Artificial aplicada**, diseñado para combinar **consultoría empresarial** y **docencia en IA**.  
Cada ejercicio muestra cómo aplicar metodologías avanzadas de **prompting y validación automatizada** sobre datasets sintéticos con errores intencionales.

---

## 📂 Estructura del repositorio

- **/data_sample/** → Datasets sintéticos de ejemplo (Excel con errores introducidos).  
- **/scripts/** → Scripts en Python (100% comentados en español).  
- **/results/** → Informes en Markdown y datasets corregidos.  
- **/docs/** → Documentación metodológica y consultiva (manuales, guías de prompting, casos sectoriales).  
- **/images/** → Diagramas y visualizaciones.  
- **/datos-ia/** → Carpeta extra para pruebas, materiales complementarios o datasets adicionales.  

---

## 📑 Índice de ejercicios

🔹 **Ejercicio 1 – Auditoría de Clientes (DSP)**  
Dataset: `data_sample/clientes.xlsx`  
Script: `scripts/audit_clientes.py`  
Resultados: `results/01_auditoria_clientes_result.md`  
Descripción: Detección de duplicados, valores nulos, ventas negativas/cero y outliers.  

---

🔹 **Ejercicio 2 – Riesgo País (España, CFS)**  
Dataset: `data_sample/riesgo_pais_spain_real.xlsx`  
Script: `scripts/auditoria_riesgo_pais.py`  
Resultados: `results/02_riesgo_pais_result.md`  
Descripción: Evaluación de riesgo país con indicadores macroeconómicos oficiales.  

---

🔹 **Ejercicio 3 – Control de Registros Educativos (DtR)**  
Dataset: `data_sample/registros_educativos.xlsx`  
Script: `scripts/control_registros.py`  
Resultados:  
- `results/03_control_registros_result.md`  
- `results/03_registros_educativos_limpio.xlsx`  
Descripción: Validación académica: duplicados, notas fuera de rango, fechas inválidas y campos vacíos.  

---

🔹 **Ejercicio 4 – Auditoría de Padrones Municipales (SC)**  
Dataset: `data_sample/municipal_padron.xlsx`  
Script: `scripts/auditoria_padron.py`  
Resultados:  
- `results/04_auditoria_padron_result.md`  
- `results/04_padron_limpio.xlsx`  
Descripción: Validación de DNIs, edades, CP–Provincia–Municipio, altas/bajas incoherentes y duplicados.  

---

🔹 **Ejercicio 5 – Auditoría de Historias Clínicas (EHR, CoT)**  
Dataset: `data_sample/historias_clinicas.xlsx`  
Script: `scripts/auditoria_ehr.py`  
Resultados:  
- `results/05_auditoria_ehr_result.md`  
- `results/05_historias_clinicas_limpio.xlsx`  
Descripción: Auditoría clínica: duplicados, fechas incoherentes, ICD-10 inválidos, edades imposibles y campos vacíos.  

---

🔹 **Ejercicio 6 – Auditoría de Transacciones Bancarias (CoT vectorizado)**  
Dataset: `data_sample/transacciones_bancarias.xlsx`  
Script: `scripts/auditoria_transacciones.py`  
Resultados:  
- `results/06_auditoria_transacciones_result.md`  
- `results/06_transacciones_limpio.xlsx`  
Descripción: Duplicados, fechas incoherentes, monedas inválidas, IBAN incorrectos, importes incoherentes y campos vacíos.  

---

🔹 **Ejercicio 7 – Auditoría de Envíos y Trazabilidad Logística (SC + CoT)**  
Dataset: `data_sample/envios_logistica.xlsx`  
Script: `scripts/auditoria_envios.py`  
Resultados:  
- `results/07_auditoria_envios_result.md`  
- `results/07_envios_limpio.xlsx`  
Descripción: Auditoría logística: duplicados, fechas incoherentes, CP–Ciudad inconsistentes, transportistas inválidos, pesos/volúmenes imposibles y registros incompletos.  

---

🔹 **Ejercicio 8 – Auditoría de Pólizas y Siniestros de Seguros (SC + CoT vectorizado)**  
Dataset: `data_sample/polizas_siniestros.xlsx`  
Script: `scripts/auditoria_seguro.py`  
Resultados:  
- `results/08_auditoria_seguro_result.md`  
- `results/08_polizas_siniestros_limpio.xlsx`  
Descripción: Auditoría de pólizas y siniestros: duplicados, fechas incoherentes, montos fuera de rango, tipos de póliza inválidos y campos vacíos.  

---

🔹 **Ejercicio 9 – Auditoría de Consumos Energéticos (CoT + reglas vectorizadas)**  
Dataset: `data_sample/consumos_energia.xlsx`  
Script: `scripts/auditoria_energia.py`  
Resultados:  
- `results/09_auditoria_energia_result.md`  
- `results/09_consumos_energia_limpio.xlsx`  
Descripción: Auditoría energética: duplicados, periodos inválidos, consumos fuera de rango, costes incoherentes, tarifas inválidas y clientes vacíos.  

---

🔹 **Ejercicio 10 – Auditoría de Inventarios y Cadenas de Suministro (ReAct)**  
Dataset: `data_sample/inventarios.xlsx`  
Script: `scripts/auditoria_inventarios.py`  
Resultados:  
- `results/10_auditoria_inventarios_result.md`  
- `results/10_inventarios_limpio.xlsx`  
Descripción: Auditoría de inventarios: duplicados, fechas incoherentes/fuera de rango, cantidades y precios inválidos, códigos de producto y almacenes no registrados.  

---

## 🎯 Objetivo
Data Agent 360 busca demostrar cómo la **IA aplicada al control de calidad de datos** puede servir tanto a:
- **Empresas** → consultoría en auditoría de datos.  
- **Educación** → materiales didácticos en IA aplicada.  

---

## 📬 Contacto
- Autor: Txema Ríos  
- GitHub: [@txema741](https://github.com/txema741)
