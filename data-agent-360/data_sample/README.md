# 📂 Carpeta de datasets – Data Agent 360

Datasets de entrada para los ejercicios.  
Cada archivo es un **Excel (.xlsx)** con errores intencionales para probar la auditoría de datos.

---

## Ejercicio 1 – Auditoría de Clientes (DSP)
- `clientes.xlsx`  
- Contiene duplicados, nulos, ventas negativas/cero y outliers.  

## Ejercicio 2 – Riesgo País (CFS)
- `riesgo_pais_spain_real.xlsx`  
- Indicadores macroeconómicos de España con umbrales para evaluar riesgo país.  

## Ejercicio 3 – Registros Educativos (DtR)
- `registros_educativos.xlsx`  
- Notas fuera de rango, fechas inválidas, duplicados y campos vacíos.  

## Ejercicio 4 – Padrones Municipales (Self-Consistency)
- `municipal_padron.xlsx`  
- DNIs inválidos, CP incoherentes, municipios fuera de provincia, fechas imposibles y duplicados.  

## Ejercicio 5 – Historias Clínicas (EHR, CoT)
- `historias_clinicas.xlsx`  
- Dataset ficticio de historias clínicas electrónicas (EHR).  
- Columnas: `ID_Paciente, Nombre, Apellidos, Fecha_Nacimiento, Sexo, Fecha_Ingreso, Fecha_Alta, Diagnóstico, Código_ICD10, Tratamiento, Médico_Responsable`  
- Errores: duplicados, edades imposibles (1890/2050), altas antes del ingreso, sexo inválido (“X”), diagnósticos/tratamientos vacíos, códigos ICD-10 inválidos.
