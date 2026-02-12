"""
Normalizador de texto para motor de búsqueda.

Este módulo proporciona funciones para normalizar texto antes de indexarlo
en un motor de búsqueda. La normalización incluye:
- Eliminación de acentos y diacríticos
- Colapso de espacios en blanco
- Eliminación de caracteres especiales
- Pipeline completa de normalización

Ejercicio 1: Text Normalizer para Motor de Búsqueda
====================================================

Objetivo: Escribir tus primeros unit tests con pytest, aplicando el patrón AAA
y cubriendo happy paths y edge cases.

Instrucciones:
1. Crea el fichero tests/test_search_normalizer.py
2. Escribe al menos 3 tests por función (remove_accents, collapse_whitespace,
   remove_special_chars, normalize_for_search)
3. Incluye al menos 1 test de caso borde por función (string vacío, solo espacios,
   solo caracteres especiales)
4. Todos los tests deben seguir el patrón AAA (Arrange, Act, Assert)
5. Nombres de test descriptivos (test_remove_accents_handles_spanish_characters)

Criterios de éxito:
- [ ] Al menos 12 tests en total
- [ ] Cobertura ≥ 90%
- [ ] Todos los tests pasan
- [ ] Nombres descriptivos

Pistas:
- Casos borde para remove_accents: "", texto sin acentos, ñ, diacríticos combinados
- Casos borde para collapse_whitespace: tabs, newlines, solo espacios, ya limpio
- Casos borde para remove_special_chars: keep="", solo especiales, texto limpio
- normalize_for_search: frase realista con mayúsculas, acentos, especiales, espacios
"""

import re
import unicodedata


def remove_accents(text: str) -> str:
    """
    Remove accents and diacritics from text.
    
    Converts accented characters to their base form. For example:
    'café' → 'cafe', 'résumé' → 'resume'
    
    :param text: Input text with potential accents
    :type text: str
    :return: Text with accents removed
    :rtype: str
    
    Example:
        >>> remove_accents("café")
        'cafe'
        >>> remove_accents("résumé")
        'resume'
    """
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def collapse_whitespace(text: str) -> str:
    """
    Replace any sequence of whitespace characters with a single space.
    
    Handles spaces, tabs, newlines, and other whitespace characters.
    Also strips leading and trailing whitespace.
    
    :param text: Input text with potential multiple whitespace
    :type text: str
    :return: Text with collapsed whitespace
    :rtype: str
    
    Example:
        >>> collapse_whitespace("hello   world")
        'hello world'
        >>> collapse_whitespace("hello\\t\\nworld")
        'hello world'
    """
    return re.sub(r"\s+", " ", text).strip()


def remove_special_chars(text: str, keep: str = "-_") -> str:
    """
    Remove special characters except those specified in 'keep'.
    
    Only keeps alphanumeric characters, spaces, and characters in the keep parameter.
    
    :param text: Input text with potential special characters
    :type text: str
    :param keep: Characters to keep (in addition to alphanumeric and spaces)
    :type keep: str
    :return: Text with special characters removed
    :rtype: str
    
    Example:
        >>> remove_special_chars("hello@world!")
        'helloworld'
        >>> remove_special_chars("hello-world_2024", keep="-_")
        'hello-world_2024'
    """
    pattern = f"[^a-zA-Z0-9\\s{re.escape(keep)}]"
    return re.sub(pattern, "", text)


def normalize_for_search(text: str) -> str:
    """
    Complete normalization pipeline for search indexing.
    
    Applies transformations in order:
    1. Convert to lowercase
    2. Remove accents
    3. Remove special characters
    4. Collapse whitespace
    
    :param text: Input text to normalize
    :type text: str
    :return: Normalized text ready for indexing
    :rtype: str
    
    Example:
        >>> normalize_for_search("  Café Résumé! ")
        'cafe resume'
        >>> normalize_for_search("HELLO   WORLD")
        'hello world'
    """
    text = text.lower()
    text = remove_accents(text)
    text = remove_special_chars(text)
    text = collapse_whitespace(text)
    return text
