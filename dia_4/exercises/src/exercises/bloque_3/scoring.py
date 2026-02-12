"""
Sistema de scoring de reviews — practica SRP y DIP.

Tu trabajo:
1. Crear modelos de datos (Review con Pydantic, ScoringResult con dataclass)
2. Implementar las clases que cumplen los Protocols
3. Crear ScoringService que SOLO orquesta — no tiene lógica de análisis
4. Los datos fluyen como argumentos entre las piezas
"""

from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel, Field

from .helpers import compute_keyword_sentiment, sentiment_label
from .protocols import ResultSaver, ReviewLoader, SentimentAnalyzer


# --- Modelos de datos ---


class Review(BaseModel):
    """
    Review de un producto.

    Hints:
    - Campos: text (str, min_length=1), rating (int, 1-5), product (str)
    - Usa Field() para restricciones de rating.
    """

    ...


@dataclass(frozen=True)
class ScoringResult:
    """
    Resultado del análisis de una review.

    Hints:
    - Campos: review_text (str), sentiment_score (float),
      label (str), scored_at (str con timestamp ISO).
    """

    ...


# --- Pieza 1: Carga de datos (responsabilidad: ¿DE DÓNDE vienen las reviews?) ---


class InMemoryReviewLoader:
    """
    Carga reviews desde una lista en memoria. Cumple ReviewLoader.

    Hints:
    - Recibe reviews: list[Review] en __init__.
    - load() simplemente devuelve la lista.
    - ¿Por qué existe esta clase? Porque en producción tendrías
      un CSVReviewLoader o un DatabaseReviewLoader. Esta es la versión
      simple para tests y desarrollo.
    """

    ...


# --- Pieza 2: Análisis (responsabilidad: ¿CÓMO se calcula el sentimiento?) ---


class KeywordSentimentAnalyzer:
    """
    Analiza sentimiento con palabras clave. Cumple SentimentAnalyzer.

    Hints:
    - Recibe positive_words: set[str] y negative_words: set[str] en __init__.
    - analyze(text) llama a compute_keyword_sentiment() de helpers.py.
    - UNA línea en el método analyze().
    """

    ...


# --- Pieza 3: Guardado (responsabilidad: ¿DÓNDE se guardan los resultados?) ---


class InMemoryResultSaver:
    """
    Guarda resultados en una lista en memoria. Cumple ResultSaver.

    Hints:
    - Tiene un atributo público results: list[ScoringResult] = []
    - save() extiende self.results con los nuevos resultados.
    - ¿Por qué público? Para poder verificar en tests qué se guardó.
    """

    ...


# --- Orquestador (responsabilidad: ¿EN QUÉ ORDEN se ejecuta el flujo?) ---


class ScoringService:
    """
    Orquesta el flujo de scoring. NO tiene lógica de análisis.

    Hints:
    - __init__ recibe: loader (ReviewLoader), analyzer (SentimentAnalyzer),
      saver (ResultSaver). Usa los Protocols como type hints.
    - Método run() -> list[ScoringResult]:
      1. Carga reviews con self._loader.load()
      2. Para cada review:
         a. Calcula score con self._analyzer.analyze(review.text)
         b. Calcula label con sentiment_label(score) de helpers.py
         c. Crea ScoringResult con los datos
      3. Guarda resultados con self._saver.save(results)
      4. Devuelve los resultados

    IMPORTANTE: ScoringService NO importa compute_keyword_sentiment.
    Solo usa self._analyzer.analyze() — no sabe qué implementación es.
    Eso es DIP.
    """

    ...
