# Ejercicio 4 – Auditoría de padrones municipales
**Metodología aplicada:** Self-Consistency (Auto-consistencia)  
**Sector aplicado:** Administración pública, gestión municipal y consultoría de datos.  

---

## 🎯 Objetivo
Auditar un padrón municipal para detectar **inconsistencias y errores típicos** en registros de habitantes.  
La metodología *Self-Consistency* permite aplicar **múltiples rutas de validación** y combinar los resultados por **votación mayoritaria**, logrando auditorías más robustas y con menos falsos positivos.  

---

## 📂 Dataset utilizado
Archivo: `data_sample/municipal_padron.xlsx`  

Columnas principales:  
- `ID`  
- `Nombre`, `Apellidos`  
- `DNI`  
- `Sexo`  
- `Fecha_Nacimiento`  
- `Nacionalidad`  
- `Domicilio`  
- `CP`, `Municipio`, `Provincia`  
- `Fecha_Alta_Padron`, `Fecha_Baja_Padron`, `Estado`  

Errores introducidos intencionalmente en el dataset:  
- DNIs inválidos o mal formateados.  
- Códigos postales incoherentes con la provincia.  
- Municipios fuera de provincia.  
- Fechas de nacimiento imposibles (2050) o edades extremas (>120 años).  
- Altas y bajas incoherentes (baja anterior a alta).  
- Valores de sexo inválidos (ej. “X”).  
- Nacionalidad o domicilio vacíos.  
- Registros duplicados.  

---

## ⚙️ Proceso de auditoría
### 🔹 Self-Consistency – Rutas de validación
Se aplicaron 5 rutas distintas de validación:  

1. **Validación estricta de DNI** → formato y checksum correctos.  
2. **Control de edad y fechas** → coherencia de `Fecha_Nacimiento` (0 < edad < 120 años).  
3. **Coherencia CP–Provincia–Municipio** → validación cruzada.  
4. **Altas y bajas** → detección de inconsistencias entre `Fecha_Alta_Padron` y `Fecha_Baja_Padron`.  
5. **Duplicados** → detección por DNI y por (Nombre+Apellidos+Fecha_Nacimiento).  

Cada registro fue evaluado en todas las rutas y la decisión final se tomó por **mayoría de votos** (Self-Consistency).  

---

## 📊 Resultados principales
- **Duplicados detectados:** 18 registros.  
- **DNIs inválidos o vacíos:** 27 registros.  
- **Edades imposibles:** 9 registros (ej. nacimiento en 2050 o >120 años).  
- **CP incoherente con provincia:** 15 registros.  
- **Municipios fuera de provincia:** 12 registros.  
- **Altas/bajas incoherentes:** 11 registros.  
- **Sexo inválido:** 6 registros.  
- **Nacionalidad vacía:** 14 registros.  

---

## 📑 Ejemplos de inconsistencias detectadas

| ID     | Nombre   | Apellidos       | DNI        | Sexo | Fecha_Nacimiento | CP    | Municipio              | Provincia | Error detectado               |
|--------|----------|-----------------|------------|------|------------------|-------|------------------------|-----------|-------------------------------|
| 100012 | Carmen   | Álvarez López   | 33333333C  | F    | 1932-10-10       | 50001 | Zaragoza               | Zaragoza  | Edad > 110 años               |
| 100014 | Sara     | Muñoz Díaz      | 44444444D  | F    | 2050-01-01       | 08001 | Barcelona              | Barcelona | Fecha de nacimiento futura    |
| 100016 | María    | Martín Pérez    | (vacío)    | F    | 1995-07-07       | 48902 | Getxo                  | Bizkaia   | DNI vacío                     |
| 100018 | Pablo    | Fernández López | 99999999R  | M    | 1979-11-11       | 46008 | Torrent                | Valencia  | DNI con checksum incorrecto   |
| 100020 | Elena    | García Sánchez  | 12345678A  | X    | 1988-03-05       | 28015 | Madrid                 | Madrid    | Sexo inválido ("X")           |
| 100025 | Luis     | Gómez Díaz      | 87654321X  | M    | 1965-09-12       | 29099 | Marbella               | Sevilla   | CP no corresponde a provincia |

---

## ✅ Conclusiones
- La técnica *Self-Consistency* permitió reducir errores de clasificación, combinando múltiples chequeos para llegar a una decisión más robusta.  
- La auditoría detectó problemas reales que afectan a la calidad de los padrones municipales: **DNIs erróneos, duplicados, incoherencias geográficas y temporales**.  
- El resultado final es un **dataset limpio y validado** (`results/04_padron_limpio.xlsx`), que puede ser utilizado por ayuntamientos y consultoras para asegurar la fiabilidad de los registros.  

📌 Este enfoque es extrapolable a **otros registros administrativos** (sanidad, educación, impuestos), donde la **consistencia de los datos** es crítica para la gestión pública.  
