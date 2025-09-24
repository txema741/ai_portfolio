# -*- coding: utf-8 -*-
"""
Health Data Guardian – Dashboard (V2)
Sube un CSV clínico, ejecuta auditoría y descarga el dataset limpio y los informes.

Requisitos: pandas, numpy, streamlit
Ejecución (local/futuro): streamlit run apps/dashboard/app.py
"""
import io
import json
import sys
from pathlib import Path

import pandas as pd
import streamlit as st # type: ignore

# Asegurar que podemos importar el core desde /scripts
ROOT = Path(__file__).resolve().parents[2]  # .../proyecto-1-health-data-guardian
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.append(str(SCRIPTS_DIR))

try:
    from audit_core import audit_dataframe, clean_dataframe  # noqa: E402
except ImportError as e:
    raise ImportError(f"Error al importar 'audit_core': {e}. Verifica que 'audit_core.py' existe en el directorio 'scripts'.")

st.set_page_config(page_title="Health Data Guardian – Dashboard", layout="wide")
st.title("🩺 Health Data Guardian – Dashboard (V2)")
st.caption("Sube un CSV con datos clínicos, ejecútalo y descarga resultados limpios y el informe.")

# Sidebar
with st.sidebar:
    st.header("⚙️ Opciones")
    sample_hint = st.checkbox("Mostrar hint sobre formato esperado", value=False)
    st.markdown("---")
    st.markdown("**Estructura esperada (columnas clave):**")
    st.code(
        "patient_id, nombre, edad, sexo, altura_cm, peso_kg, imc, "
        "tension_sistolica, tension_diastolica, frecuencia_cardiaca, "
        "glucosa_mg_dl, colesterol_total, diagnosticos, medicacion, "
        "fecha_ultima_visita, correo, telefono, codigo_postal",
        language="markdown",
    )
    st.markdown("---")
    st.caption("Los archivos se procesan en memoria. No se suben a servidores externos desde la app.")

st.markdown("### 1) Sube tu archivo CSV")
uploaded_file = st.file_uploader("Selecciona un archivo .csv", type=["csv"])

if sample_hint:
    st.info("Consejo: si no tienes un CSV a mano, usa el de `data_sample/pacientes_sinteticos.csv` de tu repo.")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error al leer el CSV: {e}")
        st.stop()

    st.subheader("👀 Vista previa del dataset")
    st.dataframe(df.head(25), use_container_width=True)

    st.markdown("### 2) Ejecutar auditoría")
    run = st.button("🔎 Ejecutar auditoría de calidad")
    if run:
        try:
            profile, issues = audit_dataframe(df)
            df_clean = clean_dataframe(df)
        except Exception as e:
            st.error(f"Error durante la auditoría: {e}")
            st.stop()

        # Panel de resultados
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("📊 Perfil del dataset")
            st.json(profile)

        with col2:
            st.subheader("🧾 Incidencias detectadas")
            issues_df = pd.DataFrame(issues)
            if issues_df.empty:
                st.success("Sin incidencias detectadas 🎉")
            else:
                st.dataframe(issues_df, use_container_width=True)

        st.markdown("### 3) Dataset limpio")
        st.dataframe(df_clean.head(25), use_container_width=True)

        # ----- Descargas -----
        st.markdown("### 4) Descargas")

        # CSV limpio
        clean_csv_bytes = df_clean.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Descargar CSV limpio",
            data=clean_csv_bytes,
            file_name="pacientes_clean.csv",
            mime="text/csv",
        )

        # Issues CSV
        issues_csv_bytes = (issues_df.to_csv(index=False) if not issues_df.empty else "row,campo,tipo\n").encode("utf-8")
        st.download_button(
            "⬇️ Descargar incidencias (CSV)",
            data=issues_csv_bytes,
            file_name="issues_detectados.csv",
            mime="text/csv",
        )

        # Profile JSON
        profile_json_bytes = json.dumps(profile, ensure_ascii=False, indent=2).encode("utf-8")
        st.download_button(
            "⬇️ Descargar perfil (JSON)",
            data=profile_json_bytes,
            file_name="profile.json",
            mime="application/json",
        )

        # Reporte Markdown (generado en memoria)
        report_md = io.StringIO()
        report_md.write("# 🩺 Reporte de Auditoría (V2 Dashboard)\n\n")
        report_md.write(f"- Filas: {profile.get('rows')}\n")
        report_md.write(f"- Columnas: {profile.get('cols')}\n")
        report_md.write(f"- Nulos por columna: {profile.get('nulls_by_col')}\n\n")
        if not issues_df.empty:
            resumen = (
                issues_df.groupby(["campo", "tipo"])
                .size()
                .reset_index(name="conteo")
                .sort_values(["conteo"], ascending=False)
            )
            report_md.write("## Resumen de incidencias (campo, tipo, conteo)\n\n")
            report_md.write(resumen.to_markdown(index=False))
            report_md.write("\n")
        else:
            report_md.write("## Sin incidencias detectadas.\n")
        report_bytes = report_md.getvalue().encode("utf-8")

        st.download_button(
            "⬇️ Descargar reporte (Markdown)",
            data=report_bytes,
            file_name="reporte_health_audit.md",
            mime="text/markdown",
        )

        st.success("Proceso finalizado. Puedes descargar los archivos generados arriba ✅")
else:
    st.info("Sube un CSV para comenzar.")
