"""
Tests para log_processor.py

Ejercicio 3: Log Processor para Observabilidad
===============================================

Parte A - Unit tests (15 min)
Parte B - Functional tests con tmp_path (30 min)

Ejecutar:
    uv run pytest tests/test_log_processor.py -v
    uv run pytest tests/test_log_processor.py -v --cov=src --cov-report=term-missing
"""

import csv
import json

import pytest

from exercises.log_processor import (
    extract_fields,
    filter_by_severity,
    parse_log_line,
    process_logs,
)


# ============================================================================
# PARTE A: Unit tests de funciones puras
# ============================================================================


# TODO: Implementa test_parse_log_line con @pytest.mark.parametrize
# Casos a cubrir:
# - Línea JSON válida → dict
# - Línea vacía → None
# - Texto plano (no JSON) → None
# - Solo espacios → None


@pytest.fixture
def sample_log_entries():
    """Sample log entries for testing."""
    return [
        {"timestamp": "2024-01-15T10:30:00", "severity": "DEBUG", "message": "Debug msg"},
        {"timestamp": "2024-01-15T10:31:00", "severity": "INFO", "message": "Info msg"},
        {"timestamp": "2024-01-15T10:32:00", "severity": "WARNING", "message": "Warning msg"},
        {"timestamp": "2024-01-15T10:33:00", "severity": "ERROR", "message": "Error msg"},
        {"timestamp": "2024-01-15T10:34:00", "severity": "CRITICAL", "message": "Critical msg"},
    ]


def test_filter_by_severity_warning(sample_log_entries):
    """Filter entries with severity >= WARNING."""
    # TODO: Implementa este test
    # Pista: result = filter_by_severity(sample_log_entries, "WARNING")
    # Debería devolver 3 entradas (WARNING, ERROR, CRITICAL)
    pass


# TODO: Añade más tests para filter_by_severity
# Casos a cubrir:
# - min_severity="DEBUG" (todas las entradas)
# - min_severity="CRITICAL" (solo 1 entrada)
# - min_severity="ERROR" (2 entradas)


def test_extract_fields_existing():
    """Extract existing fields from entries."""
    # TODO: Implementa este test
    pass


def test_extract_fields_missing():
    """Missing fields should be filled with empty string."""
    # TODO: Implementa este test
    pass


# ============================================================================
# PARTE B: Functional tests con tmp_path
# ============================================================================


def test_process_logs_happy_path(tmp_path):
    """Process JSONL logs to CSV with normal data."""
    # ARRANGE: crear fichero JSONL real
    log_file = tmp_path / "app.jsonl"
    lines = [
        '{"timestamp": "2024-01-15T10:30:00", "severity": "INFO", "message": "Started"}',
        '{"timestamp": "2024-01-15T10:31:00", "severity": "ERROR", "message": "DB down"}',
        '{"timestamp": "2024-01-15T10:32:00", "severity": "WARNING", "message": "Slow"}',
    ]
    log_file.write_text("\n".join(lines) + "\n")
    
    output_file = tmp_path / "output.csv"
    
    # ACT
    # TODO: Llama a process_logs con min_severity="WARNING"
    
    # ASSERT
    # TODO: Verifica:
    # - stats["filtered"] == 2 (ERROR + WARNING)
    # - output_file.exists()
    # - El CSV tiene 2 filas de datos (sin contar header)
    pass


def test_process_logs_empty_file(tmp_path):
    """Empty JSONL file should produce empty CSV."""
    # TODO: Implementa este test
    # Pista: crear fichero vacío con log_file.write_text("")
    pass


def test_process_logs_with_bad_lines(tmp_path):
    """JSONL with invalid lines should skip them."""
    # TODO: Implementa este test
    # Pista: mezcla líneas válidas con líneas corruptas
    # Verifica que stats["skipped_lines"] > 0
    pass


def test_process_logs_file_not_found(tmp_path):
    """Raise FileNotFoundError if input file doesn't exist."""
    # TODO: Implementa este test
    # Pista: usa pytest.raises(FileNotFoundError)
    pass


def test_process_logs_unicode(tmp_path):
    """Logs with Unicode characters should be preserved."""
    # TODO: Implementa este test
    # Pista: crea logs con mensajes como "Error en función", "Zürich"
    # Verifica que el CSV preserva los caracteres Unicode
    pass


# ============================================================================
# BONUS: Fixture reutilizable (opcional)
# ============================================================================

# Si terminas antes, crea una fixture que genere un fichero JSONL
# de ejemplo y sea reutilizable en múltiples tests:
#
# @pytest.fixture
# def sample_logs_file(tmp_path):
#     """Generate sample JSONL file."""
#     log_file = tmp_path / "app.jsonl"
#     lines = [...]
#     log_file.write_text("\n".join(lines) + "\n")
#     return log_file
