# Hatchling vs Setuptools: Guía Completa para pyproject.toml

## Introducción

Este documento explica las diferencias entre usar **Hatchling** y **Setuptools** como backend de build en tu `pyproject.toml`, con un enfoque práctico en cómo esto afecta tu configuración diaria.

---

## ¿Qué es un Build Backend?

Un **build backend** es la herramienta que:
1. Lee tu `pyproject.toml`
2. Empaqueta tu código Python
3. Genera archivos distribuibles (wheels, sdist)
4. Gestiona dependencias y metadatos

**Analogía**: Si `pyproject.toml` es la receta, el build backend es el chef que la ejecuta.

---

## Setuptools: El Enfoque Tradicional

### Configuración Básica con Setuptools

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mi-paquete"
version = "0.1.0"
description = "Mi paquete Python"
authors = [{name = "Tu Nombre", email = "tu@email.com"}]
dependencies = [
    "numpy>=1.20.0",
    "pandas>=1.3.0",
]

# Configuración específica de setuptools
[tool.setuptools]
packages = ["mi_paquete", "mi_paquete.submodulo"]

[tool.setuptools.package-data]
mi_paquete = ["data/*.json", "templates/*.html"]
```

### Problemas con Setuptools

1. **Descubrimiento manual de paquetes**: Tienes que listar explícitamente cada paquete
2. **Configuración verbosa**: Muchas secciones `[tool.setuptools.*]`
3. **Package data complicado**: Sintaxis no intuitiva para incluir archivos
4. **Herencia de setup.py**: Arrastra complejidad histórica

---

## Hatchling: El Enfoque Moderno

### Configuración Básica con Hatchling

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mi-paquete"
version = "0.1.0"
description = "Mi paquete Python"
authors = [{name = "Tu Nombre", email = "tu@email.com"}]
dependencies = [
    "numpy>=1.20.0",
    "pandas>=1.3.0",
]

# ¡Eso es todo! Hatchling descubre automáticamente los paquetes
```

### Ventajas de Hatchling

1. **Auto-descubrimiento inteligente**: Encuentra automáticamente tus paquetes
2. **Configuración mínima**: Menos líneas = menos errores
3. **Sintaxis moderna**: Diseñado desde cero para `pyproject.toml`
4. **Mejor manejo de archivos**: Incluye automáticamente archivos relevantes

---

## Comparación Lado a Lado

### Ejemplo 1: Proyecto Simple con src/ Layout

**Con Setuptools:**
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "data-processor"
version = "1.0.0"

[tool.setuptools]
package-dir = {"" = "src"}
packages = ["data_processor", "data_processor.utils", "data_processor.models"]
```

**Con Hatchling:**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "data-processor"
version = "1.0.0"

# Hatchling detecta automáticamente src/ y todos los paquetes dentro
```

**Diferencia**: Hatchling elimina 3 líneas de configuración manual.

---

### Ejemplo 2: Incluir Archivos de Datos

**Con Setuptools:**
```toml
[tool.setuptools.package-data]
data_processor = [
    "config/*.yaml",
    "templates/*.jinja2",
    "static/css/*.css",
    "static/js/*.js",
]

[tool.setuptools]
include-package-data = true
```

**Con Hatchling:**
```toml
[tool.hatch.build.targets.wheel]
packages = ["src/data_processor"]

# Archivos incluidos automáticamente si están en el paquete
# Para control explícito:
[tool.hatch.build.targets.wheel.force-include]
"config" = "data_processor/config"
"templates" = "data_processor/templates"
```

**Diferencia**: Hatchling usa rutas del sistema de archivos, más intuitivo.

---

### Ejemplo 3: Dependencias Opcionales

**Con Setuptools:**
```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
    "ruff>=0.1.0",
]
ml = [
    "scikit-learn>=1.0.0",
    "tensorflow>=2.10.0",
]
```

**Con Hatchling:**
```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
    "ruff>=0.1.0",
]
ml = [
    "scikit-learn>=1.0.0",
    "tensorflow>=2.10.0",
]
```

**Diferencia**: ¡Ninguna! Ambos usan el estándar PEP 621.

---

## Características Avanzadas de Hatchling

### 1. Versionado Dinámico

**Problema**: Mantener la versión sincronizada entre código y `pyproject.toml`.

**Solución con Hatchling:**
```toml
[project]
name = "mi-paquete"
dynamic = ["version"]

[tool.hatch.version]
path = "src/mi_paquete/__init__.py"
```

En tu `__init__.py`:
```python
__version__ = "1.0.0"
```

Hatchling lee automáticamente la versión desde tu código.

---

### 2. Metadatos Dinámicos

```toml
[project]
name = "mi-paquete"
dynamic = ["version", "description", "readme"]

[tool.hatch.metadata]
allow-direct-references = true

[tool.hatch.version]
path = "src/mi_paquete/__version__.py"
```

---

### 3. Build Hooks Personalizados

```toml
[tool.hatch.build.hooks.custom]
path = "build_hooks.py"
```

Crea `build_hooks.py`:
```python
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        # Lógica personalizada antes del build
        print(f"Building version {version}")
```

---

## Migración de Setuptools a Hatchling

### Paso 1: Cambiar el Build Backend

**Antes:**
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
```

**Después:**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

---

### Paso 2: Eliminar Configuración Redundante

**Antes:**
```toml
[tool.setuptools]
packages = ["mi_paquete", "mi_paquete.utils"]
package-dir = {"" = "src"}
```

**Después:**
```toml
# ¡Nada! Hatchling lo detecta automáticamente
```

---

### Paso 3: Actualizar Package Data (si es necesario)

**Antes:**
```toml
[tool.setuptools.package-data]
mi_paquete = ["data/*.json"]
```

**Después:**
```toml
[tool.hatch.build.targets.wheel]
packages = ["src/mi_paquete"]
# Los archivos .json dentro del paquete se incluyen automáticamente
```

---

### Paso 4: Verificar el Build

```bash
# Instalar hatchling
pip install hatchling

# Construir el paquete
python -m build

# Verificar el contenido del wheel
unzip -l dist/mi_paquete-1.0.0-py3-none-any.whl
```

---

## Casos de Uso Comunes

### Proyecto con src/ Layout

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "data-pipeline"
version = "1.0.0"
description = "ETL pipeline for data processing"
requires-python = ">=3.10"
dependencies = [
    "pandas>=2.0.0",
    "pydantic>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "ruff>=0.1.0",
]

# Hatchling detecta automáticamente src/data_pipeline/
```

**Estructura del proyecto:**
```
data-pipeline/
├── src/
│   └── data_pipeline/
│       ├── __init__.py
│       ├── readers/
│       ├── transformers/
│       └── writers/
├── tests/
├── pyproject.toml
└── README.md
```

---

### Proyecto con Múltiples Paquetes

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "ml-toolkit"
version = "2.0.0"

[tool.hatch.build.targets.wheel]
packages = [
    "src/ml_toolkit",
    "src/ml_toolkit_extras",
]
```

---

### Proyecto con Scripts CLI

```toml
[project]
name = "data-cli"
version = "1.0.0"

[project.scripts]
data-process = "data_cli.main:cli"
data-validate = "data_cli.validators:main"

# Hatchling genera automáticamente los entry points
```

---

## Tabla Comparativa Completa

| Característica | Setuptools | Hatchling |
|----------------|------------|-----------|
| **Auto-descubrimiento de paquetes** | ❌ Manual | ✅ Automático |
| **Configuración mínima** | ❌ Verbosa | ✅ Concisa |
| **src/ layout** | ⚠️ Requiere config | ✅ Detectado automáticamente |
| **Package data** | ⚠️ Sintaxis compleja | ✅ Intuitivo |
| **Versionado dinámico** | ⚠️ Plugins externos | ✅ Built-in |
| **Build hooks** | ⚠️ Complejo | ✅ Simple |
| **Velocidad de build** | ⚠️ Moderada | ✅ Rápida |
| **Compatibilidad** | ✅ Universal | ✅ Moderno (Python 3.7+) |
| **Documentación** | ⚠️ Fragmentada | ✅ Clara y moderna |

---

## Cuándo Usar Cada Uno

### Usa Setuptools Si:
- Mantienes un proyecto legacy con `setup.py`
- Necesitas compatibilidad con Python < 3.7
- Tienes builds muy complejos con extensiones C
- Tu equipo ya conoce bien setuptools

### Usa Hatchling Si:
- Empiezas un proyecto nuevo
- Quieres configuración mínima
- Usas src/ layout
- Valoras la simplicidad y modernidad
- Trabajas con Python 3.7+

---

## Ejemplo Completo: Proyecto Real

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "ml-data-processor"
version = "1.0.0"
description = "Production-ready data processing for ML pipelines"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
authors = [
    {name = "Data Team", email = "data@company.com"}
]
keywords = ["machine-learning", "data-processing", "etl"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

dependencies = [
    "pandas>=2.0.0",
    "pydantic>=2.0.0",
    "pyyaml>=6.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0",
]
ml = [
    "scikit-learn>=1.3.0",
    "numpy>=1.24.0",
]

[project.scripts]
ml-process = "ml_data_processor.cli:main"

[project.urls]
Homepage = "https://github.com/company/ml-data-processor"
Documentation = "https://ml-data-processor.readthedocs.io"
Repository = "https://github.com/company/ml-data-processor"

# Configuración de Hatchling (opcional, con valores por defecto inteligentes)
[tool.hatch.build.targets.wheel]
packages = ["src/ml_data_processor"]

[tool.hatch.build.targets.sdist]
exclude = [
    "/.github",
    "/docs",
    "/.vscode",
]
```

---

## Comandos Útiles

### Con Setuptools
```bash
# Build
python -m build

# Instalar en modo desarrollo
pip install -e .

# Instalar con extras
pip install -e ".[dev]"
```

### Con Hatchling
```bash
# Build
python -m build

# Instalar en modo desarrollo
pip install -e .

# Instalar con extras
pip install -e ".[dev]"

# Verificar configuración
hatchling metadata
```

**Nota**: Los comandos de instalación son idénticos porque ambos siguen los estándares PEP.

---

## Preguntas Frecuentes

### ¿Puedo mezclar Setuptools y Hatchling?
**No**. Solo puedes tener un build backend por proyecto.

### ¿Hatchling es compatible con todos los paquetes?
**Sí**. Hatchling genera wheels estándar compatibles con pip, conda, etc.

### ¿Necesito cambiar mi código Python?
**No**. El build backend solo afecta cómo se empaqueta, no tu código.

### ¿Qué pasa con setup.py?
Con Hatchling (y setuptools moderno), **no necesitas setup.py**. Todo va en `pyproject.toml`.

### ¿Es Hatchling más rápido?
**Sí**, generalmente 20-30% más rápido en builds porque está optimizado y tiene menos overhead.

---

## Recursos Oficiales

### Hatchling
- **Documentación**: [https://hatch.pypa.io/latest/](https://hatch.pypa.io/latest/)
- **GitHub**: [https://github.com/pypa/hatch](https://github.com/pypa/hatch)
- **PEP 621**: [https://peps.python.org/pep-0621/](https://peps.python.org/pep-0621/)

### Setuptools
- **Documentación**: [https://setuptools.pypa.io/](https://setuptools.pypa.io/)
- **Guía de pyproject.toml**: [https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)

---

## Conclusión

**Hatchling** representa la evolución moderna de empaquetado Python:
- **Menos configuración** = menos errores
- **Auto-descubrimiento** = menos mantenimiento
- **Sintaxis clara** = mejor experiencia de desarrollo

Para proyectos nuevos en 2024+, **Hatchling es la opción recomendada**. Es más simple, más rápido y está diseñado desde cero para el ecosistema moderno de Python.

**Regla de oro**: Si puedes expresar tu configuración en menos líneas sin perder funcionalidad, hazlo. Hatchling te permite exactamente eso.
