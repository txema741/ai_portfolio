# scripts/audit_clientes.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Auditoría de Clientes — unificado v1/v2.

Comportamiento por defecto (sin flags): modo v1 minimal
- Salidas: issues_detectados.csv, reporte_auditoria.md

Modo avanzado (v2) si usas --schema:
- Valida país ISO-3166 (International Organization for Standardization – Organización Internacional de Normalización)
- Normaliza teléfono E.164 (E.164 Numbering Plan – Plan de Numeración E.164)
- Tipado/fechas con --strict
- Salidas extra: perfil_columnas.json, kpi_calidad.csv (si --with-json)

Siglas:
- CSV (Comma-Separated Values – Valores Separados por Comas)
- JSON (JavaScript Object Notation – Notación de Objetos de JavaScript)
- KPI (Key Performance Indicator – Indicador Clave de Desempeño)
- CLI (Command Line Interface – Interfaz de Línea de Comandos)
"""

import argparse
import json
import os
import re
from datetime import datetime
from collections import defaultdict

import numpy as np
import pandas as pd

# --- Opcionales para modo avanzado (v2) ---
try:
    import phonenumbers  # E.164
except Exception:  # no installed -> degrade gracefully
    phonenumbers = None

try:
    import pycountry  # ISO-3166
except Exception:
    pycountry = None

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


# =========================
# Utilidades v1/v2
# =========================
def is_valid_email(v):
    if v is None or str(v).strip() == "":
        return True
    return EMAIL_RE.match(str(v).strip()) is not None


def parse_date(v, fmt):
    try:
        datetime.strptime(str(v).strip(), fmt)
        return True
    except Exception:
        return False


def is_number(v):
    try:
        float(v)
        return True
    except Exception:
        return False


def is_valid_iso_country(code):
    if pycountry is None:
        return True  # si no hay lib, no marcamos error
    code = str(code).strip().upper()
    if not code:
        return True
    return pycountry.countries.get(alpha_2=code) is not None


def normalize_e164(phone_str, default_region="ES"):
    if phonenumbers is None:
        return None, None  # sin normalización si no está la lib
    if phone_str is None or str(phone_str).strip() == "":
        return None, None
    try:
        parsed = phonenumbers.parse(str(phone_str), default_region)
        if not phonenumbers.is_valid_number(parsed):
            return None, "telefono_invalido"
        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164), None
    except Exception:
        return None, "telefono_invalido"


def profile_df(df):
    perfil = {"n_filas": int(df.shape[0]), "n_columnas": int(df.shape[1]), "columnas": {}}
    for col in df.columns:
        s = df[col]
        info = {
            "nulos": int(s.isna().sum()),
            "unicos": int(s.nunique(dropna=True)),
            "ejemplos": [str(x) for x in s.dropna().astype(str).unique()[:5]],
        }
        if pd.api.types.is_numeric_dtype(s):
            sn = pd.to_numeric(s, errors="coerce")
            if sn.notna().any():
                info["min"] = float(np.nanmin(sn))
                info["max"] = float(np.nanmax(sn))
                info["media"] = float(np.nanmean(sn))
            else:
                info["min"] = info["max"] = info["media"] = None
        perfil["columnas"][col] = info
    return perfil


def write_report(df, issues, perfil, kpis, out_md, advanced=False):
    lines = []
    lines.append("# Reporte de Auditoría de Clientes\n")
    lines.append(f"- Filas: **{df.shape[0]}**")
    lines.append(f"- Columnas: **{df.shape[1]}**")
    lines.append(f"- Incidencias detectadas: **{len(issues)}**\n")

    if advanced and kpis is not None:
        lines.append("## KPIs (Key Performance Indicator – Indicador Clave de Desempeño)")
        for k, v in kpis.get("global", {}).items():
            lines.append(f"- {k}: **{v}**")
        lines.append("")

    lines.append("## Incidencias por tipo (top 10 por tipo)")
    if not issues:
        lines.append("- Sin incidencias ✅\n")
    else:
        by_type = defaultdict(list)
        for it in issues:
            by_type[it["tipo_error"]].append(it)
        for t, items in by_type.items():
            lines.append(f"### {t} ({len(items)})")
            for ex in items[:10]:
                lines.append(f"- Fila {ex['fila']}, **{ex['columna']}** → {ex['detalle']}")
            lines.append("")

    if advanced and perfil is not None:
        lines.append("## Perfil de columnas (resumen)")
        for col, c in perfil["columnas"].items():
            base = f"- **{col}**: nulos={c['nulos']}, únicos={c['unicos']}, ejemplos={c['ejemplos']}"
            if "min" in c:
                base += f", min={c.get('min')}, max={c.get('max')}, media={c.get('media')}"
            lines.append(base)

    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def compute_kpis(df, required, issues, seg_fields, key_col=None):
    n_rows = len(df) if len(df) > 0 else 1
    pct = lambda x: round(100.0 * x / n_rows, 2)

    by_type = defaultdict(int)
    for it in issues:
        by_type[it["tipo_error"]] += 1

    kpi_global = {
        "%_nulos_en_obligatorias": pct(sum(df[c].isna().sum() if c in df.columns else len(df) for c in required) / max(len(required), 1)),
        "%_filas_con_duplicado_clave": pct(len(df[df.duplicated(subset=[key_col] if key_col else None, keep=False)])) if key_col else 0.0,
        "%_emails_invalidos": pct(by_type["email_invalido"]),
        "%_telefonos_invalidos": pct(by_type["telefono_invalido"]),
        "%_paises_no_iso": pct(by_type["pais_no_iso"]),
    }

    seg = {}
    for field in (seg_fields or []):
        if field in df.columns:
            rows = []
            for val, gdf in df.groupby(field, dropna=False):
                total = len(gdf) if len(gdf) > 0 else 1
                p = lambda x: round(100.0 * x / total, 2)
                rows.append({
                    field: str(val),
                    "filas": len(gdf),
                    "%_nulos_en_obligatorias": p(sum(gdf[c].isna().sum() if c in gdf.columns else len(gdf) for c in required) / max(len(required), 1)),
                    "%_emails_invalidos": p(sum(1 for it in issues if it["tipo_error"]=="email_invalido" and it["fila"] in gdf.index)),
                    "%_telefonos_invalidos": p(sum(1 for it in issues if it["tipo_error"]=="telefono_invalido" and it["fila"] in gdf.index)),
                    "%_paises_no_iso": p(sum(1 for it in issues if it["tipo_error"]=="pais_no_iso" and it["fila"] in gdf.index)),
                })
            seg[field] = rows

    return {"global": kpi_global, "segmentado": seg}


# =========================
# Auditoría principal
# =========================
def run_audit(
    input_csv,
    outdir,
    schema_path=None,
    default_region="ES",
    strict=False,
    with_json=False,
):
    os.makedirs(outdir, exist_ok=True)
    df = pd.read_csv(input_csv)

    # Reglas base (v1)
    REQUIRED_COLS = ["cliente_id", "nombre", "email", "telefono", "pais", "fecha_alta", "ingreso_anual"]
    issues = []

    # Columnas obligatorias
    for col in REQUIRED_COLS:
        if col not in df.columns:
            issues.append({"fila": None, "columna": col, "tipo_error": "columna_faltante",
                           "detalle": f"Falta columna obligatoria '{col}'."})

    # Nulos/vacíos
    for col in REQUIRED_COLS:
        if col in df.columns:
            vacios = df[df[col].isna() | (df[col].astype(str).str.strip() == "")]
            for idx in vacios.index:
                issues.append({"fila": int(idx), "columna": col, "tipo_error": "valor_nulo_vacio",
                               "detalle": "Valor nulo o vacío en columna obligatoria."})

    # Duplicados por cliente_id
    if "cliente_id" in df.columns:
        mask = df.duplicated(subset=["cliente_id"], keep=False)
        for idx in df[mask].index:
            issues.append({"fila": int(idx), "columna": "cliente_id", "tipo_error": "duplicado",
                           "detalle": f"cliente_id duplicado: {df.loc[idx, 'cliente_id']}"})

    # Email formato
    if "email" in df.columns:
        for idx, v in df["email"].items():
            if not is_valid_email(v):
                issues.append({"fila": int(idx), "columna": "email", "tipo_error": "email_invalido",
                               "detalle": f"Email no válido: {v}"})

    # Teléfono (patrón laxo v1)
    PHONE_RE = re.compile(r"^[+0-9()\-.\s]{7,}$")
    if "telefono" in df.columns:
        for idx, v in df["telefono"].items():
            if v is None or str(v).strip() == "":
                continue
            if not PHONE_RE.match(str(v).strip()):
                issues.append({"fila": int(idx), "columna": "telefono", "tipo_error": "telefono_invalido",
                               "detalle": f"Teléfono no válido (patrón laxo v1): {v}"})

    # ingreso_anual >= 0 y numérico
    if "ingreso_anual" in df.columns:
        for idx, v in df["ingreso_anual"].items():
            if not is_number(v):
                issues.append({"fila": int(idx), "columna": "ingreso_anual", "tipo_error": "tipo_invalido",
                               "detalle": f"No convertible a número: {v}"})
            else:
                val = float(v)
                if np.isnan(val) or val < 0:
                    issues.append({"fila": int(idx), "columna": "ingreso_anual", "tipo_error": "valor_no_permitido",
                                   "detalle": f"Ingreso anual < 0 o NaN: {v}"})

    # fecha_alta ISO (YYYY-MM-DD)
    if "fecha_alta" in df.columns:
        for idx, v in df["fecha_alta"].items():
            s = str(v).strip()
            if s == "" or pd.isna(v):
                continue
            try:
                datetime.strptime(s, "%Y-%m-%d")
            except Exception:
                issues.append({"fila": int(idx), "columna": "fecha_alta", "tipo_error": "formato_invalido",
                               "detalle": f"Esperado YYYY-MM-DD, recibido: {v}"})

    advanced = False
    perfil = None
    kpis = None

    # --- Si hay schema, activamos v2 (best-effort sin romper si faltan libs) ---
    if schema_path:
        advanced = True
        try:
            with open(schema_path, "r", encoding="utf-8") as f:
                schema = json.load(f)
        except Exception as e:
            # Si el schema no carga, seguimos en modo v1 sin romper
            schema = {}
            advanced = False

        if advanced:
            required = schema.get("required", REQUIRED_COLS)
            uniques = schema.get("unique", ["cliente_id"])
            types = schema.get("types", {})
            email_field = schema.get("email_field", "email")
            phone_field = schema.get("phone_field", "telefono")
            country_field = schema.get("country_field", "pais")
            seg_fields = schema.get("kpi_segments", ["pais"])

            # Unicidad (desde schema)
            for col in uniques:
                if col in df.columns:
                    mask = df.duplicated(subset=[col], keep=False)
                    for idx in df[mask].index:
                        issues.append({"fila": int(idx), "columna": col, "tipo_error": "duplicado",
                                       "detalle": f"Valor duplicado en clave '{col}': {df.loc[idx, col]}"})

            # Tipos y fechas (si strict)
            if strict:
                for col, t in types.items():
                    if col not in df.columns:
                        continue
                    if t.startswith("date:"):
                        fmt = t.split(":", 1)[1]
                        for idx, v in df[col].items():
                            if v is None or str(v).strip() == "":
                                continue
                            if not parse_date(v, fmt):
                                issues.append({"fila": int(idx), "columna": col, "tipo_error": "fecha_formato_invalido",
                                               "detalle": f"Esperado {fmt}, recibido: {v}"})
                    elif t.startswith("number"):
                        thr = None
                        if ">=" in t:
                            try:
                                thr = float(t.split(">=")[1])
                            except Exception:
                                thr = None
                        for idx, v in df[col].items():
                            if not is_number(v):
                                issues.append({"fila": int(idx), "columna": col, "tipo_error": "tipo_invalido",
                                               "detalle": f"No convertible a número: {v}"})
                            else:
                                val = float(v)
                                if thr is not None and val < thr:
                                    issues.append({"fila": int(idx), "columna": col, "tipo_error": "valor_no_permitido",
                                                   "detalle": f"Valor {val} < {thr}"})

            # Email (reutiliza v1)
            if email_field in df.columns:
                for idx, v in df[email_field].items():
                    if not is_valid_email(v):
                        issues.append({"fila": int(idx), "columna": email_field, "tipo_error": "email_invalido",
                                       "detalle": f"Email no válido: {v}"})

            # País ISO-3166 (si pycountry)
            if country_field in df.columns:
                for idx, v in df[country_field].items():
                    if v is None or str(v).strip() == "":
                        continue
                    if not is_valid_iso_country(v):
                        issues.append({"fila": int(idx), "columna": country_field, "tipo_error": "pais_no_iso",
                                       "detalle": f"Código país no ISO-3166 alpha-2: {v}"})

            # Teléfono E.164 (si phonenumbers)
            if phone_field in df.columns:
                norm_col = f"{phone_field}_e164"
                norm_vals = []
                for idx, v in df[phone_field].items():
                    e164, err = normalize_e164(v, default_region=default_region)
                    if err:
                        issues.append({"fila": int(idx), "columna": phone_field, "tipo_error": err,
                                       "detalle": f"No válido o no normalizable: {v}"})
                    norm_vals.append(e164)
                if phonenumbers is not None:
                    df[norm_col] = norm_vals  # solo añade la columna si se pudo intentar normalizar

            # Perfil y KPIs
            perfil = profile_df(df)
            kpis = compute_kpis(df, required, issues, seg_fields, key_col=uniques[0] if uniques else None)

    # --- Exportaciones (compatibilidad v1 por defecto) ---
    issues_path = os.path.join(outdir, "issues_detectados.csv")
    pd.DataFrame(issues, columns=["fila", "columna", "tipo_error", "detalle"]).to_csv(
        issues_path, index=False, encoding="utf-8"
    )

    report_path = os.path.join(outdir, "reporte_auditoria.md")
    write_report(df, issues, perfil, kpis, report_path, advanced=bool(schema_path))

    # Solo si el usuario quiere JSON/KPIs explícitamente (para no romper v1)
    if schema_path and with_json:
        with open(os.path.join(outdir, "perfil_columnas.json"), "w", encoding="utf-8") as f:
            json.dump(perfil or {}, f, ensure_ascii=False, indent=2)
        kpi_rows = [{"nivel": "global", **(kpis or {}).get("global", {})}]
        for field, rows in (kpis or {}).get("segmentado", {}).items():
            for r in rows:
                kpi_rows.append({"nivel": field, **r})
        pd.DataFrame(kpi_rows).to_csv(os.path.join(outdir, "kpi_calidad.csv"), index=False, encoding="utf-8")

    print(f"[OK] Issues: {issues_path}")
    print(f"[OK] Reporte: {report_path}")
    if schema_path and with_json:
        print(f"[OK] Perfil: {os.path.join(outdir, 'perfil_columnas.json')}")
        print(f"[OK] KPIs: {os.path.join(outdir, 'kpi_calidad.csv')}")


def main():
    p = argparse.ArgumentParser(description="Auditoría de datos de clientes (unificado v1/v2).")
    p.add_argument("--input", required=True, help="Ruta al CSV de entrada.")
    p.add_argument("--outdir", required=True, help="Carpeta de salida.")
    p.add_argument("--schema", help="Ruta a schema JSON para activar modo avanzado (v2).")
    p.add_argument("--default-region", default="ES", help="Región por defecto para E.164 (ISO-3166 alpha-2).")
    p.add_argument("--strict", action="store_true", help="Validación estricta de tipos/fechas (v2).")
    p.add_argument("--with-json", action="store_true", help="Exportar perfil_columnas.json y kpi_calidad.csv (v2).")
    args = p.parse_args()

    run_audit(
        input_csv=args.input,
        outdir=args.outdir,
        schema_path=args.schema,
        default_region=args.default_region,
        strict=args.strict,
        with_json=args.with_json,
    )


if __name__ == "__main__":
    main()
