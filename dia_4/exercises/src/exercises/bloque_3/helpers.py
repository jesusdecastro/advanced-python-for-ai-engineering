"""
Funciones helper para análisis de sentimiento.

YA ESTÁN IMPLEMENTADAS — úsalas desde tus clases.
"""


def compute_keyword_sentiment(
    text: str,
    positive_words: set[str],
    negative_words: set[str],
) -> float:
    """
    Calcula un score de sentimiento basado en palabras clave.

    Cuenta palabras positivas y negativas, devuelve score entre -1.0 y 1.0.
    Si el texto no tiene palabras, devuelve 0.0.
    """
    words = text.lower().split()
    if not words:
        return 0.0

    pos_count = sum(1 for w in words if w in positive_words)
    neg_count = sum(1 for w in words if w in negative_words)
    raw_score = (pos_count - neg_count) / len(words)

    return max(-1.0, min(1.0, raw_score))


def sentiment_label(score: float) -> str:
    """
    Convierte un score numérico a etiqueta.

    > 0.3 → "positive", < -0.3 → "negative", entre → "neutral"
    """
    if score > 0.3:
        return "positive"
    elif score < -0.3:
        return "negative"
    return "neutral"
