"""
Funciones helper de procesamiento de texto.

YA ESTÁN IMPLEMENTADAS — no las modifiques, solo úsalas desde tus clases.
"""

import re


def to_lowercase(text: str) -> str:
    """Convierte texto a minúsculas."""
    return text.lower()


def strip_whitespace(text: str) -> str:
    """Elimina espacios al inicio y final, y colapsa espacios múltiples."""
    return re.sub(r"\s+", " ", text.strip())


def split_by_whitespace(text: str) -> list[str]:
    """Separa texto por espacios. Devuelve lista de tokens."""
    return text.split()


def split_by_pattern(text: str, pattern: str) -> list[str]:
    """Separa texto por un patrón regex. Filtra strings vacíos."""
    return [token for token in re.split(pattern, text) if token]


def remove_stopwords(tokens: list[str], stopwords: set[str]) -> list[str]:
    """Elimina tokens que están en el conjunto de stopwords."""
    return [token for token in tokens if token not in stopwords]


def remove_short_tokens(tokens: list[str], min_length: int) -> list[str]:
    """Elimina tokens más cortos que min_length."""
    return [token for token in tokens if len(token) >= min_length]
