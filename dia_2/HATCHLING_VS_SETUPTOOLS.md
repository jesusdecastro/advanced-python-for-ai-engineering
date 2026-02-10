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

# ✅ Setuptools busca automáticamente paquetes en src/
[tool.setuptools.packages.find]
where = ["src"]
```

**Ventaja**: Auto-descubre paquetes como Hatchling. El parámetro `where` indica dónde buscar.

**Nota**: No necesitas `package-dir` cuando usas `packages.find` con `where`. Son redundantes en pyproject.toml moderno.

---

### Con Hatchling (Auto-descubrimiento)

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mi-paquete"
version = "0.1.0"

# ✅ ¡ESO ES TODO! Hatchling encuentra automáticamente src/mi_paquete/
```

**Ventaja**: Hatchling detecta automáticamente todos los paquetes dentro de `src/`. No necesitas listar nada.

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
