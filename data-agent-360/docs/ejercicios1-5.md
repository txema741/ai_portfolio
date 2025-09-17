# 📚 Guía de Ejercicios – Data Agent 360

Este documento recopila las explicaciones pedagógicas de cada ejercicio del proyecto, siguiendo el esquema:
1. Contexto y objetivo  
2. Metodología aplicada  
3. Sector aplicado  
4. Estructura de archivos  
5. Errores introducidos en el dataset  

---

## 📘 Ejercicio 1 – Auditoría de Clientes

### 🎯 Contexto y objetivo
Las PYMEs suelen tener bases de datos de clientes con **duplicados, valores nulos o ventas mal registradas**.  
El objetivo es auditar la base de datos de clientes para mejorar la calidad de los registros y permitir una **gestión comercial más eficiente**.

### 🧠 Metodología aplicada
**Directional Stimulus Prompting (DSP)**  
El modelo recibe **estímulos dirigidos** para detectar problemas específicos como duplicados, ventas negativas o outliers.  

### 🏢 Sector aplicado
- PYMEs  
- Consultoría de negocio  
- Departamentos comerciales y de ventas  

### 📂 Estructura
- Dataset: `data_sample/clientes.xlsx`  
- Script: `scripts/audit_clientes.py`  
- Informe: `results/01_auditoria_clientes_result.md`  

### ❌ Errores introducidos en el dataset
- Duplicados de clientes  
- Ventas negativas  
- Ventas en cero  
- Valores nulos  
- Outliers en importes de venta  

---

## 📘 Ejercicio 2 – Riesgo País (España)

### 🎯 Contexto y objetivo
Empresas de comercio exterior necesitan medir el **riesgo país** antes de operar internacionalmente.  
En este ejercicio se analiza España con **indicadores económicos oficiales** (Eurostat, OCDE, IMF).

### 🧠 Metodología aplicada
**Contrastive Few-Shot (CFS)**  
Se definen ejemplos contrastivos (positivos/negativos) y el modelo compara España con **umbrales predefinidos** y **países de referencia**.

### 🌍 Sector aplicado
- Comercio exterior  
- Riesgo país y geopolítica económica  

### 📂 Estructura
- Dataset: `data_sample/riesgo_pais_spain_real.xlsx`  
- Script: `scripts/audit_riesgo_pais.py`  
- Informe: `results/02_riesgo_pais_result.md`  

### ❌ Reglas de validación
- Deuda pública / PIB  
- Déficit comercial  
- Inflación  
- Crecimiento del PIB  
- Deuda externa  

**Salida esperada:** clasificación de riesgo **Bajo / Medio / Alto**.  

---

## 📘 Ejercicio 3 – Control de Registros Educativos

### 🎯 Contexto y objetivo
Los registros académicos suelen contener **notas fuera de rango, fechas inválidas o duplicados**.  
El objetivo es auditar un dataset de estudiantes y asignaturas para garantizar la **coherencia de calificaciones y matrículas**.

### 🧠 Metodología aplicada
**Draft-then-Revise (DtR)**  
1. **Draft**: detectar problemas evidentes  
2. **Revise**: revisar correcciones y normalizar los datos  

### 🎓 Sector aplicado
- Educación  
- Gestión académica  
- Control de calidad de datos en universidades e institutos  

### 📂 Estructura
- Dataset: `data_sample/registros_educativos.xlsx`  
- Script: `scripts/control_registros.py`  
- Informes:  
  - `results/03_control_registros_result.md`  
  - `results/03_registros_educativos_limpio.xlsx`  

### ❌ Errores introducidos en el dataset
- Estudiantes duplicados  
- Notas fuera de rango (p. ej., >10)  
- Fechas de matrícula inválidas  
- Campos vacíos en asignaturas o calificaciones  

---

## 📘 Ejercicio 4 – Auditoría de Padrones Municipales

### 🎯 Contexto y objetivo
Los padrones municipales son registros oficiales de habitantes.  
Un ayuntamiento debe asegurar que sus datos son **consistentes y fiables** para fines **estadísticos, fiscales y de servicios públicos**.  
Objetivo: auditar un padrón ficticio y detectar incoherencias en **DNIs, fechas, domicilios, municipios y estados de alta/baja**.

### 🧠 Metodología aplicada
**Self-Consistency (Auto-consistencia)**  
Se aplican múltiples **rutas de validación** (edad máxima, CP–provincia, duplicados) y se combinan por **votación mayoritaria**, reduciendo falsos positivos.  

### 🏛️ Sector aplicado
- Administración pública  
- Gestión municipal  
- Consultoría en datos institucionales  

### 📂 Estructura
- Dataset: `data_sample/municipal_padron.xlsx`  
- Script: `scripts/auditoria_padron.py`  
- Informes:  
  - `results/04_auditoria_padron_result.md`  
  - `results/04_padron_limpio.xlsx`  

### ❌ Errores introducidos en el dataset
- DNIs inválidos o vacíos  
- CP incoherente con provincia  
- Municipios fuera de provincia  
- Fechas imposibles (nacimientos en 2050, edades >120 años)  
- Fechas de baja anteriores a la fecha de alta  
- Sexo inválido (ej. “X”)  
- Nacionalidad y domicilio vacíos  
- Registros duplicados  

---

## 📘 Ejercicio 5 – Auditoría de Historias Clínicas Electrónicas (EHR)

### 🎯 Contexto y objetivo
Las **Historias Clínicas Electrónicas (EHR)** son críticas en sanidad.  
Se deben evitar **errores, duplicados e incoherencias** que afecten a diagnósticos, tratamientos o facturación.  
Objetivo: auditar un dataset de historias clínicas y detectar **pacientes duplicados, fechas incoherentes, campos vacíos, códigos ICD-10 inválidos y edades imposibles**.

### 🧠 Metodología aplicada
**Chain-of-Thought (CoT) – Razonamiento Encadenado**  
Se sigue un **paso a paso lógico**:  
1. Calcular edad  
2. Validar rango lógico  
3. Comprobar que **Fecha_Alta** > **Fecha_Ingreso**  
4. Validar **Código_ICD10** frente al diccionario  
5. Marcar inconsistencias acumuladas  

### 🏥 Sector aplicado
- Sanidad pública y privada  
- Consultoría en gestión hospitalaria  
- Proyectos de calidad de datos en salud digital  

### 📂 Estructura
- Dataset: `data_sample/historias_clinicas.xlsx`  
- Script: `scripts/auditoria_ehr.py`  
- Informes:  
  - `results/05_auditoria_ehr_result.md`  
  - `results/05_historias_clinicas_limpio.xlsx`  

### ❌ Errores introducidos en el dataset
- Pacientes duplicados  
- Fechas de alta anteriores al ingreso  
- Diagnósticos vacíos  
- Códigos ICD-10 no válidos  
- Edades imposibles o fechas de nacimiento erróneas  
