# 📚 Guía de Ejercicios (1–5)
Este documento resume cada ejercicio con el enfoque **“primero explicación, después estructura”** para facilitar su lectura por parte de empresas, docentes y reclutadores.

---

## 📘 Ejercicio 1 – Auditoría de Clientes

### 🎯 Contexto y objetivo
Las PYMEs suelen tener bases de datos de clientes con **duplicados, valores nulos o ventas mal registradas**.  
Objetivo: **auditar** la base de datos de clientes para mejorar la calidad de los registros y permitir una **gestión comercial** más eficiente.

### 🧠 Metodología aplicada
**Directional Stimulus Prompting (DSP)**  
El modelo recibe **estímulos dirigidos** para detectar problemas específicos (duplicados, ventas negativas, outliers, etc.), enfocando la auditoría en **errores concretos**.

### 🏢 Sector aplicado
- PYMEs  
- Consultoría de negocio  
- Departamentos comerciales y de ventas  

### 📂 Estructura
- **Dataset:** `data_sample/clientes.xlsx`  
- **Script:** `scripts/audit_clientes.py`  
- **Informe:** `results/01_auditoria_clientes_result.md`  

**Errores introducidos en el dataset:**
- Duplicados de clientes  
- Ventas negativas  
- Ventas en cero  
- Valores nulos  
- Outliers en importes de venta  

---

## 📘 Ejercicio 2 – Riesgo País (España)

### 🎯 Contexto y objetivo
Empresas de comercio exterior necesitan medir el **riesgo país** al operar internacionalmente.  
En este ejercicio se analiza **España** usando **indicadores económicos oficiales** (Eurostat, OCDE, IMF).

### 🧠 Metodología aplicada
**Contrastive Few-Shot (CFS)**  
Se definen **ejemplos contrastivos** (positivos/negativos). El modelo compara España con **umbrales predefinidos** y **países de referencia**.

### 🌍 Sector aplicado
- Comercio exterior  
- Riesgo país y geopolítica económica  

### 📂 Estructura
- **Dataset:** `data_sample/riesgo_pais_spain_real.xlsx`  
- **Script:** `scripts/audit_riesgo_pais.py`  
- **Informe:** `results/02_riesgo_pais_result.md`  

**Reglas aplicadas:**
- Deuda pública / PIB  
- Déficit comercial  
- Inflación  
- Crecimiento del PIB  
- Deuda externa  

**Salida esperada:** clasificación de riesgo **Bajo / Medio / Alto**.

---

## 📘 Ejercicio 3 – Control de Registros Educativos

### 🎯 Contexto y objetivo
Los registros académicos suelen presentar **notas fuera de rango, fechas inválidas o duplicados**.  
Objetivo: auditar un dataset de estudiantes/asignaturas y garantizar **coherencia** en calificaciones y matrículas.

### 🧠 Metodología aplicada
**Draft-then-Revise (DtR)**  
- **Draft:** detectar problemas evidentes  
- **Revise:** revisar correcciones y **normalizar** datos  

### 🎓 Sector aplicado
- Educación  
- Gestión académica  
- Control de calidad de datos en universidades e institutos  

### 📂 Estructura
- **Dataset:** `data_sample/registros_educativos.xlsx`  
- **Script:** `scripts/control_registros.py`  
- **Informes:**  
  - `results/03_control_registros_result.md`  
  - `results/03_registros_educativos_limpio.xlsx`  

**Errores introducidos en el dataset:**
- Estudiantes duplicados  
- Notas fuera de rango (p. ej., > 10)  
- Fechas de matrícula inválidas  
- Campos vacíos en asignaturas o calificaciones  

---

## 📘 Ejercicio 4 – Auditoría de Padrones Municipales

### 🎯 Contexto y objetivo
Los padrones municipales son registros oficiales de habitantes. Un ayuntamiento necesita asegurar **consistencia** para fines **estadísticos, fiscales y de servicios públicos**.  
Objetivo: auditar un padrón ficticio, detectando incoherencias en **DNIs, fechas, domicilios, municipios y estados de alta/baja**.

### 🧠 Metodología aplicada
**Self-Consistency (Auto-consistencia)**  
Se aplican varias **rutas de validación** (p. ej., edad máxima 100 vs. 120 años, CP–provincia, duplicados por DNI o por nombre) y se combinan por **votación mayoritaria** para reducir falsos positivos.

### 🏛️ Sector aplicado
- Administración pública  
- Gestión municipal  
- Consultoría en datos institucionales  

### 📂 Estructura
- **Dataset:** `data_sample/municipal_padron.xlsx`  
- **Script:** `scripts/auditoria_padron.py`  
- **Informes:**  
  - `results/04_auditoria_padron_result.md`  
  - `results/04_padron_limpio.xlsx`  

**Errores introducidos en el dataset:**
- DNIs inválidos o vacíos  
- CP incoherente con provincia  
- Municipios fuera de provincia  
- Fechas imposibles (nacimientos en 2050, edades > 120 años)  
- Fechas de baja anteriores a la fecha de alta  
- Sexo inválido (p. ej., “X”)  
- Nacionalidad y domicilio vacíos  
- Registros duplicados  

---

## 📘 Ejercicio 5 – Auditoría de Historias Clínicas Electrónicas (EHR)

### 🎯 Contexto y objetivo
Las **Historias Clínicas Electrónicas (EHR)** son críticas en sanidad. Hay que evitar **errores, duplicados e incoherencias** que afecten a diagnósticos, tratamientos o facturación.  
Objetivo: auditar un dataset de historias clínicas y detectar **pacientes duplicados, fechas incoherentes, campos médicos vacíos, códigos ICD-10 no válidos y edades imposibles**.

### 🧠 Metodología aplicada
**Chain-of-Thought (CoT) – Razonamiento Encadenado**  
En lugar de reglas directas, se sigue un **paso a paso lógico** por registro:
1. Calcular edad  
2. Validar rango lógico  
3. Comprobar que **Fecha_Alta** > **Fecha_Ingreso**  
4. Validar **Código_ICD10** frente a diccionario  
5. Marcar inconsistencias acumuladas  

### 🏥 Sector aplicado
- Sanidad pública y privada  
- Consultoría en gestión hospitalaria  
- Proyectos de calidad de datos en salud digital  

### 📂 Estructura
**Dataset de ejemplo**  
- **Ruta:** `data_sample/historias_clinicas.xlsx`  
- **Columnas:**  
  - `ID_Paciente`  
  - `Nombre`, `Apellidos`  
  - `Fecha_Nacimiento`  
  - `Sexo`  
  - `Fecha_Ingreso`  
  - `Fecha_Alta`  
  - `Diagnóstico`  
  - `Código_ICD10`  
  - `Tratamiento`  
  - `Médico_Responsable`  
- **Errores introducidos:** duplicados, edades imposibles, diagnósticos vacíos, códigos ICD-10 no válidos, **altas antes del ingreso**.

**Script Python**  
- **Ruta:** `scripts/auditoria_ehr.py`  
- **Características:**  
  - Carga el dataset  
  - Aplica auditoría con **CoT (paso a paso)**  
  - Genera:  
    - `results/05_auditoria_ehr_result.md` (informe)  
    - `results/05_historias_clinicas_limpio.xlsx` (dataset con banderas de error)  
  - **100% comentado en español**

**Informe de resultados**  
- **Ruta:** `results/05_auditoria_ehr_result.md`  
- **Contenido:** descripción del proceso, estadísticas de errores, ejemplos de registros problemáticos y **conclusiones** sobre la calidad de datos en sanidad.

