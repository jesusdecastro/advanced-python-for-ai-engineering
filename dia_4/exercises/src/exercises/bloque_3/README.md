# Bloque 3: SRP + DIP

## Objetivo

Practicar Separación de Responsabilidades (SRP) y Dependency Inversion Principle (DIP).

## Concepto que se Practica

- Single Responsibility Principle (SRP)
- Dependency Inversion Principle (DIP)
- Inyección de dependencias
- Testear con fakes
- Protocols como contratos

## Qué NO es el Foco

- Implementar análisis de sentimiento real
- La lógica de scoring se da como helper

## Descripción

Vas a crear un sistema de scoring de reviews de productos. La lógica de análisis de sentimiento está resuelta en helpers.py. Tu trabajo es separar responsabilidades y conectar las piezas con Protocols.

## Archivos Proporcionados

- `helpers.py`: Lógica de análisis YA IMPLEMENTADA
- `protocols.py`: Contratos que tus clases deben cumplir
- `scoring.py`: Esqueleto con hints para implementar

## Tips para Implementar

### 1. Empieza por Review y ScoringResult

```bash
uv run pytest tests/bloque_3/test_scoring.py::test_review_valid_creates_successfully -v
```

Son solo modelos de datos:
- **Review**: Pydantic BaseModel con `text` (min_length=1), `rating` (1-5), `product`
- **ScoringResult**: dataclass frozen con 4 campos

### 2. KeywordSentimentAnalyzer

```bash
uv run pytest tests/bloque_3/test_scoring.py::test_keyword_analyzer_positive_text -v
```

Es una línea que llama a helpers.py:
```python
def analyze(self, text: str) -> float:
    return compute_keyword_sentiment(text, self._positive_words, self._negative_words)
```

### 3. InMemoryReviewLoader e InMemoryResultSaver

```bash
uv run pytest tests/bloque_3/test_scoring.py::test_scoring_service_processes_all_reviews -v
```

Implementaciones triviales (2-3 líneas cada una):
- **InMemoryReviewLoader**: `load()` devuelve `self._reviews`
- **InMemoryResultSaver**: `save()` hace `self.results.extend(results)`

### 4. ScoringService

```bash
uv run pytest tests/bloque_3/test_scoring.py::test_scoring_service_uses_injected_analyzer -v
```

El método `run()` es un bucle for con 3 pasos dentro:
1. Cargar reviews: `reviews = self._loader.load()`
2. Para cada review:
   - Calcular score: `score = self._analyzer.analyze(review.text)`
   - Calcular label: `label = sentiment_label(score)`
   - Crear ScoringResult
3. Guardar: `self._saver.save(results)`
4. Devolver results

**Punto clave**: ScoringService NO importa `compute_keyword_sentiment`. Solo usa `self._analyzer.analyze()` — no sabe qué implementación es. Eso es DIP.

## La Pregunta Clave para Verificar SRP

Si mañana quieres cambiar cómo se calcula el sentimiento (por ejemplo, con un LLM), ¿qué clases tocas?

**Respuesta correcta**: Solo `KeywordSentimentAnalyzer` (o creas una nueva). `ScoringService` no cambia. Eso es SRP + DIP.

## Ejecutar Tests

```bash
# Todos los tests del bloque
uv run pytest tests/bloque_3/ -v

# Tests de Review
uv run pytest tests/bloque_3/ -k "review" -v

# Tests de ScoringService
uv run pytest tests/bloque_3/ -k "scoring_service" -v

# Test de DIP (el más importante)
uv run pytest tests/bloque_3/test_scoring.py::test_scoring_service_uses_injected_analyzer -v
```

## Criterios de Éxito

- [ ] Review valida text (min_length=1) y rating (1-5)
- [ ] ScoringResult es inmutable (frozen=True)
- [ ] KeywordSentimentAnalyzer usa helpers.py (una línea)
- [ ] InMemoryReviewLoader e InMemoryResultSaver son simples
- [ ] ScoringService orquesta sin lógica de análisis
- [ ] ScoringService usa Protocols como type hints
- [ ] Test con FakeAnalyzer pasa (verifica DIP)
- [ ] Todos los tests pasan

## Recursos

- **SOLID Principles**: https://en.wikipedia.org/wiki/SOLID
- **Dependency Inversion**: https://en.wikipedia.org/wiki/Dependency_inversion_principle
- **Protocols (PEP 544)**: https://peps.python.org/pep-0544/
