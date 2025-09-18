# -*- coding: utf-8 -*-
"""
scripts/auditoria_envios.py (versión ultra-optimizada)

Ejercicio 7 – Auditoría de Envíos y Trazabilidad Logística
- Vectorización total
- Uso intensivo de NumPy para máscaras/operaciones
- Normalización única de columnas
- Flags configurables y asignación en bloque
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
DATA_IN = DATA_DIR / "envios_logistica.xlsx"
REPORT_OUT = RESULTS_DIR / "07_auditoria_envios_result.md"
CLEAN_OUT = RESULTS_DIR / "07_envios_limpio.xlsx"

TODAY = pd.Timestamp("today").normalize()
MIN_DATE = pd.Timestamp("2000-01-01")
MAX_DATE = pd.Timestamp("2050-12-31")

PESO_MAX_KG = 50_000.0
VOLUMEN_MAX_M3 = 500.0

CP_CIUDAD_MAP = {
    "28001": "Madrid", "28002": "Madrid", "28003": "Madrid", "28004": "Madrid",
    "08001": "Barcelona", "08002": "Barcelona", "08003": "Barcelona", "08004": "Barcelona",
    "46001": "Valencia", "46002": "Valencia", "46003": "Valencia",
    "41001": "Sevilla", "41002": "Sevilla", "41003": "Sevilla",
    "48001": "Bilbao", "48002": "Bilbao",
}
TRANSPORTISTAS_VALIDOS = frozenset(("DHL","SEUR","MRW","Correos","UPS","GLS"))

BASE_COLS = ("ID_Envio","Fecha_Envio","Fecha_Entrega","CP","Ciudad","Transportista",
             "Peso_kg","Volumen_m3","Destinatario","Dirección")

# Flags activables (si quieres desactivar algún check, pon False)
CHECKS_ENABLED = {
    "fecha_envio_nula": True,
    "fecha_entrega_nula": True,
    "entrega_antes_envio": True,
    "fecha_fuera_rango": True,
    "cp_ciudad_incoherente": True,
    "transportista_invalido": True,
    "peso_nulo": True,
    "peso_negativo": True,
    "peso_excesivo": True,
    "volumen_nulo": True,
    "volumen_negativo": True,
    "volumen_excesivo": True,
    "destinatario_vacio": True,
    "direccion_vacio": True,
    "dup_id": True,
    "dup_clave": True,
}

# ------------------------
# Utilidades
# ------------------------
def ensure_dirs() -> None:
    for p in (DATA_DIR, RESULTS_DIR):
        p.mkdir(parents=True, exist_ok=True)

def parse_dates_stripped(s: pd.Series) -> pd.Series:
    # parseo robusto (quita espacios), todo vectorizado
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
# Núcleo ultra-optimizado
# ------------------------
def audit_shipments(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # Normalización única (strings → strip)
    # Usamos .copy() sólo en columnas necesarias para evitar vistas ambiguas
    out["CP"] = out["CP"].astype(str).str.strip()
    out["Ciudad"] = out["Ciudad"].astype(str).str.strip()
    out["Transportista"] = out["Transportista"].fillna("").astype(str).str.strip()
    out["Destinatario"] = out["Destinatario"].astype(str).str.strip()
    out["Dirección"] = out["Dirección"].astype(str).str.strip()

    # Fechas parseadas una vez + normalizadas a día
    envio_ts = parse_dates_stripped(out["Fecha_Envio"])
    entrega_ts = parse_dates_stripped(out["Fecha_Entrega"])
    out["Fecha_Envio_ts"] = envio_ts
    out["Fecha_Entrega_ts"] = entrega_ts
    out["Fecha_Envio_day"] = envio_ts.dt.normalize()
    out["Fecha_Entrega_day"] = entrega_ts.dt.normalize()

    # Numéricos robustos
    peso = pd.to_numeric(out["Peso_kg"], errors="coerce")
    volumen = pd.to_numeric(out["Volumen_m3"], errors="coerce")

    # Para rendimiento: trabajar con arrays NumPy booleans (int8 al final)
    envio_na = envio_ts.isna().to_numpy()
    entrega_na = entrega_ts.isna().to_numpy()
    envio_vals = envio_ts.to_numpy("datetime64[ns]")
    entrega_vals = entrega_ts.to_numpy("datetime64[ns]")
    peso_vals = peso.to_numpy()
    vol_vals = volumen.to_numpy()

    # Máscaras (todas vectorizadas, sin apply)
    m = {}

    if CHECKS_ENABLED["fecha_envio_nula"]:
        m["flag_fecha_envio_nula"] = envio_na
    if CHECKS_ENABLED["fecha_entrega_nula"]:
        m["flag_fecha_entrega_nula"] = entrega_na
    if CHECKS_ENABLED["entrega_antes_envio"]:
        not_na_both = (~envio_na) & (~entrega_na)
        m["flag_entrega_antes_envio"] = not_na_both & (entrega_vals < envio_vals)
    if CHECKS_ENABLED["fecha_fuera_rango"]:
        env_ok = ~envio_na
        m["flag_fecha_fuera_rango"] = env_ok & ((envio_vals < np.datetime64(MIN_DATE)) | (envio_vals > np.datetime64(MAX_DATE)))

    if CHECKS_ENABLED["cp_ciudad_incoherente"]:
        # Map CP→Ciudad esperada. Donde CP no esté en el mapa, no marcamos (queda "" y no se activa incoherencia)
        cp_expected = out["CP"].map(CP_CIUDAD_MAP).fillna("")
        exp_vals = cp_expected.to_numpy(dtype="U32")
        ciudad_vals = out["Ciudad"].to_numpy(dtype="U32")
        # incoherente := hay ciudad esperada y no coincide con la ciudad informada
        m["flag_cp_ciudad_incoherente"] = (exp_vals != "") & (exp_vals != ciudad_vals)

    if CHECKS_ENABLED["transportista_invalido"]:
        # set membership vectorizado con pandas
        m["flag_transportista_invalido"] = ~out["Transportista"].isin(TRANSPORTISTAS_VALIDOS).to_numpy()

    if CHECKS_ENABLED["peso_nulo"]:
        m["flag_peso_nulo"] = np.isnan(peso_vals)
    if CHECKS_ENABLED["peso_negativo"]:
        m["flag_peso_negativo"] = np.isnan(peso_vals) | (peso_vals <= 0)
    if CHECKS_ENABLED["peso_excesivo"]:
        m["flag_peso_excesivo"] = (~np.isnan(peso_vals)) & (peso_vals > PESO_MAX_KG)

    if CHECKS_ENABLED["volumen_nulo"]:
        m["flag_volumen_nulo"] = np.isnan(vol_vals)
    if CHECKS_ENABLED["volumen_negativo"]:
        m["flag_volumen_negativo"] = np.isnan(vol_vals) | (vol_vals <= 0)
    if CHECKS_ENABLED["volumen_excesivo"]:
        m["flag_volumen_excesivo"] = (~np.isnan(vol_vals)) & (vol_vals > VOLUMEN_MAX_M3)

    if CHECKS_ENABLED["destinatario_vacio"]:
        m["flag_destinatario_vacio"] = (out["Destinatario"] == "").to_numpy()
    if CHECKS_ENABLED["direccion_vacio"]:
        m["flag_direccion_vacio"] = (out["Dirección"] == "").to_numpy()

    if CHECKS_ENABLED["dup_id"]:
        m["flag_dup_id"] = out.duplicated(subset=("ID_Envio",), keep=False).to_numpy()
    if CHECKS_ENABLED["dup_clave"]:
        # clave funcional: Fecha_Envio_day + Destinatario + Dirección + CP
        m["flag_dup_clave"] = out.duplicated(subset=("Fecha_Envio_day","Destinatario","Dirección","CP"), keep=False).to_numpy()

    # Asignación de flags en bloque
    for k, arr in m.items():
        # Convertimos a boolean dtype en pandas (ya vienen boolean np.bool_)
        out[k] = arr

    # Suma de banderas: stack de arrays booleanos → int8
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
        "Fecha envío nula": "flag_fecha_envio_nula",
        "Fecha entrega nula": "flag_fecha_entrega_nula",
        "Entrega antes de envío": "flag_entrega_antes_envio",
        "Fecha fuera de rango": "flag_fecha_fuera_rango",
        "CP–Ciudad incoherente": "flag_cp_ciudad_incoherente",
        "Transportista inválido": "flag_transportista_invalido",
        "Peso nulo": "flag_peso_nulo",
        "Peso negativo": "flag_peso_negativo",
        "Peso excesivo": "flag_peso_excesivo",
        "Volumen nulo": "flag_volumen_nulo",
        "Volumen negativo": "flag_volumen_negativo",
        "Volumen excesivo": "flag_volumen_excesivo",
        "Destinatario vacío": "flag_destinatario_vacio",
        "Dirección vacía": "flag_direccion_vacio",
    }

    # Solo contamos flags que existan (por si desactivas alguno)
    counters = {k: int(df_flags[v].sum()) for k, v in counters_map.items() if v in df_flags.columns}

    examples = {
        "Duplicados por ID_Envio": (["ID_Envio","Fecha_Envio","Fecha_Entrega","CP","Ciudad","Transportista","Peso_kg","Volumen_m3","Destinatario","Dirección"], "flag_dup_id"),
        "Duplicados por clave (Fecha_Envio, Destinatario, Dirección, CP)": (["ID_Envio","Fecha_Envio","Destinatario","Dirección","CP"], "flag_dup_clave"),
        "Entregas antes de envío": (["ID_Envio","Fecha_Envio","Fecha_Entrega","Destinatario","Dirección","CP"], "flag_entrega_antes_envio"),
        "CP–Ciudad incoherente": (["ID_Envio","CP","Ciudad"], "flag_cp_ciudad_incoherente"),
        "Transportista inválido": (["ID_Envio","Transportista","Destinatario"], "flag_transportista_invalido"),
        "Peso/Volumen anómalos (ejemplos)": (["ID_Envio","Peso_kg","Volumen_m3","Destinatario","CP"], None),
    }

    md = []
    md.append("# Ejercicio 7 – Auditoría de Envíos y Trazabilidad Logística")
    md.append("**Metodología:** Self-Consistency + CoT vectorizado  \n**Sector:** Logística y transporte\n")
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
            sample = df_flags[(df_flags.get("flag_peso_negativo", False)) | 
                              (df_flags.get("flag_peso_excesivo", False)) | 
                              (df_flags.get("flag_volumen_excesivo", False))][cols]
        else:
            if flag not in df_flags.columns:
                md.append("_(Check desactivado)_")
                continue
            sample = df_flags[df_flags[flag]][cols]
        md.append(to_md_table(sample))

    md.append("\n---\n## ✅ Conclusiones")
    md.append("- Validación híbrida y vectorizada: alto rendimiento con múltiples rutas de control.")
    md.append("- El Excel de salida contiene `flag_*`, `flags_total` y `registro_valido` para priorizar limpieza.")
    md.append("- Próximos pasos: ampliar CP→Ciudad, validar direcciones (geocoding) y reglas según tipología de carga.")

    return "\n".join(md)

# ------------------------
# Main
# ------------------------
def main() -> None:
    ensure_dirs()
    if not DATA_IN.exists():
        raise FileNotFoundError(f"No se encontró {DATA_IN}. Genera o copia el dataset antes de ejecutar.")

    df = pd.read_excel(DATA_IN, sheet_name="envios")
    audited = audit_shipments(df)

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
