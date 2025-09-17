# Ejercicio 5 – Auditoría de Historias Clínicas Electrónicas (EHR)
**Metodología:** Chain-of-Thought (CoT) – Razonamiento encadenado  
**Sector aplicado:** Sanidad pública y privada, gestión hospitalaria y salud digital

---

## 🎯 Objetivo
Auditar un dataset de EHR para detectar:
- **Duplicados** (por `ID_Paciente` y por clave `(Nombre, Apellidos, Fecha_Nacimiento)`).
- **Fechas incoherentes** (`Fecha_Alta` < `Fecha_Ingreso`).
- **Códigos ICD-10 inválidos**.
- **Edades imposibles** (negativas o > 120 años).
- **Campos vacíos** en diagnóstico y tratamiento.
- **Sexo inválido** (p. ej., “X”).

> **Nota**: el dataset es sintético con **errores intencionales** para docencia.

---

## 🧠 Metodología (CoT) – Lógica paso a paso
Para cada registro se realiza un razonamiento encadenado:

1. **Parseo robusto de fechas** y normalización de strings.
2. **Cálculo de edad**: `(hoy – Fecha_Nacimiento) / 365.25`.
3. **Validación temporal**: exigir `Fecha_Alta > Fecha_Ingreso`.
4. **Validación clínica**: `Código_ICD10` ∈ catálogo (demo) y `Sexo` ∈ {M, F}.
5. **Completitud**: `Diagnóstico` y `Tratamiento` no vacíos.
6. **Duplicados**: detección por `ID_Paciente` y por clave `(Nombre, Apellidos, Fecha_Nacimiento)`.

Cada regla levanta una **bandera** (`flag_*`); la suma de banderas por fila permite priorizar la corrección.

---

## 📦 Dataset
- **Archivo**: `data_sample/historias_clinicas.xlsx`  
- **Columnas**:  
  `ID_Paciente, Nombre, Apellidos, Fecha_Nacimiento, Sexo, Fecha_Ingreso, Fecha_Alta, Diagnóstico, Código_ICD10, Tratamiento, Médico_Responsable`.

---

## 📊 Resumen de incidencias (vista rápida)
> Las cifras concretas pueden variar si se regenera el dataset; consulta las tablas de ejemplo y el Excel “limpio” para detalle por registro.

- Duplicados por **ID_Paciente**: detectados  
- Duplicados por **clave** `(Nombre, Apellidos, Fecha_Nacimiento)`: detectados  
- **Edades imposibles**: detectadas  
- **Altas** anteriores al **ingreso**: detectadas  
- **ICD-10 inválidos** (no vacíos): detectados  
- **Sexo inválido**: pueden existir  
- **Diagnóstico/Tratamiento vacíos**: pueden existir

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
| 500117      | Miguel | Torres Álvarez      | 2001-07-28       | 2019-10-06    | 2019-10-07 |
| 500122      | Laura  | García Martínez     | 1998-09-26       | 2011-02-12    | 2011-03-13 |
| 500130      | Nuria  | Ruiz González       | 1890-01-01       | 2023-08-07    | 2023-08-22 |
| 500152      | Pablo  | López Gómez         | 1964-06-10       | 2018-10-04    | 2018-10-14 |
| 500177      | Pablo  | Moreno Gómez        | 1945-04-06       | 2023-07-17    | 2023-08-14 |
| 500182      | Raúl   | Moreno Fernández    | 1969-08-26       | 2024-02-04    | 2024-02-04 |

---

### ⏳ Altas anteriores al ingreso
| ID_Paciente | Nombre | Apellidos           | Fecha_Ingreso | Fecha_Alta |
|------------:|:-------|:--------------------|:--------------|:-----------|
| 500009      | Carlos | Fernández González  | 2015-12-01    | 2015-11-27 |
| 500017      | Sofía  | González Gómez      | 2010-06-04    | 2010-05-31 |
| 500019      | Diego  | Castro Ruiz         | 2018-07-22    | 2018-07-21 |
| 500024      | Lucía  | García García       | 2019-03-28    | 2019-03-24 |
| 500028      | Carmen | Pérez Moreno        | 2022-12-13    | 2022-12-12 |
| 500030      | Marta  | Vázquez Díaz        | 2021-04-27    | 2021-04-24 |
| 500036      | Juan   | Navarro Gómez       | 2022-05-31    | 2022-05-28 |
| 500038      | Marta  | García Álvarez      | 2023-05-25    | 2023-05-23 |
| 500046      | Alberto| Hernández Gómez     | 2013-02-15    | 2013-02-13 |
| 500050      | Víctor | Sánchez García      | 2018-05-13    | 2018-05-09 |
| 500057      | Carlos | Navarro Castro      | 2022-02-09    | 2022-02-04 |
| 500059      | Sofía  | Ruiz Vázquez        | 2018-06-07    | 2018-06-02 |

---

### ❌ Códigos ICD-10 inválidos (no vacíos)
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
| 500031      | J4S          | Migraña          | 2015-01-27    |
| 500035      | Z0O          | Ansiedad         | 2019-12-16    |
| 500036      | 123          | (vacío)          | 2022-05-31    |
| 500037      | 123          | Migraña          | 2023-04-22    |

---

### 👵👶 Edades imposibles
| ID_Paciente | Fecha_Nacimiento | Edad (aprox.) |
|------------:|:-----------------|--------------:|
| 500022      | 2050-01-01       | -24.29        |
| 500031      | 2050-01-01       | -24.29        |
| 500041      | 1890-01-01       | 135.71        |
| 500130      | 1890-01-01       | 135.71        |
| 500135      | 1890-01-01       | 135.71        |
| 500213      | 2050-01-01       | -24.29        |
| 500217      | 1890-01-01       | 135.71        |
| 500130      | 1890-01-01       | 135.71        |

> **Nota**: se muestran filas de ejemplo; el Excel “limpio” contiene todas las banderas por registro.

---

## 🛠️ Recomendaciones
- **Duplicados**: consolidar historiales y unificar `ID_Paciente`; mantener auditoría por clave `(Nombre, Apellidos, Fecha_Nacimiento)`.
- **Fechas**: bloquear estancias con `alta < ingreso`; reglas en ETL para recortar espacios y validar formatos.
- **ICD-10**: usar un catálogo oficial (lookup) y **validación previa** a persistencia.
- **Edad**: límites 0–120 años; investigar casos con 1890/2050.
- **Completitud**: forzar `Diagnóstico`/`Tratamiento` no vacíos en el alta.
- **Sexo**: restringir a {M, F} según requisitos del sistema (o mapear catálogos ampliados si aplica).

---

## 📤 Entregables
- **Informe** (este Markdown): `results/05_auditoria_ehr_result.md`  
- **Dataset marcado/limpio**: `results/05_historias_clinicas_limpio.xlsx`  
  (incluye columnas `flag_*`, `flags_total` y `registro_valido`).

---

## 🔁 Reproducibilidad
Ejecutar desde la raíz del proyecto:
```bash
python scripts/auditoria_ehr.py
