# Ejercicio 3 – Auditoría de registros educativos (Draft-then-Revise)

**Dataset original:** `data_sample\alumnos.xlsx`

**Dataset corregido:** `data_sample\alumnos_corregido.xlsx`


## Diagnóstico inicial (Draft)
### nulos
|   id_alumno | nombre     | asignatura   |   nota | email                  |
|------------:|:-----------|:-------------|-------:|:-----------------------|
|           5 | Elena Díaz | Historia     |    5   | nan                    |
|          10 | Iván Ríos  | Lengua       |    3   | nan                    |
|          16 | Marta Sol  | Matemáticas  |    5.5 | nan                    |
|          19 | nan        | Historia     |    6   | sin.nombre@example.com |

### notas_fuera_rango
|   id_alumno | nombre      | asignatura   |   nota | email                   |
|------------:|:------------|:-------------|-------:|:------------------------|
|           2 | Luis Gómez  | Matemáticas  |     11 | luis.gomez@example.com  |
|           4 | Carlos Soto | Ciencias     |     -2 | carlos.soto@example.com |
|          17 | Javier Roa  | Inglés       |     12 | javier.roa@example.com  |
|          18 | Celia Luz   | Ciencias     |     -5 | celia.luz@example.com   |

### duplicados
- Sin incidencias detectadas.

## Revisión con correcciones propuestas (Revise)
|   id_alumno | nombre      | asignatura   |   nota | email                   |
|------------:|:------------|:-------------|-------:|:------------------------|
|           1 | Ana Pérez   | Matemáticas  |    8.5 | ana.perez@example.com   |
|           2 | Luis Gómez  | Matemáticas  |   10   | luis.gomez@example.com  |
|           3 | María Ruiz  | Lengua       |    7   | maria.ruiz@example.com  |
|           4 | Carlos Soto | Ciencias     |    0   | carlos.soto@example.com |
|           5 | Elena Díaz  | Historia     |    5   | N/D                     |
|           6 | Sergio León | Inglés       |    6.5 | sergio.leon@example.com |
|           7 | Lucía Gil   | Matemáticas  |    9   | lucia.gil@example.com   |
|           8 | Óscar Peña  | Ciencias     |    4   | oscar.pena@example.com  |
|           9 | Nuria Cano  | Historia     |    7.5 | nuria.cano@example.com  |
|          10 | Iván Ríos   | Lengua       |    3   | N/D                     |
|          11 | Rosa Vidal  | Inglés       |   10   | rosa.vidal@example.com  |
|          12 | Pablo Rey   | Matemáticas  |    0   | pablo.rey@example.com   |
|          13 | Sofía Lara  | Ciencias     |    6   | sofia.lara@example.com  |
|          14 | Andrés Paz  | Historia     |    8   | andres.paz@example.com  |
|          15 | Mario Núñez | Lengua       |    2   | mario.nunez@example.com |
|          16 | Marta Sol   | Matemáticas  |    5.5 | N/D                     |
|          17 | Javier Roa  | Inglés       |   10   | javier.roa@example.com  |
|          18 | Celia Luz   | Ciencias     |    0   | celia.luz@example.com   |
|          19 | N/D         | Historia     |    6   | sin.nombre@example.com  |
|          20 | Ana Pérez   | Matemáticas  |    8.5 | ana.perez@example.com   |

## Recomendaciones consultivas
- Completar correos electrónicos faltantes para garantizar comunicación.
- Validar criterios de evaluación para evitar notas fuera de rango.
- Analizar duplicados por (id_alumno, asignatura) y consolidar actas si procede.

## Validación
- Nivel de confianza: Alta (reglas deterministas y reproducibles).
- Limitaciones: el valor 'N/D' es temporal, requiere validación institucional.
