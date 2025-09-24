# Metodología DSP (Directional Stimulus Prompting – Estímulo Direccional de Prompting)

La metodología **DSP (Directional Stimulus Prompting – Estímulo Direccional de Prompting)** se basa en la idea de guiar a un modelo o sistema de auditoría con **estímulos de referencia**, definidos como ejemplos positivos y negativos.  
Esto permite traducir conceptos abstractos de calidad de datos en **reglas concretas y verificables** que un auditor (humano o automático) puede aplicar.

---

## 1️⃣ Estímulos positivos y negativos
Los estímulos se dividen en dos grupos:

- **Ejemplos positivos** — casos válidos que cumplen con el formato correcto.  
  - Email válido: `usuario@dominio.com`  
  - Teléfono válido: `+34 600112233`  
  - País válido: `ES`, `MX`, `AR` (códigos ISO – *International Organization for Standardization – Organización Internacional de Normalización*).  

- **Ejemplos negativos** — casos incorrectos que deben ser detectados como incidencias.  
  - Email inválido: `usuario@@dominio.com`, `usuario@dominio` (sin TLD – *Top-Level Domain – Dominio de Nivel Superior*).  
  - Teléfono inválido: `12345` (menos de 9 dígitos).  
  - País inválido: `ZZ` (no existe en la lista ISO).  
  - Fecha inválida: `2024-02-30` (día inexistente) o `2025-12-01` (fecha futura).  

---

## 2️⃣ Traducción a reglas de negocio
A partir de los estímulos, se crean **reglas programáticas** que permiten validar automáticamente el dataset:

- **Regex** para validar email.  
- **Longitud mínima** para teléfonos.  
- **Lista ISO** de países permitidos.  
- **Formato ISO `YYYY-MM-DD`** y chequeo de que la fecha no sea futura.  
- **Control de duplicados** en `email` y `telefono`.  

---

## 3️⃣ Métricas y KPIs (Key Performance Indicators – Indicadores Clave de Desempeño)
El sistema de auditoría genera métricas que permiten evaluar la **calidad del dataset**:

- **% de registros válidos** sobre el total.  
- **% de incidencias por tipo** (email, teléfono, país, fecha, duplicados).  
- **Ratio de duplicados** detectados en campos críticos.  

Estas métricas se guardan en el informe `results/reporte_clientes.md`.

---

## 4️⃣ Extensiones posibles
La metodología DSP puede complementarse con:

- **Integración de APIs abiertas** (ejemplo: validación de países vía ISO o listas de referencia).  
- **Normalización de datos** mediante procesos ETL (*Extract, Transform, Load – Extraer, Transformar y Cargar*).  
- **Uso de modelos de IA** para detectar inconsistencias semánticas más avanzadas (ejemplo: detectar que un cliente con país `ES` tiene un teléfono con prefijo de Argentina).  

---

## 5️⃣ Ventajas y limitaciones
### ✅ Ventajas
- Claridad: las reglas son transparentes y fáciles de replicar.  
- Reproducibilidad: cualquier auditor puede obtener los mismos resultados.  
- Escalabilidad: se pueden añadir más estímulos sin rediseñar todo el sistema.  

### ⚠️ Limitaciones
- Rigidez: solo detecta problemas que han sido definidos previamente.  
- No captura errores semánticos complejos sin apoyo de IA.  
- Requiere mantener las listas de referencia (ej. países ISO).  

---

## 6️⃣ Conexión con auditoría de clientes
Aplicar **DSP (Directional Stimulus Prompting – Estímulo Direccional de Prompting)** en la auditoría de clientes permite:

- Traducir la experiencia de un consultor de datos en **reglas prácticas**.  
- Mejorar la **calidad de bases de clientes** para PYMEs (*Small and Medium Enterprises – Pequeñas y Medianas Empresas*).  
- Facilitar el cumplimiento de normativas como **GDPR (General Data Protection Regulation – Reglamento General de Protección de Datos)** en el manejo de **PII (Personally Identifiable Information – Información de Identificación Personal)**.  

---

