"""
Tests para record_validator.py

Ejercicio 2: Validador de Registros para Data Pipeline
=======================================================

Parte A - Funciones puras con parametrize (25 min)
Parte B - Funciones I/O con mocks (25 min)

Ejecutar:
    uv run pytest tests/test_record_validator.py -v
    uv run pytest tests/test_record_validator.py -v --cov=src --cov-report=term-missing
"""

import json
from unittest.mock import MagicMock, mock_open, patch

import pytest

from exercises.record_validator import (
    load_records_from_json,
    validate_age,
    validate_and_split,
    validate_date_format,
    validate_email,
    validate_record,
)


# ============================================================================
# PARTE A: Funciones puras con parametrize
# ============================================================================


# TODO: Implementa test_validate_email con @pytest.mark.parametrize
# Casos a cubrir (al menos 10):
# - Emails válidos: user@example.com, user.name@example.co.uk, user+tag@example.com
# - Emails inválidos: bad-email, @example.com, user@, "", user@domain (sin TLD)


# TODO: Implementa test_validate_age con @pytest.mark.parametrize
# Casos a cubrir (al menos 8):
# - Edades válidas: 0, 30, 120
# - Edades inválidas: None, -1, 121, "25" (string), 25.5 (float)


def test_validate_date_format_valid():
    """Valid date format should return True."""
    # TODO: Implementa este test
    pass


def test_validate_date_format_invalid():
    """Invalid date format should return False."""
    # TODO: Implementa este test
    pass


# TODO: Implementa test_validate_record
# Casos a cubrir:
# - Registro válido completo
# - Registro con email inválido
# - Registro con age inválido
# - Registro con fecha inválida
# - Registro con múltiples errores
# - Registro vacío {}


# ============================================================================
# PARTE B: Funciones I/O con mocks
# ============================================================================


def test_load_records_from_json_valid():
    """Load valid JSON array of records."""
    # TODO: Implementa este test usando mock_open y patch
    # Pista:
    # fake_json = json.dumps([{"name": "Alice"}])
    # with patch("builtins.open", mock_open(read_data=fake_json)):
    #     with patch("pathlib.Path.exists", return_value=True):
    #         records = load_records_from_json("fake.json")
    pass


def test_load_records_from_json_file_not_found():
    """Raise FileNotFoundError if file doesn't exist."""
    # TODO: Implementa este test
    # Pista: usa patch("pathlib.Path.exists", return_value=False)
    # y pytest.raises(FileNotFoundError)
    pass


def test_load_records_from_json_not_array():
    """Raise TypeError if JSON is not an array."""
    # TODO: Implementa este test
    # Pista: fake_json = json.dumps({"not": "array"})
    pass


@patch("exercises.record_validator.load_records_from_json")
def test_validate_and_split_mixed(mock_load):
    """Split records into valid and invalid."""
    # TODO: Implementa este test
    # Pista:
    # mock_load.return_value = [
    #     {"email": "alice@test.com", "age": 30},  # válido
    #     {"email": "bad", "age": -1},              # inválido
    # ]
    # result = validate_and_split("fake_path.json")
    # assert result["summary"]["valid_count"] == 1
    pass


# ============================================================================
# BONUS: Tests adicionales (opcional)
# ============================================================================

# Si terminas antes, añade tests para:
# - validate_date_format con diferentes formatos (fmt="%d/%m/%Y")
# - validate_record con campos opcionales
# - load_records_from_json con JSON malformado
