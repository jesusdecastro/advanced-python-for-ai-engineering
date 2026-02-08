# Ejemplos: Packages con y sin `__init__.py`

## Descripción

Estos ejemplos demuestran la diferencia entre **namespace packages** (sin `__init__.py`) y **regular packages** (con `__init__.py`) en Python 3.3+.

## Estructura de Archivos

```
day_1/examples/
├── README.md                          # Este archivo
│
├── namespace_package/                 # ❌ SIN __init__.py
│   ├── utils.py
│   └── models.py
│
├── regular_package/                   # ✅ CON __init__.py
│   ├── __init__.py                    # ← Hace la diferencia
│   ├── utils.py
│   └── models.py
│
├── run_namespace_package.py           # Entry point ejemplo 1
└── run_regular_package.py             # Entry point ejemplo 2
```

## Cómo Ejecutar

### Desde el directorio `day_1`:

```bash
# Ejemplo 1: Namespace Package (sin __init__.py)
python examples/run_namespace_package.py

# Ejemplo 2: Regular Package (con __init__.py)
python examples/run_regular_package.py
```

### Desde el directorio raíz del proyecto:

```bash
# Ejemplo 1
python day_1/examples/run_namespace_package.py

# Ejemplo 2
python day_1/examples/run_regular_package.py
```

## Ejemplo 1: Namespace Package (SIN `__init__.py`)

### Estructura

```
namespace_package/
├── utils.py      # ← Sin __init__.py
└── models.py
```

### ✅ Qué FUNCIONA

```python
# Imports explícitos de módulos
from examples.namespace_package.utils import greet
from examples.namespace_package.models import User

greet("Alice")  # ✅ Funciona
user = User("Bob", "bob@example.com")  # ✅ Funciona
```

### ❌ Qué NO FUNCIONA

```python
# Import del paquete directamente
import examples.namespace_package as pkg
pkg.greet("Alice")  # ❌ AttributeError

# from package import *
from examples.namespace_package import *  # ❌ No importa nada útil
```

### Cuándo Usar

- **Plugins distribuidos**: Múltiples paquetes con el mismo nombre en diferentes ubicaciones
- **Extensiones**: Permitir que otros añadan módulos a tu namespace
- **Casos avanzados**: Cuando necesitas flexibilidad extrema

### Limitaciones

- No puedes acceder a funciones/clases directamente desde el paquete
- No hay control sobre la API pública
- No puedes definir metadata del paquete (`__version__`, etc.)
- Experiencia de usuario menos amigable

## Ejemplo 2: Regular Package (CON `__init__.py`)

### Estructura

```
regular_package/
├── __init__.py   # ← Hace la diferencia
├── utils.py
└── models.py
```

### Contenido de `__init__.py`

```python
"""Regular package with clean API."""

# Exponer funciones y clases
from .utils import greet, calculate_sum
from .models import User, Product

# Metadata
__version__ = "1.0.0"
__author__ = "Python Course"

# Control de exports
__all__ = ['greet', 'calculate_sum', 'User', 'Product']
```

### ✅ Qué FUNCIONA (TODO)

```python
# 1. Import del paquete directamente
import examples.regular_package as pkg
pkg.greet("Alice")  # ✅ Funciona
pkg.User("Bob", "bob@example.com")  # ✅ Funciona

# 2. from package import *
from examples.regular_package import *
greet("Charlie")  # ✅ Funciona

# 3. Imports selectivos
from examples.regular_package import greet, User

# 4. Metadata
print(pkg.__version__)  # ✅ "1.0.0"
```

### Ventajas

- ✅ **API limpia**: Usuarios pueden hacer `pkg.function()` directamente
- ✅ **Control**: Decides qué exponer con `__all__`
- ✅ **Metadata**: Puedes definir `__version__`, `__author__`, etc.
- ✅ **Inicialización**: Código que se ejecuta al importar el paquete
- ✅ **Mejor UX**: Experiencia más amigable para usuarios

### Cuándo Usar

- ✅ **Librerías públicas**: Cualquier paquete que otros usarán
- ✅ **APIs claras**: Cuando quieres simplificar imports
- ✅ **Proyectos profesionales**: Estándar de la industria
- ✅ **Siempre**: Es la mejor práctica por defecto

## Comparación Lado a Lado

| Característica | Namespace Package | Regular Package |
|----------------|-------------------|-----------------|
| `__init__.py` | ❌ No tiene | ✅ Tiene |
| `import pkg; pkg.func()` | ❌ No funciona | ✅ Funciona |
| `from pkg import *` | ❌ No útil | ✅ Funciona |
| `from pkg.mod import func` | ✅ Funciona | ✅ Funciona |
| Control de API | ❌ No | ✅ Sí (`__all__`) |
| Metadata | ❌ No | ✅ Sí |
| Inicialización | ❌ No | ✅ Sí |
| Plugins distribuidos | ✅ Sí | ❌ No |
| Uso recomendado | Casos avanzados | **Por defecto** |

## Experimentos Sugeridos

### 1. Modificar `__init__.py`

Edita `regular_package/__init__.py` y:

- Añade más funciones a `__all__`
- Cambia `__version__`
- Añade código de inicialización
- Observa cómo afecta al comportamiento

### 2. Crear tu Propio Paquete

```bash
# Crear estructura
mkdir my_package
touch my_package/__init__.py
touch my_package/utils.py

# Editar __init__.py
# from .utils import my_function
# __all__ = ['my_function']

# Probar
python -c "import my_package; my_package.my_function()"
```

### 3. Comparar Comportamiento

```python
# Inspeccionar namespace package
import examples.namespace_package as ns
print(hasattr(ns, '__file__'))  # False

# Inspeccionar regular package
import examples.regular_package as reg
print(hasattr(reg, '__file__'))  # True
print(reg.__file__)  # Ruta a __init__.py
```

## Preguntas Frecuentes

### ¿Cuándo NO usar `__init__.py`?

**Casi nunca.** Los únicos casos válidos son:

1. **Plugin systems**: Múltiples paquetes con el mismo nombre
2. **Extensiones distribuidas**: Permitir que otros añadan al namespace
3. **Casos muy específicos**: Cuando realmente necesitas namespace packages

### ¿Puede estar vacío `__init__.py`?

**Sí**, pero es mejor aprovecharlo:

```python
# __init__.py vacío (válido pero no óptimo)
# (archivo vacío)

# __init__.py mínimo (mejor)
"""My package."""
__version__ = "1.0.0"

# __init__.py completo (óptimo)
"""My package with clean API."""
from .utils import main_function
__version__ = "1.0.0"
__all__ = ['main_function']
```

### ¿Qué pasa si mezclo ambos enfoques?

```
my_package/
├── __init__.py          # ← Regular package
└── subpackage/
    ├── module.py        # ← Sin __init__.py (namespace)
    └── ...
```

**Resultado**: `my_package` es regular, `subpackage` es namespace. Funciona pero puede confundir. **Recomendación**: Usa `__init__.py` en todos los niveles.

## Recursos Adicionales

- [PEP 420 - Implicit Namespace Packages](https://peps.python.org/pep-0420/)
- [Python Packaging Guide](https://packaging.python.org/)
- [Real Python - Python Modules and Packages](https://realpython.com/python-modules-packages/)

## Conclusión

**Regla de oro**: **Siempre usa `__init__.py`** en tus paquetes.

- Es el estándar de la industria
- Proporciona mejor experiencia de usuario
- Te da control sobre la API pública
- Evita confusión

Los namespace packages son para casos muy específicos. Si tienes dudas, usa `__init__.py`.
