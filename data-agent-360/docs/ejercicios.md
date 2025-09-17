📘 Ejercicio 1 – Auditoría de Clientes
🎯 Contexto y objetivo

Las empresas pequeñas y medianas (PYMEs) suelen tener bases de datos de clientes con duplicados, valores nulos o ventas mal registradas.
El objetivo de este ejercicio es auditar una base de datos de clientes para mejorar la calidad de los registros y permitir una gestión comercial más eficiente.

🧠 Metodología aplicada

Directional Stimulus Prompting (DSP)

El modelo recibe estímulos o ejemplos dirigidos para detectar problemas específicos: duplicados, ventas negativas, outliers, etc.

Permite focalizar la auditoría en errores concretos.

🏢 Sector aplicado

PYMEs

Consultoría de negocio

Departamentos comerciales y de ventas

📂 Estructura del Ejercicio 1

Dataset: data_sample/clientes.xlsx

Script: scripts/audit_clientes.py

Informe: results/01_auditoria_clientes_result.md

Errores introducidos en el dataset:

Duplicados de clientes.

Ventas negativas.

Ventas en cero.

Valores nulos.

Outliers en importes de venta.

📘 Ejercicio 2 – Riesgo País (España)
🎯 Contexto y objetivo

Las empresas de comercio exterior necesitan medir el riesgo país al operar en mercados internacionales.
En este ejercicio se analiza el riesgo de España usando indicadores económicos oficiales (Eurostat, OCDE, IMF).

🧠 Metodología aplicada

Contrastive Few-Shot (CFS)

Se entrenan ejemplos positivos y negativos contrastivos.

El modelo compara España con umbrales predefinidos y otros países de referencia.

🌍 Sector aplicado

Comercio exterior

Riesgo país y geopolítica económica

📂 Estructura del Ejercicio 2

Dataset: data_sample/riesgo_pais_spain_real.xlsx

Script: scripts/audit_riesgo_pais.py

Informe: results/02_riesgo_pais_result.md

Reglas aplicadas en la auditoría:

Deuda pública / PIB

Déficit comercial

Inflación

Crecimiento del PIB

Deuda externa

Salida: clasificación de riesgo Bajo / Medio / Alto.

📘 Ejercicio 3 – Control de Registros Educativos
🎯 Contexto y objetivo

Los registros académicos suelen tener problemas como notas fuera de rango, fechas inválidas o duplicados.
El objetivo es auditar un dataset de estudiantes y asignaturas para garantizar que las calificaciones y matrículas sean coherentes.

🧠 Metodología aplicada

Draft-then-Revise (DtR)

Primera iteración (Draft): se detectan los problemas más evidentes.

Segunda iteración (Revise): se revisan las correcciones y se normalizan los datos.

🎓 Sector aplicado

Educación

Gestión académica

Control de calidad de datos en universidades e institutos

📂 Estructura del Ejercicio 3

Dataset: data_sample/registros_educativos.xlsx

Script: scripts/control_registros.py

Informes:

results/03_control_registros_result.md

results/03_registros_educativos_limpio.xlsx

Errores introducidos en el dataset:

Estudiantes duplicados.

Notas fuera de rango (ej. >10).

Fechas de matrícula inválidas.

Campos vacíos en asignaturas o calificaciones.

📘 Ejercicio 4 – Auditoría de Padrones Municipales
🎯 Contexto y objetivo

Los padrones municipales son registros oficiales de habitantes.
Un ayuntamiento necesita asegurar que los datos de su padrón son consistentes para fines estadísticos, fiscales y de servicios públicos.

👉 El objetivo del ejercicio es auditar un padrón ficticio, detectando incoherencias en DNIs, fechas, domicilios, municipios y estados de alta/baja.

🧠 Metodología aplicada

Self-Consistency (Auto-consistencia)

Se aplican varias “rutas de validación” (ej. edad máxima 100 vs. 120 años, validación CP–provincia, duplicados por DNI o nombre).

Los resultados se combinan por votación mayoritaria, reduciendo falsos positivos.

🏛️ Sector aplicado

Administración pública

Gestión municipal

Consultoría en datos institucionales

📂 Estructura del Ejercicio 4

Dataset: data_sample/municipal_padron.xlsx

Script: scripts/auditoria_padron.py

Informes:

results/04_auditoria_padron_result.md

results/04_padron_limpio.xlsx

Errores introducidos en el dataset:

DNIs inválidos o vacíos.

CP incoherente con provincia.

Municipios fuera de provincia.

Fechas imposibles (nacimientos en 2050, edades >120 años).

Fechas de baja anteriores a la fecha de alta.

Sexo inválido (ej. “X”).
📘 Ejercicio 5 – Auditoría de Historias Clínicas Electrónicas (EHR)
🎯 Contexto y objetivo

Las Historias Clínicas Electrónicas (EHR, Electronic Health Records) son bases de datos críticas en el sector sanitario.
Un hospital o clínica necesita asegurar que los registros médicos de pacientes no tengan errores, duplicados o incoherencias que puedan afectar a diagnósticos, tratamientos o facturación.

👉 El objetivo del ejercicio es aplicar técnicas de auditoría de datos sobre un dataset ficticio de historias clínicas, detectando:

Pacientes duplicados.

Fechas incoherentes (ej. alta hospitalaria anterior al ingreso).

Campos médicos vacíos (diagnóstico, tratamiento).

Códigos de enfermedad incorrectos (ej. ICD-10).

Edades imposibles o fechas de nacimiento erróneas.

🧠 Metodología aplicada

En este ejercicio aplicaremos Chain-of-Thought (CoT) o Razonamiento Encadenado.

En lugar de reglas directas, el sistema sigue un paso a paso lógico para evaluar la coherencia de cada registro.

Ejemplo:

Calcular edad del paciente.

Validar que está en un rango lógico.

Revisar que la fecha de alta sea posterior a la fecha de ingreso.

Validar que el código de enfermedad existe en el diccionario ICD-10.

Marcar inconsistencias acumuladas.

Esto refleja cómo un médico o un auditor humano razona paso a paso al revisar historias clínicas.

🏥 Sector aplicado

Sanidad pública y privada

Consultoría en gestión hospitalaria

Proyectos de calidad de datos en salud digital

📂 Estructura del Ejercicio 5
1) Dataset de ejemplo

Ruta: data_sample/historias_clinicas.xlsx

Columnas:

ID_Paciente

Nombre, Apellidos

Fecha_Nacimiento

Sexo

Fecha_Ingreso

Fecha_Alta

Diagnóstico

Código_ICD10

Tratamiento

Médico_Responsable

Errores introducidos: duplicados, edades imposibles, diagnósticos vacíos, códigos ICD-10 no válidos, altas antes del ingreso.

2) Script Python

Ruta: scripts/auditoria_ehr.py

Características:

Carga el dataset de historias clínicas.

Aplica la lógica de auditoría con Chain-of-Thought (paso a paso).

Genera dos salidas:

results/05_auditoria_ehr_result.md (informe en Markdown).

results/05_historias_clinicas_limpio.xlsx (dataset con banderas de error).

Todo el código estará 100% comentado en español.

3) Informe de resultados

Ruta: results/05_auditoria_ehr_result.md

Contendrá:

Descripción del proceso de auditoría.

Estadísticas de errores detectados.

Tablas de ejemplos de registros problemáticos.

Conclusiones sobre la importancia de la calidad de datos en sanidad.

Nacionalidad y domicilio vacíos.

Registros duplicados.
