# Guía de Instalación Incremental

Este curso utiliza un enfoque incremental para la gestión de dependencias. Cada día añadirás las librerías necesarias editando `pyproject.toml` manualmente, practicando la gestión de dependencias de forma realista.

**Importante:** Los archivos `day_X/requirements.txt` son solo referencia de qué dependencias necesitas. La instalación siempre se hace editando `pyproject.toml`.

## Configuración Inicial (Día 1)

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/advanced-python-for-ai-engineering.git
cd advanced-python-for-ai-engineering
```

### 2. Crear Entorno Virtual

```bash
# Con venv (estándar)
python -m venv venv

# Activar el entorno
# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar Dependencias del Día 1

Consulta `day_1/requirements.txt` para ver qué necesitas instalar. Luego edita `pyproject.toml`:

```toml
[project]
name = "advanced-python-ai"
version = "1.0.0"
description = "Advanced Python for AI Engineering Course"
readme = "README.md"
requires-python = ">=3.11"
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

Instala el proyecto en modo editable:

```bash
pip install -e ".[dev]"
```

### 4. Verificar Instalación

```bash
jupyter --version
ruff --version
pyright --version
pytest --version
```

## Día 2: Código Pythónico

El Día 2 utiliza únicamente la biblioteca estándar de Python.

**No hay instalación necesaria para este día.**

## Día 3: Código Limpio

El Día 3 usa las herramientas ya instaladas en el Día 1 (ruff, pyright).

**No hay instalación necesaria para este día.**

## Día 4: Programación Orientada a Objetos

Consulta `day_4/requirements.txt` para ver qué necesitas. Edita `pyproject.toml` añadiendo pydantic:

```toml
[project]
dependencies = [
    "jupyter>=1.1.0",
    "notebook>=7.0.0",
    "pydantic>=2.0.0",  # NUEVO
]
```

Actualiza la instalación:

```bash
pip install -e ".[dev]"
```

## Día 5: Testing y Optimización de Datos

Consulta `day_5/requirements.txt` para ver qué necesitas. Edita `pyproject.toml` añadiendo numpy, pandas y herramientas de profiling:

```toml
[project]
dependencies = [
    "jupyter>=1.1.0",
    "notebook>=7.0.0",
    "pydantic>=2.0.0",
    "numpy>=1.24.0",     # NUEVO
    "pandas>=2.0.0",     # NUEVO
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",        # NUEVO
    "ruff>=0.8.0",
    "pyright>=1.1.0",
    "memory-profiler>=0.61.0",  # NUEVO
]
```

Actualiza la instalación:

```bash
pip install -e ".[dev]"
```

## Día 6: Proyecto Integrador

Para el proyecto integrador, las dependencias dependerán del proyecto elegido. Consulta la guía específica de tu proyecto en `proyectos_integradores/`.

Dependencias comunes ya instaladas:
- Todos los proyectos: pydantic, pytest, pytest-cov
- Data Pipeline, Log Analyzer, CSV Cleaner, Data Validator: pandas, numpy
- Config Manager: Necesitarás añadir pyyaml y toml
- Text Processing: Solo stdlib

## Verificación Final

Al finalizar el curso, tu `pyproject.toml` debería verse así:

```toml
[project]
name = "advanced-python-ai"
version = "1.0.0"
description = "Advanced Python for AI Engineering Course"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "jupyter>=1.1.0",
    "notebook>=7.0.0",
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

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W"]
ignore = ["E501"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"

[tool.pyright]
typeCheckingMode = "standard"
reportMissingTypeStubs = false
```

## Comandos Útiles

### Ver dependencias instaladas

```bash
pip list
```

### Reinstalar el proyecto después de cambios en pyproject.toml

```bash
pip install -e ".[dev]"
```

### Desinstalar una dependencia

```bash
pip uninstall nombre-paquete
# Luego elimínala de pyproject.toml
```

## Solución de Problemas

### "pip: command not found"
Asegúrate de que el entorno virtual está activado. Deberías ver `(venv)` en tu terminal.

### Cambios en pyproject.toml no se reflejan
Ejecuta `pip install -e ".[dev]"` después de editar pyproject.toml.

### Conflictos de versiones
Si encuentras conflictos, elimina el entorno y créalo de nuevo:
```bash
deactivate
rm -rf venv  # Linux/Mac
rmdir /s venv  # Windows
python -m venv venv
```

## Filosofía del Enfoque Incremental

Este enfoque te enseña:

1. **Gestión de dependencias realista**: Editas pyproject.toml como en proyectos reales
2. **Comprensión del propósito**: Sabes por qué necesitas cada librería
3. **Práctica con pyproject.toml**: Refuerzas lo aprendido en Día 1
4. **Proyectos ligeros**: Solo instalas lo que necesitas
5. **Debugging más fácil**: Menos dependencias = menos conflictos potenciales

## Nota sobre requirements.txt

Los archivos `day_X/requirements.txt` son **solo para referencia**. Te indican qué dependencias necesitas ese día y por qué (con comentarios explicativos). 

**Nunca ejecutes `pip install -r requirements.txt`** - siempre edita `pyproject.toml` y ejecuta `pip install -e ".[dev]"`.
