"""
Pipeline de preprocesamiento de texto — composición sobre herencia.

Tu trabajo:
1. Implementar las clases que cumplen los Protocols de protocols.py
2. Cada clase usa las funciones de helpers.py — NO reimplementes la lógica
3. Ninguna clase hereda de otra
4. Crear PreprocessingResult como dataclass inmutable
5. Crear TextPreprocessingPipeline que COMPONE las piezas
"""

from dataclasses import dataclass

from .helpers import (
    remove_short_tokens,
    remove_stopwords,
    split_by_pattern,
    split_by_whitespace,
    strip_whitespace,
    to_lowercase,
)
from .protocols import TextNormalizer, TokenFilter, Tokenizer


# --- Estructura de datos: resultado del procesamiento ---


@dataclass(frozen=True)
class PreprocessingResult:
    """
    Resultado inmutable del preprocesamiento.

    Hints:
    - Campos: original_text (str), normalized_text (str),
      tokens (list[str]), filtered_tokens (list[str])
    """

    ...


# --- Piezas de normalización ---


class LowercaseNormalizer:
    """
    Cumple TextNormalizer. Convierte a minúsculas y limpia espacios.

    Hints:
    - El método normalize() debe llamar a to_lowercase() y strip_whitespace()
      de helpers.py.
    - Aplica primero strip_whitespace, luego to_lowercase. O al revés,
      ambos órdenes dan el mismo resultado aquí.
    """

    ...


# --- Piezas de tokenización ---


class WhitespaceTokenizer:
    """
    Cumple Tokenizer. Separa por espacios.

    Hints:
    - El método tokenize() llama a split_by_whitespace() de helpers.py.
    - Una línea.
    """

    ...


class RegexTokenizer:
    """
    Cumple Tokenizer. Separa por patrón regex configurable.

    Hints:
    - Recibe pattern: str en __init__ y lo guarda.
    - El método tokenize() llama a split_by_pattern(text, self._pattern).
    """

    ...


# --- Piezas de filtrado ---


class StopwordFilter:
    """
    Cumple TokenFilter. Elimina stopwords.

    Hints:
    - Recibe stopwords: set[str] en __init__.
    - El método filter_tokens() llama a remove_stopwords() de helpers.py.
    """

    ...


class MinLengthFilter:
    """
    Cumple TokenFilter. Elimina tokens cortos.

    Hints:
    - Recibe min_length: int en __init__ (default 2).
    - El método filter_tokens() llama a remove_short_tokens() de helpers.py.
    """

    ...


# --- Pipeline: compone las piezas ---


class TextPreprocessingPipeline:
    """
    Pipeline que COMPONE un normalizer, un tokenizer y N filters.

    NO hereda de nada. Recibe las piezas en __init__.

    Hints:
    - __init__ recibe: normalizer (TextNormalizer), tokenizer (Tokenizer),
      filters (list[TokenFilter]).
    - Método process(text: str) -> PreprocessingResult:
      1. Normaliza el texto con self._normalizer.normalize(text)
      2. Tokeniza el texto normalizado con self._tokenizer.tokenize(...)
      3. Aplica cada filter en orden sobre los tokens
      4. Devuelve PreprocessingResult con los 4 campos
    """

    ...
