# 📂 Carpeta de Datasets – Data Agent 360

En esta carpeta se almacenan los **datasets sintéticos** utilizados en los diferentes ejercicios del proyecto.  
Todos los ficheros están generados con errores intencionales para poder probar los procesos de auditoría.  

---

## ✅ Ejercicio 1 – Auditoría de Clientes
- **Archivo:** `clientes.xlsx`  
- **Contenido:**  
  Base de datos de clientes de PYMEs con errores comunes.  
- **Errores introducidos:**  
  - Duplicados de clientes  
  - Ventas negativas  
  - Ventas en cero  
  - Valores nulos  
  - Outliers en importes de venta  

---

## ✅ Ejercicio 2 – Riesgo País (España)
- **Archivo:** `riesgo_pais_spain_real.xlsx`  
- **Contenido:**  
  Indicadores económicos de España (Eurostat, OCDE, IMF).  
- **Errores introducidos:**  
  - Registros con deuda pública, déficit, inflación o PIB fuera de rango  
  - Clasificación de riesgo: Bajo / Medio / Alto  

---

## ✅ Ejercicio 3 – Control de Registros Educativos
- **Archivo:** `registros_educativos.xlsx`  
- **Contenido:**  
  Base de datos de estudiantes, asignaturas y calificaciones.  
- **Errores introducidos:**  
  - Estudiantes duplicados  
  - Notas fuera de rango (>10)  
  - Fechas inválidas de matrícula  
  - Campos vacíos en asignaturas o calificaciones  

---

## ✅ Ejercicio 4 – Auditoría de Padrones Municipales
- **Archivo:** `municipal_padron.xlsx`  
- **Contenido:**  
  Registro ficticio de habitantes en un municipio.  
- **Errores introducidos:**  
  - DNIs inválidos o vacíos  
  - CP incoherente con provincia  
  - Municipios fuera de la provincia  
  - Fechas imposibles (nacimientos en 2050, edades >120 años)  
  - Fechas de baja anteriores a la de alta  
  - Sexo inválido (ejemplo: “X”)  

---

## ✅ Ejercicio 5 – Auditoría de Historias Clínicas (EHR)
- **Archivo:** `historias_clinicas.xlsx`  
- **Contenido:**  
  Registros médicos de pacientes.  
- **Errores introducidos:**  
  - Pacientes duplicados  
  - Altas anteriores al ingreso  
  - Diagnósticos vacíos  
  - Códigos ICD-10 inválidos  
  - Edades imposibles o fechas de nacimiento erróneas  

---

## ✅ Ejercicio 6 – Auditoría de Transacciones Bancarias
- **Archivo:** `transacciones_bancarias.xlsx`  
- **Contenido:**  
  Dataset de operaciones financieras (ingresos, transferencias, pagos).  
- **Errores introducidos:**  
  - Duplicados por ID y clave  
  - Fechas futuras y anteriores a 2000  
  - Importes incoherentes (ingresos negativos)  
  - Monedas inválidas (XXX, vacías)  
  - IBAN mal formados  
  - Beneficiario o Concepto vacíos  

---

## ✅ Ejercicio 7 – Auditoría de Envíos y Trazabilidad Logística
- **Archivo:** `envios_logistica.xlsx`  
- **Contenido:**  
  Envíos de paquetes con datos de trazabilidad.  
- **Errores introducidos:**  
  - Duplicados por ID y por clave `(Fecha_Envio, Destinatario, Dirección, CP)`  
  - Fechas incoherentes (entrega antes del envío, fechas futuras en 2050)  
  - CP–Ciudad no coincidentes  
  - Transportistas inválidos (ej. “XXX Transportes”)  
  - Pesos ≤ 0 o > 50.000 kg  
  - Volúmenes ≤ 0 o > 500 m³  
  - Destinatario/Dirección vacíos  

---

## ✅ Ejercicio 8 – Auditoría de Pólizas y Siniestros de Seguros
- **Archivo:** `polizas_siniestros.xlsx`  
- **Contenido:**  
  Dataset ficticio de pólizas y siniestros en una aseguradora.  
- **Errores introducidos:**  
  - Pólizas duplicadas por ID y clave `(Asegurado, Tipo_Poliza, Fecha_Poliza)`  
  - Fechas incoherentes (siniestro antes de la póliza, fechas futuras en 2050)  
  - Montos inválidos (negativos o mayores que la póliza)  
  - Tipos de póliza inválidos (ejemplo: “Test”, “XXX”)  
  - Beneficiarios o descripciones vacías
 
  - ---

## ✅ Ejercicio 9 – Auditoría de Consumos Energéticos
- **Archivo:** `consumos_energia.xlsx`  
- **Contenido:**  
  Dataset de consumos eléctricos mensuales de clientes.  
- **Errores introducidos:**  
  - Duplicados por `(ID_Cliente, Periodo)`  
  - Periodos inválidos (`YYYY-MM` mal formateado o fuera de rango)  
  - Consumos negativos o superiores a 1.000.000 kWh  
  - Costes incoherentes (importe ≤ 0 o excesivo)  
  - Tarifas inválidas (ejemplo: “XXX”, vacías)  
  - Clientes vacíos o inexistentes  

---

## ✅ Ejercicio 10 – Auditoría de Inventarios y Cadenas de Suministro
- **Archivo:** `inventarios.xlsx`  
- **Contenido:**  
  Registros de entradas y salidas de productos en distintos almacenes.  
- **Errores introducidos:**  
  - Duplicados por `(ID_Producto, ID_Almacén, Fecha_Entrada)`  
  - Fechas incoherentes (salida < entrada) o fuera de rango (antes del 2000 o en 2055)  
  - Cantidades negativas o mayores a 100.000 unidades  
  - Precios unitarios negativos o > 10.000 €/unidad  
  - Códigos de producto inválidos (ejemplo: “12345”, “PRDX-12345”)  
  - Almacenes no registrados (ejemplo: “ALM-99X”, “ALMX-01”)  

