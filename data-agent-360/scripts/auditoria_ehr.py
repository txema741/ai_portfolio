# -*- coding: utf-8 -*-
"""
scripts/auditoria_ehr.py

Ejercicio 5 – Auditoría de Historias Clínicas Electrónicas (EHR)
Metodología: Chain-of-Thought (CoT) con implementación vectorizada y reglas agrupadas.

Entradas:
  data_sample/historias_clinicas.xlsx

Salidas:
  results/05_auditoria_ehr_result.md
  results/05_historias_clinicas_limpio.xlsx
"""

from pathlib import Path
from datetime import datetime
import numpy as np
import pandas as pd

# -----------------------------------------
# Rutas
# -----------------------------------------
ROOT = Path(__file__).resolve().parents[1] if Path(__file__).parent.name == "scripts" else Path(".")
DATA_DIR = ROOT / "data_sample"
RESULTS_DIR = ROOT / "results"
DATA_IN = DATA_DIR / "historias_clinicas.xlsx"
REPORT_OUT = RESULTS_DIR / "05_auditoria_ehr_result.md"
CLEAN_OUT = RESULTS_DIR / "05_historias_clinicas_limpio.xlsx"

# Catálogo demo ICD-10 (válidos)
ICD10_VALID = {"I10","E11","J45","M54","K21","N39","F41","L20","G43","Z00","R51","B34","A09","H52","S06"}

# -----------------------------------------
# Utilidades
# -----------------------------------------
def ensure_dirs():
    for p in (DATA_DIR, RESULTS_DIR):
        p.mkdir(parents=True, exist_ok=True)

def parse_dates(series: pd.Series) -> pd.Series:
    """Parseo robusto de fechas (vectorizado)."""
    return pd.to_datetime(series.astype(str).str.strip(), errors="coerce")

def to_md_table(df: pd.DataFrame, limit: int = 12) -> str:
    """Convierte un DF a tabla Markdown (recortada)."""
    if df is None or df.empty:
        return "_(Sin filas que mostrar)_"
    head = df.head(limit)
    try:
        return head.to_markdown(index=False)
    except Exception:
        return head.to_string(index=False)

# -----------------------------------------
# Núcleo: comprobaciones CoT (vectorizadas)
# -----------------------------------------
def cot_checks(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # 1) Parseo de fechas (vectorizado)
    out["Fecha_Nacimiento_ts"] = parse_dates(out["Fecha_Nacimiento"])
    out["Fecha_Ingreso_ts"] = parse_dates(out["Fecha_Ingreso"])
    out["Fecha_Alta_ts"] = parse_dates(out["Fecha_Alta"])

    # 2) Edad (vectorizada) → años aproximados por días/365.25
    ref = pd.Timestamp("today").normalize()
    out["Edad"] = (ref - out["Fecha_Nacimiento_ts"]).dt.days / 365.25

    # 3) Reglas agrupadas (más fácil de mantener)
    rules = {
        "flag_edad_imposible": (out["Edad"] <= 0) | (out["Edad"] > 120),
        "flag_alta_antes_ingreso": out["Fecha_Alta_ts"].notna() & out["Fecha_Ingreso_ts"].notna() & (out["Fecha_Alta_ts"] < out["Fecha_Ingreso_ts"]),
        "flag_icd10_invalido": out["Código_ICD10"].notna() & ~out["Código_ICD10"].isin(ICD10_VALID),
        "flag_sexo_invalido": ~out["Sexo"].isin(["M","F"]),
        "flag_diag_vacio": out["Diagnóstico"].isna() | (out["Diagnóstico"].astype(str).str.strip() == ""),
        "flag_trat_vacio": out["Tratamiento"].isna() | (out["Tratamiento"].astype(str).str.strip() == ""),
    }
    for col, mask in rules.items():
        out[col] = mask

    # 4) Duplicados: por ID y por clave (Nombre+Apellidos+Fecha_Nac)
    out["_Fecha_Nac_date"] = out["Fecha_Nacimiento_ts"].dt.date
    dup_rules = {
        "flag_dup_idpac": ["ID_Paciente"],
        "flag_dup_clave": ["Nombre","Apellidos","_Fecha_Nac_date"],
    }
    for col, subset in dup_rules.items():
        out[col] = out.duplicated(subset=subset, keep=False)

    # 5) Suma de banderas y etiqueta global
    flag_cols = [c for c in out.columns if c.startswith("flag_")]
    out["flags_total"] = out[flag_cols].sum(axis=1)
    out["registro_valido"] = out["flags_total"] == 0

    return out

# -----------------------------------------
# Informe Markdown
# -----------------------------------------
def markdown_report(df_raw: pd.DataFrame, df_flags: pd.DataFrame) -> str:
    total = len(df_raw)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Resumen principal (conteos)
    summary_map = {
        "Duplicados por ID": "flag_dup_idpac",
        "Duplicados por clave": "flag_dup_clave",
        "Edades imposibles": "flag_edad_imposible",
        "Alta antes de ingreso": "flag_alta_antes_ingreso",
        "ICD10 inválido (no vacío)": "flag_icd10_invalido",
        "Sexo inválido": "flag_sexo_invalido",
        "Diagnóstico vacío": "flag_diag_vacio",
        "Tratamiento vacío": "flag_trat_vacio",
    }
    resumen = {k: int(df_flags[v].sum()) for k, v in summary_map.items()}

    # Ejemplos (título → DF con columnas relevantes)
    examples = {
        "Duplicados por ID_Paciente": df_flags[df_flags["flag_dup_idpac"]][
            ["ID_Paciente","Nombre","Apellidos","Fecha_Nacimiento","Fecha_Ingreso","Fecha_Alta"]
        ],
        "Altas anteriores al ingreso": df_flags[df_flags["flag_alta_antes_ingreso"]][
            ["ID_Paciente","Nombre","Apellidos","Fecha_Ingreso","Fecha_Alta"]
        ],
        "Códigos ICD-10 inválidos (no vacíos)": df_flags[df_flags["flag_icd10_invalido"]][
            ["ID_Paciente","Código_ICD10","Diagnóstico","Fecha_Ingreso"]
        ],
        "Edades imposibles": df_flags[df_flags["flag_edad_imposible"]][
            ["ID_Paciente","Fecha_Nacimiento","Edad"]
        ],
    }

    md = []
    md.append("# Ejercicio 5 – Auditoría de Historias Clínicas (EHR)")
    md.append("**Metodología:** Chain-of-Thought (CoT) – Razonamiento Encadenado  \n"
              "**Sector aplicado:** Sanidad, gestión hospitalaria y salud digital.\n")
    md.append("---\n")
    md.append("## 🗓️ Ejecución")
    md.append(f"- Fecha y hora de auditoría: **{ts}**")
    md.append(f"- Filas totales (entrada): **{total}**\n")

    md.append("## 📊 Resumen de incidencias")
    for k, v in resumen.items():
        md.append(f"- {k}: **{v}**")

    md.append("\n## 📑 Ejemplos")
    for title, dfx in examples.items():
        md.append(f"**{title}**")
        md.append(to_md_table(dfx))

    md.append("\n---\n## ✅ Conclusiones")
    md.append("- El razonamiento encadenado (CoT) se implementa de forma vectorizada para mayor rendimiento.")
    md.append("- El dataset exportado incluye **banderas de error por registro** para priorizar correcciones.")
    md.append("- En proyectos reales, amplía el diccionario ICD-10 y añade reglas clínicas específicas del servicio.")

    return "\n".join(md)

# -----------------------------------------
# Main
# -----------------------------------------
def main():
    ensure_dirs()
    if not DATA_IN.exists():
        raise FileNotFoundError(f"No se encontró {DATA_IN}. Genera o copia el dataset antes de ejecutar.")

    # Carga
    df = pd.read_excel(DATA_IN)

    # Auditoría
    df_flags = cot_checks(df)

    # Export: dataset marcado/limpio
    base_cols = [
        "ID_Paciente","Nombre","Apellidos","Fecha_Nacimiento","Sexo",
        "Fecha_Ingreso","Fecha_Alta","Diagnóstico","Código_ICD10","Tratamiento","Médico_Responsable"
    ]
    extra_cols = [c for c in df_flags.columns if c not in base_cols]
    df_flags[base_cols + extra_cols].to_excel(CLEAN_OUT, index=False)

    # Export: informe Markdown
    report_md = markdown_report(df, df_flags)
    with open(REPORT_OUT, "w", encoding="utf-8") as f:
        f.write(report_md)

    print(f"[OK] Informe generado: {REPORT_OUT}")
    print(f"[OK] Dataset marcado/limpio: {CLEAN_OUT}")

if __name__ == "__main__":
    main()
