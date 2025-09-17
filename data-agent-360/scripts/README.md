🔹 Ejercicio 1 – Auditoría de clientes (DSP)
Archivo: scripts/audit_clientes.py
Metodología aplicada: Directional Stimulus Prompting (DSP)
Dataset: data_sample/clientes.xlsx
Informes generados:
- results/01_auditoria_clientes_result.md
Descripción: Detección de duplicados, valores nulos, ventas negativas/cero y outliers en importes de venta.

🔹 Ejercicio 2 – Riesgo País (España, CFS)
Archivo: scripts/audit_riesgo_pais.py
Metodología aplicada: Contrastive Few-Shot (CFS)
Dataset: data_sample/riesgo_pais_spain_real.xlsx
Informes generados:
- results/02_riesgo_pais_result.md
Descripción: Evaluación del riesgo país de España con indicadores oficiales (Eurostat, OCDE, IMF). Reglas: deuda pública/PIB, déficit comercial, inflación, crecimiento del PIB, deuda externa. Salida: Bajo / Medio / Alto.

🔹 Ejercicio 3 – Control de registros educativos (Draft-then-Revise)
Archivo: scripts/control_registros.py
Metodología aplicada: Draft-then-Revise (DtR)
Dataset: data_sample/registros_educativos.xlsx
Informes generados:
- results/03_control_registros_result.md
- results/03_registros_educativos_limpio.xlsx
Descripción: Detección de duplicados, notas fuera de rango, valores nulos y validación de fechas de matrícula mediante dos iteraciones (borrador y revisión).

🔹 Ejercicio 4 – Auditoría de padrones municipales (Self-Consistency)
Archivo: scripts/auditoria_padron.py
Metodología aplicada: Self-Consistency (Auto-consistencia)
Dataset: data_sample/municipal_padron.xlsx
Informes generados:
- results/04_auditoria_padron_result.md
- results/04_padron_limpio.xlsx
Descripción: Valida DNIs, edades, coherencia CP–Provincia–Municipio, altas y bajas incoherentes y duplicados. Combina múltiples rutas de validación por votación mayoritaria.

🔹 Ejercicio 5 – Auditoría de historias clínicas (EHR, CoT)
Archivo: scripts/auditoria_ehr.py
Metodología aplicada: Chain-of-Thought (CoT)
Dataset: data_sample/historias_clinicas.xlsx
Informes generados:
- results/05_auditoria_ehr_result.md
- results/05_historias_clinicas_limpio.xlsx
Descripción: Detecta duplicados, fechas incoherentes (alta < ingreso), códigos ICD-10 inválidos, edades imposibles y campos vacíos (diagnóstico, tratamiento) mediante razonamiento encadenado paso a paso.

