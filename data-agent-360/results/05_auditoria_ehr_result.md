# Ejercicio 5 – Auditoría de Historias Clínicas (EHR)
**Metodología:** Chain-of-Thought (CoT) – Razonamiento Encadenado  
**Sector aplicado:** Sanidad, gestión hospitalaria y salud digital.

---

## 🗓️ Ejecución
- Fecha y hora de auditoría: **2025-09-17 20:10**
- Filas totales (entrada): **278**

## 📊 Resumen de incidencias
- Duplicados por ID: **36**
- Duplicados por clave: **36**
- Edades imposibles: **8**
- Alta antes de ingreso: **42**
- ICD10 inválido (no vacío): **74**
- Sexo inválido: **98**
- Diagnóstico vacío: **30**
- Tratamiento vacío: **33**

## 📑 Ejemplos
**Duplicados por ID_Paciente**
|   ID_Paciente | Nombre   | Apellidos         | Fecha_Nacimiento   | Fecha_Ingreso   | Fecha_Alta   |
|--------------:|:---------|:------------------|:-------------------|:----------------|:-------------|
|        500003 | Marta    | Ruiz López        | 1946-07-15         | 2010-06-11      | 2010-06-15   |
|        500030 | Marta    | Vázquez Díaz      | 1993-05-07         | 2021-04-27      | 2021-04-24   |
|        500065 | Pablo    | Vázquez Hernández | 1985-11-18         | 2013-06-04      | 2013-07-02   |
|        500078 | Lucía    | Gómez Fernández   | 1992-10-01         | 2016-07-11      | 2016-08-02   |
|        500102 | Carlos   | Álvarez Vázquez   | 1968-10-19         | 2019-02-21      | 2019-03-22   |
|        500114 | Sara     | Moreno González   | 1940-11-20         | 2023-10-23      | 2023-10-31   |
|        500117 | Miguel   | Torres Álvarez    | 2001-07-28         | 2019-10-06      | 2019-10-07   |
|        500122 | Laura    | García Martínez   | 1998-09-26         | 2011-02-12      | 2011-03-13   |
|        500130 | Nuria    | Ruiz González     | 1890-01-01         | 2023-08-07      | 2023-08-22   |
|        500152 | Pablo    | López Gómez       | 1964-06-10         | 2018-10-04      | 2018-10-14   |
|        500177 | Pablo    | Moreno Gómez      | 1945-04-06         | 2023-07-17      | 2023-08-14   |
|        500182 | Raúl     | Moreno Fernández  | 1969-08-26         | 2024-02-04      | 2024-02-04   |
**Altas anteriores al ingreso**
|   ID_Paciente | Nombre   | Apellidos          | Fecha_Ingreso   | Fecha_Alta   |
|--------------:|:---------|:-------------------|:----------------|:-------------|
|        500009 | Carlos   | Fernández González | 2015-12-01      | 2015-11-27   |
|        500017 | Sofía    | González Gómez     | 2010-06-04      | 2010-05-31   |
|        500019 | Diego    | Castro Ruiz        | 2018-07-22      | 2018-07-21   |
|        500024 | Lucía    | García García      | 2019-03-28      | 2019-03-24   |
|        500028 | Carmen   | Pérez Moreno       | 2022-12-13      | 2022-12-12   |
|        500030 | Marta    | Vázquez Díaz       | 2021-04-27      | 2021-04-24   |
|        500036 | Juan     | Navarro Gómez      | 2022-05-31      | 2022-05-28   |
|        500038 | Marta    | García Álvarez     | 2023-05-25      | 2023-05-23   |
|        500046 | Alberto  | Hernández Gómez    | 2013-02-15      | 2013-02-13   |
|        500050 | Víctor   | Sánchez García     | 2018-05-13      | 2018-05-09   |
|        500057 | Carlos   | Navarro Castro     | 2022-02-09      | 2022-02-04   |
|        500059 | Sofía    | Ruiz Vázquez       | 2018-06-07      | 2018-06-02   |
**Códigos ICD-10 inválidos (no vacíos)**
|   ID_Paciente | Código_ICD10   | Diagnóstico     | Fecha_Ingreso   |
|--------------:|:---------------|:----------------|:----------------|
|        500000 | J4S            | Gastroenteritis | 2022-02-13      |
|        500004 | QQ1            | Asma            | 2014-02-04      |
|        500014 | QQ1            | Asma            | 2025-02-02      |
|        500017 | QQ1            | Ansiedad        | 2010-06-04      |
|        500024 | 123            | Asma            | 2019-03-28      |
|        500027 | Z0O            | Reflujo         | 2014-12-25      |
|        500029 | X99            | Gastroenteritis | 2018-11-11      |
|        500030 | L2O            | Diabetes tipo 2 | 2021-04-27      |
|        500031 | J4S            | Migraña         | 2015-01-27      |
|        500035 | Z0O            | Ansiedad        | 2019-12-16      |
|        500036 | 123            | nan             | 2022-05-31      |
|        500037 | 123            | Migraña         | 2023-04-22      |
**Edades imposibles**
|   ID_Paciente | Fecha_Nacimiento   |     Edad |
|--------------:|:-------------------|---------:|
|        500022 | 2050-01-01         | -24.2902 |
|        500031 | 2050-01-01         | -24.2902 |
|        500041 | 1890-01-01         | 135.707  |
|        500130 | 1890-01-01         | 135.707  |
|        500135 | 1890-01-01         | 135.707  |
|        500213 | 2050-01-01         | -24.2902 |
|        500217 | 1890-01-01         | 135.707  |
|        500130 | 1890-01-01         | 135.707  |

---
## ✅ Conclusiones
- El razonamiento encadenado (CoT) se implementa de forma vectorizada para mayor rendimiento.
- El dataset exportado incluye **banderas de error por registro** para priorizar correcciones.
- En proyectos reales, amplía el diccionario ICD-10 y añade reglas clínicas específicas del servicio.