
📘 Ejercicio 6 – Auditoría de Transacciones Bancarias (SMEs, CoT + Rules)
🎯 Contexto y objetivo

Los bancos y entidades financieras manejan millones de transacciones cada día. La calidad de los datos es crítica para detectar fraudes, evitar duplicidades contables y cumplir con regulaciones.

👉 El objetivo de este ejercicio es auditar un dataset ficticio de transacciones bancarias para detectar:

Duplicados de transacciones.

Importes negativos incoherentes (ej. depósitos con valor negativo).

Fechas inválidas (transacción futura o anterior a apertura de cuenta).

Monedas inválidas (distintas de {EUR, USD, GBP}).

IBANs inválidos (longitud incorrecta o vacíos).

Campos vacíos (concepto, beneficiario).

🧠 Metodología aplicada

Chain-of-Thought (CoT) vectorizado:
Se aplica razonamiento paso a paso, pero implementado en reglas vectorizadas y agrupadas para eficiencia.

Reglas agrupadas en diccionarios → fácil extender o modificar.

Detección de duplicados por ID_Transacción y por clave (Cuenta, Fecha, Importe, Beneficiario).

🏦 Sector aplicado

Banca y seguros

Consultoría financiera

Proyectos de cumplimiento regulatorio (KYC/AML, auditoría interna)

📂 Estructura del Ejercicio 6

Dataset de ejemplo
data_sample/transacciones_bancarias.xlsx
Columnas:
ID_Transaccion, Cuenta_IBAN, Fecha, Importe, Moneda, Beneficiario, Concepto

Script Python
scripts/auditoria_transacciones.py

Carga dataset

Aplica reglas de auditoría optimizadas

Exporta dataset con banderas + informe en Markdown

Salidas

results/06_auditoria_transacciones_result.md

results/06_transacciones_limpio.xlsx

📊 Errores introducidos en el dataset

Duplicados: mismos ID o misma clave (Cuenta, Fecha, Importe, Beneficiario).

Importes negativos incoherentes (ej. ingresos < 0).

Fechas futuras o anteriores a 2000.

Monedas inválidas (ej. “XXX”, vacíos).

IBANs mal formados (menos de 24 caracteres, nulos).

Beneficiario/Concepto vacíos.
