# Reporte de Auditoría de Clientes

- Filas: **15**
- Columnas: **7**
- Incidencias detectadas: **10**

## Incidencias por tipo (top 10 por tipo)
### columna_faltante (2)
- Fila None, **cliente_id** → Falta columna obligatoria 'cliente_id'.
- Fila None, **ingreso_anual** → Falta columna obligatoria 'ingreso_anual'.

### valor_nulo_vacio (2)
- Fila 8, **nombre** → Valor nulo o vacío en columna obligatoria.
- Fila 10, **telefono** → Valor nulo o vacío en columna obligatoria.

### email_invalido (3)
- Fila 1, **email** → Email no válido: luis.gomez@ejemplo
- Fila 9, **email** → Email no válido: camila.soto@@example.com
- Fila 13, **email** → Email no válido: paula.rey@example

### telefono_invalido (2)
- Fila 10, **telefono** → Teléfono no válido (patrón laxo v1): nan
- Fila 11, **telefono** → Teléfono no válido (patrón laxo v1): 12345

### formato_invalido (1)
- Fila 1, **fecha_alta** → Esperado YYYY-MM-DD, recibido: 2024-02-30

