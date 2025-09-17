# audit_clientes.py
# ----------------------------------------------------------
# Auditoría de datos de clientes en Excel (versión final).
# - Perfil de calidad con:
#     * filas_totales
#     * duplicados_exactos (fila idéntica)
#     * duplicados_negocio (por clave cliente+email / cliente+ciudad / cliente)
#     * nulos_por_columna
# - Reglas explícitas en 'ventas': negativas, cero, outliers IQR (complementario)
# - Opción de guardar un informe Markdown en /results/
#
# Uso (Windows):
#   python scripts\audit_clientes.py data_sample\clientes.xlsx --reporte results\01_auditoria_clientes_result.md
#
# Autor: Txema Ríos (GitHub @txema741)
# ----------------------------------------------------------

import argparse
from pathlib import Path
import pandas as pd

# ---------- Carga y utilidades ----------

def cargar_excel(path_excel: str) -> pd.DataFrame:
    """Carga el Excel y normaliza columnas clave."""
    df = pd.read_excel(path_excel)
    df.columns = [c.strip().lower() for c in df.columns]  # normalizar nombres
    # Convertir 'ventas' a numérico por si llega como texto
    if "ventas" in df.columns:
        df["ventas"] = pd.to_numeric(df["ventas"], errors="coerce")
    return df

def detectar_duplicados_negocio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Busca duplicados por claves de negocio.
    Prioridad:
      1) cliente + email (si existen)
      2) cliente + ciudad (si no hay email)
      3) cliente (fallback)
    Devuelve un DataFrame con solo los registros duplicados y una columna
    'criterio_duplicado' indicando el criterio aplicado.
    """
    cols = set(df.columns)
    if {"cliente", "email"}.issubset(cols):
        subset = ["cliente", "email"]
        criterio = "cliente+email"
    elif {"cliente", "ciudad"}.issubset(cols):
        subset = ["cliente", "ciudad"]
        criterio = "cliente+ciudad"
    elif "cliente" in cols:
        subset = ["cliente"]
        criterio = "cliente"
    else:
        # Si no hay columnas típicas, no podemos evaluar duplicado de negocio
        # devolvemos DF vacío con las mismas columnas
        dups = df.iloc[0:0].copy()
        return dups

    dups = df[df.duplicated(subset=subset, keep=False)].copy()
    if not dups.empty:
        dups["criterio_duplicado"] = criterio
    return dups

def detectar_outliers_iqr(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
    Detecta valores atípicos usando IQR (InterQuartile Range).
    No sustituye reglas de negocio; es un complemento estadístico.
    """
    if columna not in df.columns:
        return df.iloc[0:0]
    serie = df[columna].dropna()
    if serie.empty:
        return df.iloc[0:0]
    Q1, Q3 = serie.quantile(0.25), serie.quantile(0.75)
    IQR = Q3 - Q1
    low, high = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
    mask = (df[columna] < low) | (df[columna] > high)
    return df[mask]

# ---------- Métricas y reporte ----------

def perfil_calidad(df: pd.DataFrame) -> dict:
    """
    Devuelve el perfil de calidad:
      - filas_totales
      - duplicados_exactos (fila idéntica)
      - duplicados_negocio (conteo de filas afectadas por el criterio)
      - nulos_por_columna (dict)
    """
    dup_exactos = int(df.duplicated().sum())
    dup_negocio_df = detectar_duplicados_negocio(df)
    dup_negocio_count = int(len(dup_negocio_df)) if not dup_negocio_df.empty else 0

    return {
        "filas_totales": int(len(df)),
        "duplicados_exactos": dup_exactos,
        "duplicados_negocio": dup_negocio_count,
        "nulos_por_columna": df.isna().sum().to_dict()
    }

def detectar_reglas_ventas(df: pd.DataFrame) -> dict:
    """Aplica reglas explícitas sobre 'ventas': negativas, cero, y outliers IQR."""
    if "ventas" not in df.columns:
        vacio = df.iloc[0:0]
        return {"negativas": vacio, "cero": vacio, "outliers_iqr": vacio}
    negativas = df[df["ventas"] < 0]
    cero = df[df["ventas"] == 0]
    outliers = detectar_outliers_iqr(df, "ventas")
    return {"negativas": negativas, "cero": cero, "outliers_iqr": outliers}

def generar_recomendaciones(dups: pd.DataFrame, reglas: dict) -> list:
    """Sugerencias de negocio/operación basadas en hallazgos."""
    rec = []
    if not dups.empty:
        rec.append("- Resolver **duplicados por clave de negocio** (unificar registros y consolidar ventas).")
    if not reglas["negativas"].empty:
        rec.append("- Revisar **ventas negativas**: pueden ser devoluciones mal registradas; validar con finanzas.")
    if not reglas["cero"].empty:
        rec.append("- Analizar **ventas a 0**: decidir si son registros de prueba o incompletos; limpiar o documentar.")
    if not reglas["outliers_iqr"].empty:
        rec.append("- Investigar **valores atípicos** (IQR): confirmar si son casos reales o errores de carga.")
    if not rec:
        rec.append("- Sin incidencias críticas detectadas; mantener controles y documentar políticas de calidad.")
    return rec

def imprimir_consola(perfil: dict, dups: pd.DataFrame, reglas: dict):
    """Salida legible en consola."""
    print("### PERFIL DE CALIDAD ###")
    print(f"- filas_totales: {perfil['filas_totales']}")
    print(f"- duplicados_exactos: {perfil['duplicados_exactos']}")
    print(f"- duplicados_negocio: {perfil['duplicados_negocio']}")
    print(f"- nulos_por_columna: {perfil['nulos_por_columna']}")

    print("\n### DUPLICADOS (por clave de negocio) ###")
    if dups.empty:
        print("No se detectaron duplicados según la clave de negocio.")
    else:
        print(dups)

    print("\n### REGLAS SOBRE 'ventas' ###")
    print("- Ventas negativas:")
    print(reglas["negativas"] if not reglas["negativas"].empty else "  (ninguna)")
    print("- Ventas a 0:")
    print(reglas["cero"] if not reglas["cero"].empty else "  (ninguna)")
    print("- Outliers IQR (complementario):")
    print(reglas["outliers_iqr"] if not reglas["outliers_iqr"].empty else "  (ninguno)")

def guardar_markdown(reporte_path: Path, perfil: dict, dups: pd.DataFrame, reglas: dict, excel_path: str):
    """Genera un informe Markdown reproducible para /results/."""
    reporte_path.parent.mkdir(parents=True, exist_ok=True)
    with open(reporte_path, "w", encoding="utf-8") as f:
        f.write(f"# Ejercicio 1 – Auditoría de clientes (DSP)\n\n")
        f.write(f"**Dataset:** `{excel_path}`\n\n")
        f.write("## Resultados del script\n")
        f.write(f"- Filas totales: {perfil['filas_totales']}\n")
        f.write(f"- Duplicados exactos: {perfil['duplicados_exactos']}\n")
        f.write(f"- Duplicados de negocio: {perfil['duplicados_negocio']}\n")
        f.write(f"- Nulos por columna: `{perfil['nulos_por_columna']}`\n\n")

        f.write("### Duplicados por clave de negocio\n")
        if dups.empty:
            f.write("- No se detectaron duplicados.\n\n")
        else:
            f.write(dups.to_markdown(index=False))
            f.write("\n\n")

        f.write("### Reglas sobre 'ventas'\n")
        f.write("**Ventas negativas:**\n\n")
        f.write((reglas["negativas"].to_markdown(index=False) + "\n\n") if not reglas["negativas"].empty else "- Ninguna\n\n")
        f.write("**Ventas a 0:**\n\n")
        f.write((reglas["cero"].to_markdown(index=False) + "\n\n") if not reglas["cero"].empty else "- Ninguna\n\n")
        f.write("**Outliers IQR:**\n\n")
        f.write((reglas["outliers_iqr"].to_markdown(index=False) + "\n\n") if not reglas["outliers_iqr"].empty else "- Ninguno\n\n")

        recomendaciones = generar_recomendaciones(dups, reglas)
        f.write("## Recomendaciones\n")
        for r in recomendaciones:
            f.write(f"{r}\n")

        f.write("\n## Validación\n- Nivel de confianza: Alta (Python + pandas)\n- Limitaciones: dataset de ejemplo; validar con datos reales\n")

# ---------- Main ----------

def main():
    parser = argparse.ArgumentParser(description="Auditoría de clientes (calidad de datos).")
    parser.add_argument("excel", help="Ruta al Excel de clientes (ej. data_sample\\clientes.xlsx)")
    parser.add_argument("--reporte", help="Ruta Markdown para guardar el informe (ej. results\\01_auditoria_clientes_result.md)")
    args = parser.parse_args()

    df = cargar_excel(args.excel)
    perfil = perfil_calidad(df)
    dups = detectar_duplicados_negocio(df)
    reglas = detectar_reglas_ventas(df)

    imprimir_consola(perfil, dups, reglas)

    if args.reporte:
        guardar_markdown(Path(args.reporte), perfil, dups, reglas, args.excel)
        print(f"\nInforme guardado en: {args.reporte}")

if __name__ == "__main__":
    main()
