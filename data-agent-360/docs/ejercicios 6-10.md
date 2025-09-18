# 📘 Ejercicio 6 – Auditoría de Transacciones Bancarias

**Metodología aplicada:** Chain-of-Thought (CoT) vectorizado + reglas agrupadas  
**Sector aplicado:** Banca, seguros y consultoría financiera  

---

## 🎯 Contexto y objetivo
Los bancos y entidades financieras procesan millones de transacciones al día. La calidad de los datos es crítica para detectar fraudes, evitar duplicidades contables y cumplir con normativas regulatorias (KYC, AML).  

👉 En este ejercicio auditamos un dataset ficticio de transacciones para identificar:  
- **Duplicados** de transacciones  
- **Importes negativos incoherentes**  
- **Fechas inválidas** (futuras o anteriores a 2000)  
- **Monedas inválidas** (distintas de EUR, USD, GBP)  
- **IBANs inválidos** (longitud incorrecta o vacíos)  
- **Campos vacíos** (beneficiario, concepto)  

---

## 🧠 Metodología
- **CoT vectorizado**: razonamiento paso a paso implementado con reglas vectorizadas para eficiencia.  
- **Reglas agrupadas en diccionario**: fácil extender o modificar validaciones.  
- **Duplicados**: detectados tanto por `ID_Transaccion` como por clave `(Cuenta, Fecha, Importe, Beneficiario)`.  

---

## 📂 Estructura del ejercicio
- **Dataset de entrada:**  
  `data_sample/transacciones_bancarias.xlsx`  

- **Script de auditoría:**  
  `scripts/auditoria_transacciones.py`  

- **Resultados generados:**  
  - `results/06_auditoria_transacciones_result.md`  
  - `results/06_transacciones_limpio.xlsx`  

---

## 📊 Errores introducidos en el dataset
- Duplicados por **ID** o por clave `(Cuenta, Fecha, Importe, Beneficiario)`  
- **Importes negativos incoherentes** (ej. ingresos < 0)  
- **Fechas futuras** o anteriores a 2000  
- **Monedas inválidas** (ej. “XXX”, vacías)  
- **IBANs mal formados** (longitud incorrecta, nulos)  
- **Beneficiario/Concepto vacíos**  

---

## ▶️ Ejecución
Desde la raíz del proyecto:  
```bash
python scripts/auditoria_transacciones.py

Salidas esperadas
[OK] Informe generado: results/06_auditoria_transacciones_result.md
[OK] Dataset marcado/limpio: results/06_transacciones_limpio.xlsx

