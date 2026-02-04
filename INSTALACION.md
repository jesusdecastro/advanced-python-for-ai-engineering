# Guía de Instalación Incremental

Este curso utiliza un enfoque incremental para la gestión de dependencias. Cada día añadirás las librerías necesarias a tu proyecto, practicando la gestión de dependencias de forma realista.

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

```bash
pip install -r day_1/requirements.txt
```

Esto instala:
- **jupyter** y **notebook** - Entorno interactivo para notebooks
- **ruff** - Linter y formateador extremadamente rápido
- **pyright** - Type checker estático para validar type hints
- **pytest** - Framework de testing

### 4. Verificar Instalación

```bash
# Verificar que las herramientas están disponibles
ruff --version
pyright --version
pytest --version
jupyter --version
```

## Día 2: Código Pythónico

El Día 2 utiliza únicamente la biblioteca estándar de Python. Los conceptos (comprehensions, generators, decorators, context managers) no requieren dependencias externas.

**No hay instalación necesaria para este día.**

## Día 3: Código Limpio

El Día 3 se enfoca en principios de código limpio usando las herramientas ya instaladas en el Día 1 (ruff, pyright).

**No hay instalación necesaria para este día.**

## Día 4: Programación Orientada a Objetos

### Instalar Pydantic

```bash
pip install -r day_4/requirements.txt
```

Esto instala:
- **pydantic** - Validación de datos usando type hints con modelos declarativos

### Actualizar pyproject.toml

Añade pydantic a las dependencias del proyecto:

```toml
[project]
dependencies = [
    "pydantic>=2.0.0",
]
```

## Día 5: Testing y Optimización de Datos

### Instalar NumPy, pandas y herramientas de profiling

```bash
pip install -r day_5/requirements.txt
```

Esto instala:
- **numpy** - Computación numérica eficiente con arrays multidimensionales
- **pandas** - Análisis y manipulación de datos tabulares
- **pytest-cov** - Plugin para medir cobertura de tests
- **memory-profiler** - Profiling de uso de memoria línea por línea

### Actualizar pyproject.toml

Añade las nuevas dependencias:

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

## Día 6: Proyecto Integrador

Para el proyecto integrador, las dependencias dependerán del proyecto elegido. Consulta la guía específica de tu proyecto en `proyectos_integradores/`.

Dependencias comunes:
- Todos los proyectos: `pydantic`, `pytest`, `pytest-cov`
- Data Pipeline, Log Analyzer, CSV Cleaner, Data Validator: `pandas`, `numpy`
- Config Manager: `pyyaml`, `toml`
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

## Comandos Útiles

### Instalar todas las dependencias de una vez (no recomendado para aprendizaje)

```bash
pip install -e ".[dev]"
```

### Ver dependencias instaladas

```bash
pip list
```

### Congelar dependencias exactas

```bash
pip freeze > requirements-lock.txt
```

### Desinstalar una dependencia

```bash
pip uninstall nombre-paquete
```

## Solución de Problemas

### "pip: command not found"
Asegúrate de que el entorno virtual está activado. Deberías ver `(venv)` en tu terminal.

### Conflictos de versiones
Si encuentras conflictos, elimina el entorno y créalo de nuevo:
```bash
deactivate
rm -rf venv  # Linux/Mac
rmdir /s venv  # Windows
python -m venv venv
```

### Instalación lenta
Actualiza pip antes de instalar:
```bash
pip install --upgrade pip
```

## Filosofía del Enfoque Incremental

Este enfoque te enseña:

1. **Gestión de dependencias realista**: Así es como se desarrollan proyectos reales
2. **Comprensión del propósito**: Sabes por qué necesitas cada librería
3. **Práctica con pyproject.toml**: Refuerzas lo aprendido en Día 1
4. **Proyectos ligeros**: Solo instalas lo que necesitas
5. **Debugging más fácil**: Menos dependencias = menos conflictos potenciales
