# Ejercicios Día 2 - Python Avanzado

Ejercicios prácticos para dominar los conceptos avanzados de Python del Día 2.

## Inicio Rápido

El proyecto ya está configurado con `pyproject.toml`. Solo necesitas:

### 1. Configurar el Entorno

```bash
# Navega al directorio de ejercicios
cd dia_2/exercises

# Sincroniza dependencias (crea .venv e instala todo automáticamente)
uv sync
```

**¿Qué hace `uv sync`?**
- Crea el entorno virtual `.venv/` si no existe
- Lee `pyproject.toml` y `uv.lock`
- Instala todas las dependencias (pytest, ruff, etc.)
- Instala tu paquete `dia2-exercises` en modo editable
- Todo en un solo comando, sin necesidad de activar el entorno

### 2. Ejecutar Tests

```bash
# Ejecutar un test específico
uv run pytest tests/test_comprehensions.py

# Ejecutar todos los tests
uv run pytest

# Ejecutar un test individual
uv run pytest tests/test_comprehensions.py::test_filter_even_numbers
```

**¿Por qué `uv run`?**
- Ejecuta comandos dentro del entorno virtual automáticamente
- No necesitas activar/desactivar el entorno manualmente
- Más rápido y conveniente

## Estructura del Proyecto

```
dia_2/exercises/
├── .venv/                  # Entorno virtual (creado por uv sync)
├── src/
│   └── dia2_exercises/     # Tu paquete
│       ├── __init__.py
│       ├── comprehensions.py
│       ├── generators_iterators.py
│       ├── decorators.py
│       └── context_managers.py
├── tests/
│   ├── __init__.py
│   └── test_*.py           # Tests unitarios
├── pyproject.toml          # Ya configurado
├── uv.lock                 # Lock file con versiones exactas
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
# Test específico del ejercicio que estás haciendo
uv run pytest tests/test_comprehensions.py

# Todos los tests
uv run pytest

# Un test individual
uv run pytest tests/test_comprehensions.py::test_filter_even_numbers

# Con más detalle
uv run pytest -v
```

### 4. Verificar Calidad del Código

```bash
# Verificar estilo
uv run ruff check src/

# Formatear código automáticamente
uv run ruff format src/
```

## Cómo Funcionan los Imports

**El problema original:**
```python
from dia2_exercises.comprehensions import filter_even_numbers
# ModuleNotFoundError: No module named 'dia2_exercises'
```

**Después de `uv sync`:**
```python
from dia2_exercises.comprehensions import filter_even_numbers
# Funciona porque el paquete está instalado en modo editable
```

**¿Por qué funciona?**

1. `uv sync` instala el paquete en modo editable (`-e`)
2. Crea un link en `.venv/lib/site-packages/` que apunta a `src/dia2_exercises/`
3. Python encuentra el módulo cuando lo importas
4. Los cambios en tu código se reflejan inmediatamente (no necesitas reinstalar)

## Comandos Rápidos

```bash
# Configuración inicial (una vez)
cd dia_2/exercises
uv sync

# Ejecutar tests mientras trabajas
uv run pytest tests/test_comprehensions.py      # Test del ejercicio actual
uv run pytest tests/test_decorators.py          # Otro ejercicio
uv run pytest                                    # Todos los tests

# Verificar código
uv run ruff check src/                           # Verificar estilo
uv run ruff format src/                          # Formatear código
```

## Módulos de Ejercicios

1. **comprehensions.py** - List, dict y set comprehensions
2. **generators_iterators.py** - Generadores e iteradores
3. **decorators.py** - Decoradores
4. **context_managers.py** - Context managers

## Solución de Problemas

**Error: `ModuleNotFoundError: No module named 'dia2_exercises'`**
- Solución: Ejecuta `uv sync` desde `dia_2/exercises/`

**Error: `uv: command not found`**
- Solución: Instala UV siguiendo las instrucciones del paso 1

**Los tests no se ejecutan**
- Verifica que estás en el directorio correcto: `cd dia_2/exercises`
- Ejecuta: `uv sync` para asegurar que todo está instalado

**Quiero usar el entorno virtual manualmente**
```bash
# Activar entorno (opcional, uv run lo hace automáticamente)
# Windows (CMD)
.venv\Scripts\activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

# Luego puedes usar pytest directamente
pytest tests/test_comprehensions.py
```

## Recursos

- **UV**: https://docs.astral.sh/uv/
- **pytest**: https://docs.pytest.org/
- **Hatchling**: https://hatch.pypa.io/latest/
- **Ruff**: https://docs.astral.sh/ruff/
