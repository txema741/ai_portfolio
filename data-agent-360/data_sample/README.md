# 📂 Carpeta de datasets – Data Agent 360

## 📘 Descripción
En esta carpeta se encuentran los **datasets de ejemplo** utilizados en los ejercicios del proyecto **Data Agent 360 – Auditoría y Calidad de Datos Empresariales con IA**.  

Los datasets son **ficticios pero realistas**, con errores intencionales añadidos para mostrar la utilidad de las auditorías de datos.  
Todos los ficheros están en formato **Excel (.xlsx)**, fácilmente legibles y editables.

---

## 📂 Índice de datasets

### 🔹 Ejercicio 1 – Auditoría de clientes (DSP)
- **Archivo:** `data_sample/clientes.xlsx`  
- **Contenido:** Información de clientes de una pyme, incluyendo ventas, importes y campos de identificación.  
- **Errores introducidos:** duplicados, valores nulos, ventas negativas, ventas en cero y outliers en importes.  
- **Uso:** Detectar inconsistencias básicas en datos de negocio.  

---

### 🔹 Ejercicio 2 – Riesgo País (España, CFS)
- **Archivo:** `data_sample/riesgo_pais_spain_real.xlsx`  
- **Contenido:** Indicadores macroeconómicos de España (deuda pública, déficit, inflación, PIB, etc.).  
- **Errores introducidos:** valores inconsistentes y rangos fuera de umbral.  
- **Uso:** Clasificación de riesgo país en Bajo / Medio / Alto mediante reglas contrastivas.  

---

### 🔹 Ejercicio 3 – Control de registros educativos (DtR)
- **Archivo:** `data_sample/registros_educativos.xlsx`  
- **Contenido:** Registros académicos de estudiantes (ID, nombre, asignatura, fecha de matrícula, nota final).  
- **Errores introducidos:** duplicados, notas fuera de rango, fechas inválidas y campos vacíos.  
- **Uso:** Demostrar cómo una doble revisión (*Draft-then-Revise*) mejora la limpieza de datos educativos.  

---

### 🔹 Ejercicio 4 – Auditoría de padrones municipales (Self-Consistency)
- **Archivo:** `data_sample/municipal_padron.xlsx`  
- **Contenido:** Registros de habitantes (ID, nombre, apellidos, DNI, sexo, nacionalidad, domicilio, CP, municipio, provincia, altas/bajas).  
- **Errores introducidos:**  
  - DNIs inválidos o vacíos.  
  - Códigos postales incoherentes con la provincia.  
  - Municipios fuera de provincia.  
  - Fechas imposibles de nacimiento o incoherentes entre alta/baja.  
  - Sexo inválido.  
  - Nacionalidad y domicilio vacíos.  
  - Registros duplicados.  
- **Uso:** Ejemplo de auditoría compleja con *Self-Consistency*, combinando múltiples rutas de validación.  

---

## 🎯 Objetivo de esta carpeta
Centralizar los **datasets de entrada** de todos los ejercicios.  
Son la **materia prima** que los scripts de `scripts/` utilizan para demostrar cómo la Inteligencia Artificial y las técnicas de *prompting avanzado* pueden aplicarse a la **auditoría y calidad de datos** en distintos sectores.

