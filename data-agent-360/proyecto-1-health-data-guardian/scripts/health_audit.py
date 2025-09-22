# -*- coding: utf-8 -*-
"""
Health Data Guardian – CLI (V1).
Audita un CSV clínico y genera informe + dataset limpio.
"""

import argparse, os, sys, pandas as pd
from audit_core import audit_dataframe, clean_dataframe, write_outputs


def main():
    parser = argparse.ArgumentParser(description="Auditoría de datos clínicos (V1 CLI)")
    parser.add_argument("--input", required=True, help="Ruta al CSV de entrada")
    parser.add_argument("--outdir", required=True, help="Carpeta de salida para resultados")
    args = parser.parse_args()

    # Validar input
    if not os.path.exists(args.input):
        sys.exit(f"❌ No se encontró el archivo de entrada: {args.input}")

    try:
        df = pd.read_csv(args.input)
    except Exception as e:
        sys.exit(f"❌ Error al leer el CSV: {e}")

    try:
        profile, issues = audit_dataframe(df)
        df_clean = clean_dataframe(df)
        write_outputs(args.outdir, profile, issues, df_clean)
        print(f"✅ Auditoría completada. Resultados en {args.outdir}")
    except Exception as e:
        sys.exit(f"❌ Error en la auditoría: {e}")


if __name__ == "__main__":
    main()
