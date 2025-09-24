# 🤖 Health Data Guardian – V4 (Agente Extractivo sin descargas)

Agente conversacional **ligero** que responde preguntas sobre los resultados de auditoría leyendo:
- `results/issues_detectados.csv`
- `results/profile.json`
- `results/analyst_summary.md` (opcional, de V3)

No usa modelos generativos ni APIs. **No descarga nada**.

## ▶️ Ejecución
```bash
pip install -r requirements_v4.txt
streamlit run apps/ai_agent/agent_extractive.py

Abre: http://localhost:8501

❓ Ejemplos de preguntas

¿Qué campo tiene más errores?

Errores por tipo

Errores por campo

Ejemplos campo correo

¿Cuántas filas y columnas tiene el dataset?

Recomendaciones

🧩 Notas

Necesitas haber ejecutado V1/V2 (y V3 si quieres usar el summary) para que existan archivos en results/.

Este agente es determinista y auditables (rule-based). Ideal para entornos con poca memoria o sin Internet.

Se puede extender a embeddings/LLM si el cliente lo requiere (V4 avanzado).

---

# ▶️ Cómo lanzarlo (resumen)

1) Instala deps mínimas:
```bash
pip install -r requirements_v4.txt
Asegúrate de tener results/issues_detectados.csv y results/profile.json (ejecuta V1/V2 antes).

Ejecuta:streamlit run apps/ai_agent/agent_extractive.py
Navega a http://localhost:8501 y pregunta cosas como:

“¿Qué campo tiene más errores?”

“Errores por tipo”

“Ejemplos campo correo”
