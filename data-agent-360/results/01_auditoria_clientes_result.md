# Ejercicio 1 – Auditoría de clientes (DSP)

**Dataset:** `data_sample\clientes.xlsx`

## Resultados del script
- Filas totales: 10
- Duplicados exactos: 0
- Duplicados de negocio: 3
- Nulos por columna: `{'id': 0, 'cliente': 0, 'ciudad': 0, 'email': 2, 'ventas': 0}`

### Duplicados por clave de negocio
|   id | cliente   | ciudad   | email        |   ventas | criterio_duplicado   |
|-----:|:----------|:---------|:-------------|---------:|:---------------------|
|    1 | Acme SA   | Madrid   | info@acme.es |     5000 | cliente+email        |
|    2 | Acme SA   | Madrid   | info@acme.es |     5000 | cliente+email        |
|    9 | Acme SA   | Madrid   | info@acme.es |     2850 | cliente+email        |

### Reglas sobre 'ventas'
**Ventas negativas:**

|   id | cliente   | ciudad   | email              |   ventas |
|-----:|:----------|:---------|:-------------------|---------:|
|    5 | Gamma SL  | Sevilla  | contacto@gamma.com |     -200 |

**Ventas a 0:**

|   id | cliente   | ciudad   |   email |   ventas |
|-----:|:----------|:---------|--------:|---------:|
|    8 | Nova SL   | A Coruña |     nan |        0 |

**Outliers IQR:**

|   id | cliente   | ciudad   | email            |   ventas |
|-----:|:----------|:---------|:-----------------|---------:|
|    4 | Delta SL  | Valencia | ventas@delta.com |    12000 |

## Recomendaciones
- Resolver **duplicados por clave de negocio** (unificar registros y consolidar ventas).
- Revisar **ventas negativas**: pueden ser devoluciones mal registradas; validar con finanzas.
- Analizar **ventas a 0**: decidir si son registros de prueba o incompletos; limpiar o documentar.
- Investigar **valores atípicos** (IQR): confirmar si son casos reales o errores de carga.

## Validación
- Nivel de confianza: Alta (Python + pandas)
- Limitaciones: dataset de ejemplo; validar con datos reales
