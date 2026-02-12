"""
Protocols que definen los contratos de cada pieza del pipeline.

NO MODIFICAR — tus clases deben cumplir estos contratos por estructura.
"""

from typing import Protocol


class TextNormalizer(Protocol):
    """Normaliza texto crudo. Devuelve texto limpio."""

    def normalize(self, text: str) -> str: ...


class Tokenizer(Protocol):
    """Convierte texto en lista de tokens."""

    def tokenize(self, text: str) -> list[str]: ...


class TokenFilter(Protocol):
    """Filtra tokens de una lista. Devuelve la lista filtrada."""

    def filter_tokens(self, tokens: list[str]) -> list[str]: ...
