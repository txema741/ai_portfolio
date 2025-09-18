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
Informe generado: results/06_auditoria_transacciones_result.md
Dataset marcado/limpio: results/06_transacciones_limpio.xlsx

# 📘 Ejercicio 7 – Auditoría de Envíos y Trazabilidad Logística

**Metodología aplicada:** Self-Consistency + Chain-of-Thought híbrido  
**Sector aplicado:** Logística, transporte y supply chain  

---

## 🎯 Contexto y objetivo
Las empresas de **logística y transporte** gestionan miles de envíos diarios. La calidad de los datos es crítica para:  
- Asegurar entregas puntuales.  
- Reducir incidencias (pérdidas, retrasos, entregas fallidas).  
- Cumplir con la trazabilidad exigida por clientes y reguladores.  

👉 En este ejercicio auditaremos un dataset ficticio de **envíos** para detectar:  
- **Duplicados** de envíos.  
- **Fechas incoherentes** (entrega antes del envío).  
- **CP y ciudades no coincidentes**.  
- **Transportistas inválidos** (fuera del catálogo permitido).  
- **Pesos y volúmenes imposibles** (negativos o excesivos).  
- **Campos vacíos** en dirección de entrega o destinatario.  

---

## 🧠 Metodología
- **Self-Consistency + Chain-of-Thought híbrido**:  
  Varias rutas de validación (fechas, CP–ciudad, pesos, duplicados) consolidadas por votación mayoritaria para reducir falsos positivos.  
- **Vectorización** de reglas para eficiencia.  
- **Claves de duplicado**:  
  - `(ID_Envio)`  
  - `(Fecha_Envio, Destinatario, Dirección, CP)`  

---

## 🚚 Sector aplicado
- Logística de última milla  
- Transporte y distribución nacional/internacional  
- Consultoría de supply chain y optimización logística  

---

## 📂 Estructura del ejercicio

- **Dataset de ejemplo**  
  `data_sample/envios_logistica.xlsx`  
  Columnas esperadas:  
  - `ID_Envio`  
  - `Fecha_Envio`  
  - `Fecha_Entrega`  
  - `CP`  
  - `Ciudad`  
  - `Transportista`  
  - `Peso_kg`  
  - `Volumen_m3`  
  - `Destinatario`  
  - `Dirección`  

- **Script Python**  
  `scripts/auditoria_envios.py`  
  - Carga el dataset.  
  - Aplica reglas de auditoría optimizadas.  
  - Genera informe en Markdown y dataset limpio con banderas de error.  

- **Salidas esperadas**  
  - `results/07_auditoria_envios_result.md`  
  - `results/07_envios_limpio.xlsx`  

---

## 📊 Errores introducidos en el dataset
- Duplicados por **ID_Envio** y por clave `(Fecha_Envio, Destinatario, Dirección, CP)`.  
- **Fechas incoherentes**: entrega anterior al envío, o fechas en el futuro extremo (ej. año 2050).  
- **CP–Ciudad no coincidentes** (ejemplo: CP 28001 con ciudad “Barcelona”).  
- **Transportistas inválidos** (ejemplo: “XXX Transportes”).  
- **Pesos o volúmenes imposibles** (≤ 0, o > 50.000 kg / 500 m³).  
- **Campos vacíos** en `Destinatario` o `Dirección`.  
