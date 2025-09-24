# -*- coding: utf-8 -*-
"""
Tests de seguridad y validación para audit_clientes.py
Ejecutar con: pytest -v
"""

import sys
import os
import pytest
import pandas as pd

# 👇 Añadir la ruta raíz del proyecto al sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from scripts import audit_clientes as auditor


def test_valid_email_ok():
    assert auditor.valid_email("usuario@example.com")
    assert not auditor.valid_email("usuario@@example.com")
    assert not auditor.valid_email("malformado")


def test_valid_phone_ok():
    assert auditor.valid_phone("+34600111222")
    assert not auditor.valid_phone("12345")


def test_valid_country_ok():
    assert auditor.valid_country("ES")
    assert not auditor.valid_country("ZZ")


def test_valid_iso_date_ok():
    assert auditor.valid_iso_date("2024-01-01")
    assert not auditor.valid_iso_date("2024-02-30")  # fecha inválida


def test_is_future_date_ok():
    assert auditor.is_future_date("2999-01-01")
    assert not auditor.is_future_date("2000-01-01")


def test_secure_path_traversal(tmp_path):
    p = auditor.secure_path(str(tmp_path / "test.csv"))
    assert p.startswith(str(tmp_path))


def test_check_file_size(tmp_path):
    file_path = tmp_path / "small.csv"
    file_path.write_text("id_cliente,nombre\n1,Ana")
    auditor.check_file_size(str(file_path))  # no debe fallar

    big_file = tmp_path / "big.csv"
    with open(big_file, "wb") as f:
        f.write(b"x" * (6 * 1024 * 1024))  # 6 MB
    with pytest.raises(ValueError):
        auditor.check_file_size(str(big_file))


def test_audit_detects_issues():
    data = {
        "id_cliente": [1, 2],
        "nombre": ["Ana", "Luis"],
        "email": ["ana.perez@example.com", "bad-email"],
        "telefono": ["34600111222", "123"],
        "pais": ["ES", "ZZ"],
        "fecha_alta": ["2024-01-01", "2024-02-30"],
        "notas": ["ok", "error"]
    }
    df = pd.DataFrame(data)
    issues = auditor.audit(df)

    assert not issues.empty
    assert "email_invalido" in issues["issue"].values
    assert "telefono_invalido" in issues["issue"].values
    assert "pais_no_iso" in issues["issue"].values
    assert "fecha_formato_invalido" in issues["issue"].values
