# -*- coding: utf-8 -*-
"""
scripts/auditoria_transacciones.py

Ejercicio 6 – Auditoría de Transacciones Bancarias
Optimizado: CoT vectorizado, reglas agrupadas, duplicados compactos y reporte eficiente.

Entradas
  data_sample/transacciones_bancarias.xlsx  (hoja: "transacciones")

Salidas
  results/06_auditoria_transacciones_result.md
  results/06_transacciones_limpio.xlsx
"""

from __future__ import annotations
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np

# =========================
# Rutas y parámetros
# =========================
ROOT = Path(__file__).resolve().parents[1] if Path(__file__).parent.name == "scripts" else Path(".")
DATA_DIR = ROOT / "data_sample"
RESULTS_DIR = ROOT / "results"
DATA_IN = DATA_DIR / "transacciones_bancarias.xlsx"
REPORT_OUT = RESULTS_DIR / "06_auditoria_transacciones_result.md"
CLEAN_OUT = RESULTS_DIR / "06_transacciones_limpio.xlsx"

ALLOWED_CURRENCIES = frozenset(("EUR", "USD", "GBP"))
INCOME_CONCEPTS   = frozenset(("Ingreso ventanilla", "Ingreso cajero", "Nómina"))
TODAY   = pd.Timestamp("today").normalize()
MINDATE = pd.Timestamp("2000-01-01")

BASE_COLS = ("ID_Transaccion","Cuenta_IBAN","Fecha","Importe","Moneda","Beneficiario","Concepto")

# =========================
# Utilidades rápidas
# =========================
def ensure_dirs() -> None:
    for p in (DATA_DIR, RESULTS_DIR):
        p.mkdir(parents=True, exist_ok=True)

def parse_dates_stripped(s: pd.Series) -> pd.Series:
    # parseo robusto y rápido (vectorizado)
    return pd.to_datetime(s.astype(str).str.strip(), errors="coerce")

def is_valid_es_iban(series: pd.Series) -> pd.Series:
    # Validación básica de IBAN ES: prefijo 'ES' + longitud 24
    s = series.fillna("")
    return s.str.len().eq(24) & s.str.startswith("ES")

def to_md_table(df: pd.DataFrame, limit: int = 12) -> str:
    if df is None or df.empty:
        return "_(Sin filas que mostrar)_"
    head = df.head(limit)
    try:
        return head.to_markdown(index=False)
    except Exception:
        return head.to_string(index=False)

# =========================
# Núcleo de auditoría
# =========================
def audit_transactions(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # 1) Normalizaciones mínimas y parseo (una sola vez)
    fecha_ts = parse_dates_stripped(out["Fecha"])
    out["Fecha_ts"] = fecha_ts
    # Normalizamos a día (Timestamp) en vez de .dt.date para mantener tipo datetime64[ns]
    out["Fecha_day"] = fecha_ts.dt.normalize()

    # 2) Máscaras booleanas (todas vectorizadas, calculadas una vez)
    # Extrae Series locales para reducir búsquedas de atributos
    moneda = out["Moneda"]
    iban   = out["Cuenta_IBAN"]
    conc   = out["Concepto"]
    imp    = out["Importe"]

    m_fecha_nula         = fecha_ts.isna()
    m_fecha_fuera_rango  = ~m_fecha_nula & ((fecha_ts < MINDATE) | (fecha_ts > TODAY))
    m_moneda_invalida    = ~moneda.isin(ALLOWED_CURRENCIES)
    m_iban_invalido      = ~is_valid_es_iban(iban)
    m_benef_vacio        = out["Beneficiario"].isna() | (out["Beneficiario"].astype(str).str.strip() == "")
    m_concepto_vacio     = conc.isna() | (conc.astype(str).str.strip() == "")
    m_importe_incoh      = conc.isin(INCOME_CONCEPTS) & (imp < 0)

    # 3) Duplicados
    #    - por ID
    m_dup_id = out.duplicated(subset=("ID_Transaccion",), keep=False)
    #    - por clave funcional: (IBAN, Fecha_day, Importe, Beneficiario)
    m_dup_key = out.duplicated(subset=("Cuenta_IBAN","Fecha_day","Importe","Beneficiario"), keep=False)

    # 4) Asignación en bloque (evita overhead de múltiples líneas)
    flags = {
        "flag_fecha_nula": m_fecha_nula,
        "flag_fecha_fuera_rango": m_fecha_fuera_rango,
        "flag_moneda_invalida": m_moneda_invalida,
        "flag_iban_invalido": m_iban_invalido,
        "flag_beneficiario_vacio": m_benef_vacio,
        "flag_concepto_vacio": m_concepto_vacio,
        "flag_importe_incoherente": m_importe_incoh,
        "flag_dup_id": m_dup_id,
        "flag_dup_clave": m_dup_key,
    }
    out = out.assign(**flags)

    # 5) Etiqueta global (suma de banderas)
    flag_cols = [c for c in out.columns if c.startswith("flag_")]
    # usa .to_numpy(dtype=int) para sumar rápido en numpy
    out["flags_total"] = np.sum(out[flag_cols].to_numpy(dtype=np.int8), axis=1)
    out["registro_valido"] = out["flags_total"].eq(0)

    return out

# =========================
# Informe Markdown eficiente
# =========================
def build_report(df_raw: pd.DataFrame, df_flags: pd.DataFrame) -> str:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    total = len(df_raw)

    counters_map = {
        "Duplicados por ID": "flag_dup_id",
        "Duplicados por clave": "flag_dup_clave",
        "Fecha nula": "flag_fecha_nula",
        "Fecha fuera de rango": "flag_fecha_fuera_rango",
        "Moneda inválida": "flag_moneda_invalida",
        "IBAN inválido": "flag_iban_invalido",
        "Beneficiario vacío": "flag_beneficiario_vacio",
        "Concepto vacío": "flag_concepto_vacio",
        "Importe incoherente (ingreso negativo)": "flag_importe_incoherente",
    }
    counters = {k: int(df_flags[v].sum()) for k, v in counters_map.items()}

    # Tablas de ejemplo (columnas relevantes ya filtradas)
    examples = {
        "Duplicados por ID_Transaccion": df_flags[df_flags["flag_dup_id"]][
            ["ID_Transaccion","Cuenta_IBAN","Fecha","Importe","Moneda","Beneficiario","Concepto"]
        ],
        "Duplicados por clave (IBAN, Fecha, Importe, Beneficiario)": df_flags[df_flags["flag_dup_clave"]][
            ["Cuenta_IBAN","Fecha","Importe","Beneficiario","Concepto"]
        ],
        "Fechas fuera de rango (futuras o < 2000-01-01)": df_flags[df_flags["flag_fecha_fuera_rango"]][
            ["ID_Transaccion","Fecha","Importe","Beneficiario"]
        ],
        "IBAN inválido": df_flags[df_flags["flag_iban_invalido"]][
            ["ID_Transaccion","Cuenta_IBAN","Beneficiario","Importe"]
        ],
        "Moneda inválida": df_flags[df_flags["flag_moneda_invalida"]][
            ["ID_Transaccion","Moneda","Importe","Beneficiario"]
        ],
        "Importe incoherente (ingreso negativo)": df_flags[df_flags["flag_importe_incoherente"]][
            ["ID_Transaccion","Concepto","Importe","Beneficiario","Fecha"]
        ],
    }

    md = []
    md.append("# Ejercicio 6 – Auditoría de Transacciones Bancarias")
    md.append("**Metodología:** CoT vectorizado + reglas agrupadas  \n**Sector:** Banca, seguros y consultoría financiera\n")
    md.append("---\n")
    md.append("## 🗓️ Ejecución")
    md.append(f"- Fecha y hora: **{ts}**")
    md.append(f"- Filas totales (entrada): **{total}**\n")

    md.append("## 📊 Resumen de incidencias")
    for k, v in counters.items():
        md.append(f"- {k}: **{v}**")

    md.append("\n## 📑 Ejemplos")
    for title, dfx in examples.items():
        md.append(f"**{title}**")
        md.append(to_md_table(dfx))

    md.append("\n---\n## ✅ Conclusiones")
    md.append("- Auditoría vectorizada lista para escalar a millones de filas.")
    md.append("- El Excel de salida incluye **banderas por fila** y `flags_total` para priorizar limpieza.")
    md.append("- Para producción: validación IBAN con checksum, catálogo ISO 4217 completo y reglas AML/KYC específicas.")

    return "\n".join(md)

# =========================
# Main
# =========================
def main() -> None:
    ensure_dirs()
    if not DATA_IN.exists():
        raise FileNotFoundError(f"No se encontró {DATA_IN}. Genera o copia el dataset antes de ejecutar.")

    # Carga: evita inferencias pesadas; deja que pandas infiera lo justo
    df = pd.read_excel(DATA_IN, sheet_name="transacciones")

    audited = audit_transactions(df)

    # Export rápido (orden de columnas: base + flags)
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
