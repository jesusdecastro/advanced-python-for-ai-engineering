"""
Protocols del sistema de scoring.

NO MODIFICAR — tus clases deben cumplir estos contratos.
"""

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .scoring import Review, ScoringResult


class ReviewLoader(Protocol):
    """Carga reviews desde alguna fuente."""

    def load(self) -> list["Review"]: ...


class SentimentAnalyzer(Protocol):
    """Analiza el sentimiento de un texto. Devuelve score -1.0 a 1.0."""

    def analyze(self, text: str) -> float: ...


class ResultSaver(Protocol):
    """Guarda una lista de resultados de scoring."""

    def save(self, results: list["ScoringResult"]) -> None: ...
