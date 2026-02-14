"""
Validador de registros para un pipeline de datos de usuarios.

Ejercicio 2: Validador de Registros para Data Pipeline
=======================================================

Objetivo: Aplicar @pytest.mark.parametrize, fixtures y mocks.

Parte A - Funciones puras con parametrize (25 min):
- test_validate_email con @pytest.mark.parametrize — al menos 5 válidos + 5 inválidos
- test_validate_age con @pytest.mark.parametrize — incluye None, string, float, negativos
- test_validate_date_format — formatos correctos e incorrectos
- test_validate_record — registros válidos, con errores, vacío

Parte B - Funciones I/O con mocks (25 min):
- test_load_records_from_json con mock_open y patch
- test_validate_and_split — mock de load_records_from_json

Criterios de éxito:
- [ ] test_validate_email con parametrize (≥10 casos)
- [ ] test_validate_age con parametrize (≥8 casos)
- [ ] test_load_records_from_json con mocks
- [ ] Cobertura ≥ 95%
"""

import json
import re
from datetime import datetime
from pathlib import Path


def validate_email(email: str) -> bool:
    """
    Validate basic email format.
    
    :param email: Email address to validate
    :type email: str
    :return: True if valid format, False otherwise
    :rtype: bool
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_age(age: int | None) -> bool:
    """
    Validate that age is reasonable (0-120).
    
    :param age: Age value to validate
    :type age: int | None
    :return: True if valid, False otherwise
    :rtype: bool
    """
    if age is None:
        return False
    return isinstance(age, int) and 0 <= age <= 120


def validate_date_format(date_str: str, fmt: str = "%Y-%m-%d") -> bool:
    """
    Validate that a date string matches the expected format.
    
    :param date_str: Date string to validate
    :type date_str: str
    :param fmt: Expected date format
    :type fmt: str
    :return: True if valid format, False otherwise
    :rtype: bool
    """
    try:
        datetime.strptime(date_str, fmt)
        return True
    except (ValueError, TypeError):
        return False


def validate_record(record: dict) -> dict:
    """
    Validate a complete record and return result with errors.
    
    :param record: Record dictionary to validate
    :type record: dict
    :return: Dict with 'is_valid' (bool) and 'errors' (list[str])
    :rtype: dict
    """
    errors = []
    
    if "email" not in record or not validate_email(record.get("email", "")):
        errors.append("invalid_email")
    
    if not validate_age(record.get("age")):
        errors.append("invalid_age")
    
    if "created_at" in record and not validate_date_format(record["created_at"]):
        errors.append("invalid_date")
    
    return {"is_valid": len(errors) == 0, "errors": errors}


def load_records_from_json(filepath: str) -> list[dict]:
    """
    Load records from a JSON file.
    
    :param filepath: Path to JSON file
    :type filepath: str
    :return: List of record dictionaries
    :rtype: list[dict]
    :raises FileNotFoundError: If file doesn't exist
    :raises TypeError: If JSON is not an array
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    with open(path) as f:
        data = json.load(f)
    
    if not isinstance(data, list):
        raise TypeError("Expected a JSON array of records")
    
    return data


def validate_and_split(filepath: str) -> dict:
    """
    Load records, validate them, and split into valid/invalid.
    
    :param filepath: Path to JSON file with records
    :type filepath: str
    :return: Dict with 'valid', 'invalid', and 'summary'
    :rtype: dict
    """
    records = load_records_from_json(filepath)
    valid = []
    invalid = []
    
    for record in records:
        result = validate_record(record)
        if result["is_valid"]:
            valid.append(record)
        else:
            invalid.append({"record": record, "errors": result["errors"]})
    
    return {
        "valid": valid,
        "invalid": invalid,
        "summary": {
            "total": len(records),
            "valid_count": len(valid),
            "invalid_count": len(invalid),
        },
    }
