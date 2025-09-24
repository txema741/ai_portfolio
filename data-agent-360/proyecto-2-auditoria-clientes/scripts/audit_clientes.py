# -*- coding: utf-8 -*-
"""
Auditoría de Clientes con IA
Optimizado con enfoque en seguridad informática y eficiencia.

Metodología:
DSP (Directional Stimulus Prompting – Estímulo Direccional de Prompting)

Detecta:
- Campos obligatorios faltantes
- Emails inválidos
- Teléfonos inválidos
- Países fuera de lista ISO
- Fechas inválidas o futuras
- Duplicados por email y teléfono

Uso:
python scripts/audit_clientes.py --input data_sample/clientes_sinteticos.csv --outdir results
"""

import argparse
import os
import re
from datetime import datetime, date
import pandas as pd

# Configuración de seguridad
MAX_FILE_SIZE_MB = 5
ALLOWED_COLUMNS = {"id_cliente", "nombre", "email", "telefono", "pais", "fecha_alta", "notas"}

# Regex robusta y segura para emails
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9.-]{1,255}\.[A-Za-z]{2,10}$")

# Config parámetros
PHONE_MIN_LEN = 9
ISO_COUNTRIES = {"ES", "MX", "PT", "AR", "CO", "IT"}
REQUIRED_COLS = ["id_cliente", "nombre", "email", "telefono", "pais", "fecha_alta"]


# ---------------------------
# Funciones utilitarias
# ---------------------------

def secure_path(path: str) -> str:
    """Evita path traversal, fuerza escritura en carpeta segura."""
    return os.path.abspath(path)


def check_file_size(path: str) -> None:
    """Previene apertura de archivos demasiado grandes."""
    size_mb = os.path.getsize(path) / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        raise ValueError(f"Archivo demasiado grande: {size_mb:.2f} MB (máximo {MAX_FILE_SIZE_MB} MB)")


def valid_email(s: str) -> bool:
    return bool(EMAIL_RE.match(s.strip())) if s else False


def valid_phone(s: str) -> bool:
    digits = re.sub(r"\D", "", s)
    return len(digits) >= PHONE_MIN_LEN


def valid_country(s: str) -> bool:
    return s in ISO_COUNTRIES


def valid_iso_date(s: str) -> bool:
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return True
    except Exception:
        return False


def is_future_date(s: str) -> bool:
    try:
        d = datetime.strptime(s, "%Y-%m-%d").date()
        return d > date.today()
    except Exception:
        return False


# ---------------------------
# Auditoría de datos
# ---------------------------

def audit(df: pd.DataFrame) -> pd.DataFrame:
    issues = []

    # Campos obligatorios faltantes
    for col in REQUIRED_COLS:
        if col not in df.columns:
            issues.append({"row": None, "field": col, "issue": "columna_ausente"})

    if issues:
        return pd.DataFrame(issues)

    # Emails inválidos
    mask_email = ~df["email"].apply(valid_email)
    issues.extend(
        [{"row": idx + 1, "field": "email", "issue": "email_invalido"} for idx in df[mask_email].index]
    )

    # Teléfonos inválidos o vacíos
    mask_tel = ~df["telefono"].apply(valid_phone)
    issues.extend(
        [{"row": idx + 1, "field": "telefono", "issue": "telefono_invalido"} for idx in df[mask_tel].index]
    )

    mask_tel_empty = df["telefono"].eq("")
    issues.extend(
        [{"row": idx + 1, "field": "telefono", "issue": "valor_faltante"} for idx in df[mask_tel_empty].index]
    )

    # Países inválidos
    mask_pais = ~df["pais"].apply(valid_country)
    issues.extend(
        [{"row": idx + 1, "field": "pais", "issue": "pais_no_iso"} for idx in df[mask_pais].index]
    )

    # Fechas inválidas o futuras
    mask_fecha_invalida = ~df["fecha_alta"].apply(valid_iso_date)
    issues.extend(
        [{"row": idx + 1, "field": "fecha_alta", "issue": "fecha_formato_invalido"} for idx in df[mask_fecha_invalida].index]
    )

    mask_fecha_futura = df["fecha_alta"].apply(is_future_date)
    issues.extend(
        [{"row": idx + 1, "field": "fecha_alta", "issue": "fecha_futura"} for idx in df[mask_fecha_futura].index]
    )

    # Duplicados por email y teléfono
    for field in ["email", "telefono"]:
        mask_dup = df[field].str.lower().duplicated(keep=False)
        issues.extend(
            [{"row": idx + 1, "field": field, "issue": "duplicado"} for idx in df[mask_dup].index]
        )

    return pd.DataFrame(issues)


def kpis(df: pd.DataFrame, issues_df: pd.DataFrame):
    total = len(df)
    with_issues = len(issues_df["row"].dropna().unique()) if not issues_df.empty else 0

    kpi_main = {
        "registros_totales": total,
        "registros_con_incidencias": with_issues,
        "porcentaje_con_incidencias": round((with_issues / total) * 100, 2) if total > 0 else 0.0,
    }
    kpi_breakdown = issues_df["issue"].value_counts().to_dict() if not issues_df.empty else {}
    return kpi_main, kpi_breakdown


def write_report(outdir: str, kpi_main: dict, kpi_breakdown: dict) -> None:
    os.makedirs(outdir, exist_ok=True)
    report_path = os.path.join(outdir, "reporte_clientes.md")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Informe de Auditoría — Clientes\n\n")
        f.write("**Metodología:** DSP (Directional Stimulus Prompting – Estímulo Direccional de Prompting)\n\n")
        f.write("## Resumen ejecutivo\n")
        f.write(f"- Registros totales: **{kpi_main['registros_totales']}**\n")
        f.write(f"- Registros con incidencias: **{kpi_main['registros_con_incidencias']}**\n")
        f.write(f"- % con incidencias: **{kpi_main['porcentaje_con_incidencias']}%**\n\n")
        f.write("## Desglose por tipo de incidencia\n")
        if kpi_breakdown:
            for issue, count in kpi_breakdown.items():
                f.write(f"- {issue}: **{count}**\n")
        else:
            f.write("- No se detectaron incidencias.\n")
        f.write("\n---\n")
        f.write("## Notas\n")
        f.write("- Validaciones: email/telefono/pais/fecha y duplicados.\n")
        f.write("- Basado en la metodología DSP (Directional Stimulus Prompting – Estímulo Direccional de Prompting).\n")


# ---------------------------
# Main
# ---------------------------

def main():
    parser = argparse.ArgumentParser(description="Auditoría de clientes (segura)")
    parser.add_argument("--input", required=True, help="Ruta al CSV de entrada")
    parser.add_argument("--outdir", required=True, help="Carpeta de salida")
    args = parser.parse_args()

    input_path = secure_path(args.input)
    outdir = secure_path(args.outdir)

    # Validación de seguridad en archivo
    check_file_size(input_path)

    try:
        df = pd.read_csv(input_path, dtype=str, encoding="utf-8").fillna("")
    except Exception as e:
        raise SystemExit(f"Error al leer CSV: {e}")

    # Solo permitir columnas esperadas
    df = df[[c for c in df.columns if c in ALLOWED_COLUMNS]]

    # Auditoría
    issues_df = audit(df)

    os.makedirs(outdir, exist_ok=True)

    issues_path = os.path.join(outdir, "issues_detectados.csv")
    issues_df.to_csv(issues_path, index=False, encoding="utf-8")

    kpi_main, kpi_breakdown = kpis(df, issues_df)
    write_report(outdir, kpi_main, kpi_breakdown)

    print(f"[OK] Incidencias -> {issues_path}")
    print(f"[OK] Reporte -> {os.path.join(outdir, 'reporte_clientes.md')}")


if __name__ == "__main__":
    main()
