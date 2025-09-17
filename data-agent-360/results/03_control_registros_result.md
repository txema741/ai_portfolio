# Ejercicio 3 – Control de registros educativos
**Metodología aplicada:** Draft-then-Revise (DtR) – *Borrador y Revisión*  
**Sector aplicado:** Educación, gestión académica y control de calidad de datos.  

---

## 🎯 Objetivo
Auditar un conjunto de **registros académicos** para detectar y corregir inconsistencias.  
La metodología *Draft-then-Revise* permite:  
1. Realizar un **primer borrador de revisión rápida**.  
2. Ejecutar una **segunda pasada de revisión más precisa**, aplicando validaciones adicionales.  

---

## 📂 Dataset utilizado
Archivo: `data_sample/registros_educativos.xlsx`  

Columnas incluidas:  
- `ID_Estudiante`  
- `Nombre`  
- `Asignatura`  
- `Fecha_Matricula`  
- `Nota_Final`  

Errores intencionales introducidos en el dataset:  
- **Duplicados** en IDs y nombres.  
- **Fechas inválidas** de matrícula (ej. fuera del rango académico).  
- **Notas fuera de rango** (valores < 0 o > 10).  
- **Campos vacíos** en asignaturas y calificaciones.  

---

## ⚙️ Proceso de auditoría
### 🔹 Fase 1 – *Draft* (borrador inicial)
- Detección de **duplicados en ID_Estudiante**.  
- Identificación de **valores nulos en Nombre y Nota_Final**.  
- Localización de **notas fuera de rango** (<0 o >10).  

📊 Resultados de la fase Draft:  
- 12 registros duplicados.  
- 5 valores nulos.  
- 3 notas fuera de rango.  

---

### 🔹 Fase 2 – *Revise* (revisión y mejora)
- Validación de coherencia en **Fecha_Matricula** (ej. dentro del curso 2023–2024).  
- **Normalización de nombres** (ej. eliminación de espacios en blanco, formato “Nombre Apellido”).  
- Limpieza definitiva de duplicados mediante reglas de negocio.  
- Corrección de asignaturas vacías con valores por defecto (“Sin asignar”).  

📊 Resultados de la fase Revise:  
- Fechas inválidas detectadas: 7.  
- Nombres normalizados: 15.  
- Registros finales corregidos: 150 (sobre un total inicial de 177).  

---

## 📊 Informe de salida
El script `scripts/control_registros.py` generó este informe automáticamente en Markdown, mostrando:  
- **Errores encontrados por categoría.**  
- **Correcciones aplicadas.**  
- **Dataset final limpio y normalizado.**  

Ejemplo de tabla de errores detectados (fase Draft):  

| ID_Estudiante | Nombre       | Asignatura  | Fecha_Matricula | Nota_Final | Error Detectado        |
|---------------|--------------|-------------|-----------------|------------|------------------------|
| 1023          | Juan Pérez   | Matemáticas | 2025-09-15      | 12         | Nota fuera de rango    |
| 1044          | *NULL*       | Historia    | 2025-09-10      | 8          | Nombre vacío           |
| 1088          | Ana López    | Lengua      | 2018-05-20      | 7          | Fecha fuera de rango   |
| 1023          | Juan Pérez   | Matemáticas | 2025-09-15      | 12         | Registro duplicado     |

---

## ✅ Conclusiones
- La técnica *Draft-then-Revise* demuestra que **dos pasadas sucesivas mejoran sustancialmente la calidad de los datos**.  
- En el contexto educativo, esta metodología permite:  
  - Prevenir errores de calificaciones y matrículas.  
  - Garantizar la fiabilidad de los registros oficiales.  
  - Asegurar la trazabilidad de las correcciones aplicadas.  

📌 Este enfoque es aplicable en **universidades, institutos y centros de formación**, donde la **coherencia de datos académicos** es crítica para procesos de acreditación, informes oficiales y toma de decisiones.  
