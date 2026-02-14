"""
Tests para search_normalizer.py

Ejercicio 1: Text Normalizer para Motor de Búsqueda
====================================================

Instrucciones:
1. Completa los tests siguiendo el patrón AAA (Arrange, Act, Assert)
2. Escribe al menos 3 tests por función
3. Incluye casos borde (string vacío, solo espacios, etc.)
4. Usa nombres descriptivos

Ejecutar:
    uv run pytest tests/test_search_normalizer.py -v
    uv run pytest tests/test_search_normalizer.py -v --cov=src --cov-report=term-missing
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
    # ARRANGE
    input_text = "café"
    expected = "cafe"
    
    # ACT
    result = remove_accents(input_text)
    
    # ASSERT
    assert result == expected


# TODO: Añade más tests para remove_accents
# Casos a cubrir:
# - Texto sin acentos (debería quedar igual)
# - String vacío
# - Caracteres con diéresis (ü, ö)
# - Texto con múltiples acentos (café résumé)
# - La letra ñ


# ============================================================================
# Tests para collapse_whitespace
# ============================================================================


def test_collapse_whitespace_multiple_spaces():
    """Collapse multiple spaces into one."""
    # TODO: Implementa este test
    pass


# TODO: Añade más tests para collapse_whitespace
# Casos a cubrir:
# - Tabs y newlines
# - Espacios al inicio y final
# - String vacío
# - Solo espacios
# - Texto ya limpio (sin espacios extra)


# ============================================================================
# Tests para remove_special_chars
# ============================================================================


def test_remove_special_chars_default_keep():
    """Remove special characters keeping default - and _."""
    # TODO: Implementa este test
    pass


# TODO: Añade más tests para remove_special_chars
# Casos a cubrir:
# - Con keep="" (sin excepciones)
# - Solo caracteres especiales
# - Texto sin caracteres especiales
# - Mezcla de letras, números y especiales


# ============================================================================
# Tests para normalize_for_search
# ============================================================================


def test_normalize_for_search_complete_pipeline():
    """Test the complete normalization pipeline."""
    # TODO: Implementa este test con una frase realista
    # Ejemplo: "  Café Résumé! " → "cafe resume"
    pass


# TODO: Añade más tests para normalize_for_search
# Casos a cubrir:
# - Texto con mayúsculas, acentos, especiales y espacios extra
# - String vacío
# - Texto ya normalizado


# ============================================================================
# BONUS: Tests adicionales (opcional)
# ============================================================================

# Si terminas antes, añade tests para:
# - Caracteres Unicode exóticos (emojis, CJK)
# - Strings muy largos
# - Casos de uso reales de tu proyecto
