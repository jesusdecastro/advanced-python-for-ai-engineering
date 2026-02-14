"""
Procesador de logs para pipeline de observabilidad.

Ejercicio 3: Log Processor para Observabilidad
===============================================

Objetivo: Escribir functional tests completos para un pipeline de I/O (JSONL → CSV).

Parte A - Unit tests (15 min):
- test_parse_log_line con parametrize
- test_filter_by_severity con fixture
- test_extract_fields

Parte B - Functional tests con tmp_path (30 min):
- test_process_logs_happy_path
- test_process_logs_with_bad_lines
- test_process_logs_empty_file
- test_process_logs_file_not_found
- test_process_logs_unicode

Criterios de éxito:
- [ ] Al menos 12 tests en total
- [ ] Todos los functional tests usan tmp_path
- [ ] Tests verifican contenido del CSV y estadísticas
- [ ] Cobertura ≥ 95%
"""

import csv
import json
from pathlib import Path


def parse_log_line(line: str) -> dict | None:
    """
    Parse a log line in JSON format.
    
    :param line: Log line to parse
    :type line: str
    :return: Dict with log fields, or None if invalid
    :rtype: dict | None
    """
    line = line.strip()
    if not line:
        return None
    try:
        entry = json.loads(line)
        return entry
    except json.JSONDecodeError:
        return None


def filter_by_severity(entries: list[dict], min_severity: str = "WARNING") -> list[dict]:
    """
    Filter entries by minimum severity level.
    
    Levels (from lowest to highest): DEBUG, INFO, WARNING, ERROR, CRITICAL
    
    :param entries: List of log entries
    :type entries: list[dict]
    :param min_severity: Minimum severity to include
    :type min_severity: str
    :return: Filtered list of entries
    :rtype: list[dict]
    """
    severity_levels = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}
    min_level = severity_levels.get(min_severity.upper(), 2)
    
    return [
        entry
        for entry in entries
        if severity_levels.get(entry.get("severity", "").upper(), -1) >= min_level
    ]


def extract_fields(entries: list[dict], fields: list[str]) -> list[dict]:
    """
    Extract only specified fields from each entry.
    
    Missing fields are filled with empty string.
    
    :param entries: List of log entries
    :type entries: list[dict]
    :param fields: Fields to extract
    :type fields: list[str]
    :return: List of dicts with only specified fields
    :rtype: list[dict]
    """
    return [{field: entry.get(field, "") for field in fields} for entry in entries]


def process_logs(
    input_path: str,
    output_path: str,
    min_severity: str = "WARNING",
    fields: list[str] | None = None,
) -> dict:
    """
    Complete pipeline: read JSONL logs → filter → export CSV.
    
    :param input_path: Path to JSONL log file
    :type input_path: str
    :param output_path: Path for output CSV
    :type output_path: str
    :param min_severity: Minimum severity to include
    :type min_severity: str
    :param fields: Fields to include in CSV (None = all from first record)
    :type fields: list[str] | None
    :return: Statistics dict
    :rtype: dict
    :raises FileNotFoundError: If input file doesn't exist
    """
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"Log file not found: {input_path}")
    
    # Parse
    entries = []
    skipped = 0
    with open(input_file, encoding="utf-8") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed is not None:
                entries.append(parsed)
            else:
                skipped += 1
    
    total_lines = len(entries) + skipped
    
    # Filter
    filtered = filter_by_severity(entries, min_severity)
    
    # Select fields
    if fields is None and filtered:
        fields = list(filtered[0].keys())
    elif fields is None:
        fields = []
    
    exported = extract_fields(filtered, fields)
    
    # Write CSV
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(exported)
    
    return {
        "total_lines": total_lines,
        "parsed": len(entries),
        "filtered": len(filtered),
        "exported": len(exported),
        "skipped_lines": skipped,
    }
