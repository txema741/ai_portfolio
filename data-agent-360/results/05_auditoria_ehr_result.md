# Ejercicio 5 – Auditoría de Historias Clínicas Electrónicas (EHR)

**Metodología:** Chain-of-Thought (CoT) – Razonamiento Encadenado  
**Sector aplicado:** Sanidad pública y privada, gestión hospitalaria y salud digital.

---

## 🎯 Objetivo
Auditar un dataset de EHR para detectar:
- Pacientes duplicados  
- Fechas incoherentes (`Fecha_Alta` < `Fecha_Ingreso`)  
- Códigos ICD-10 inválidos  
- Edades imposibles  
- Campos vacíos en diagnóstico/tratamiento  

---

## 📊 Resumen de incidencias
- Duplicados por ID: **12**  
- Duplicados por clave (Nombre+Apellidos+Fecha_Nac): **10**  
- Edades imposibles: **7**  
- Altas antes de ingreso: **12**  
- ICD-10 inválido (no vacío): **12**  
- Sexo inválido: **X detectados**  
- Diagnóstico vacío: **N detectados**  
- Tratamiento vacío: **N detectados**

> Nota: las cifras pueden variar si se regenera el dataset.

---

## 📑 Ejemplos detectados

### 🔁 Duplicados por ID_Paciente
| ID_Paciente | Nombre | Apellidos           | Fecha_Nacimiento | Fecha_Ingreso | Fecha_Alta |
|------------:|:-------|:--------------------|:-----------------|:--------------|:-----------|
| 500003      | Marta  | Ruiz López          | 1946-07-15       | 2010-06-11    | 2010-06-15 |
| 500030      | Marta  | Vázquez Díaz        | 1993-05-07       | 2021-04-27    | 2021-04-24 |
| 500065      | Pablo  | Vázquez Hernández   | 1985-11-18       | 2013-06-04    | 2013-07-02 |
| 500078      | Lucía  | Gómez Fernández     | 1992-10-01       | 2016-07-11    | 2016-08-02 |
| 500102      | Carlos | Álvarez Vázquez     | 1968-10-19       | 2019-02-21    | 2019-03-22 |
| 500114      | Sara   | Moreno González     | 1940-11-20       | 2023-10-23    | 2023-10-31 |

---

### ⏳ Altas anteriores al ingreso
| ID_Paciente | Nombre | Apellidos           | Fecha_Ingreso | Fecha_Alta   |
|------------:|:-------|:--------------------|:--------------|:-------------|
| 500009      | Carlos | Fernández González  | 2015-12-01    | 2015-11-27   |
| 500017      | Sofía  | González Gómez      | 2010-06-04    | 2010-05-31   |
| 500019      | Diego  | Castro Ruiz         | 2018-07-22    | 2018-07-21   |
| 500024      | Lucía  | García García       | 2019-03-28    | 2019-03-24   |
| 500028      | Carmen | Pérez Moreno        | 2022-12-13    | 2022-12-12   |
| 500030      | Marta  | Vázquez Díaz        | 2021-04-27    | 2021-04-24   |

---

### ❌ Códigos ICD-10 inválidos
| ID_Paciente | Código_ICD10 | Diagnóstico      | Fecha_Ingreso |
|------------:|:-------------|:-----------------|:--------------|
| 500000      | J4S          | Gastroenteritis  | 2022-02-13    |
| 500004      | QQ1          | Asma             | 2014-02-04    |
| 500014      | QQ1          | Asma             | 2025-02-02    |
| 500017      | QQ1          | Ansiedad         | 2010-06-04    |
| 500024      | 123          | Asma             | 2019-03-28    |
| 500027      | Z0O          | Reflujo          | 2014-12-25    |
| 500029      | X99          | Gastroenteritis  | 2018-11-11    |
| 500030      | L2O          | Diabetes tipo 2  | 2021-04-27    |

---

### 👵👶 Edades imposibles
| ID_Paciente | Fecha_Nacimiento | Edad    |
|------------:|:-----------------|--------:|
| 500022      | 2050-01-01       | -24.29  |
| 500031      | 2050-01-01       | -24.29  |
| 500041      | 1890-01-01       | 135.70  |
| 500130      | 1890-01-01       | 135.70  |
| 500135      | 1890-01-01       | 135.70  |
| 500213      | 2050-01-01       | -24.29  |
| 500217      | 1890-01-01       | 135.70  |

---

## ✅ Conclusiones
- El razonamiento encadenado (CoT) permite auditar paso a paso la coherencia clínica de los registros.  
- Se detectaron múltiples tipos de errores: **duplicados, incoherencias temporales, códigos inválidos y edades imposibles**.  
- El dataset de salida (`results/05_historias_clinicas_limpio.xlsx`) incluye banderas de error por registro para priorizar correcciones.  
- Este enfoque es escalable a otros módulos hospitalarios (urgencias, farmacia, facturación).

---
