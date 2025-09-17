# -*- coding: utf-8 -*-
"""
scripts/generar_padron_realista.py

Genera un padrón municipal realista con ~250 filas y errores intencionados.
Salida principal: data_sample/municipal_padron.xlsx
Plan B (si falla Excel): data_sample/municipal_padron.csv

Incluye:
- DNIs válidos/ inválidos/ nulos
- CP coherente / incoherente con provincia
- Municipios fuera de provincia
- Fechas imposibles y altas/bajas incoherentes
- Duplicados por DNI y por (Nombre+Apellidos+Fecha_Nacimiento)
- Campos nulos (nacionalidad, domicilio)
"""

import re
import random
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

# ----------------- Configuración -----------------
random.seed(13)
np.random.seed(13)

DATA_DIR = Path("data_sample")
DATA_DIR.mkdir(parents=True, exist_ok=True)
XLSX_PATH = DATA_DIR / "municipal_padron.xlsx"
CSV_FALLBACK = DATA_DIR / "municipal_padron.csv"

# Provincias y prefijos CP (simplificado, suficiente para demo)
CP_PROV_PREFIX = {
    "08": "Barcelona",
    "28": "Madrid",
    "29": "Málaga",
    "41": "Sevilla",
    "46": "Valencia",
    "48": "Bizkaia",
    "50": "Zaragoza",
}
MUNICIPIOS = {
    "Madrid": ["Madrid", "Alcalá de Henares", "Móstoles", "Fuenlabrada", "Leganés"],
    "Barcelona": ["Barcelona", "Hospitalet de Llobregat", "Badalona", "Terrassa", "Sabadell"],
    "Valencia": ["València", "Gandia", "Paterna", "Torrent", "Sagunt"],
    "Sevilla": ["Sevilla", "Dos Hermanas", "Alcalá de Guadaíra", "Utrera", "Mairena del Aljarafe"],
    "Zaragoza": ["Zaragoza", "Calatayud", "Ejea de los Caballeros", "Utebo", "Cuarte de Huerva"],
    "Málaga": ["Málaga", "Marbella", "Mijas", "Vélez-Málaga", "Estepona"],
    "Bizkaia": ["Bilbao", "Barakaldo", "Getxo", "Portugalete", "Basauri"],
}
NOMBRES = ["Juan","María","Lucía","Pablo","Ana","Marta","Carlos","Elena","Javier","Sofía","Miguel","Laura","Raúl","Beatriz","Alberto","Carmen","Diego","Sara","Víctor"]
APELLIDOS = ["García","Fernández","González","López","Martínez","Sánchez","Pérez","Gómez","Jiménez","Ruiz","Hernández","Díaz","Moreno","Muñoz","Álvarez"]
NACIONALIDADES = ["España","Marruecos","Rumanía","Colombia","Venezuela","Italia","China"]
DOMICILIOS = ["C/ Mayor","Av. Libertad","Pza. España","C/ Real","Av. Andalucía","C/ Sol","C/ Luna"]

# ----------------- Utilidades -----------------
def rand_date(start: datetime, end: datetime) -> datetime:
    delta = (end - start).days
    return start + timedelta(days=int(np.random.randint(0, max(1, delta))))

def dni_checksum(num8: int) -> str:
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[num8 % 23]

def make_valid_dni() -> str:
    n = np.random.randint(10_000_000, 99_999_999)
    return f"{n}{dni_checksum(n)}"

def make_invalid_dni() -> str:
    if np.random.rand() < 0.5:
        n = np.random.randint(10_000_000, 99_999_999)
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        # letra incorrecta
        bad_letter = letras[(n % 23 + 1) % 23]
        return f"{n}{bad_letter}"
    # formato mal
    return f"{np.random.randint(1_000_000, 9_999_999)}X9"

def make_cp(prov_name: str) -> str:
    # 80% coherente, 20% incoherente
    if np.random.rand() < 0.8:
        pref = [k for k, v in CP_PROV_PREFIX.items() if v == prov_name][0]
    else:
        pref = np.random.choice(list(CP_PROV_PREFIX.keys()))
    return f"{pref}{np.random.randint(0, 1000):03d}"

# ----------------- Generación -----------------
def generar_padron(n_base: int = 240) -> pd.DataFrame:
    rows = []
    provs = list(CP_PROV_PREFIX.values())
    start_birth = datetime(1915, 1, 1)
    end_birth = datetime(2024, 1, 1)
    start_alta = datetime(1996, 1, 1)
    end_alta = datetime(2025, 9, 1)

    for i in range(n_base):
        prov = np.random.choice(provs)
        muni = np.random.choice(MUNICIPIOS[prov])
        nombre = np.random.choice(NOMBRES)
        ap1, ap2 = np.random.choice(APELLIDOS, size=2, replace=True)
        nacionalidad = np.random.choice(NACIONALIDADES + [None])

        sexo = np.random.choice(["M","F","X"], p=[0.48,0.48,0.04])  # algunos 'X' inválidos
        domicilio = f"{np.random.choice(DOMICILIOS)} {np.random.randint(1, 200)}" if np.random.rand() > 0.05 else None
        cp = make_cp(prov)
        dni = make_valid_dni() if np.random.rand() < 0.85 else (None if np.random.rand() < 0.4 else make_invalid_dni())

        # Fechas
        f_nac = rand_date(start_birth, end_birth)
        if np.random.rand() < 0.03:   # imposible futuro
            f_nac = datetime(2050, 1, 1)
        if np.random.rand() < 0.02:   # edad extrema
            f_nac = datetime(1890, 1, 1)

        f_alta = rand_date(start_alta, end_alta)
        if np.random.rand() < 0.05:
            f_alta_str = f"  {f_alta.strftime('%Y-%m-%d')}  "  # con espacios
        else:
            f_alta_str = f_alta.strftime('%Y-%m-%d')

        if np.random.rand() < 0.22:
            # puede ser incoherente (baja antes de alta)
            f_baja = f_alta + timedelta(days=np.random.randint(-1200, 2000))
            estado = "Baja"
            f_baja_str = f_baja.strftime('%Y-%m-%d')
        else:
            estado = "Alta"
            f_baja_str = None

        # 4% municipio fuera de la provincia
        if np.random.rand() < 0.04:
            muni = "Municipio Desconocido"

        rows.append({
            "ID": 100000 + i,
            "Nombre": nombre,
            "Apellidos": f"{ap1} {ap2}",
            "DNI": dni,
            "Sexo": sexo,
            "Fecha_Nacimiento": f_nac.strftime("%Y-%m-%d"),
            "Nacionalidad": nacionalidad,
            "Domicilio": domicilio,
            "CP": cp,
            "Municipio": muni,
            "Provincia": prov,
            "Fecha_Alta_Padron": f_alta_str,
            "Fecha_Baja_Padron": f_baja_str,
            "Estado": estado,
            "Observaciones": None
        })

    df = pd.DataFrame(rows)

    # Duplicados: 10 por DNI + 10 por (Nombre,Apellidos,Fecha_Nacimiento)
    if (df["DNI"].notna()).sum() >= 20:
        dup_dni_idx = df[df["DNI"].notna()].sample(10, random_state=7).index
        df = pd.concat([df, df.loc[dup_dni_idx].assign(Domicilio="C/ Duplicada 1")], ignore_index=True)

    key_cols = ["Nombre","Apellidos","Fecha_Nacimiento"]
    dup_key_idx = df.sample(10, random_state=11).index
    df = pd.concat([df, df.loc[dup_key_idx].assign(Domicilio="C/ Duplicada 2")], ignore_index=True)

    return df

def guardar(df: pd.DataFrame) -> None:
    # Intenta Excel; si falla, CSV
    try:
        df.to_excel(XLSX_PATH, index=False)
        print(f"[OK] Generado: {XLSX_PATH}  | Filas: {len(df)}  | Columnas: {len(df.columns)}")
    except Exception as e:
        print(f"[WARN] No se pudo escribir Excel ({e}). Guardando CSV de respaldo…")
        df.to_csv(CSV_FALLBACK, index=False, encoding="utf-8")
        print(f"[OK] Generado: {CSV_FALLBACK}  | Filas: {len(df)}  | Columnas: {len(df.columns)}")

def main():
    df = generar_padron(n_base=240)
    # Validación mínima para evitar archivos vacíos
    assert not df.empty, "El DataFrame está vacío"
    assert set(["ID","Nombre","Apellidos","CP","Municipio","Provincia"]).issubset(df.columns), "Faltan columnas clave"
    # Guardar
    guardar(df)
    # Resumen rápido en consola
    print("\nVista rápida (5 filas):")
    print(df.head(5).to_string(index=False))
    print("\nRecuento por provincia:")
    print(df["Provincia"].value_counts())

if __name__ == "__main__":
    main()
