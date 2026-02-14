# Bloque 2: Composición sobre Herencia

## Objetivo

Practicar composición sobre herencia, Protocols como contratos, y datos como argumentos (no self.data mutable).

## Concepto que se Practica

- Composición sobre herencia
- Protocols como contratos
- Datos como argumentos (no self.data mutable)
- @dataclass(frozen=True) para resultados inmutables

## Qué NO es el Foco

- Implementar lógica de NLP
- Las operaciones de texto se dan resueltas en helpers.py

## Descripción

Vas a diseñar un pipeline de preprocesamiento de texto para NLP. Recibes los Protocols definidos y las implementaciones de la lógica de texto ya resueltas como funciones puras helper. Tu trabajo es diseñar las clases que cumplan los Protocols, componer el pipeline y asegurar que los datos fluyen como argumentos.

## Archivos Proporcionados

- `helpers.py`: Funciones de procesamiento de texto YA IMPLEMENTADAS
- `protocols.py`: Contratos que tus clases deben cumplir
- `preprocessing.py`: Esqueleto con hints para implementar

## Tips para Implementar

### 1. Empieza por LowercaseNormalizer y WhitespaceTokenizer

```bash
uv run pytest tests/bloque_2/test_preprocessing.py::test_lowercase_normalizer -v
uv run pytest tests/bloque_2/test_preprocessing.py::test_whitespace_tokenizer -v
```

Cada clase es muy corta (3-6 líneas de código real). Si te sale larga, estás reimplementando lógica que ya está en helpers.py.

**LowercaseNormalizer**:
- Método `normalize()` llama a `strip_whitespace()` y `to_lowercase()` de helpers.py
- Una línea: `return to_lowercase(strip_whitespace(text))`

**WhitespaceTokenizer**:
- Método `tokenize()` llama a `split_by_whitespace()` de helpers.py
- Una línea: `return split_by_whitespace(text)`

### 2. RegexTokenizer, StopwordFilter, MinLengthFilter

```bash
uv run pytest tests/bloque_2/test_preprocessing.py::test_regex_tokenizer_with_comma_pattern -v
uv run pytest tests/bloque_2/test_preprocessing.py::test_stopword_filter -v
uv run pytest tests/bloque_2/test_preprocessing.py::test_min_length_filter -v
```

Mismo patrón: reciben configuración en `__init__`, usan helpers.py en sus métodos.

### 3. PreprocessingResult

```bash
uv run pytest tests/bloque_2/test_preprocessing.py::test_result_is_frozen_dataclass -v
```

Es un `@dataclass(frozen=True)` con 4 campos:
- `original_text: str`
- `normalized_text: str`
- `tokens: list[str]`
- `filtered_tokens: list[str]`

### 4. TextPreprocessingPipeline

```bash
uv run pytest tests/bloque_2/test_preprocessing.py::test_pipeline_composes_all_steps -v
```

El método `process()` son 4 pasos:
1. Normalizar: `normalized = self._normalizer.normalize(text)`
2. Tokenizar: `tokens = self._tokenizer.tokenize(normalized)`
3. Filtrar: `filtered = tokens` → aplicar cada filter en bucle
4. Devolver: `return PreprocessingResult(...)`

**Punto clave**: TextPreprocessingPipeline no sabe qué normalizer/tokenizer/filters recibe — solo sabe que cumplen los Protocols. Eso es composición.

## Ejecutar Tests

```bash
# Todos los tests del bloque
uv run pytest tests/bloque_2/ -v

# Tests de normalización
uv run pytest tests/bloque_2/ -k "normalizer" -v

# Tests de pipeline completo
uv run pytest tests/bloque_2/ -k "pipeline" -v
```

## Criterios de Éxito

- [ ] Cada clase es corta (3-6 líneas de código real)
- [ ] Ninguna clase hereda de otra
- [ ] Todas las clases usan funciones de helpers.py
- [ ] PreprocessingResult es inmutable (frozen=True)
- [ ] TextPreprocessingPipeline compone las piezas sin conocer implementaciones
- [ ] Los datos fluyen como argumentos (no self.data)
- [ ] Todos los tests pasan

## Recursos

- **Protocols (PEP 544)**: https://peps.python.org/pep-0544/
- **Dataclasses**: https://docs.python.org/3/library/dataclasses.html
- **Composition over Inheritance**: https://en.wikipedia.org/wiki/Composition_over_inheritance
