# -*- coding: utf-8 -*-
"""
Health Data Guardian – núcleo de auditoría de datos clínicos (V1).
Incluye validación, limpieza y generación de informes.
Optimizado para seguridad y eficiencia.
"""

import os, re, json, logging
from datetime import datetime, date
from typing import Tuple, List, Dict, Any
import numpy as np
import pandas as pd

# Configuración de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Regex precompiladas para validación
EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
PHONE_REGEX = re.compile(r"^(?:\+?\d{1,3}[\s-]?)?(?:\d{2,3}[\s-]?){2,4}\d{2,3}$")
POSTAL_REGEX = re.compile(r"^\d{5}$")

# Rango fisiológicos plausibles
RANGES: Dict[str, Tuple[int, int]] = {
    "edad": (0, 120),
    "altura_cm": (40, 250),
    "peso_kg": (2, 350),
    "tension_sistolica": (70, 240),
    "tension_diastolica": (40, 140),
    "frecuencia_cardiaca": (30, 220),
    "glucosa_mg_dl": (40, 600),
    "colesterol_total": (70, 600),
}

EXPECTED_COLS: List[str] = [
    "patient_id","nombre","edad","sexo","altura_cm","peso_kg","imc",
    "tension_sistolica","tension_diastolica","frecuencia_cardiaca",
    "glucosa_mg_dl","colesterol_total","diagnosticos","medicacion",
    "fecha_ultima_visita","correo","telefono","codigo_postal"
]


def compute_bmi(peso: Any, altura: Any) -> float:
    """
    Calcula el IMC (kg/m²).
    Retorna NaN si no es posible calcularlo.
    """
    try:
        h = float(altura) / 100
        w = float(peso)
        if h <= 0 or w <= 0:
            return np.nan
        return round(w / (h**2), 1)
    except (ValueError, TypeError):
        return np.nan


def audit_dataframe(df: pd.DataFrame) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Audita un DataFrame y devuelve:
    - profile: estadísticas del dataset
    - issues: lista de incidencias encontradas
    """
    # Validar columnas esperadas
    missing = [c for c in EXPECTED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"❌ El dataset no contiene las columnas necesarias: {missing}")

    # Perfil general
    profile: Dict[str, Any] = {
        "rows": int(len(df)),
        "cols": int(len(df.columns)),
        "nulls_by_col": df.isna().sum().to_dict(),
    }
    issues: List[Dict[str, Any]] = []

    # Duplicados
    dup_mask = df.duplicated(subset=["patient_id"], keep="first")
    if dup_mask.any():
        issues.extend([
            {"row": int(i), "campo": "patient_id", "tipo": "duplicado"}
            for i in df[dup_mask].index
        ])

    # Nulos
    nulls = df.isna()
    for col in EXPECTED_COLS:
        issues.extend([
            {"row": int(i), "campo": col, "tipo": "nulo"}
            for i in nulls.index[nulls[col]]
        ])

    # Rangos fisiológicos
    for col,(lo,hi) in RANGES.items():
        vals = pd.to_numeric(df[col], errors="coerce")
        mask = (vals < lo) | (vals > hi)
        issues.extend([
            {"row": int(i), "campo": col, "tipo": "rango"}
            for i in mask.index[mask]
        ])

    # IMC inconsistente
    calc = df.apply(lambda r: compute_bmi(r["peso_kg"], r["altura_cm"]), axis=1)
    imc = pd.to_numeric(df["imc"], errors="coerce")
    mask = (~imc.isna()) & (abs(imc - calc) > 1.0)
    issues.extend([
        {"row": int(i), "campo": "imc", "tipo": "consistencia"}
        for i in mask.index[mask]
    ])

    # Formatos
    issues.extend([
        {"row": int(i), "campo": "correo", "tipo": "formato"}
        for i,v in df["correo"].items() if pd.notna(v) and not EMAIL_REGEX.match(str(v))
    ])
    issues.extend([
        {"row": int(i), "campo": "telefono", "tipo": "formato"}
        for i,v in df["telefono"].items() if pd.notna(v) and not PHONE_REGEX.match(str(v))
    ])
    issues.extend([
        {"row": int(i), "campo": "codigo_postal", "tipo": "formato"}
        for i,v in df["codigo_postal"].items() if pd.notna(v) and not POSTAL_REGEX.match(str(v))
    ])

    # Fechas
    today = date.today()
    for i,v in df["fecha_ultima_visita"].items():
        try:
            d = datetime.strptime(str(v), "%Y-%m-%d").date()
            if d > today:
                issues.append({"row": int(i),"campo":"fecha_ultima_visita","tipo":"fecha_futura"})
        except Exception:
            issues.append({"row": int(i),"campo":"fecha_ultima_visita","tipo":"formato_fecha"})

    return profile, issues


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpieza básica:
    - Eliminar duplicados por patient_id
    - Normalizar correos y teléfonos
    - Recalcular IMC
    """
    dfc = df.drop_duplicates(subset=["patient_id"], keep="first").copy()
    dfc["correo"] = dfc["correo"].astype(str).str.strip().str.lower()
    dfc["telefono"] = dfc["telefono"].astype(str).str.strip()
    dfc["imc"] = dfc.apply(lambda r: compute_bmi(r["peso_kg"], r["altura_cm"]), axis=1)
    return dfc


def write_outputs(outdir: str, profile: Dict[str, Any], issues: List[Dict[str, Any]], df_clean: pd.DataFrame) -> None:
    """
    Guarda resultados en:
    - issues_detectados.csv
    - profile.json
    - reporte_health_audit.md
    - clean/pacientes_clean.csv
    """
    if not outdir:
        raise ValueError("❌ Carpeta de salida inválida")

    os.makedirs(outdir, exist_ok=True)
    os.makedirs(os.path.join(outdir,"clean"), exist_ok=True)

    pd.DataFrame(issues).to_csv(os.path.join(outdir,"issues_detectados.csv"), index=False, encoding="utf-8")

    with open(os.path.join(outdir,"profile.json"),"w",encoding="utf-8") as f:
        json.dump(profile, f, indent=2, ensure_ascii=False)

    with open(os.path.join(outdir,"reporte_health_audit.md"),"w",encoding="utf-8") as f:
        f.write("# 🩺 Reporte de Auditoría\n")
        f.write(f"- Filas: {profile['rows']}\n")
        f.write(f"- Columnas: {profile['cols']}\n")
        f.write(f"- Nulos por columna: {profile['nulls_by_col']}\n")

    df_clean.to_csv(os.path.join(outdir,"clean","pacientes_clean.csv"), index=False, encoding="utf-8")

    logging.info("✅ Resultados escritos en %s", outdir)
