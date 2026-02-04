# Día 1: Configuración de Proyectos Python

## Contenido

1. **01_python_idioms_intro.ipynb** - Python Idioms
2. **02_virtual_environments.ipynb** - Entornos Virtuales
3. **03_modules_and_imports.ipynb** - Módulos e Imports
4. **04_type_hinting.ipynb** - Type Hinting
5. **05_code_quality_tools.ipynb** - Herramientas de Calidad
6. **06_package_distribution.ipynb** - Distribución de Paquetes

## Dependencias

**Notebook 01:** No requiere instalación - usa solo Python stdlib

**Notebooks 02-06:** Consulta `day_1/requirements.txt` para ver qué dependencias necesitas. Edita `pyproject.toml` añadiendo:

```toml
[project]
dependencies = [
    "jupyter>=1.1.0",
    "notebook>=7.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "ruff>=0.8.0",
    "pyright>=1.1.0",
]
```

Instala:
```bash
pip install -e ".[dev]"
```

## Ejercicios

Ejecutar tests:

```bash
pytest day_1/exercises/tests/
```

Validar código:

```bash
ruff check day_1/exercises/
```

```bash
pyright day_1/exercises/
```
