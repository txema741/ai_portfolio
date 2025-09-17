# audit_riesgo_pais.py
# ----------------------------------------------------------
# Evaluación de Riesgo País (España) a partir de indicadores
# oficiales (Eurostat/OCDE/IMF) ya consolidados en un Excel.
#
# Entrada:
#   data_sample\riesgo_pais_spain_real.xlsx
# Salida:
#   results\02_riesgo_pais_result.md  (informe Markdown)
#
# Reglas de riesgo (umbrales por defecto, editables por CLI):
#   - deuda_publica_pct_pib      > 90        -> riesgo
#   - deuda_externa_pct_pib      > 100       -> riesgo (si N/D: no puntúa)
#   - balanza_comercial_musd     < 0         -> riesgo
#   - inflacion_anual_pct        > 5         -> riesgo
#   - crecimiento_pib_pct        < 0         -> riesgo
#
# Cálculo:
#   - Se evalúa año a año.
#   - Se asigna una puntuación (0..5) según cuántas reglas se activan.
#   - Se etiqueta riesgo: Bajo (0-1), Medio (2-3), Alto (4-5).
#
# Uso (Windows):
#   python scripts\audit_riesgo_pais.py ^
#       --excel data_sample\riesgo_pais_spain_real.xlsx ^
#       --reporte results\02_riesgo_pais_result.md
#
# Dependencias:
#   pip install pandas openpyxl tabulate
#
# Nota importante:
#   - Este script NO descarga datos. Usa el Excel que tú subas a data_sample.
#   - En el informe se deja una sección "Fuentes" para que indiques las URLs
#     oficiales (Eurostat/OCDE/IMF) correspondientes a tu fichero.
# ----------------------------------------------------------

import argparse
from pathlib import Path
import pandas as pd
import math

# ---------- Utilidades ----------

def nd(x):
    """Convierte NaN/None a 'N/D' para presentación."""
    if x is None:
        return "N/D"
    if isinstance(x, float) and (math.isnan(x) or x is None):
        return "N/D"
    if pd.isna(x):
        return "N/D"
    return x

def cargar_excel(ruta_excel: str) -> pd.DataFrame:
    """
    Carga el Excel con columnas esperadas:
      año, deuda_publica_pct_pib, deuda_externa_pct_pib,
      balanza_comercial_musd, inflacion_anual_pct, crecimiento_pib_pct
    """
    df = pd.read_excel(ruta_excel)
    # Normalizamos nombres de columnas a minúsculas sin espacios
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

def evaluar_reglas_row(row, umbrales):
    """
    Evalúa las reglas de riesgo para una fila (un año).
    Devuelve dict con flags (True/False) y número de reglas activadas.
    Si un valor está N/D (NaN), esa regla no suma puntos.
    """
    flags = {}

    # Helper para comparar con N/D seguro
    def gt(value, thr):
        return (value is not None) and (not pd.isna(value)) and (value > thr)
    def lt(value, thr):
        return (value is not None) and (not pd.isna(value)) and (value < thr)

    flags["deuda_publica_alta"] = gt(row.get("deuda_publica_pct_pib"), umbrales["deuda_publica_pct_pib"])
    # deuda externa puede ser N/D
    val_deuda_ext = row.get("deuda_externa_pct_pib")
    flags["deuda_externa_alta"] = gt(val_deuda_ext, umbrales["deuda_externa_pct_pib"]) if not pd.isna(val_deuda_ext) else False
    flags["deficit_comercial"]  = lt(row.get("balanza_comercial_musd"), 0)   # < 0 déficit
    flags["inflacion_alta"]     = gt(row.get("inflacion_anual_pct"), umbrales["inflacion_anual_pct"])
    flags["pib_negativo"]       = lt(row.get("crecimiento_pib_pct"), 0)

    score = sum(1 for v in flags.values() if v)
    if score <= 1:
        nivel = "Bajo"
    elif score <= 3:
        nivel = "Medio"
    else:
        nivel = "Alto"

    return flags, score, nivel

def perf_calidad(df: pd.DataFrame):
    """Perfil básico de calidad del dataset cargado."""
    return {
        "filas_totales": int(len(df)),
        "nulos_por_columna": df.isna().sum().to_dict()
    }

def generar_tabla_resumen(df_eval: pd.DataFrame) -> str:
    """
    Convierte un DataFrame a tabla Markdown.
    Requiere 'tabulate' vía pandas.to_markdown.
    """
    return df_eval.to_markdown(index=False)

def guardar_markdown(path_md: Path, perfil: dict, df_eval: pd.DataFrame, umbrales: dict, fuentes: list, excel_path: str):
    """Guarda un informe Markdown completo en /results/."""
    path_md.parent.mkdir(parents=True, exist_ok=True)
    with open(path_md, "w", encoding="utf-8") as f:
        f.write("# Ejercicio 2 – Evaluación de Riesgo País (España)\n\n")
        f.write(f"**Dataset:** `{excel_path}`\n\n")
        f.write("## Perfil de calidad del dataset\n")
        f.write(f"- Filas totales: {perfil['filas_totales']}\n")
        f.write(f"- Nulos por columna: `{perfil['nulos_por_columna']}`\n\n")

        f.write("## Umbrales de riesgo aplicados\n")
        f.write(f"- deuda_publica_pct_pib > {umbrales['deuda_publica_pct_pib']}\n")
        f.write(f"- deuda_externa_pct_pib > {umbrales['deuda_externa_pct_pib']} (si N/D, no puntúa)\n")
        f.write(f"- balanza_comercial_musd < 0 (déficit)\n")
        f.write(f"- inflacion_anual_pct > {umbrales['inflacion_anual_pct']}\n")
        f.write(f"- crecimiento_pib_pct < 0\n\n")

        f.write("## Resultado por año\n")
        f.write(generar_tabla_resumen(df_eval))
        f.write("\n\n")

        f.write("## Interpretación (ejemplo consultivo)\n")
        f.write("- *Bajo*: situación controlada; mantener vigilancia macro habitual.\n")
        f.write("- *Medio*: hay tensiones (p. ej., deuda/deflactor o déficit externo) → revisar liquidez y cobertura.\n")
        f.write("- *Alto*: multiplicidad de riesgos; activar planes de contingencia (hedging, diversificación de mercados/proveedores, seguros de crédito a la exportación).\n\n")

        f.write("## Fuentes (debes completar con tus URLs oficiales)\n")
        if fuentes:
            for src in fuentes:
                f.write(f"- {src}\n")
        else:
            f.write("- Eurostat (deuda pública, balanza comercial)\n")
            f.write("- OCDE (crecimiento PIB)\n")
            f.write("- IMF SDDS (deuda externa)\n")
        f.write("\n\n")

        f.write("## Validación\n")
        f.write("- Nivel de confianza: Alta (reglas reproducibles; datos de fuentes oficiales).\n")
        f.write("- Limitaciones: si algún valor es N/D, la regla asociada no puntúa; el análisis depende de la cobertura de la fuente.\n")

# ---------- Main CLI ----------

def main():
    parser = argparse.ArgumentParser(description="Evaluación de Riesgo País (España) a partir de indicadores oficiales.")
    parser.add_argument("--excel", required=True, help="Ruta al Excel consolidado (ej. data_sample\\riesgo_pais_spain_real.xlsx)")
    parser.add_argument("--reporte", required=True, help="Ruta de salida Markdown (ej. results\\02_riesgo_pais_result.md)")

    # Umbrales configurables por CLI
    parser.add_argument("--thr_deuda_publica", type=float, default=90.0)
    parser.add_argument("--thr_deuda_externa", type=float, default=100.0)
    parser.add_argument("--thr_inflacion", type=float, default=5.0)

    # Fuentes opcionales (puedes pasar varias con --fuente repetido)
    parser.add_argument("--fuente", action="append", default=[], help="URL o referencia de la fuente (puedes repetir la bandera)")

    args = parser.parse_args()

    # Configuración de umbrales
    umbrales = {
        "deuda_publica_pct_pib": args.thr_deuda_publica,
        "deuda_externa_pct_pib": args.thr_deuda_externa,
        "inflacion_anual_pct": args.thr_inflacion
    }

    # Cargar
    df = cargar_excel(args.excel)

    # Perfil de calidad
    perfil = perf_calidad(df)

    # Evaluación año a año
    registros = []
    cols = ["año", "deuda_publica_pct_pib", "deuda_externa_pct_pib", "balanza_comercial_musd", "inflacion_anual_pct", "crecimiento_pib_pct"]
    for _, row in df.iterrows():
        flags, score, nivel = evaluar_reglas_row(row, umbrales)

        registros.append({
            "año": nd(row.get("año")),
            "deuda_publica_pct_pib": nd(row.get("deuda_publica_pct_pib")),
            "deuda_externa_pct_pib": nd(row.get("deuda_externa_pct_pib")),
            "balanza_comercial_musd": nd(row.get("balanza_comercial_musd")),
            "inflacion_anual_pct": nd(row.get("inflacion_anual_pct")),
            "crecimiento_pib_pct": nd(row.get("crecimiento_pib_pct")),
            "flags_activas": ", ".join([k for k, v in flags.items() if v]) if any(flags.values()) else "-",
            "score_riesgo": score,
            "nivel_riesgo": nivel
        })

    df_eval = pd.DataFrame(registros)

    # Mostrar por consola y guardar informe
    print("### PERFIL DE CALIDAD ###")
    print(perfil)
    print("\n### RESULTADO POR AÑO ###")
    print(df_eval)

    guardar_markdown(Path(args.reporte), perfil, df_eval, umbrales, args.fuente, args.excel)
    print(f"\nInforme guardado en: {args.reporte}")

if __name__ == "__main__":
    main()
