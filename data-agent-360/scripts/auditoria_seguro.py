# -*- coding: utf-8 -*-
"""
scripts/auditoria_seguro.py  (versión ultra-optimizada)

Ejercicio 8 – Auditoría de Pólizas y Siniestros de Seguros
- Vectorización total (sin apply)
- Uso intensivo de NumPy para máscaras y suma de flags
- Normalización única de columnas
- Flags configurables y asignación en bloque

Entradas:
  data_sample/polizas_siniestros.xlsx  (hoja: "polizas")

Salidas:
  results/08_auditoria_seguro_result.md
  results/08_polizas_siniestros_limpio.xlsx
"""

from __future__ import annotations
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np

# ------------------------
# Rutas y parámetros
# ------------------------
ROOT = Path(__file__).resolve().parents[1] if Path(__file__).parent.name == "scripts" else Path(".")
DATA_DIR = ROOT / "data_sample"
RESULTS_DIR = ROOT / "results"
DATA_IN = DATA_DIR / "polizas_siniestros.xlsx"
REPORT_OUT = RESULTS_DIR / "08_auditoria_seguro_result.md"
CLEAN_OUT = RESULTS_DIR / "08_polizas_siniestros_limpio.xlsx"

# Fechas y catálogos
MIN_DATE = pd.Timestamp("2000-01-01")
MAX_DATE = pd.Timestamp("2050-12-31")
TIPOS_VALIDOS = frozenset(("Auto", "Hogar", "Vida", "Salud", "Viaje"))

# Columnas base (orden export)
BASE_COLS = (
    "ID_Poliza", "Asegurado", "Beneficiario", "Tipo_Poliza",
    "Fecha_Poliza", "Fecha_Siniestro", "Monto_Poliza", "Monto_Siniestro",
    "Descripción_Siniestro"
)

# Flags activables (pon False para desactivar)
CHECKS_ENABLED = {
    "fecha_poliza_nula": True,
    "fecha_siniestro_nula": True,
    "siniestro_antes_poliza": True,
    "fecha_fuera_rango": True,
    "monto_poliza_invalido": True,
    "monto_siniestro_negativo": True,
    "monto_siniestro_mayor_poliza": True,
    "tipo_invalido": True,
    "asegurado_vacio": True,
    "beneficiario_vacio": True,
    "descripcion_vacia": True,
    "dup_id": True,
    "dup_clave": True,  # (Asegurado, Tipo_Poliza, Fecha_Poliza_day)
}

# ------------------------
# Utilidades
# ------------------------
def ensure_dirs() -> None:
    for p in (DATA_DIR, RESULTS_DIR):
        p.mkdir(parents=True, exist_ok=True)

def parse_dates_stripped(s: pd.Series) -> pd.Series:
    """Parseo robusto: strip + to_datetime con coerce."""
    return pd.to_datetime(s.astype(str).str.strip(), errors="coerce")

def to_md_table(df: pd.DataFrame, limit: int = 12) -> str:
    """Tabla Markdown corta (preview)."""
    if df is None or df.empty:
        return "_(Sin filas que mostrar)_"
    head = df.head(limit)
    try:
        return head.to_markdown(index=False)
    except Exception:
        return head.to_string(index=False)

# ------------------------
# Núcleo: auditoría vectorizada
# ------------------------
def audit_insurance(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # Normalización única de strings para rendimiento
    out["Asegurado"] = out["Asegurado"].astype(str).str.strip()
    out["Beneficiario"] = out["Beneficiario"].astype(str).str.strip()
    out["Tipo_Poliza"] = out["Tipo_Poliza"].astype(str).str.strip()
    out["Descripción_Siniestro"] = out["Descripción_Siniestro"].astype(str).str.strip()

    # Fechas (parseo + normalización a día)
    pol_ts = parse_dates_stripped(out["Fecha_Poliza"])
    sin_ts = parse_dates_stripped(out["Fecha_Siniestro"])
    out["Fecha_Poliza_ts"] = pol_ts
    out["Fecha_Siniestro_ts"] = sin_ts
    out["Fecha_Poliza_day"] = pol_ts.dt.normalize()

    # Numéricos robustos
    monto_pol = pd.to_numeric(out["Monto_Poliza"], errors="coerce")
    monto_sin = pd.to_numeric(out["Monto_Siniestro"], errors="coerce")

    # Arrays NumPy para máxima velocidad
    pol_na = pol_ts.isna().to_numpy()
    sin_na = sin_ts.isna().to_numpy()
    pol_vals = pol_ts.to_numpy("datetime64[ns]")
    sin_vals = sin_ts.to_numpy("datetime64[ns]")
    mpol_vals = monto_pol.to_numpy()
    msin_vals = monto_sin.to_numpy()

    # Máscaras (todas vectorizadas)
    m = {}

    if CHECKS_ENABLED["fecha_poliza_nula"]:
        m["flag_fecha_poliza_nula"] = pol_na
    if CHECKS_ENABLED["fecha_siniestro_nula"]:
        m["flag_fecha_siniestro_nula"] = sin_na
    if CHECKS_ENABLED["siniestro_antes_poliza"]:
        both = (~pol_na) & (~sin_na)
        m["flag_siniestro_antes_poliza"] = both & (sin_vals < pol_vals)
    if CHECKS_ENABLED["fecha_fuera_rango"]:
        m["flag_fecha_fuera_rango"] = (~pol_na) & ((pol_vals < np.datetime64(MIN_DATE)) | (pol_vals > np.datetime64(MAX_DATE)))

    if CHECKS_ENABLED["monto_poliza_invalido"]:
        m["flag_monto_poliza_invalido"] = np.isnan(mpol_vals) | (mpol_vals <= 0)
    if CHECKS_ENABLED["monto_siniestro_negativo"]:
        m["flag_monto_siniestro_negativo"] = np.isnan(msin_vals) | (msin_vals < 0)
    if CHECKS_ENABLED["monto_siniestro_mayor_poliza"]:
        # válido comparar solo cuando ambos valores están definidos
        both_num = (~np.isnan(msin_vals)) & (~np.isnan(mpol_vals))
        m["flag_monto_siniestro_mayor_poliza"] = both_num & (msin_vals > mpol_vals)

    if CHECKS_ENABLED["tipo_invalido"]:
        m["flag_tipo_invalido"] = ~out["Tipo_Poliza"].isin(TIPOS_VALIDOS).to_numpy()
    if CHECKS_ENABLED["asegurado_vacio"]:
        m["flag_asegurado_vacio"] = (out["Asegurado"] == "").to_numpy()
    if CHECKS_ENABLED["beneficiario_vacio"]:
        m["flag_beneficiario_vacio"] = (out["Beneficiario"] == "").to_numpy()
    if CHECKS_ENABLED["descripcion_vacia"]:
        m["flag_descripcion_vacia"] = (out["Descripción_Siniestro"] == "").to_numpy()

    if CHECKS_ENABLED["dup_id"]:
        m["flag_dup_id"] = out.duplicated(subset=("ID_Poliza",), keep=False).to_numpy()
    if CHECKS_ENABLED["dup_clave"]:
        # clave funcional: (Asegurado, Tipo_Poliza, Fecha_Poliza_day)
        m["flag_dup_clave"] = out.duplicated(subset=("Asegurado","Tipo_Poliza","Fecha_Poliza_day"), keep=False).to_numpy()

    # Asignación de flags en bloque
    for k, arr in m.items():
        out[k] = arr

    # Suma de banderas (np.int8 → suma int16 para evitar overflow)
    if m:
        flags_mat = np.vstack([arr.astype(np.int8, copy=False) for arr in m.values()])
        out["flags_total"] = flags_mat.sum(axis=0, dtype=np.int16)
    else:
        out["flags_total"] = 0

    out["registro_valido"] = out["flags_total"].eq(0)
    return out

# ------------------------
# Informe Markdown (rápido)
# ------------------------
def build_report(df_raw: pd.DataFrame, df_flags: pd.DataFrame) -> str:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    total = len(df_raw)

    counters_map = {
        "Duplicados por ID": "flag_dup_id",
        "Duplicados por clave": "flag_dup_clave",
        "Fecha póliza nula": "flag_fecha_poliza_nula",
        "Fecha siniestro nula": "flag_fecha_siniestro_nula",
        "Siniestro antes de póliza": "flag_siniestro_antes_poliza",
        "Fecha póliza fuera de rango": "flag_fecha_fuera_rango",
        "Monto póliza inválido": "flag_monto_poliza_invalido",
        "Monto siniestro negativo": "flag_monto_siniestro_negativo",
        "Monto siniestro > póliza": "flag_monto_siniestro_mayor_poliza",
        "Tipo de póliza inválido": "flag_tipo_invalido",
        "Asegurado vacío": "flag_asegurado_vacio",
        "Beneficiario vacío": "flag_beneficiario_vacio",
        "Descripción vacía": "flag_descripcion_vacia",
    }
    counters = {k: int(df_flags[v].sum()) for k, v in counters_map.items() if v in df_flags.columns}

    examples = {
        "Duplicados por ID_Poliza": (
            ["ID_Poliza","Asegurado","Tipo_Poliza","Fecha_Poliza","Monto_Poliza"],
            "flag_dup_id"
        ),
        "Duplicados por clave (Asegurado, Tipo_Poliza, Fecha_Poliza)": (
            ["ID_Poliza","Asegurado","Tipo_Poliza","Fecha_Poliza","Monto_Poliza"],
            "flag_dup_clave"
        ),
        "Siniestro antes de póliza": (
            ["ID_Poliza","Fecha_Poliza","Fecha_Siniestro","Asegurado"],
            "flag_siniestro_antes_poliza"
        ),
        "Tipo de póliza inválido": (
            ["ID_Poliza","Asegurado","Tipo_Poliza"],
            "flag_tipo_invalido"
        ),
        "Montos anómalos": (
            ["ID_Poliza","Monto_Poliza","Monto_Siniestro","Asegurado"],
            None  # combinación de dos flags
        ),
    }

    md = []
    md.append("# Ejercicio 8 – Auditoría de Pólizas y Siniestros de Seguros")
    md.append("**Metodología:** Self-Consistency + CoT vectorizado  \n**Sector:** Seguros y gestión de riesgos\n")
    md.append("---\n")
    md.append("## 🗓️ Ejecución")
    md.append(f"- Fecha y hora: **{ts}**")
    md.append(f"- Filas totales (entrada): **{total}**\n")

    md.append("## 📊 Resumen de incidencias")
    for k, v in counters.items():
        md.append(f"- {k}: **{v}**")

    md.append("\n## 📑 Ejemplos")
    for title, (cols, flag) in examples.items():
        md.append(f"**{title}**")
        if flag is None:
            sample = df_flags[
                (df_flags.get("flag_monto_siniestro_negativo", False)) |
                (df_flags.get("flag_monto_siniestro_mayor_poliza", False)) |
                (df_flags.get("flag_monto_poliza_invalido", False))
            ][cols]
        else:
            if flag not in df_flags.columns:
                md.append("_(Check desactivado)_")
                continue
            sample = df_flags[df_flags[flag]][cols]
        md.append(to_md_table(sample))

    md.append("\n---\n## ✅ Conclusiones")
    md.append("- Auditoría vectorizada y escalable con banderas por registro y `flags_total` para priorizar correcciones.")
    md.append("- Para producción: integrar reglas antifraude y catálogos ampliados de productos/ramas.")

    return "\n".join(md)

# ------------------------
# Main
# ------------------------
def main() -> None:
    ensure_dirs()
    if not DATA_IN.exists():
        raise FileNotFoundError(f"No se encontró {DATA_IN}. Copia o genera el dataset antes de ejecutar.")

    # Carga rápida
    df = pd.read_excel(DATA_IN, sheet_name="polizas")

    audited = audit_insurance(df)

    # Export: base + flags
    base_cols = list(BASE_COLS)
    extra_cols = [c for c in audited.columns if c not in base_cols]
    audited[base_cols + extra_cols].to_excel(CLEAN_OUT, index=False)

    report_md = build_report(df, audited)
    with open(REPORT_OUT, "w", encoding="utf-8") as f:
        f.write(report_md)

    print(f"[OK] Informe generado: {REPORT_OUT}")
    print(f"[OK] Dataset marcado/limpio: {CLEAN_OUT}")

if __name__ == "__main__":
    main()
