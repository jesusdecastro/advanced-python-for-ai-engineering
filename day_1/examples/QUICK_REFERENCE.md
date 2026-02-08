# Quick Reference: `__init__.py`

## TL;DR

**Siempre usa `__init__.py` en tus paquetes.** Es el estándar de la industria.

## Ejecución Rápida

```bash
# Desde day_1/
python examples/run_namespace_package.py  # Sin __init__.py
python examples/run_regular_package.py    # Con __init__.py
```

## Comparación Rápida

### Sin `__init__.py` (Namespace Package)

```python
# ✅ Funciona
from package.module import function

# ❌ NO funciona
import package
package.function()  # AttributeError
```

### Con `__init__.py` (Regular Package)

```python
# ✅ TODO funciona
import package
package.function()  # ✅ Funciona

from package import *  # ✅ Funciona
from package import function  # ✅ Funciona
```

## Template Mínimo de `__init__.py`

```python
"""
My package description.
"""

# Exponer API pública
from .module1 import function1, function2
from .module2 import Class1, Class2

# Metadata
__version__ = "1.0.0"
__author__ = "Your Name"

# Control de exports
__all__ = [
    'function1',
    'function2',
    'Class1',
    'Class2',
]
```

## Cuándo NO Usar `__init__.py`

**Casi nunca.** Solo para:
- Plugin systems distribuidos
- Casos muy específicos de namespace packages

## Regla de Oro

> **Si tienes dudas, usa `__init__.py`.**

Es mejor tener un `__init__.py` vacío que no tenerlo.
