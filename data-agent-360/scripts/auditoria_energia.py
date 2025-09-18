# -*- coding: utf-8 -*-
"""
scripts/auditoria_energia.py  (versión optimizada y corregida)

Ejercicio 9 – Auditoría de Consumos Energéticos y Facturación Eléctrica
- Vectorización total
- Reglas de auditoría activables
- Genera informe en Markdown + dataset limpio en Excel

Entradas:
  data_sample/consumos_energia.xlsx  (hoja: "facturas")

Salidas:
  results/09_auditoria_energia_result.md
  results/09_consumos_energia_limpio.xlsx
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
DATA_IN = DATA_DIR / "consumos_energia.xlsx"
REPORT_OUT = RESULTS_DIR / "09_auditoria_energia_result.md"
CLEAN_OUT = RESULTS_DIR / "09_consumos_energia_limpio.xlsx"

MIN_DATE = pd.Timestamp("2000-01-01")
MAX_DATE = pd.Timestamp("2050-12-31")

TARIFAS_VALIDAS = frozenset(("2.0TD", "3.0TD", "3.0A", "6.1TD"))

# Catálogo demo CP→Provincia
CP_PROV_MAP = {
    "28001": "Madrid", "28002": "Madrid", "28003": "Madrid", "28004": "Madrid", "28005": "Madrid",
    "08001": "Barcelona", "08002": "Barcelona", "08003": "Barcelona", "08004": "Barcelona", "08005": "Barcelona",
    "46001": "Valencia", "46002": "Valencia", "46003": "Valencia", "46004": "Valencia",
    "41001": "Sevilla", "41002": "Sevilla", "41003": "Sevilla",
    "48001": "Bizkaia", "48002": "Bizkaia", "48003": "Bizkaia",
}

# Umbrales técnicos/económicos
KWH_MAX = 20_000.0
KW_CONTRATADA_MAX = 100.0
PRECIO_MIN = 0.12
PRECIO_MAX = 0.35

BASE_COLS = (
    "ID_Factura", "ID_Contrato", "Periodo", "Fecha_Factura", "CUPS", "CP", "Provincia",
    "Cliente", "Dirección", "Tarifa", "kWh", "kW_Contratada", "Importe_Factura"
)

# Checks activables
CHECKS_ENABLED = {
    "dup_id": True,
    "dup_clave": True,
    "fecha_fuera_rango": True,
    "periodo_invalido": True,
    "cups_malformado": True,
    "cp_prov_incoherente": True,
    "tarifa_invalida": True,
    "kwh_invalido": True,
    "kw_contratada_invalida": True,
    "importe_sospechoso": True,
    "outlier_kwh": True,
    "outlier_importe": True,
    "cliente_vacio": True,
    "direccion_vacia": True,
}

# ------------------------
# Funciones auxiliares
# ------------------------
def ensure_dirs() -> None:
    for p in (DATA_DIR, RESULTS_DIR):
        p.mkdir(parents=True, exist_ok=True)

def parse_dates_stripped(s: pd.Series) -> pd.Series:
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
# Auditoría principal
# ------------------------
def audit_energy(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # Normalizar strings
    for col in ["Periodo", "CUPS", "CP", "Provincia", "Cliente", "Dirección", "Tarifa"]:
        out[col] = out[col].astype(str).str.strip()

    # Fechas
    fact_ts = parse_dates_stripped(out["Fecha_Factura"])
    out["Fecha_Factura_ts"] = fact_ts

    # Numéricos
    kwh = pd.to_numeric(out["kWh"], errors="coerce")
    kwc = pd.to_numeric(out["kW_Contratada"], errors="coerce")
    imp = pd.to_numeric(out["Importe_Factura"], errors="coerce")

    # Arrays para vectorización
    fact_na = fact_ts.isna().to_numpy()
    fact_vals = fact_ts.to_numpy("datetime64[ns]")
    kwh_vals = kwh.to_numpy()
    kwc_vals = kwc.to_numpy()
    imp_vals = imp.to_numpy()

    # €/kWh calculado
    with np.errstate(divide="ignore", invalid="ignore"):
        eur_kwh = np.where(kwh_vals > 0, imp_vals / kwh_vals, np.nan)

    # Percentiles para outliers (p99)
    def p99(x: pd.Series) -> float:
        try:
            return float(np.nanpercentile(x.to_numpy(dtype=float), 99))
        except Exception:
            return np.nan

    kwh_p99 = p99(kwh)
    imp_p99 = p99(imp)

    m = {}

    # Duplicados
    if CHECKS_ENABLED["dup_id"]:
        m["flag_dup_id"] = out.duplicated(subset=("ID_Factura",), keep=False).to_numpy()
    if CHECKS_ENABLED["dup_clave"]:
        m["flag_dup_clave"] = out.duplicated(subset=("ID_Contrato", "Periodo"), keep=False).to_numpy()

    # Fechas y periodo
    if CHECKS_ENABLED["fecha_fuera_rango"]:
        m["flag_fecha_fuera_rango"] = (~fact_na) & (
            (fact_vals < np.datetime64(MIN_DATE)) | (fact_vals > np.datetime64(MAX_DATE))
        )
    if CHECKS_ENABLED["periodo_invalido"]:
        m["flag_periodo_invalido"] = ~out["Periodo"].str.match(r"^\d{4}-(0[1-9]|1[0-2])$", na=False).to_numpy()

    # CUPS
    if CHECKS_ENABLED["cups_malformado"]:
        m["flag_cups_malformado"] = ~out["CUPS"].str.match(r"^ES[A-Z0-9]{18,20}$", na=False).to_numpy()

    # CP–Provincia
    if CHECKS_ENABLED["cp_prov_incoherente"]:
        prov_expected = out["CP"].map(CP_PROV_MAP).fillna("")
        m["flag_cp_prov_incoherente"] = (prov_expected != "") & (prov_expected != out["Provincia"])

    # Tarifa
    if CHECKS_ENABLED["tarifa_invalida"]:
        m["flag_tarifa_invalida"] = ~out["Tarifa"].isin(TARIFAS_VALIDAS).to_numpy()

    # Magnitudes
    if CHECKS_ENABLED["kwh_invalido"]:
        m["flag_kwh_invalido"] = np.isnan(kwh_vals) | (kwh_vals <= 0) | (kwh_vals > KWH_MAX)
    if CHECKS_ENABLED["kw_contratada_invalida"]:
        m["flag_kw_contratada_invalida"] = np.isnan(kwc_vals) | (kwc_vals <= 0) | (kwc_vals > KW_CONTRATADA_MAX)
    if CHECKS_ENABLED["importe_sospechoso"]:
        m["flag_importe_sospechoso"] = (~np.isnan(eur_kwh)) & ((eur_kwh < PRECIO_MIN) | (eur_kwh > PRECIO_MAX))

    # Outliers
    if CHECKS_ENABLED["outlier_kwh"]:
        m["flag_outlier_kwh"] = (~np.isnan(kwh_vals)) & (kwh_vals > kwh_p99 if not np.isnan(kwh_p99) else False)
    if CHECKS_ENABLED["outlier_importe"]:
        m["flag_outlier_importe"] = (~np.isnan(imp_vals)) & (imp_vals > imp_p99 if not np.isnan(imp_p99) else False)

    # Completitud
    if CHECKS_ENABLED["cliente_vacio"]:
        m["flag_cliente_vacio"] = (out["Cliente"] == "").to_numpy()
    if CHECKS_ENABLED["direccion_vacia"]:
        m["flag_direccion_vacia"] = (out["Dirección"] == "").to_numpy()

    # Añadir flags al dataframe
    for k, arr in m.items():
        out[k] = arr

    # Suma de banderas
    if m:
        flags_mat = np.vstack([arr.astype(np.int8, copy=False) for arr in m.values()])
        out["flags_total"] = flags_mat.sum(axis=0, dtype=np.int16)
    else:
        out["flags_total"] = 0

    out["registro_valido"] = out["flags_total"].eq(0)
    return out

# ------------------------
# Generación del informe
# ------------------------
def build_report(df_raw: pd.DataFrame, df_flags: pd.DataFrame) -> str:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    total = len(df_raw)

    counters_map = {
        "Duplicados por ID_Factura": "flag_dup_id",
        "Duplicados por (ID_Contrato, Periodo)": "flag_dup_clave",
        "Fecha de factura fuera de rango": "flag_fecha_fuera_rango",
        "Periodo inválido": "flag_periodo_invalido",
        "CUPS mal formado": "flag_cups_malformado",
        "CP–Provincia incoherente": "flag_cp_prov_incoherente",
        "Tarifa inválida": "flag_tarifa_invalida",
        "kWh inválidos": "flag_kwh_invalido",
        "kW contratada inválida": "flag_kw_contratada_invalida",
        "Importe sospechoso vs kWh": "flag_importe_sospechoso",
        "Outlier kWh (p99)": "flag_outlier_kwh",
        "Outlier Importe (p99)": "flag_outlier_importe",
        "Cliente vacío": "flag_cliente_vacio",
        "Dirección vacía": "flag_direccion_vacia",
    }
    counters = {k: int(df_flags[v].sum()) for k, v in counters_map.items() if v in df_flags.columns}

    examples = {
        "Duplicados por (ID_Contrato, Periodo)": (["ID_Contrato", "Periodo", "ID_Factura", "kWh", "Importe_Factura"], "flag_dup_clave"),
        "CUPS mal formado": (["CUPS", "Cliente", "Periodo"], "flag_cups_malformado"),
        "Importe sospechoso vs kWh": (["ID_Factura", "kWh", "Importe_Factura"], "flag_importe_sospechoso"),
        "CP–Provincia incoherente": (["CP", "Provincia", "Cliente"], "flag_cp_prov_incoherente"),
        "Outliers (kWh o Importe)": (["ID_Factura", "kWh", "Importe_Factura"], None),
    }

    md = []
    md.append("# Ejercicio 9 – Auditoría de Consumos Energéticos y Facturación")
    md.append("**Metodología:** Self-Consistency + CoT vectorizado  \n**Sector:** Energía (utilities)\n")
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
            sample = df_flags[(df_flags.get("flag_outlier_kwh", False)) | (df_flags.get("flag_outlier_importe", False))][cols]
        else:
            if flag not in df_flags.columns:
                md.append("_(Check desactivado)_")
                continue
            sample = df_flags[df_flags[flag]][cols]
        md.append(to_md_table(sample))

    md.append("\n---\n## ✅ Conclusiones")
    md.append("- Validaciones vectorizadas y combinadas por `flags_total` para priorizar correcciones.")
    md.append("- Recomendación: ampliar catálogo de tarifas, mapa CP–Provincia y añadir checksum real de CUPS.")

    return "\n".join(md)

# ------------------------
# Main
# ------------------------
def main() -> None:
    ensure_dirs()
    if not DATA_IN.exists():
        raise FileNotFoundError(f"No se encontró {DATA_IN}. Coloca el dataset en {DATA_IN}.")

    df = pd.read_excel(DATA_IN, sheet_name="facturas")
    audited = audit_energy(df)

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

