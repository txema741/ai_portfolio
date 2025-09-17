# audit_alumnos.py
# -------------------------------------------------------
# Ejercicio 3 – Auditoría de registros educativos (nivel básico)
# Metodología: Draft-then-Revise (DtR)
#
# Qué hace este script:
#  1) Carga un Excel de alumnos (data_sample/alumnos.xlsx).
#  2) Fase "Draft": detecta problemas (nulos, notas fuera de [0,10], duplicados por id_alumno+asignatura).
#  3) Fase "Revise": propone y aplica correcciones simples:
#       - Rellenar nulos con 'N/D'
#       - Ajustar notas al rango [0,10]
#  4) Genera un informe Markdown en results/03_auditoria_alumnos_result.md.
#  5) (Opcional) Guarda un Excel corregido en data_sample/alumnos_corregido.xlsx.
#
# Dependencias:
#   pip install pandas openpyxl tabulate
#
# Uso en Windows (ejemplo):
#   python scripts\audit_alumnos.py data_sample\alumnos.xlsx --reporte results\03_auditoria_alumnos_result.md --excel_corregido data_sample\alumnos_corregido.xlsx
# -------------------------------------------------------

import pandas as pd
from pathlib import Path
import argparse

def cargar_datos(ruta_excel: str) -> pd.DataFrame:
    """
    Carga el dataset de alumnos desde un archivo Excel.
    Retorna un DataFrame de pandas.
    """
    df = pd.read_excel(ruta_excel)
    # Normalizamos los nombres de columnas por si tienen espacios extras
    df.columns = [c.strip() for c in df.columns]
    return df

def diagnostico(df: pd.DataFrame) -> dict:
    """
    Fase Draft: detecta problemas típicos de calidad de datos.
    - Filas con nulos.
    - Notas fuera de rango [0,10].
    - Duplicados por (id_alumno, asignatura).
    Retorna un diccionario con DataFrames filtrados por cada problema.
    """
    problemas = {}
    problemas["nulos"] = df[df.isna().any(axis=1)]
    problemas["notas_fuera_rango"] = df[(df["nota"] < 0) | (df["nota"] > 10)]
    problemas["duplicados"] = df[df.duplicated(subset=["id_alumno", "asignatura"], keep=False)]
    return problemas

def revision(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fase Revise: aplica correcciones seguras y mínimas.
    - Rellenar nulos con 'N/D' (no disponible).
    - Convertir 'nota' a numérico si es posible; si no, 'N/D'.
    - Limitar notas al rango [0,10].
    Retorna un DataFrame corregido.
    """
    dfc = df.copy()
    # 1) Nulos -> 'N/D'
    dfc = dfc.fillna("N/D")

    # 2) Función para corregir notas de forma robusta
    def fix_nota(x):
        try:
            v = float(x)
        except:
            # Si no se puede convertir a número, devolvemos 'N/D'
            return "N/D"
        # Forzamos a rango 0..10
        if v < 0:
            return 0.0
        if v > 10:
            return 10.0
        return v

    dfc["nota"] = dfc["nota"].apply(fix_nota)
    return dfc

def guardar_markdown(path_md: Path, problemas: dict, df_corregido: pd.DataFrame,
                     ruta_excel_original: str, ruta_excel_corregido: str | None):
    """
    Crea un informe Markdown con:
    - Diagnóstico (tablas de nulos, notas fuera de rango, duplicados).
    - Tabla completa corregida.
    - Recomendaciones consultivas y nota de validación.
    """
    path_md.parent.mkdir(parents=True, exist_ok=True)  # asegúranos de que existe /results/
    with open(path_md, "w", encoding="utf-8") as f:
        f.write("# Ejercicio 3 – Auditoría de registros educativos (Draft-then-Revise)\n\n")
        f.write(f"**Dataset original:** `{ruta_excel_original}`\n")
        if ruta_excel_corregido:
            f.write(f"\n**Dataset corregido:** `{ruta_excel_corregido}`\n")
        f.write("\n\n## Diagnóstico inicial (Draft)\n")

        # Bloques de problemas
        for nombre, dfp in problemas.items():
            f.write(f"### {nombre}\n")
            if dfp.empty:
                f.write("- Sin incidencias detectadas.\n\n")
            else:
                f.write(dfp.to_markdown(index=False))
                f.write("\n\n")

        # Tabla final corregida
        f.write("## Revisión con correcciones propuestas (Revise)\n")
        f.write(df_corregido.to_markdown(index=False))
        f.write("\n\n")

        # Recomendaciones de uso real (consultoría/docencia)
        f.write("## Recomendaciones consultivas\n")
        f.write("- Completar correos electrónicos faltantes para garantizar comunicación.\n")
        f.write("- Validar criterios de evaluación para evitar notas fuera de rango.\n")
        f.write("- Analizar duplicados por (id_alumno, asignatura) y consolidar actas si procede.\n")

        f.write("\n## Validación\n")
        f.write("- Nivel de confianza: Alta (reglas deterministas y reproducibles).\n")
        f.write("- Limitaciones: el valor 'N/D' es temporal, requiere validación institucional.\n")

def main():
    # CLI: definimos argumentos de entrada/salida
    parser = argparse.ArgumentParser(description="Ejercicio 3 – Auditoría de registros educativos (DtR).")
    parser.add_argument("excel", help="Ruta al Excel original (ej. data_sample\\alumnos.xlsx)")
    parser.add_argument("--reporte", required=True, help="Ruta al informe Markdown (ej. results\\03_auditoria_alumnos_result.md)")
    parser.add_argument("--excel_corregido", help="Ruta para guardar el Excel corregido (ej. data_sample\\alumnos_corregido.xlsx)")
    args = parser.parse_args()

    # 1) Cargar
    df = cargar_datos(args.excel)

    # 2) Diagnóstico (Draft)
    problemas = diagnostico(df)

    # 3) Corrección (Revise)
    df_corregido = revision(df)

    # 4) Guardar Excel corregido, si se solicitó
    if args.excel_corregido:
        Path(args.excel_corregido).parent.mkdir(parents=True, exist_ok=True)
        df_corregido.to_excel(args.excel_corregido, index=False)

    # 5) Guardar informe Markdown
    guardar_markdown(Path(args.reporte), problemas, df_corregido, args.excel, args.excel_corregido)

    # Mensajes en consola
    print(f"Informe guardado en: {args.reporte}")
    if args.excel_corregido:
        print(f"Excel corregido guardado en: {args.excel_corregido}")

if __name__ == "__main__":
    main()
