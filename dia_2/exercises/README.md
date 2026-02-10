# Ejercicios Día 2 - Python Avanzado

Ejercicios prácticos para dominar los conceptos avanzados de Python del Día 2.

## El Problema: Cómo Ejecutar los Tests

Los tests necesitan importar tus ejercicios:

```python
# tests/test_comprehensions.py
from dia2_exercises.comprehensions import filter_even_numbers
```

Pero Python no encuentra `dia2_exercises` porque está en `src/`. La solución profesional es crear un **paquete instalable**.

## Configuración del Entorno (Paso a Paso)

### 1. Instalar UV

```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Crear Entorno Virtual

```bash
cd dia_2/exercises
uv venv
```

### 3. Activar Entorno

```bash
# Windows (CMD)
.venv\Scripts\activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

### 4. Crear pyproject.toml

Crea el archivo `pyproject.toml` en `dia_2/exercises/`:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "dia2-exercises"
version = "0.1.0"
description = "Ejercicios prácticos del Día 2"
requires-python = ">=3.10"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "ruff>=0.1.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-v"

[tool.ruff]
line-length = 100
target-version = "py310"
```

**¿Qué hace este archivo?**
- Define un paquete Python llamado `dia2-exercises`
- Usa Hatchling como build backend (moderno y simple)
- Declara pytest y ruff como dependencias de desarrollo
- Configura pytest para buscar tests en `tests/`

### 5. Instalar el Paquete en Modo Editable

```bash
uv pip install -e ".[dev]"
```

**¿Qué hace `-e`?**
- Instala el paquete en modo "editable"
- Los cambios en tu código se reflejan inmediatamente
- Python puede importar `dia2_exercises` desde cualquier lugar

**¿Qué hace `[dev]`?**
- Instala también pytest y ruff

**Resultado**: Python crea un link en `site-packages/` que apunta a `src/dia2_exercises/`

### 6. Verificar Instalación

```bash
python -c "import dia2_exercises; print(dia2_exercises.__version__)"
# Output: 0.1.0
```

## Estructura del Proyecto

```
dia_2/exercises/
├── .venv/                  # Entorno virtual (creado por UV)
├── src/
│   └── dia2_exercises/     # Tu paquete
│       ├── __init__.py
│       ├── comprehensions.py
│       ├── generators_iterators.py
│       ├── decorators.py
│       ├── functional_programming.py
│       ├── context_managers.py
│       └── magic_methods.py
├── tests/
│   ├── __init__.py
│   └── test_*.py           # Tests unitarios
├── pyproject.toml          # Configuración del paquete (TÚ LO CREAS)
└── README.md
```

## Flujo de Trabajo

### 1. Leer el Ejercicio

```python
# src/dia2_exercises/comprehensions.py

def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    Filter even numbers from a list using list comprehension.
    
    Example:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    # TODO: Implementa usando list comprehension
    pass
```

### 2. Implementar la Solución

```python
def filter_even_numbers(numbers: list[int]) -> list[int]:
    """Filter even numbers from a list using list comprehension."""
    return [n for n in numbers if n % 2 == 0]
```

### 3. Ejecutar Tests

```bash
# Todos los tests
pytest

# Un módulo específico
pytest tests/test_comprehensions.py

# Un test específico
pytest tests/test_comprehensions.py::test_filter_even_numbers
```

### 4. Verificar Calidad

```bash
# Verificar estilo
ruff check src/

# Formatear código
ruff format src/
```

## Cómo Funcionan los Imports

**Antes de instalar el paquete:**
```python
from dia2_exercises.comprehensions import filter_even_numbers
# ModuleNotFoundError: No module named 'dia2_exercises'
```

**Después de `uv pip install -e .`:**
```python
from dia2_exercises.comprehensions import filter_even_numbers
# ✓ Funciona porque Python encuentra el paquete en site-packages
```

**¿Por qué funciona?**

1. `uv pip install -e .` crea un link simbólico:
   ```
   .venv/lib/site-packages/dia2_exercises -> ../../src/dia2_exercises/
   ```

2. Python busca módulos en `site-packages/`

3. Encuentra el link y carga tu código

4. Los cambios se reflejan inmediatamente (modo editable)

## Comandos Rápidos

```bash
# Configuración inicial (una vez)
uv venv
# Crear pyproject.toml (ver arriba)
uv pip install -e ".[dev]"

# Trabajo diario
pytest                              # Ejecutar tests
pytest tests/test_comprehensions.py # Test específico
ruff check src/                     # Verificar código
ruff format src/                    # Formatear código
```

## Módulos de Ejercicios

1. **comprehensions.py** - List, dict y set comprehensions
2. **generators_iterators.py** - Generadores e iteradores
3. **decorators.py** - Decoradores
4. **functional_programming.py** - map, filter, reduce
5. **context_managers.py** - Context managers
6. **magic_methods.py** - Métodos mágicos

## Solución de Problemas

**Error: `ModuleNotFoundError: No module named 'dia2_exercises'`**
- Solución: `uv pip install -e ".[dev]"`

**Error: `pytest: command not found`**
- Solución: Activa el entorno virtual

**Tests pasan pero el código está mal**
- Los tests son simples, verifica el docstring y prueba casos adicionales

## Recursos

- **UV**: https://docs.astral.sh/uv/
- **pytest**: https://docs.pytest.org/
- **Hatchling**: https://hatch.pypa.io/latest/
