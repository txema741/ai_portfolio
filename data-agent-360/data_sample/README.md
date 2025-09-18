# 📂 Carpeta de datasets – Data Agent 360

Datasets de entrada para los ejercicios.  
Cada archivo es un **Excel (.xlsx)** con errores intencionales para probar la auditoría.

---

## Ejercicio 1 – Auditoría de Clientes (DSP)
- `clientes.xlsx` → Duplicados, nulos, ventas negativas/cero y outliers.  

## Ejercicio 2 – Riesgo País (CFS)
- `riesgo_pais_spain_real.xlsx` → Indicadores macroeconómicos de España con umbrales de riesgo.  

## Ejercicio 3 – Registros Educativos (DtR)
- `registros_educativos.xlsx` → Notas fuera de rango, fechas inválidas, duplicados y vacíos.  

## Ejercicio 4 – Padrones Municipales (Self-Consistency)
- `municipal_padron.xlsx` → DNIs inválidos, CP incoherentes, municipios fuera de provincia, fechas imposibles, duplicados.  

## Ejercicio 5 – Historias Clínicas (EHR, CoT)
- `historias_clinicas.xlsx` → Registros clínicos con duplicados, edades imposibles, fechas incoherentes, diagnósticos vacíos y códigos ICD-10 inválidos.  

## Ejercicio 6 – Transacciones Bancarias (CoT vectorizado)
- `transacciones_bancarias.xlsx`  
- Columnas: `ID_Transaccion, Cuenta_IBAN, Fecha, Importe, Moneda, Beneficiario, Concepto`  
- Errores introducidos:  
  - Duplicados por ID y por clave `(Cuenta, Fecha, Importe, Beneficiario)`  
  - Fechas futuras o <2000  
  - Importes incoherentes (ej. ingresos negativos)  
  - Monedas inválidas (XXX, vacías)  
  - IBAN mal formado o vacío  
  - Beneficiario/Concepto vacíos
