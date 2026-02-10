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

En `dia_2/exercises/pyproject.toml`, usamos configuración explícita:

```toml
[project]
name = "dia2-exercises"  # Nombre con guion

[tool.hatchling.build.targets.wheel]
packages = ["src/dia2_exercises"]  # Paquete con guion bajo
```

**¿Por qué usamos configuración explícita aquí?**

Aunque Hatchling podría auto-descubrir `src/dia2_exercises/` (porque coincide con el nombre del proyecto), usamos `packages` explícito por:

1. **Claridad educativa**: Los estudiantes ven exactamente qué se está incluyendo
2. **Documentación**: Hace explícito el mapeo nombre-proyecto → nombre-paquete
3. **Robustez**: Funciona incluso si cambiamos el nombre del proyecto más adelante
4. **Mejores prácticas**: En proyectos profesionales, la configuración explícita evita sorpresas

**Ambas opciones funcionan**, pero para un curso es mejor ser explícito.
