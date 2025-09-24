# scripts/validators.py
# -*- coding: utf-8 -*-
"""
Utilidades de validación para Auditoría v2.
Incluye: ISO-3166 (International Organization for Standardization – Organización Internacional de Normalización),
E.164 (E.164 Numbering Plan – Plan de Numeración E.164), email, tipos y fechas.
"""

import re
from datetime import datetime
from typing import Optional, Tuple

import phonenumbers  # normalización E.164
import pycountry     # validación ISO-3166

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def is_valid_iso_country(code: str) -> bool:
    if not code:
        return False
    code = str(code).strip().upper()
    try:
        return pycountry.countries.get(alpha_2=code) is not None
    except Exception:
        return False


def normalize_e164(phone_str: str, default_region: str = "ES") -> Tuple[Optional[str], Optional[str]]:
    """
    Intenta normalizar a E.164. Devuelve (e164, error).
    default_region: usada si el número no incluye prefijo internacional.
    """
    if phone_str is None or str(phone_str).strip() == "":
        return None, None
    try:
        parsed = phonenumbers.parse(str(phone_str), default_region)
        if not phonenumbers.is_valid_number(parsed):
            return None, "telefono_invalido"
        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164), None
    except Exception:
        return None, "telefono_invalido"


def is_valid_email(email: str) -> bool:
    if email is None or str(email).strip() == "":
        return True  # el nulo se controla fuera; aquí validamos formato si viene valor
    return EMAIL_RE.match(str(email).strip()) is not None


def parse_date(date_str: str, fmt: str) -> bool:
    try:
        datetime.strptime(str(date_str).strip(), fmt)
        return True
    except Exception:
        return False


def check_numeric(val) -> bool:
    try:
        float(val)
        return True
    except Exception:
        return False
