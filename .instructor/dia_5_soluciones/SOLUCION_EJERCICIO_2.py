"""
SOLUCIÓN COMPLETA - Ejercicio 2: Record Validator

Este archivo contiene las soluciones completas para el ejercicio 2.
"""

import json
from unittest.mock import mock_open, patch

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


@pytest.mark.parametrize(
    "email, expected",
    [
        # Válidos
        ("user@example.com", True),
        ("user.name@example.co.uk", True),
        ("user+tag@example.com", True),
        ("test_user@domain.org", True),
        ("a@b.co", True),
        # Inválidos
        ("bad-email", False),
        ("@example.com", False),
        ("user@", False),
        ("", False),
        ("user@domain", False),  # Sin TLD
        ("user domain@example.com", False),  # Espacio
    ],
)
def test_validate_email(email, expected):
    """Validate email format with various inputs."""
    assert validate_email(email) == expected


@pytest.mark.parametrize(
    "age, expected",
    [
        # Válidos
        (0, True),
        (30, True),
        (120, True),
        (1, True),
        (119, True),
        # Inválidos
        (None, False),
        (-1, False),
        (121, False),
        ("25", False),  # String
        (25.5, False),  # Float
    ],
)
def test_validate_age(age, expected):
    """Validate age with various inputs."""
    assert validate_age(age) == expected


def test_validate_date_format_valid():
    """Valid date format should return True."""
    assert validate_date_format("2024-01-15") is True
    assert validate_date_format("2023-12-31") is True


def test_validate_date_format_invalid():
    """Invalid date format should return False."""
    assert validate_date_format("15-01-2024") is False
    assert validate_date_format("2024/01/15") is False
    assert validate_date_format("not-a-date") is False
    assert validate_date_format("") is False


def test_validate_date_format_custom_format():
    """Validate with custom date format."""
    assert validate_date_format("15/01/2024", fmt="%d/%m/%Y") is True
    assert validate_date_format("2024-01-15", fmt="%d/%m/%Y") is False


def test_validate_record_valid():
    """Valid record should return is_valid=True."""
    record = {"email": "alice@test.com", "age": 30}
    result = validate_record(record)
    assert result["is_valid"] is True
    assert result["errors"] == []


def test_validate_record_invalid_email():
    """Record with invalid email should have error."""
    record = {"email": "bad-email", "age": 30}
    result = validate_record(record)
    assert result["is_valid"] is False
    assert "invalid_email" in result["errors"]


def test_validate_record_invalid_age():
    """Record with invalid age should have error."""
    record = {"email": "alice@test.com", "age": -5}
    result = validate_record(record)
    assert result["is_valid"] is False
    assert "invalid_age" in result["errors"]


def test_validate_record_invalid_date():
    """Record with invalid date should have error."""
    record = {"email": "alice@test.com", "age": 30, "created_at": "bad-date"}
    result = validate_record(record)
    assert result["is_valid"] is False
    assert "invalid_date" in result["errors"]


def test_validate_record_multiple_errors():
    """Record with multiple errors should list all."""
    record = {"email": "bad", "age": -1, "created_at": "bad-date"}
    result = validate_record(record)
    assert result["is_valid"] is False
    assert len(result["errors"]) == 3


def test_validate_record_empty():
    """Empty record should have errors."""
    record = {}
    result = validate_record(record)
    assert result["is_valid"] is False
    assert "invalid_email" in result["errors"]
    assert "invalid_age" in result["errors"]


# ============================================================================
# PARTE B: Funciones I/O con mocks
# ============================================================================


def test_load_records_from_json_valid():
    """Load valid JSON array of records."""
    fake_json = json.dumps([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}])
    
    with patch("builtins.open", mock_open(read_data=fake_json)):
        with patch("pathlib.Path.exists", return_value=True):
            records = load_records_from_json("fake.json")
    
    assert len(records) == 2
    assert records[0]["name"] == "Alice"


def test_load_records_from_json_file_not_found():
    """Raise FileNotFoundError if file doesn't exist."""
    with patch("pathlib.Path.exists", return_value=False):
        with pytest.raises(FileNotFoundError, match="File not found"):
            load_records_from_json("nonexistent.json")


def test_load_records_from_json_not_array():
    """Raise TypeError if JSON is not an array."""
    fake_json = json.dumps({"not": "array"})
    
    with patch("builtins.open", mock_open(read_data=fake_json)):
        with patch("pathlib.Path.exists", return_value=True):
            with pytest.raises(TypeError, match="Expected a JSON array"):
                load_records_from_json("fake.json")


@patch("exercises.record_validator.load_records_from_json")
def test_validate_and_split_mixed(mock_load):
    """Split records into valid and invalid."""
    mock_load.return_value = [
        {"email": "alice@test.com", "age": 30},  # válido
        {"email": "bad", "age": -1},  # inválido
        {"email": "carol@test.com", "age": 45},  # válido
    ]
    
    result = validate_and_split("fake_path.json")
    
    assert result["summary"]["total"] == 3
    assert result["summary"]["valid_count"] == 2
    assert result["summary"]["invalid_count"] == 1
    assert len(result["valid"]) == 2
    assert len(result["invalid"]) == 1


@patch("exercises.record_validator.load_records_from_json")
def test_validate_and_split_all_valid(mock_load):
    """All valid records."""
    mock_load.return_value = [
        {"email": "alice@test.com", "age": 30},
        {"email": "bob@test.com", "age": 25},
    ]
    
    result = validate_and_split("fake_path.json")
    
    assert result["summary"]["valid_count"] == 2
    assert result["summary"]["invalid_count"] == 0


@patch("exercises.record_validator.load_records_from_json")
def test_validate_and_split_all_invalid(mock_load):
    """All invalid records."""
    mock_load.return_value = [
        {"email": "bad", "age": -1},
        {"email": "also-bad", "age": 200},
    ]
    
    result = validate_and_split("fake_path.json")
    
    assert result["summary"]["valid_count"] == 0
    assert result["summary"]["invalid_count"] == 2
