# Script: auditoria_transacciones.py

## 📘 Descripción
Ejercicio 6 – **Auditoría de Transacciones Bancarias**.  
Audita un dataset de transacciones financieras para detectar **duplicados**, **fechas incoherentes**, **IBAN inválidos**, **monedas no admitidas**, **importes incoherentes** y **campos vacíos**.  

## 📂 Archivos vinculados
- **Entrada:** `data_sample/transacciones_bancarias.xlsx`
- **Script:** `scripts/auditoria_transacciones.py`
- **Salidas:**
  - `results/06_auditoria_transacciones_result.md`
  - `results/06_transacciones_limpio.xlsx`

## ▶️ Ejecución
Desde la raíz del proyecto:
```bash
python scripts/auditoria_transacciones.py

Reglas de auditoría

Fechas válidas entre 2000 y hoy.

Moneda ∈ {EUR, USD, GBP}.

IBAN válido (España, longitud 24, prefijo “ES”).

Concepto y beneficiario no vacíos.

Importes coherentes (no negativos para ingresos).

Duplicados por ID y por clave (Cuenta, Fecha, Importe, Beneficiario).

✅ Salidas esperadas
[OK] Informe generado: results/06_auditoria_transacciones_result.md
[OK] Dataset marcado/limpio: results/06_transacciones_limpio.xlsx
