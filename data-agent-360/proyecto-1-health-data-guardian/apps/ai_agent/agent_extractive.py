# -*- coding: utf-8 -*-
"""
Health Data Guardian – V4 (Modo Extractivo, sin descargas ni APIs)
Agente conversacional simple que responde sobre los resultados de auditoría
leyendo issues_detectados.csv, profile.json y analyst_summary.md (opcional).

Requisitos: pandas, streamlit
Ejecución: streamlit run apps/ai_agent/agent_extractive.py
"""

from pathlib import Path
import json
import re
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]   # carpeta raíz del proyecto
RESULTS = ROOT / "results"

# -------- CARGA DE DATOS --------
def load_issues() -> pd.DataFrame:
    f = RESULTS / "issues_detectados.csv"
    if not f.exists():
        return pd.DataFrame(columns=["row","campo","tipo","detalle"])
    return pd.read_csv(f, dtype=str).fillna("")

def load_profile() -> dict:
    f = RESULTS / "profile.json"
    if not f.exists():
        return {}
    return json.loads(f.read_text(encoding="utf-8"))

def load_summary() -> str:
    f = RESULTS / "analyst_summary.md"
    if not f.exists():
        return ""
    return f.read_text(encoding="utf-8")

# -------- LÓGICA DE RESPUESTAS (REGLAS) --------
def answer_query(query: str, issues: pd.DataFrame, profile: dict, summary: str) -> str:
    q = (query or "").lower().strip()
    if not q:
        return "Escribe una pregunta. Ejemplos: '¿Qué campo tiene más errores?', 'Errores por tipo', 'Ejemplos campo correo'."

    # Reglas frecuentes
    if not issues.empty:
        if ("total" in q and ("error" in q or "incidencia" in q)) or "cuántos errores" in q:
            return f"Total de incidencias detectadas: **{len(issues)}**."

        if ("campo" in q and "más" in q and "error" in q) or "campo con más errores" in q:
            vc = issues["campo"].value_counts()
            if vc.empty:
                return "No hay incidencias registradas."
            campo_top, cnt = vc.index[0], int(vc.iloc[0])
            return f"El campo con más errores es **`{campo_top}`** (**{cnt}** incidencias)."

        if "por tipo" in q:
            d = issues["tipo"].value_counts().to_dict()
            return f"Errores por tipo: `{d}`"

        if "por campo" in q:
            d = issues["campo"].value_counts().to_dict()
            return f"Errores por campo: `{d}`"

        m = re.search(r"ejemplos?\s+campo\s+([a-z0-9_]+)", q)
        if m:
            campo = m.group(1)
            ex = issues[issues["campo"].str.lower() == campo.lower()].head(8)
            return f"**Ejemplos para `{campo}`**:\n\n{ex.to_string(index=False) if not ex.empty else 'No hay ejemplos.'}"

        if any(w in q for w in ["recomend", "qué hacer", "suger"]):
            tipos = list(issues["tipo"].value_counts().index)
            recs = recommended_actions(tipos)
            return "**Recomendaciones rápidas:**\n- " + "\n- ".join(recs)

    if profile:
        if any(w in q for w in ["filas", "columnas", "tamaño", "rows", "cols"]):
            return f"Filas: **{profile.get('rows','?')}**, Columnas: **{profile.get('cols','?')}**."

    # Búsqueda simple en analyst_summary.md (opcional)
    if summary:
        # Si pide "recomendaciones", intenta extraer líneas relevantes
        if any(w in q for w in ["recomend", "suger"]):
            lines = [L for L in summary.splitlines() if "recomend" in L.lower() or "accionable" in L.lower()]
            return "\n".join(lines[:10]) if lines else "No encontré recomendaciones en el resumen."
        # Fallback: buscar última palabra clave
        key = q.split()[-1]
        lines = [L for L in summary.splitlines() if key in L.lower()]
        if lines:
            return "Fragmentos relevantes del resumen:\n\n" + "\n".join(lines[:8])

    return "No entendí la pregunta o no hay datos suficientes. Prueba con: '¿Qué campo tiene más errores?', 'Errores por tipo', 'Ejemplos campo correo'."

def recommended_actions(types: list) -> list:
    t = set(types)
    recs = []
    if "nulo" in t:
        recs.append("Definir imputación/validación para campos clínicos críticos (edad, IMC, tensión).")
    if "formato" in t:
        recs.append("Normalizar email/teléfono/CP con regex y plantillas.")
    if "rango" in t:
        recs.append("Ajustar umbrales fisiológicos con el equipo clínico; revisar outliers.")
    if "duplicado" in t:
        recs.append("Deduplicar por `patient_id` y establecer clave única en origen.")
    if "consistencia" in t:
        recs.append("Recalcular IMC desde peso/altura; bloquear edición manual del IMC.")
    if "fecha_futura" in t or "formato_fecha" in t:
        recs.append("Estandarizar fechas `YYYY-MM-DD` y bloquear fechas futuras en visitas.")
    return recs or ["No hay tipos con incidencias suficientes para recomendar acciones específicas."]

# -------- UI STREAMLIT --------
def main():
    st.set_page_config(page_title="Health Data Guardian – Agente (Extractivo)", layout="wide")
    st.title("🤖 Health Data Guardian – V4 (Modo Extractivo)")
    st.caption("Agente conversacional ligero, sin descargas ni APIs. Responde con fragmentos y reglas.")

    issues = load_issues()
    profile = load_profile()
    summary = load_summary()

    st.sidebar.header("Datos cargados")
    st.sidebar.write(f"- Incidencias: {len(issues)}")
    st.sidebar.write(f"- Profile.json: {'sí' if profile else 'no'}")
    st.sidebar.write(f"- Analyst summary: {'sí' if summary else 'no'}")

    st.markdown("### Pregunta")
    query = st.text_input("Ejemplos: '¿Qué campo tiene más errores?', 'Errores por tipo', 'Ejemplos campo correo'")

    if st.button("Consultar"):
        respuesta = answer_query(query, issues, profile, summary)
        st.markdown("### Respuesta")
        st.write(respuesta)

    with st.expander("Ver incidencias (raw)"):
        st.dataframe(issues, use_container_width=True)
    with st.expander("Ver profile.json (raw)"):
        st.json(profile)
    with st.expander("Ver analyst_summary.md (raw)"):
        st.text(summary[:2000] + ("..." if len(summary) > 2000 else ""))

if __name__ == "__main__":
    main()
