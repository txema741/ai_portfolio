# 📊 Almacenamiento, Visualización y Procesamiento de Datos

Portafolio profesional (consultoría + docencia). Este repositorio demuestra cómo transformar **datos → insights → decisiones** con **agentes de IA** (ChatGPT Plus/Gemini/Copilot), entregables ejecutivos y materiales de aula.

---

## Índice
1. [Resumen ejecutivo](#1-resumen-ejecutivo)
2. [Cómo usar este repositorio](#2-cómo-usar-este-repositorio)
3. [Teoría aplicada (consultoría + docencia)](#3-teoría-aplicada-consultoría--docencia)
   - [3.1 Fundamentos](#31-fundamentos)
   - [3.2 Almacenamiento](#32-almacenamiento)
   - [3.3 Procesamiento](#33-procesamiento)
   - [3.4 Visualización y storytelling](#34-visualización-y-storytelling)
   - [3.5 Agentes de análisis](#35-agentes-de-análisis)
   - [3.6 Ética, privacidad y cumplimiento](#36-ética-privacidad-y-cumplimiento)
4. [Pack de Prompts (10) con técnica](#4-pack-de-prompts-10-con-técnica)
5. [Ejercicios (20) — con técnicas del Prompting Guide](#5-ejercicios-20--con-técnicas-del-prompting-guide)
6. [Prácticas / Proyectos (8) — sectoriales](#6-prácticas--proyectos-8--sectoriales)
7. [Plantillas y recursos](#7-plantillas-y-recursos)
8. [Rúbrica de calidad y auditoría](#8-rúbrica-de-calidad-y-auditoría)
9. [Roadmap y backlog](#9-roadmap-y-backlog)
10. [Changelog](#10-changelog)

---

## 1. Resumen ejecutivo
- **Propósito:** acelerar análisis y reporting con IA, desde **datasets pequeños/medianos** y documentos de soporte.  
- **Valor inmediato:** KPIs claros, riesgos identificados, acciones priorizadas, con **trazabilidad** (citas).  
- **Ámbitos:** pymes, educación, AAPP/transparencia, operaciones/finanzas.  
- **Confianza:** **Alta** para metodologías y entregables; los datos de ejemplo deben ser ficticios/anonimizados.

## 2. Cómo usar este repositorio
1) Elige un **prompt** del apartado 4 o un **ejercicio** del apartado 5.  
2) Pega un **CSV/tabla abreviada** (o referencia a Drive en Gemini).  
3) Exporta el resultado y súbelo como evidencia a `projects/<proyecto>/samples/`.  

---

## 3. Teoría aplicada (consultoría + docencia)

### 3.1 Fundamentos
- **Qué es:** ciclo **datos → información → insight → decisión**. (*Confianza: Alta*)  
- **Por qué importa:** sin limpieza ni contexto, los KPIs engañan.  
- **Cómo aplicar:** define **pregunta de negocio**, **métrica objetivo** y **umbral de acción** antes de analizar.

### 3.2 Almacenamiento
- **Archivos locales:** CSV/Excel/JSON (rápido, barato).  
- **Nube ligera:** Drive/OneDrive para colaboración.  
- **Buenas prácticas:** esquema de nombres, control de versiones manual, **diccionario de datos**. (*Confianza: Alta*)

### 3.3 Procesamiento
- **Limpieza:** faltantes, duplicados, outliers, tipos.  
- **Normalización:** fechas, categorías, monedas.  
- **Enriquecimiento:** claves externas (ej. calendario, regiones).  
- **Trazabilidad:** deja constancia de cada cambio. (*Confianza: Alta*)

### 3.4 Visualización y storytelling
- **Gráficos adecuados:** línea (evolución), barras (comparación), heatmap (matrices), *small multiples* (comparables).  
- **Storytelling ejecutivo:** 3 hallazgos → 3 acciones → 1 decisión. (*Confianza: Alta*)

### 3.5 Agentes de análisis
- **Patrones:**  
  - **Analista** (resume, compara, explica KPIs).  
  - **Auditor** (detecta errores con evidencia de celda).  
  - **Narrador** (convierte tablas en lenguaje claro).  
- **Técnicas:** ZS/FS/CoT/ReAct/RAG/ToT/Chain/DSP/Ref/AC/AP/Ctr. (*Confianza: Alta*)

### 3.6 Ética, privacidad y cumplimiento
- **Reglas mínimas:** datos ficticios o anonimizados, no usar PII, **citar documentos** en RAG, “**no sé**” si no hay evidencia.  
- **Riesgos:** sobreconfianza, cherry-picking, simplificación excesiva. (*Confianza: Media–Alta*)

---

## 4. Pack de Prompts (10) con técnica
> *Listos para copiar/pegar. Sustituye `{{placeholders}}`.*

1) **(ZS)** Resumen ejecutivo de dataset — KPIs (tabla), 2 riesgos, 3 acciones.  
2) **(FS)** Resumen guiado por ejemplos — imita tono/estructura A/B.  
3) **(CoT)** KPIs con pasos — 3–5 pasos por KPI + 3 recomendaciones.  
4) **(ReAct)** Auditoría con evidencia — Problema | Celda | Corrección | Riesgo.  
5) **(RAG)** Informe CSV+PDF — cita doc/página en cada afirmación.  
6) **(ToT)** 3 interpretaciones → decisión — puntuar Impacto/Riesgo/Factibilidad.  
7) **(Chain)** Limpieza → visual → relato — flujo en 3 secciones.  
8) **(DSP)** Foco trimestral — descarta ruido <1.5% impacto.  
9) **(Ref+AP)** Pregunta antes — 3 preguntas críticas → brief.  
10) **(AC+Ctr)** v1/v2/v3 → consenso — fusiona justificando qué tomas de cada versión.

---

## 5. Ejercicios (20) — con técnicas del Prompting Guide
> *Entrega siempre: **qué hiciste**, **qué encontraste**, **qué decides**. Señala **N/D** si falta dato.*  

1. **ZS** — Tres KPIs y dos riesgos desde {{csv_simple}}.  
2. **FS** — Imitar dos resúmenes A/B y generar uno nuevo ({{tabla}}).  
3. **CoT** — Calcular margen, crecimiento y churn con 3–5 pasos.  
4. **ReAct** — Encontrar duplicados/outliers con **celda/rango** de evidencia.  
5. **RAG** — Informe de cumplimiento con {{manual.pdf}} y {{csv_costes}} (citas).  
6. **ToT** — Tres lecturas del mismo patrón (estacionalidad, ciclo, ruido) y decisión.  
7. **Chain** — Pipeline: limpieza→gráficos propuestos→narrativa ejecutiva (≤150 palabras).  
8. **DSP** — Solo variaciones trimestrales; ignora cambios <1.5%.  
9. **Ref** — ¿Qué suposiciones podrían sesgar el análisis? (3 riesgos + mitigación).  
10. **AC** — Genera 3 resúmenes y **consenso** final explicado.  
11. **ReAct** — Clasificar errores por severidad y urgencia con evidencia.  
12. **FS+CoT** — Dos ejemplos de outliers explicados → aplica a dataset nuevo.  
13. **RAG+Chain** — CSV + 2 PDFs → 1-pager con hallazgos y plan.  
14. **ToT** — Árbol de opciones para reducir coste de reporte mensual.  
15. **DSP+Ref** — Prioriza **factualidad** (no creatividad) y reflexiona sobre límites.  
16. **AP** — Antes de analizar, pregunta **objetivo / métrica / horizonte**; luego resuelve.  
17. **Ctr** — “Mal” vs “Buen” gráfico para la misma pregunta; justificar.  
18. **Chain+AC** — Dos pipelines alternativos → selección por consenso.  
19. **ZS+Translation** — Breve informe en ES y EN para comité internacional (si aplica).  
20. **RAG** — Comparar cifras con **fuente canónica**; marcar discrepancias con cita y “no sé” si procede.

---

## 6. Prácticas / Proyectos (8) — sectoriales
> **Entregable mínimo por proyecto:** 1-pager (situación, hallazgos, acciones) **+** evidencia (tablas/citas).  

| Proyecto | Ruta | Objetivo | Técnicas | Ventajas | Limitaciones | Coste | Confianza |
|---|---|---|---|---|---|---:|---|
| Data Viz Chain Agent | `projects/data-viz-chain-agent/` | Pipeline datos→gráficos→narrativa | ZS, FS, CoT, Chain | Rápido y replicable | Visual conceptual | Gratis | Alta |
| Anomaly Tree Detector | `projects/anomaly-tree-detector/` | Detectar errores/outliers con evidencia | ToT, ReAct, AC | Auditoría trazable | No análisis estadístico formal | Gratis | Alta |
| RAG Transparency Agent | `projects/rag-transparency-agent/` | Informe CSV+PDF con citas | RAG, ReAct | Valor AAPP/compliance | OCR/estructuras complejas | Gratis | Alta |
| Dashboard Narrativo Auto | `projects/dashboard-narrativo-auto/` | Varias narrativas → consenso | AC, Chain | Transparencia | Más tokens/tiempo | Gratis | Media-Alta |
| Pyme Consulting Zero | `projects/pyme-consulting-zero/` | Estrategia desde datos mínimos | ZS, DSP | Arranque rápido | Menos pulido que FS | Gratis | Media |
| Citizen Data Storyteller | `projects/citizen-data-storyteller/` | Lenguaje claro ciudadano | DSP, Ref | Transparencia | Simplificación | Gratis | Alta |
| Edu Data Explorer | `projects/edu-data-explorer/` | Insights educativos claros | ZS, Chain | Docencia lista | Sensible: anonimizar | Gratis | Alta |
| Zapier Data Pipeline | `projects/zapier-data-pipeline/` | Gmail→Sheets→Resumen | Chain | Automatiza reporting | Límites plan free | Gratis | Alta |

> **Instrucción:** crea `samples/` con **datasets ficticios** y **salidas** (capturas/txt/markdown). Señala **N/D** si algo falta.

---

## 7. Plantillas y recursos
- **KPIs (tabla):** `KPI | Valor | Cómo se calcula`  
- **1-pager ejecutivo:** *Situación / Hallazgos / Recomendaciones / Próximos pasos*  
- **Checklist de datos:** *Faltantes / Duplicados / Outliers / Consistencia / Trazabilidad*  
- **Política “no sé”:** si no hay evidencia, **indicarlo** y proponer cómo obtenerla.

---

## 8. Rúbrica de calidad y auditoría
- **Exactitud factual (0–3):** citas en RAG, coherencia de KPIs.  
- **Claridad ejecutiva (0–3):** 3 hallazgos + 3 acciones priorizadas.  
- **Trazabilidad (0–2):** celdas citadas (ReAct), fuentes (doc/pág).  
- **Ética/privacidad (0–2):** anonimización, “no sé”, N/D.  
**Apto ≥ 7/10**. Si <7: **rechazar, corregir y reentregar**.

---

## 9. Roadmap y backlog
- **Añadir** `samples/` a todos los proyectos.  
- **Capturas** en `/images/` (gráficos/indicadores).  
- **Sectores extra:** comercio exterior (costes de envío), salud **no clínico** (citas y recordatorios).  
- **Medición de ROI:** tiempo ahorrado por ejercicio.

---

## 10. Changelog
- **v1.0**: README con teoría, prompts (10), ejercicios (20), proyectos (8).  
- **v1.1**: Añadir evidencias/samples y capturas.

---

