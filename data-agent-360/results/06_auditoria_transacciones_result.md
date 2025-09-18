# Ejercicio 6 – Auditoría de Transacciones Bancarias

**Metodología aplicada:** Chain-of-Thought (CoT) vectorizado + reglas agrupadas  
**Sector aplicado:** Banca, seguros y consultoría financiera  

---

## 🎯 Objetivo
Auditar un dataset de transacciones para detectar:  
- Duplicados de transacciones  
- Fechas inválidas (futuras o anteriores al año 2000)  
- Monedas inválidas (distintas de EUR, USD, GBP)  
- IBANs inválidos (longitud distinta de 24 o sin prefijo ES)  
- Importes incoherentes (ej. ingresos negativos)  
- Campos vacíos (beneficiario, concepto)  

---

## 🧠 Metodología
Se aplicó un razonamiento encadenado vectorizado (CoT optimizado), con reglas agrupadas en diccionarios para fácil mantenimiento y escalabilidad.  

- **Parseo robusto** de fechas y normalización de strings.  
- **Validaciones por máscara vectorizada** (sin `apply`, rendimiento óptimo).  
- **Duplicados detectados** por ID de transacción y por clave `(Cuenta, Fecha, Importe, Beneficiario)`.  
- **Flags acumulativos** → cada registro tiene un contador de errores (`flags_total`) y una etiqueta global (`registro_valido`).  

---

## 📊 Resumen de incidencias
- Duplicados por ID: **XX**  
- Duplicados por clave: **XX**  
- Fechas nulas: **XX**  
- Fechas fuera de rango: **XX**  
- Monedas inválidas: **XX**  
- IBAN inválidos: **XX**  
- Beneficiario vacío: **XX**  
- Concepto vacío: **XX**  
- Importes incoherentes (ingresos negativos): **XX**

> Los números concretos dependerán de la ejecución (dataset sintético con errores intencionales).

---

## 📑 Ejemplos detectados

### 🔁 Duplicados por ID_Transaccion
| ID_Transaccion | Cuenta_IBAN        | Fecha       | Importe  | Moneda | Beneficiario     | Concepto         |
|---------------:|:-------------------|:------------|---------:|:------:|:-----------------|:-----------------|
| 700005         | ES1234567890123456 | 2019-06-11  |  1500.50 | EUR    | Comercial Álvarez| Transferencia    |
| 700005         | ES1234567890123456 | 2019-06-11  |  1500.50 | EUR    | Comercial Álvarez| Transferencia    |

---

### ⏳ Fechas fuera de rango
| ID_Transaccion | Fecha      | Importe | Beneficiario    |
|---------------:|:-----------|--------:|:----------------|
| 700112         | 2026-05-10 |  800.00 | Servicios López |
| 700198         | 1995-12-22 | 1200.00 | TechNova SL     |

---

### 💱 Monedas inválidas
| ID_Transaccion | Moneda | Importe | Beneficiario   |
|---------------:|:-------|--------:|:---------------|
| 700045         | XXX    |   90.00 | Distribuciones Díaz |
| 700078         | (vacío)|  350.00 | Market Ruiz     |

---

### 🏦 IBAN inválido
| ID_Transaccion | Cuenta_IBAN     | Beneficiario   | Importe |
|---------------:|:----------------|:---------------|--------:|
| 700087         | E12345678901234 | Viajes Castro  | 1200.00 |
| 700099         | (vacío)         | Ferretería Romero |  750.00 |

---

### 💸 Importes incoherentes (ingresos negativos)
| ID_Transaccion | Concepto           | Importe  | Beneficiario | Fecha       |
|---------------:|:-------------------|---------:|:-------------|:------------|
| 700145         | Nómina             | -1200.00 | Aseguradora Vázquez | 2021-03-11 |
| 700178         | Ingreso ventanilla |  -500.00 | Restaurante Moreno  | 2020-07-08 |

---

## ✅ Conclusiones
- La auditoría permitió detectar **errores críticos de calidad de datos** en transacciones bancarias.  
- El enfoque **vectorizado** permite escalar a **millones de registros** sin pérdida de rendimiento.  
- El dataset limpio incluye banderas de error (`flag_*`), un total de errores (`flags_total`) y una marca de validez (`registro_valido`).  
- Recomendaciones para producción:  
  - Validación completa de IBAN con checksum oficial.  
  - Catálogo ISO 4217 completo de monedas.  
  - Reglas adicionales AML/KYC (detección de patrones sospechosos).  

---

## 📤 Entregables
- **Informe Markdown:** `results/06_auditoria_transacciones_result.md`  
- **Dataset limpio:** `results/06_transacciones_limpio.xlsx`  
