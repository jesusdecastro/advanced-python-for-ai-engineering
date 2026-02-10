# Hatchling vs Setuptools: Lo Esencial para que tus Imports Funcionen

## El Problema que Resuelve

Cuando creas un paquete Python con estructura `src/`, necesitas que Python encuentre tus módulos para que los imports funcionen:

```python
# Quieres que esto funcione:
from mi_paquete.utils import helper_function
```

El **build backend** en `pyproject.toml` le dice a Python dónde buscar tus paquetes. Hay dos opciones principales: **Setuptools** (tradicional) y **Hatchling** (moderno).

---

## Comparación Rápida: Lo que Necesitas Cambiar

### Con Setuptools (Auto-descubrimiento)

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mi-paquete"
version = "0.1.0"

# Setuptools necesita que le digas dónde buscar
[tool.setuptools.packages.find]
where = ["src"]
```

**Ventaja**: Auto-descubre todos los paquetes en `src/`. El parámetro `where` indica dónde buscar.

**Nota**: No necesitas `package-dir` cuando usas `packages.find` con `where`. Son redundantes en pyproject.toml moderno.

---

### Con Hatchling (Auto-descubrimiento Inteligente)

**Opción 1: Sin configuración (recomendado si el nombre coincide)**

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mi-paquete"  # Hatchling buscará src/mi_paquete/__init__.py
version = "0.1.0"

# ✅ ¡ESO ES TODO! Hatchling auto-descubre si el nombre coincide
```

**Opción 2: Con configuración explícita (más control)**

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mi-paquete"
version = "0.1.0"

# Usa esto cuando:
# - El nombre del paquete NO coincide con project.name
# - Tienes múltiples paquetes
# - Quieres control explícito
[tool.hatchling.build.targets.wheel]
packages = ["src/mi_paquete"]
```

**Cómo funciona el auto-descubrimiento de Hatchling:**

Hatchling busca tu paquete en este orden (usando `project.name` como referencia):
1. `<NAME>/__init__.py` (flat layout)
2. `src/<NAME>/__init__.py` (src layout) ← Más común
3. `<NAME>.py` (módulo único)
4. `<NAMESPACE>/<NAME>/__init__.py` (namespace package)

**Importante**: El nombre del directorio del paquete debe coincidir con `project.name` (con guiones convertidos a guiones bajos).

**Ejemplo**: Si `project.name = "mi-paquete"`, Hatchling busca `src/mi_paquete/` (nota el guion bajo).

---

## Cuándo Usar Cada Opción

### Usa Hatchling sin configuración cuando:
- Tu paquete está en `src/<nombre_paquete>/`
- El nombre del directorio coincide con `project.name` (con guiones → guiones bajos)
- Solo tienes un paquete principal
- Quieres la configuración más simple

### Usa Hatchling con `packages` explícito cuando:
- El nombre del paquete NO coincide con `project.name`
- Tienes múltiples paquetes en `src/`
- Quieres control explícito sobre qué se incluye
- Estás migrando desde setuptools y quieres mantener control

### Usa Setuptools cuando:
- Trabajas en un proyecto legacy que ya usa setuptools
- Necesitas características específicas de setuptools
- Tu equipo ya está familiarizado con setuptools

---

## Ejemplo Práctico: Proyecto con src/ Layout

**Estructura del proyecto:**
```
mi-proyecto/
├── src/
│   └── mi_paquete/
│       ├── __init__.py
│       ├── utils/
│       │   ├── __init__.py
│       │   └── helpers.py
│       └── models/
│           ├── __init__.py
│           └── data.py
├── tests/
├── pyproject.toml
└── README.md
```
---

### Instala tu Paquete en Modo Desarrollo

```bash
# Con UV (recomendado - más rápido)
# UV hace instalación editable con sync
uv sync

# o

uv pip install -e .

# Sin UV (alternativa tradicional)
pip install -e .
```

**¿Qué hace `-e` (editable)?**
- Crea un enlace al código fuente en lugar de copiarlo
- Los cambios en tu código se reflejan inmediatamente
- No necesitas reinstalar después de cada cambio

**Más detalles**: Ver [UV.md](UV.md) para entender cómo funciona internamente.

### Paso 2: Verifica que los Imports Funcionan

```python
# Desde cualquier lugar, deberías poder hacer:
from mi_paquete.utils.helpers import mi_funcion
from mi_paquete.models.data import MiClase
```

---

## Nota sobre el Proyecto de Ejercicios del Curso

En `dia_2/exercises/pyproject.toml`, usamos auto-descubrimiento de Hatchling:

```toml
[project]
name = "exercises"  # Nombre del proyecto

# Hatchling auto-descubre src/exercises/ automáticamente
# No necesitamos [tool.hatchling.build.targets.wheel]
```

**¿Por qué funciona sin configuración explícita?**

Hatchling busca automáticamente `src/exercises/` porque:
1. El nombre del directorio (`exercises`) coincide con `project.name`
2. Está en la ubicación estándar `src/`
3. Tiene un `__init__.py`

**Ventajas del auto-descubrimiento**:
- Configuración más simple y limpia
- Menos lugares donde pueden ocurrir errores
- Sigue las convenciones estándar de Python

---

## Dependencias de Desarrollo con UV

UV ofrece dos formas de manejar dependencias de desarrollo. Para proyectos educativos que no se publican, recomendamos `[dependency-groups]`.

### Opción 1: Dependency Groups (Recomendado para Desarrollo)

**Configuración:**
```toml
[dependency-groups]
dev = [
    "pytest",
    "ruff",
    "pyright",
]
```

**Comandos:**
```bash
# Añadir dependencia de desarrollo
uv add --dev pytest

# Instalar todas las dependencias (incluye dev por defecto)
uv sync

# Instalar SIN dependencias de desarrollo
uv sync --no-dev

# Instalar SOLO dependencias de desarrollo
uv sync --only-dev
```

**Características:**
- Basado en PEP 735 (estándar moderno)
- Se instalan por defecto con `uv sync`
- NO se publican en PyPI
- Ideal para herramientas de desarrollo (pytest, ruff, etc.)

### Opción 2: Optional Dependencies (Para Extras Publicables)

**Configuración:**
```toml
[project.optional-dependencies]
dev = [
    "pytest",
    "ruff",
    "pyright",
]
```

**Comandos:**
```bash
# Añadir dependencia opcional
uv add --optional dev pytest

# Instalar con extras específicos
uv sync --extra dev

# Instalar con TODOS los extras
uv sync --all-extras

# Instalar SIN extras
uv sync
```

**Características:**
- Basado en PEP 621 (estándar tradicional)
- NO se instalan por defecto con `uv sync`
- SÍ se publican en PyPI como extras opcionales
- Ideal para funcionalidades opcionales de librerías (ej: `pandas[excel]`)

### ¿Cuál Usar?

| Caso de Uso | Usar |
|-------------|------|
| Herramientas de desarrollo (pytest, ruff, mypy) | `[dependency-groups]` |
| Proyecto que NO se publica (ejercicios, scripts) | `[dependency-groups]` |
| Funcionalidades opcionales de librería publicada | `[project.optional-dependencies]` |
| Extras que usuarios pueden instalar (ej: `pkg[gpu]`) | `[project.optional-dependencies]` |

**Para el proyecto de ejercicios del curso**, usamos `[dependency-groups]` porque:
1. Es más simple para estudiantes (solo `uv sync`)
2. No vamos a publicar el paquete
3. Son herramientas de desarrollo, no funcionalidades opcionales
