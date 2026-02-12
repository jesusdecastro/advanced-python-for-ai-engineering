# Ejercicios de Testing - Día 5

Este directorio contiene los ejercicios prácticos para el módulo de Testing.

## Estructura

```
exercises/
├── pyproject.toml              # Configuración del proyecto
├── README.md                   # Este archivo
├── src/
│   └── exercises/
│       ├── __init__.py
│       ├── search_normalizer.py      # Ejercicio 1
│       ├── record_validator.py       # Ejercicio 2
│       └── log_processor.py          # Ejercicio 3
└── tests/
    ├── __init__.py
    ├── test_search_normalizer.py     # Tests para ejercicio 1
    ├── test_record_validator.py      # Tests para ejercicio 2
    └── test_log_processor.py         # Tests para ejercicio 3
```

## Instalación

```bash
# Instalar dependencias con uv
uv sync

# O con pip
pip install -e ".[dev]"
```

## Ejecutar Tests

```bash
# Todos los tests
uv run pytest

# Con cobertura
uv run pytest --cov=src --cov-report=term-missing

# Un fichero específico
uv run pytest tests/test_search_normalizer.py -v

# Un test específico
uv run pytest tests/test_search_normalizer.py::test_remove_accents -v
```

## Ejercicios

### Ejercicio 1: Text Normalizer para Motor de Búsqueda

**Objetivo**: Escribir unit tests básicos con pytest y el patrón AAA.

**Ficheros**:
- `src/exercises/search_normalizer.py` - Código a testear
- `tests/test_search_normalizer.py` - Tus tests aquí

**Tiempo estimado**: 50 minutos

### Ejercicio 2: Validador de Registros para Data Pipeline

**Objetivo**: Aplicar `@pytest.mark.parametrize`, fixtures y mocks.

**Ficheros**:
- `src/exercises/record_validator.py` - Código a testear
- `tests/test_record_validator.py` - Tus tests aquí

**Tiempo estimado**: 50 minutos

### Ejercicio 3: Log Processor para Observabilidad

**Objetivo**: Escribir functional tests con `tmp_path` para I/O real.

**Ficheros**:
- `src/exercises/log_processor.py` - Código a testear
- `tests/test_log_processor.py` - Tus tests aquí

**Tiempo estimado**: 55 minutos

## Criterios de Éxito

Para cada ejercicio:

- [ ] Tests siguen el patrón AAA (Arrange, Act, Assert)
- [ ] Nombres de test descriptivos
- [ ] Cobertura ≥ 90%
- [ ] Todos los tests pasan
- [ ] Código pasa ruff sin errores

## Comandos Útiles

```bash
# Ejecutar ruff
uv run ruff check src/ tests/

# Formatear código
uv run ruff format src/ tests/

# Ver cobertura en HTML
uv run pytest --cov=src --cov-report=html
# Abre htmlcov/index.html en tu navegador
```

## Notas

- Los ficheros de código en `src/exercises/` están completos y funcionan
- Tu tarea es escribir los tests en `tests/`
- Cada ejercicio tiene instrucciones detalladas en los comentarios del código
- Las soluciones están en `.instructor/` (solo para profesores)
