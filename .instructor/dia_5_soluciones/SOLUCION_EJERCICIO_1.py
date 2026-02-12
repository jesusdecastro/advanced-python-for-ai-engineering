"""
SOLUCIÓN COMPLETA - Ejercicio 1: Text Normalizer

Este archivo contiene las soluciones completas para el ejercicio 1.
Los estudiantes deben intentar resolver los ejercicios por su cuenta
antes de consultar estas soluciones.
"""

import pytest

from exercises.search_normalizer import (
    collapse_whitespace,
    normalize_for_search,
    remove_accents,
    remove_special_chars,
)


# ============================================================================
# Tests para remove_accents
# ============================================================================


def test_remove_accents_spanish_characters():
    """Remove accents from common Spanish characters."""
    assert remove_accents("café") == "cafe"


def test_remove_accents_multiple_accents():
    """Remove multiple accents from text."""
    assert remove_accents("café résumé") == "cafe resume"


def test_remove_accents_no_accents():
    """Text without accents should remain unchanged."""
    assert remove_accents("hello world") == "hello world"


def test_remove_accents_empty_string():
    """Empty string should return empty string."""
    assert remove_accents("") == ""


def test_remove_accents_umlaut():
    """Remove umlaut characters."""
    assert remove_accents("Zürich") == "Zurich"


def test_remove_accents_spanish_n():
    """Handle Spanish ñ character."""
    assert remove_accents("mañana") == "manana"


# ============================================================================
# Tests para collapse_whitespace
# ============================================================================


def test_collapse_whitespace_multiple_spaces():
    """Collapse multiple spaces into one."""
    assert collapse_whitespace("hello   world") == "hello world"


def test_collapse_whitespace_tabs_and_newlines():
    """Collapse tabs and newlines."""
    assert collapse_whitespace("hello\t\nworld") == "hello world"


def test_collapse_whitespace_leading_trailing():
    """Strip leading and trailing spaces."""
    assert collapse_whitespace("  hello world  ") == "hello world"


def test_collapse_whitespace_empty_string():
    """Empty string should return empty string."""
    assert collapse_whitespace("") == ""


def test_collapse_whitespace_only_spaces():
    """String with only spaces should return empty string."""
    assert collapse_whitespace("     ") == ""


def test_collapse_whitespace_already_clean():
    """Already clean text should remain unchanged."""
    assert collapse_whitespace("hello world") == "hello world"


# ============================================================================
# Tests para remove_special_chars
# ============================================================================


def test_remove_special_chars_default_keep():
    """Remove special characters keeping default - and _."""
    assert remove_special_chars("hello-world_2024") == "hello-world_2024"


def test_remove_special_chars_no_keep():
    """Remove all special characters when keep is empty."""
    assert remove_special_chars("hello@world!", keep="") == "helloworld"


def test_remove_special_chars_only_special():
    """String with only special characters should return empty."""
    assert remove_special_chars("@#$%", keep="") == ""


def test_remove_special_chars_no_special():
    """Text without special characters should remain unchanged."""
    assert remove_special_chars("hello world 123") == "hello world 123"


def test_remove_special_chars_mixed():
    """Mixed text with letters, numbers, and special chars."""
    result = remove_special_chars("café_2024@test.com", keep="_")
    assert result == "caf_2024testcom"


# ============================================================================
# Tests para normalize_for_search
# ============================================================================


def test_normalize_for_search_complete_pipeline():
    """Test the complete normalization pipeline."""
    assert normalize_for_search("  Café Résumé! ") == "cafe resume"


def test_normalize_for_search_uppercase():
    """Convert uppercase to lowercase."""
    assert normalize_for_search("HELLO WORLD") == "hello world"


def test_normalize_for_search_empty_string():
    """Empty string should return empty string."""
    assert normalize_for_search("") == ""


def test_normalize_for_search_already_normalized():
    """Already normalized text should remain unchanged."""
    assert normalize_for_search("hello world") == "hello world"


def test_normalize_for_search_complex():
    """Complex text with all transformations."""
    input_text = "  ¡Hola Mundo! ¿Cómo estás?  "
    expected = "hola mundo como estas"
    assert normalize_for_search(input_text) == expected
