# Día 5: Testing y Optimización de Datos

## Contenido

1. **01_unit_testing_pytest.ipynb** - Unit Testing con pytest
2. **02_tdd.ipynb** - Test-Driven Development
3. **03_numpy_vectorization.ipynb** - Vectorización con NumPy
4. **04_pandas_optimization.ipynb** - Optimización con pandas
5. **05_memory_profiling.ipynb** - Memory Profiling

## Dependencias

Instalar dependencias del Día 5:

```bash
pip install -r day_5/requirements.txt
```

Actualizar `pyproject.toml`:

```toml
[project]
dependencies = [
    "pydantic>=2.0.0",
    "numpy>=1.24.0",
    "pandas>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "ruff>=0.8.0",
    "pyright>=1.1.0",
    "memory-profiler>=0.61.0",
]
```

## Ejercicios

Ejecutar tests con cobertura:
```bash
pytest day_5/exercises/tests/ --cov=day_5/exercises
```
