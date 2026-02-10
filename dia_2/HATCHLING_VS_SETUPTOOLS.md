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

### Opción 1: Setuptools (Recomendado con find_packages)

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mi-paquete"
version = "0.1.0"

[tool.setuptools.packages.find]
where = ["src"]
```

**Nota**: `find_packages()` busca automáticamente todos los paquetes en `src/`, similar a Hatchling.

### Opción 2: Hatchling (Recomendado)

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mi-paquete"
version = "0.1.0"

# Hatchling detecta automáticamente src/mi_paquete/ y todos sus submódulos
```

---

## Cómo Hacer que tus Imports Funcionen

### Paso 1: Instala tu Paquete en Modo Desarrollo

```bash
# Desde la raíz del proyecto (donde está pyproject.toml)
pip install -e .
```

El flag `-e` (editable) instala tu paquete en modo desarrollo. Los cambios en tu código se reflejan inmediatamente sin reinstalar.

### Paso 2: Verifica que los Imports Funcionan

```python
# Desde cualquier lugar, deberías poder hacer:
from mi_paquete.utils.helpers import mi_funcion
from mi_paquete.models.data import MiClase
```

---

## Migración Rápida: Setuptools → Hatchling

Si tu proyecto usa Setuptools y quieres cambiarlo a Hatchling:

### Antes (Setuptools con find_packages)
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "data-processor"
version = "1.0.0"

[tool.setuptools.packages.find]
where = ["src"]
```

### Después (Hatchling)
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "data-processor"
version = "1.0.0"

# ¡Elimina toda la sección [tool.setuptools]!
```

### Reinstala el Paquete
```bash
pip install -e .
```

---

## Tabla Comparativa: Lo Esencial

| Aspecto | Setuptools (find_packages) | Hatchling |
|---------|---------------------------|-----------|
| **Configuración para src/ layout** | `packages.find` + `where` | Automática (sin config) |
| **Añadir nuevo submódulo** | Nada, se detecta automáticamente | Nada, se detecta automáticamente |
| **Líneas de configuración** | ~2 líneas extra | 0 líneas extra |
| **Riesgo de error** | Bajo (auto-detecta) | Bajo (auto-detecta) |
| **Simplicidad** | Media | Alta |
| **Madurez** | Muy estable (años en producción) | Moderno (más reciente) |

---

## Cuándo Usar Cada Uno

### Usa Hatchling Si:
- Empiezas un proyecto nuevo
- Usas estructura `src/`
- Quieres menos configuración manual
- **Recomendado para este curso**

### Usa Setuptools Si:
- Mantienes un proyecto legacy existente
- Tu equipo ya tiene configuración Setuptools funcionando
- Necesitas compatibilidad con Python < 3.7

---

## Comandos Esenciales

```bash
# Instalar en modo desarrollo (ambos backends)
pip install -e .

# Instalar con dependencias de desarrollo
pip install -e ".[dev]"

# Verificar que el paquete está instalado
pip list | grep mi-paquete

# Construir el paquete (opcional, para distribución)
python -m build
```

---

## Preguntas Frecuentes

### ¿Por qué mis imports no funcionan?
1. Verifica que instalaste el paquete: `pip install -e .`
2. Verifica que tu estructura tiene `__init__.py` en cada carpeta
3. Verifica que el nombre en `pyproject.toml` coincide con la carpeta en `src/`

### ¿Necesito cambiar mi código Python?
No. El build backend solo afecta la configuración, no tu código.

### ¿Puedo cambiar de Setuptools a Hatchling?
Sí. Solo cambia el `[build-system]` y elimina `[tool.setuptools]`, luego reinstala con `pip install -e .`

### ¿Por qué no necesito package-dir con packages.find?

El parámetro `where` en `packages.find` ya le dice a setuptools dónde buscar. `package-dir` es para configuración manual de paquetes, no para auto-descubrimiento.

**Correcto (auto-descubrimiento)**:
```toml
[tool.setuptools.packages.find]
where = ["src"]  # Busca automáticamente en src/
```

**Incorrecto (redundante)**:
```toml
[tool.setuptools]
package-dir = {"" = "src"}  # ❌ No necesario con packages.find

[tool.setuptools.packages.find]
where = ["src"]  # Ya indica dónde buscar
```

---

## Recomendación para el Curso

**Usa Hatchling** en tus proyectos integradores:
- Menos configuración = menos errores
- Auto-descubrimiento = menos mantenimiento
- Enfócate en el código, no en la configuración

**Configuración mínima recomendada:**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "tu-proyecto"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "pandas>=2.0.0",
    "pydantic>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "ruff>=0.1.0",
]
```

Luego instala: `pip install -e ".[dev]"` y tus imports funcionarán.
