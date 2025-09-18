# -*- coding: utf-8 -*-
"""
scripts/auditoria_inventarios.py

Ejercicio 10 – Auditoría de Inventarios y Cadenas de Suministro
Metodología: ReAct (Reason + Act)
- Vectorización con NumPy/Pandas
- Reglas activables
- Informe Markdown + Excel con flags

Entradas:
  data_sample/inventarios.xlsx  (hoja: "inventario")

Salidas:
  results/10_auditoria_inventarios_result.md
  results/10_inventarios_limpio.xlsx
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
DATA_IN = DATA_DIR / "inventarios.xlsx"
REPORT_OUT = RESULTS_DIR / "10_auditoria_inventarios_result.md"
CLEAN_OUT = RESULTS_DIR / "10_inventarios_limpio.xlsx"

MIN_DATE = pd.Timestamp("2000-01-01")
MAX_DATE = pd.Timestamp("2050-12-31")

VALID_ALMACENES = frozenset({"ALM-01", "ALM-02", "ALM-03", "ALM-04", "ALM-05"})

BASE_COLS = (
    "ID_Producto","ID_Almacén","Fecha_Entrada","Fecha_Salida","Cantidad","Precio_Unitario"
)

CHECKS_ENABLED = {
    "dup_clave": True,            # (ID_Producto, ID_Almacén, Fecha_Entrada)
    "fecha_incoherente": True,    # Salida < Entrada o fechas fuera de rango
    "cantidad_invalida": True,    # <=0 o >100000
    "precio_invalido": True,      # <=0 o >10000
    "producto_invalido": True,    # PRD-XXXXX
    "almacen_invalido": True,     # fuera de catálogo
}

# ------------------------
# Utils
# ------------------------
def ensure_dirs() -> None:
    for p in (DATA_DIR, RESULTS_DIR):
        p.mkdir(parents=True, exist_ok=True)

def parse_date(s: pd.Series) -> pd.Series:
    return pd.to_datetime(s.astype(str).str.strip(), errors="coerce")

def to_md_table(df: pd.DataFrame, limit: int = 12) -> str:
    if df is None or df.empty:
        return "_(Sin filas que mostrar)_"
    head = df.head(limit)
    try:
        return head.to_markdown(index=False)
    except Exception:
        return head.to_string(index=False)

# ------------------------
# Auditoría
# ------------------------
def audit_inventory(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # Normalizar strings
    for c in ["ID_Producto","ID_Almacén","Fecha_Entrada","Fecha_Salida"]:
        out[c] = out[c].astype(str).str.strip()

    # Fechas
    fe_ts = parse_date(out["Fecha_Entrada"])
    fs_ts = parse_date(out["Fecha_Salida"])
    out["Fecha_Entrada_ts"] = fe_ts
    out["Fecha_Salida_ts"] = fs_ts

    # Numéricos
    cant = pd.to_numeric(out["Cantidad"], errors="coerce")
    punit = pd.to_numeric(out["Precio_Unitario"], errors="coerce")

    # Arrays
    fe_na = fe_ts.isna().to_numpy()
    fs_na = fs_ts.isna().to_numpy()
    fe_vals = fe_ts.to_numpy("datetime64[ns]")
    fs_vals = fs_ts.to_numpy("datetime64[ns]")
    cant_vals = cant.to_numpy()
    punit_vals = punit.to_numpy()

    m = {}

    # Duplicados por clave
    if CHECKS_ENABLED["dup_clave"]:
        m["flag_dup"] = out.duplicated(subset=("ID_Producto","ID_Almacén","Fecha_Entrada"), keep=False).to_numpy()

    # Fechas incoherentes / fuera de rango
    if CHECKS_ENABLED["fecha_incoherente"]:
        ok_range_ent = (~fe_na) & (fe_vals >= np.datetime64(MIN_DATE)) & (fe_vals <= np.datetime64(MAX_DATE))
        ok_range_sal = (~fs_na) & (fs_vals >= np.datetime64(MIN_DATE)) & (fs_vals <= np.datetime64(MAX_DATE))
        incoh = (~fe_na) & (~fs_na) & (fs_vals < fe_vals)
        fuera_rango = (~ok_range_ent) | (~ok_range_sal)
        m["flag_fecha_incoherente"] = incoh | fuera_rango

    # Cantidades
    if CHECKS_ENABLED["cantidad_invalida"]:
        m["flag_cant_invalida"] = np.isnan(cant_vals) | (cant_vals <= 0) | (cant_vals > 100_000)

    # Precios
    if CHECKS_ENABLED["precio_invalido"]:
        m["flag_precio_invalido"] = np.isnan(punit_vals) | (punit_vals <= 0) | (punit_vals > 10_000)

    # Producto
    if CHECKS_ENABLED["producto_invalido"]:
        m["flag_producto_invalido"] = ~out["ID_Producto"].str.match(r"^PRD-\d{5}$", na=False).to_numpy()

    # Almacén
    if CHECKS_ENABLED["almacen_invalido"]:
        m["flag_almacen_invalido"] = ~out["ID_Almacén"].isin(VALID_ALMACENES).to_numpy()

    # Asignación de flags
    for k, arr in m.items():
        out[k] = arr

    # Suma de banderas
    flags = list(m.keys())
    out["flags_total"] = out[flags].sum(axis=1).astype("int16") if flags else 0
    out["registro_valido"] = out["flags_total"].eq(0)

    return out

# ------------------------
# Informe
# ------------------------
def build_report(df: pd.DataFrame, audited: pd.DataFrame) -> str:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    total = len(df)

    counters = {
        "Duplicados (ID_Producto, ID_Almacén, Fecha_Entrada)": int(audited.get("flag_dup", False).sum()),
        "Fechas incoherentes / fuera de rango": int(audited.get("flag_fecha_incoherente", False).sum()),
        "Cantidades inválidas": int(audited.get("flag_cant_invalida", False).sum()),
        "Precios inválidos": int(audited.get("flag_precio_invalido", False).sum()),
        "Códigos de producto inválidos": int(audited.get("flag_producto_invalido", False).sum()),
        "Almacenes inválidos": int(audited.get("flag_almacen_invalido", False).sum()),
    }

    md = []
    md.append("# Ejercicio 10 – Auditoría de Inventarios y Cadenas de Suministro")
    md.append(f"**Ejecución:** {ts}  \n**Filas totales (entrada):** {total}\n")
    md.append("## 📊 Resumen de incidencias")
    for k, v in counters.items():
        md.append(f"- {k}: **{v}**")

    md.append("\n## 📑 Ejemplos")
    md.append("**Duplicados por clave**\n" + to_md_table(
        audited[audited.get("flag_dup", False)][["ID_Producto","ID_Almacén","Fecha_Entrada","Cantidad","Precio_Unitario"]]
    ))
    md.append("**Fechas incoherentes / fuera de rango**\n" + to_md_table(
        audited[audited.get("flag_fecha_incoherente", False)][["ID_Producto","Fecha_Entrada","Fecha_Salida","ID_Almacén"]]
    ))
    md.append("**Códigos de producto inválidos**\n" + to_md_table(
        audited[audited.get("flag_producto_invalido", False)][["ID_Producto","ID_Almacén"]]
    ))

    md.append("\n---\n## ✅ Conclusiones")
    md.append("- Reglas vectorizadas y `flags_total` para priorizar correcciones.")
    md.append("- Recomendación: integrar maestro de productos y catálogo de almacenes de ERP/WMS.")
    return "\n".join(md)

# ------------------------
# Main
# ------------------------
def main() -> None:
    ensure_dirs()
    if not DATA_IN.exists():
        raise FileNotFoundError(f"No se encontró {DATA_IN}. Coloca el dataset en {DATA_IN}.")

    df = pd.read_excel(DATA_IN, sheet_name="inventario")
    audited = audit_inventory(df)

    # Export
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
