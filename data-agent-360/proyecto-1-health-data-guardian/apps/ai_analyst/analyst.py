# -*- coding: utf-8 -*-
"""
Health Data Guardian – V3: AI Analyst (heurístico)
Lee issues_detectados.csv + profile.json y genera un resumen ejecutivo en Markdown.

Uso:
  python apps/ai_analyst/analyst.py \
      --issues results/issues_detectados.csv \
      --profile results/profile.json \
      --out results/analyst_summary.md
"""
import argparse
import json
from pathlib import Path
import pandas as pd

def load_issues(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=["row","campo","tipo","detalle"])
    df = pd.read_csv(path)
    # Normalizar columnas esperadas
    if "detalle" not in df.columns:
        df["detalle"] = ""
    return df

def load_profile(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def summarize_issues(df: pd.DataFrame) -> dict:
    """Devuelve conteos por tipo/campo y top problemas."""
    if df.empty:
        return {
            "total": 0,
            "by_tipo": {},
            "by_campo": {},
            "examples": [],
        }
    by_tipo = df.groupby("tipo").size().sort_values(ascending=False).to_dict()
    by_campo = df.groupby("campo").size().sort_values(ascending=False).to_dict()
    examples = df.head(10).to_dict(orient="records")
    return {
        "total": int(len(df)),
        "by_tipo": by_tipo,
        "by_campo": by_campo,
        "examples": examples,
    }

def heuristics_recommendations(by_tipo: dict, by_campo: dict) -> list:
    """Recomendaciones rápidas según incidencias detectadas."""
    recs = []
    # Por tipo
    if "nulo" in by_tipo:
        recs.append("Completar valores nulos en campos clínicos críticos (edad, tensión, IMC) con reglas y/o imputación controlada.")
    if "formato" in by_tipo:
        recs.append("Normalizar formatos de email/teléfono/código postal con expresiones regulares y plantillas.")
    if "rango" in by_tipo:
        recs.append("Validar umbrales fisiológicos con comité clínico y rechazar valores fuera de rango.")
    if "duplicado" in by_tipo:
        recs.append("Desduplicar por `patient_id` y establecer clave única en el origen.")
    if "consistencia" in by_tipo:
        recs.append("Recalcular IMC desde peso/altura y bloquear escritura directa del campo.")
    if "outlier_iqr" in by_tipo:
        recs.append("Revisar outliers con IQR y z-score; confirmar si son errores o casos clínicos raros.")
    if "formato_fecha" in by_tipo or "fecha_futura" in by_tipo:
        recs.append("Estandarizar fecha `YYYY-MM-DD` y bloquear fechas futuras en admisión/visitas.")

    # Por campo (ejemplos dirigidos)
    foco = list(by_campo.keys())[:5]
    if foco:
        recs.append(f"Priorizar limpieza en campos más problemáticos: {', '.join(foco)}.")
    return recs

def make_report(profile: dict, summary: dict) -> str:
    rows = profile.get("rows", "NA")
    cols = profile.get("cols", "NA")
    nulls_by_col = profile.get("nulls_by_col", {})
    md = []
    md.append("# 🧠 Health Data Guardian – Resumen Ejecutivo (V3)")
    md.append("")
    md.append("## 1) Visión general del dataset")
    md.append(f"- Filas: **{rows}**")
    md.append(f"- Columnas: **{cols}**")
    if nulls_by_col:
        # Top 5 columnas con más nulos
        top_nulls = sorted(nulls_by_col.items(), key=lambda x: x[1], reverse=True)[:5]
        md.append("- Top columnas con nulos:")
        for c, n in top_nulls:
            md.append(f"  - `{c}` → {n} nulos")
    else:
        md.append("- No se dispone de `profile.json` (se omitió el análisis de nulos).")

    md.append("")
    md.append("## 2) Incidencias detectadas")
    total = summary["total"]
    md.append(f"- Total de incidencias: **{total}**")
    if total == 0:
        md.append("✅ No se detectaron incidencias. El dataset está en buen estado.")
        return "\n".join(md)

    if summary["by_tipo"]:
        md.append("- Por tipo:")
        for t, cnt in sorted(summary["by_tipo"].items(), key=lambda x: x[1], reverse=True):
            md.append(f"  - **{t}** → {cnt}")
    if summary["by_campo"]:
        md.append("- Por campo:")
        for c, cnt in sorted(summary["by_campo"].items(), key=lambda x: x[1], reverse=True)[:10]:
            md.append(f"  - `{c}` → {cnt}")

    md.append("")
    md.append("## 3) Recomendaciones rápidas (accionables)")
    recs = heuristics_recommendations(summary["by_tipo"], summary["by_campo"])
    if recs:
        for r in recs:
            md.append(f"- {r}")
    else:
        md.append("- Sin recomendaciones adicionales.")

    md.append("")
    md.append("## 4) Muestras de incidencias")
    if summary["examples"]:
        md.append("| fila | campo | tipo | detalle |")
        md.append("|-----:|:------|:-----|:--------|")
        for r in summary["examples"]:
            md.append(f"| {r.get('row','')} | {r.get('campo','')} | {r.get('tipo','')} | {str(r.get('detalle','')).replace('|','\\|')} |")
    else:
        md.append("_Sin ejemplos disponibles_")

    return "\n".join(md)

def main():
    ap = argparse.ArgumentParser(description="AI Analyst (heurístico) – Resumen de incidencias")
    ap.add_argument("--issues", required=True, help="Ruta a results/issues_detectados.csv")
    ap.add_argument("--profile", required=False, default="", help="Ruta a results/profile.json (opcional)")
    ap.add_argument("--out", required=False, default="results/analyst_summary.md", help="Ruta de salida Markdown")
    args = ap.parse_args()

    issues_df = load_issues(Path(args.issues))
    profile = load_profile(Path(args.profile)) if args.profile else {}

    summary = summarize_issues(issues_df)
    report_md = make_report(profile, summary)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report_md, encoding="utf-8")
    print(f"✅ Resumen generado en {out_path}")

if __name__ == "__main__":
    main()
