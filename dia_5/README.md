# Día 5: Testing para AI Engineers

## Descripción

Este módulo cubre las prácticas esenciales de testing para proyectos de Data Science y AI Engineering. Aprenderás a escribir tests efectivos que detecten bugs antes de producción, te permitan refactorizar con confianza, y garanticen que tu pipeline de datos funciona correctamente.

**Conexión con Data/IA**: En proyectos de AI y Data Engineering, los bugs más peligrosos son los silenciosos — funciones que no fallan pero producen resultados incorrectos. Un pipeline de limpieza de datos que convierte strings vacíos a 0.0 en vez de NaN puede contaminar tu dataset de entrenamiento sin que nadie se entere hasta semanas después. Los tests son tu primera línea de defensa contra estos errores.

## Objetivos de Aprendizaje

Al finalizar este módulo, serás capaz de:

- Distinguir los tipos de tests (unit, integration, functional, E2E) y elegir cuál aplicar según el contexto
- Escribir unit tests con pytest siguiendo el patrón AAA (Arrange, Act, Assert)
- Usar `@pytest.mark.parametrize` para testear múltiples inputs sin duplicar código
- Crear fixtures reutilizables para preparar datos de test
- Aplicar mocks (`patch`, `mock_open`) para aislar tu código de dependencias externas
- Escribir functional tests para la capa I/O usando `tmp_path` con ficheros reales
- Medir cobertura de tests con `pytest-cov` e interpretar el reporte

**Intuición que desarrollarás**: Saber cuándo un test es necesario, qué tipo de test escribir, y cómo estructurarlo para que sea mantenible y efectivo.

## Contenido

### Teoría

1. [Introducción al Testing](testing/01_introduccion_testing.md) - Por qué testear, tipos de tests, la pirámide de testing
2. [pytest Básico](testing/02_pytest_basico.md) - Primeros tests, patrón AAA, convenciones
3. [Parametrize](testing/03_parametrize.md) - Testing con tablas de datos
4. [Fixtures](testing/04_fixtures.md) - Setup reutilizable y aislamiento
5. [Mocks](testing/05_mocks.md) - Aislar dependencias externas
6. [Functional Testing](testing/06_functional_testing.md) - Tests de I/O con tmp_path

### Ejercicios Prácticos

Los ejercicios están en el directorio `exercises/` con estructura de proyecto completo:

- **Ejercicio 1**: Text Normalizer para Motor de Búsqueda (unit tests básicos)
- **Ejercicio 2**: Validador de Registros para Data Pipeline (parametrize, fixtures, mocks)
- **Ejercicio 3**: Log Processor para Observabilidad (functional tests con I/O real)

## Estructura del Directorio

```
dia_5/
├── README.md                          # Este archivo
├── testing/                           # Contenido teórico
│   ├── 01_introduccion_testing.md
│   ├── 02_pytest_basico.md
│   ├── 03_parametrize.md
│   ├── 04_fixtures.md
│   ├── 05_mocks.md
│   └── 06_functional_testing.md
└── exercises/                         # Ejercicios prácticos
    ├── pyproject.toml
    ├── README.md
    ├── src/
    │   └── exercises/
    │       ├── search_normalizer.py
    │       ├── record_validator.py
    │       └── log_processor.py
    └── tests/
        ├── test_search_normalizer.py
        ├── test_record_validator.py
        └── test_log_processor.py
```

## Cómo Usar Este Módulo

1. **Lee la teoría en orden**: Los conceptos se construyen uno sobre otro
2. **Ejecuta los ejemplos**: Todos los ejemplos de código son ejecutables
3. **Haz los ejercicios**: La práctica es esencial para desarrollar intuición
4. **Aplica a tu proyecto**: Usa los tests en tu proyecto integrador

## Instalación

Los ejercicios usan `uv` para gestión de dependencias:

```bash
cd dia_5/exercises
uv sync
```

## Ejecutar Tests

```bash
# Todos los tests con output detallado
uv run pytest tests/ -v

# Con cobertura
uv run pytest tests/ -v --cov=src --cov-report=term-missing

# Un test específico
uv run pytest tests/test_search_normalizer.py::test_remove_accents -v
```

## Tiempo Estimado

- Teoría: 2-3 horas
- Ejercicios: 2-3 horas
- Total: 4-6 horas

## Prerrequisitos

- Día 1-2: Proyecto Python con uv, estructura de módulos, imports
- Día 3: Clean Code (funciones pequeñas, naming descriptivo, type hints)
- Día 4: Pydantic y modelado de datos
- Familiaridad con `assert` de Python y excepciones

## Recursos Adicionales

- [pytest Documentation](https://docs.pytest.org/)
- [Working Effectively with Legacy Code](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) - Michael Feathers
- [Clean Code - Chapter 9: Unit Tests](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) - Robert C. Martin
