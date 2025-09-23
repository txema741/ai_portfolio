# 🤖 Proyecto 1 – Health Data Guardian (V4 Extractivo)

Esta versión añade un **agente conversacional ligero y determinista**, que responde preguntas en lenguaje natural sobre los resultados de auditoría.  
A diferencia de otros agentes que dependen de modelos grandes o APIs de pago, esta versión es **100% local, sin descargas adicionales, rápida y ejecutable en cualquier ordenador**.

---

## 🚀 Novedades de V4
- Interfaz conversacional con **Streamlit**.
- Sin dependencias pesadas: solo `pandas` y `streamlit`.
- Respuestas **extractivas y basadas en reglas**:
  - Total de incidencias.
  - Campo con más errores.
  - Errores por tipo y por campo.
  - Ejemplos de incidencias por campo.
  - Filas y columnas del dataset.
  - Recomendaciones rápidas (a partir de los tipos de incidencias detectadas).
- Opcional: búsqueda de palabras clave en el informe `analyst_summary.md`.

---

## 📂 Estructura del proyecto (añadidos en V4)

proyecto-1-health-data-guardian/
├─ apps/
│ └─ ai_agent/
│ └─ agent_extractive.py # agente conversacional ligero
├─ results/
│ ├─ issues_detectados.csv # generado en V1 o V2
│ ├─ profile.json # generado en V1 o V2
│ ├─ analyst_summary.md # generado en V3
│ └─ ...
├─ requirements_v4.txt # dependencias mínimas
└─ README_V4.md


---

## 🔧 Requisitos

Instalar dependencias mínimas:

```bash
pip install pandas streamlit

Contenido de requirements_v4.txt:

pandas
streamlit

▶️ Ejecución del agente

Ejecutar desde la raíz del proyecto:

streamlit run apps/ai_agent/agent_extractive.py


Abrir en el navegador: http://localhost:8501

Tú: ¿Qué campo tiene más errores?
🤖: El campo con más errores es **correo** (18 incidencias).

Tú: ¿Cuántos errores hay en total?
🤖: Total de incidencias: 73

Tú: Dame ejemplos del campo codigo_postal
🤖:
Ejemplos para `codigo_postal`:
 row campo tipo   detalle
  3  codigo_postal formato  2800A
  7  codigo_postal formato  123

Limitaciones del V4 extractivo

No usa modelos generativos → no “redacta” respuestas largas, solo devuelve fragmentos y reglas predefinidas.

No entiende preguntas demasiado abiertas o ambiguas.

El valor está en que es rápido, transparente y ejecutable en cualquier máquina sin coste adicional.

🔮 Extensiones futuras

Sustituir el motor extractivo por un LLM local (ej. HuggingFace, Flan-T5).

Integrar embeddings (FAISS + SentenceTransformers) para mejorar la búsqueda semántica.

Versión API → conectar el agente con sistemas externos.

📌 Conclusión: con este V4, el proyecto Health Data Guardian ya cubre el ciclo completo:

V1: CLI para auditar y limpiar datos.

V2: Dashboard interactivo en Streamlit.

V3: Analista heurístico que resume hallazgos.

V4: Agente conversacional extractivo, ligero y extensible.
