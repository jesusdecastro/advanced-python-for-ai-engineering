"""
SOLUCIÓN COMPLETA - Ejercicio 3: Log Processor

Este archivo contiene las soluciones completas para el ejercicio 3.
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


@pytest.mark.parametrize(
    "line, expected",
    [
        ('{"level": "INFO", "msg": "test"}', {"level": "INFO", "msg": "test"}),
        ("", None),
        ("not json", None),
        ("   ", None),
        ("{invalid json}", None),
    ],
)
def test_parse_log_line(line, expected):
    """Parse log line with various inputs."""
    assert parse_log_line(line) == expected


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
    result = filter_by_severity(sample_log_entries, "WARNING")
    assert len(result) == 3  # WARNING, ERROR, CRITICAL


def test_filter_by_severity_debug(sample_log_entries):
    """Filter with DEBUG should return all entries."""
    result = filter_by_severity(sample_log_entries, "DEBUG")
    assert len(result) == 5


def test_filter_by_severity_critical(sample_log_entries):
    """Filter with CRITICAL should return only critical."""
    result = filter_by_severity(sample_log_entries, "CRITICAL")
    assert len(result) == 1


def test_filter_by_severity_error(sample_log_entries):
    """Filter with ERROR should return ERROR and CRITICAL."""
    result = filter_by_severity(sample_log_entries, "ERROR")
    assert len(result) == 2


def test_extract_fields_existing():
    """Extract existing fields from entries."""
    entries = [
        {"name": "Alice", "age": 30, "city": "Madrid"},
        {"name": "Bob", "age": 25, "city": "Barcelona"},
    ]
    result = extract_fields(entries, ["name", "age"])
    assert len(result) == 2
    assert result[0] == {"name": "Alice", "age": 30}
    assert "city" not in result[0]


def test_extract_fields_missing():
    """Missing fields should be filled with empty string."""
    entries = [{"name": "Alice"}, {"name": "Bob", "age": 25}]
    result = extract_fields(entries, ["name", "age"])
    assert result[0] == {"name": "Alice", "age": ""}
    assert result[1] == {"name": "Bob", "age": 25}


def test_extract_fields_empty_list():
    """Empty entries list should return empty list."""
    result = extract_fields([], ["name", "age"])
    assert result == []


# ============================================================================
# PARTE B: Functional tests con tmp_path
# ============================================================================


def test_process_logs_happy_path(tmp_path):
    """Process JSONL logs to CSV with normal data."""
    # ARRANGE
    log_file = tmp_path / "app.jsonl"
    lines = [
        '{"timestamp": "2024-01-15T10:30:00", "severity": "INFO", "message": "Started"}',
        '{"timestamp": "2024-01-15T10:31:00", "severity": "ERROR", "message": "DB down"}',
        '{"timestamp": "2024-01-15T10:32:00", "severity": "WARNING", "message": "Slow"}',
    ]
    log_file.write_text("\n".join(lines) + "\n")
    
    output_file = tmp_path / "output.csv"
    
    # ACT
    stats = process_logs(str(log_file), str(output_file), min_severity="WARNING")
    
    # ASSERT
    assert stats["filtered"] == 2  # ERROR + WARNING
    assert stats["total_lines"] == 3
    assert stats["skipped_lines"] == 0
    assert output_file.exists()
    
    # Verify CSV content
    with open(output_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert len(rows) == 2


def test_process_logs_empty_file(tmp_path):
    """Empty JSONL file should produce empty CSV."""
    log_file = tmp_path / "empty.jsonl"
    log_file.write_text("")
    
    output_file = tmp_path / "output.csv"
    stats = process_logs(str(log_file), str(output_file))
    
    assert stats["total_lines"] == 0
    assert stats["filtered"] == 0
    assert output_file.exists()


def test_process_logs_with_bad_lines(tmp_path):
    """JSONL with invalid lines should skip them."""
    log_file = tmp_path / "mixed.jsonl"
    lines = [
        '{"timestamp": "2024-01-15T10:30:00", "severity": "ERROR", "message": "Valid"}',
        "this is not json",
        "",
        '{"timestamp": "2024-01-15T10:31:00", "severity": "WARNING", "message": "Also valid"}',
    ]
    log_file.write_text("\n".join(lines) + "\n")
    
    output_file = tmp_path / "output.csv"
    stats = process_logs(str(log_file), str(output_file), min_severity="WARNING")
    
    assert stats["skipped_lines"] == 2
    assert stats["parsed"] == 2
    assert stats["filtered"] == 2


def test_process_logs_file_not_found(tmp_path):
    """Raise FileNotFoundError if input file doesn't exist."""
    output_file = tmp_path / "output.csv"
    
    with pytest.raises(FileNotFoundError, match="Log file not found"):
        process_logs("nonexistent.jsonl", str(output_file))


def test_process_logs_unicode(tmp_path):
    """Logs with Unicode characters should be preserved."""
    log_file = tmp_path / "unicode.jsonl"
    lines = [
        '{"timestamp": "2024-01-15T10:30:00", "severity": "ERROR", "message": "Error en función"}',
        '{"timestamp": "2024-01-15T10:31:00", "severity": "WARNING", "message": "Zürich"}',
    ]
    log_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    
    output_file = tmp_path / "output.csv"
    process_logs(str(log_file), str(output_file), min_severity="WARNING")
    
    # Verify Unicode is preserved
    with open(output_file, encoding="utf-8") as f:
        content = f.read()
    assert "función" in content
    assert "Zürich" in content


def test_process_logs_custom_fields(tmp_path):
    """Process logs with custom field selection."""
    log_file = tmp_path / "app.jsonl"
    lines = [
        '{"timestamp": "2024-01-15T10:30:00", "severity": "ERROR", "message": "Error", "extra": "data"}',
    ]
    log_file.write_text("\n".join(lines) + "\n")
    
    output_file = tmp_path / "output.csv"
    stats = process_logs(
        str(log_file), str(output_file), min_severity="ERROR", fields=["severity", "message"]
    )
    
    # Verify only selected fields in CSV
    with open(output_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert set(rows[0].keys()) == {"severity", "message"}


# ============================================================================
# BONUS: Fixture reutilizable
# ============================================================================


@pytest.fixture
def sample_logs_file(tmp_path):
    """Generate sample JSONL file."""
    log_file = tmp_path / "sample.jsonl"
    lines = [
        '{"timestamp": "2024-01-15T10:30:00", "severity": "INFO", "message": "Started"}',
        '{"timestamp": "2024-01-15T10:31:00", "severity": "ERROR", "message": "Failed"}',
        '{"timestamp": "2024-01-15T10:32:00", "severity": "WARNING", "message": "Slow"}',
    ]
    log_file.write_text("\n".join(lines) + "\n")
    return log_file


def test_with_fixture(sample_logs_file, tmp_path):
    """Test using the reusable fixture."""
    output_file = tmp_path / "output.csv"
    stats = process_logs(str(sample_logs_file), str(output_file), min_severity="WARNING")
    assert stats["filtered"] == 2
