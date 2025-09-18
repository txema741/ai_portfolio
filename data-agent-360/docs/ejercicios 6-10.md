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

--.
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

# 📘 Ejercicio 8 – Auditoría de Pólizas y Siniestros de Seguros

**Metodología aplicada:** Self-Consistency + CoT vectorizado  
**Sector aplicado:** Seguros, consultoría actuarial y gestión de riesgos  

---

## 🎯 Contexto y objetivo
Las compañías de **seguros** gestionan miles de pólizas y siniestros cada año.  
La **calidad de los datos** es fundamental para:  
- Evitar fraudes o duplicidades.  
- Asegurar la coherencia en la gestión de pólizas.  
- Cumplir con requisitos legales y regulatorios.  

👉 En este ejercicio auditaremos un dataset ficticio de **pólizas y siniestros** para detectar:  
- Pólizas duplicadas o con inconsistencias.  
- Fechas incoherentes (siniestro antes de la póliza, fechas futuras extremas).  
- Montos de siniestros fuera de rango (ej. negativos o excesivos).  
- Tipos de póliza inválidos o vacíos.  
- Campos vacíos en asegurado, beneficiario o descripción del siniestro.  

---

## 📂 Archivos vinculados
- **Dataset de entrada:** `data_sample/polizas_siniestros.xlsx`  
- **Script:** `scripts/auditoria_seguro.py`  
- **Salidas generadas:**  
  - `results/08_auditoria_seguro_result.md`  
  - `results/08_polizas_siniestros_limpio.xlsx`  

---

## 🧪 Reglas de auditoría implementadas
- **Fechas**
  - `Fecha_Poliza` no nula.  
  - `Fecha_Siniestro` no nula.  
  - `Fecha_Siniestro` ≥ `Fecha_Poliza`.  
  - Fechas en rango válido [2000, 2050].  

- **Montos**
  - `Monto_Poliza` > 0.  
  - `Monto_Siniestro` ≥ 0 y ≤ `Monto_Poliza`.  

- **Tipos de póliza**
  - Deben pertenecer al catálogo definido: {Auto, Hogar, Vida, Salud, Viaje}.  

- **Completitud**
  - `Asegurado` no vacío.  
  - `Beneficiario` no vacío.  
  - `Descripción_Siniestro` no vacía.  

- **Duplicados**
  - Por **ID_Poliza**.  
  - Por clave funcional `(Asegurado, Tipo_Poliza, Fecha_Poliza)`.  

---

## 🖥️ Ejecución del script
Desde la raíz del proyecto:  

python scripts/auditoria_seguro.py

✅ Salidas esperadas

Informe generado: results/08_auditoria_seguro_result.md

Dataset marcado/limpio: results/08_polizas_siniestros_limpio.xlsx

# 📘 Ejercicio 9 – Auditoría de Consumos Energéticos y Facturación Eléctrica

**Metodología aplicada:** Self-Consistency + CoT vectorizado  
**Sector aplicado:** Energía (utilities), facturación y eficiencia energética

---

## 🎯 Contexto y objetivo
Las comercializadoras y auditoras energéticas gestionan miles de puntos de suministro (CUPS) con facturas mensuales.  
La **calidad del dato** es clave para:
- Evitar errores de facturación y reclamaciones.
- Detectar consumos anómalos (fraude, averías, lecturas mal registradas).
- Cumplir auditorías y reporting regulatorio.

👉 En este ejercicio auditaremos un dataset ficticio de **consumos y facturas eléctricas** para detectar:
- Duplicados de facturas.
- Fechas y periodos incoherentes.
- **CUPS** mal formados.
- **CP–Provincia** incoherentes.
- **Tarifas** inválidas.
- **Consumos/Importes** imposibles o desproporcionados.
- **kW contratada** inválida.
- Campos vacíos críticos (Cliente, Dirección).

---

## 📂 Archivos vinculados
- **Dataset de entrada:** `data_sample/consumos_energia.xlsx`  
- **Script:** `scripts/auditoria_energia.py`  
- **Salidas generadas:**  
  - `results/09_auditoria_energia_result.md`  
  - `results/09_consumos_energia_limpio.xlsx`

---

## 🧪 Reglas de auditoría implementadas
- **Fechas & Periodos**
  - `Fecha_Factura` no nula y en rango [2000, 2050].
  - `Periodo` mensual válido en formato `YYYY-MM` y coherente con `Fecha_Factura`.
  - No se permiten dos facturas **(ID_Factura)** iguales ni **(ID_Contrato, Periodo)** repetidos.

- **Identificadores energéticos**
  - `CUPS` no vacío y con patrón **ES** + 18–20 caracteres alfanuméricos (validación de forma, sin checksum).
  - `Tarifa` ∈ {2.0TD, 3.0TD, 3.0A, 6.1TD} (catálogo demo; ampliable).

- **Coherencia geográfica**
  - `CP–Provincia` coherente según mapa (demo incluido en script para principales provincias).
  - `Dirección` y `Cliente` no vacíos.

- **Magnitudes técnicas y económicas**
  - `kWh` > 0 y ≤ 20.000 por mes (umbral configurable).
  - `kW_Contratada` > 0 y ≤ 100 (umbral configurable).
  - `Importe_Factura` > 0.
  - **Regla de plausibilidad económica**: `Importe_Factura` ≈ `kWh * precio_estimado` (precio base por defecto: 0,20 €/kWh).  
    - Se marca **sospechoso** si sale del rango [0,6 × kWh, 0,6; 0,35 × kWh, 0,35] (ejemplo: [0,12; 0,35] €/kWh).  
    - Considera peajes/impuestos de manera laxa (check de plausibilidad, no exacto).

- **Outliers técnicos**
  - Detección de outliers por percentiles (p99) para `kWh` y `Importe_Factura` (marcados como **pico_anómalo**).

> Todas las reglas están vectorizadas; las “rutas” (fechas, CUPS, CP–Provincia, tarifas, consumos, importes) se combinan para un **`flags_total`** por registro y la etiqueta **`registro_valido`**.

---

📘 Ejercicio 10 – Auditoría de Inventarios y Cadenas de Suministro
🎯 Contexto y objetivo

Las empresas industriales y de retail gestionan inventarios complejos: materias primas, productos en proceso y artículos terminados en múltiples almacenes.
Los errores en estos datos generan roturas de stock, sobrecostes logísticos y pérdidas financieras.

👉 El objetivo de este ejercicio es auditar un dataset ficticio de inventarios, detectando:

Duplicados por ID_Producto/Almacén.

Cantidades negativas o incoherentes.

Fechas de entrada/salida imposibles (ej. salida antes de la entrada).

Códigos de producto inválidos.

Precios unitarios anómalos.

Almacenes no registrados.

🧠 Metodología aplicada

ReAct (Reason + Act)

El sistema combina razonamiento paso a paso con acciones concretas:

Detectar anomalías.

Razonar su impacto en la cadena de suministro.

Marcar banderas de error en el dataset.

🏭 Sector aplicado

Industria manufacturera

Retail

Consultoría logística y SCM

📂 Estructura del ejercicio

Dataset de entrada: data_sample/inventarios.xlsx

Script Python: scripts/auditoria_inventarios.py

Resultados esperados:

results/10_auditoria_inventarios_result.md

results/10_inventarios_limpio.xlsx

📑 Reglas de auditoría

Duplicados: (ID_Producto, ID_Almacén, Fecha_Entrada)

Fechas: Fecha_Salida ≥ Fecha_Entrada, ambas en rango [2000, 2050]

Cantidades: >0 y ≤ 100.000 unidades

Precios unitarios: >0 y ≤ 10.000 €/unidad

Códigos de producto: Formato PRD-XXXXX (5 dígitos)

Almacén: debe existir en catálogo de almacenes válidos

