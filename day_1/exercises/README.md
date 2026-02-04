# Ejercicios - Día 1: Type Hinting

## Descripción

Esta carpeta contiene ejercicios prácticos para el notebook de Type Hinting. **Tu tarea es agregar type hints a código ya implementado**, no implementar la lógica.

## Estructura

```
exercises/
├── 02_type_hinting.py          # Código SIN type hints (tu tarea: agregarlos)
├── tests/
│   └── test_02_type_hinting.py # Tests funcionales + validación Pyright
└── README.md                    # Este archivo
```

## Objetivo del Ejercicio

El código en `02_type_hinting.py` **ya está implementado y funciona correctamente**, pero le faltan:

1. **Type hints** en parámetros de funciones
2. **Type hints** en valores de retorno
3. **Type hints** en atributos de clases
4. **Anotaciones Sphinx** en docstrings (:param, :type, :return, :rtype)

Tu trabajo es agregar todos los type hints necesarios para que Pyright no reporte ningún error.

## Cómo Trabajar con los Ejercicios

### 1. Abre el archivo de ejercicios

```bash
# Desde la carpeta day_1
code exercises/02_type_hinting.py
```

### 2. Lee el código y entiende qué hace cada función

Cada función ya está implementada. Lee el código y los ejemplos en los docstrings para entender:
- Qué tipo de parámetros recibe
- Qué tipo de valor retorna
- Si puede retornar None (Optional)

### 3. Agrega los type hints

Reemplaza las líneas que dicen `# TODO` con los type hints correctos.

**Ejemplo:**

```python
# ANTES (sin type hints)
def calculate_rectangle_area(width, height):
    return width * height

# DESPUÉS (con type hints)
def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height
```

### 4. Actualiza los docstrings

Agrega las anotaciones Sphinx en los docstrings:

```python
"""
Calculate the area of a rectangle.

:param width: Width of the rectangle
:type width: float
:param height: Height of the rectangle
:type height: float
:return: Area of the rectangle
:rtype: float
"""
```

### 5. Valida con Pyright

```bash
# Desde la carpeta day_1
pyright exercises/02_type_hinting.py
```

Pyright debe reportar **0 errores**.

### 6. Ejecuta los tests

```bash
# Desde la carpeta day_1
pytest exercises/tests/test_02_type_hinting.py -v
```

Los tests validan:
- ✓ Que el código funcione correctamente (tests funcionales)
- ✓ Que Pyright no reporte errores (validación de type hints)

## Ejercicios

### Ejercicio 1: `calculate_rectangle_area`

**Tarea:** Agregar type hints básicos (float → float)

**Pistas:**
- Recibe dos números decimales
- Retorna un número decimal

---

### Ejercicio 2: `calculate_statistics`

**Tarea:** Agregar type hints para list y dict

**Pistas:**
- Recibe una lista de floats
- Retorna un diccionario con claves string y valores float
- Puede lanzar ValueError

---

### Ejercicio 3: `process_value`

**Tarea:** Agregar union type (int | str)

**Pistas:**
- El parámetro puede ser int O str
- Siempre retorna str
- Usa la sintaxis `int | str` (Python 3.10+)

---

### Ejercicio 4: `find_user`

**Tarea:** Agregar Optional type

**Pistas:**
- Recibe un int
- Puede retornar un dict o None
- Usa `Optional[dict[str, str]]` o `dict[str, str] | None`
- Necesitas importar Optional de typing

---

### Ejercicio 5: `DataProcessor` (Clase)

**Tarea:** Agregar type hints a todos los métodos y atributos

**Pistas:**
- `__init__` retorna None
- `self.name` es str
- `self.data` es list[float]
- `get_average()` puede retornar float o None
- `get_data()` retorna list[float]

---

### Ejercicio 6: `validate_and_process` (Avanzado)

**Tarea:** Agregar type hints complejos (union + tuple)

**Pistas:**
- Parámetro puede ser int, str o float
- Retorna una tupla de (bool, resultado)
- El resultado puede ser str, float o None
- Usa `tuple[bool, str | float | None]`

---

## Imports Necesarios

Necesitarás importar tipos del módulo `typing`:

```python
from typing import Optional
```

Para Python 3.10+, puedes usar la sintaxis moderna:
- `int | str` en lugar de `Union[int, str]`
- `dict[str, str] | None` en lugar de `Optional[dict[str, str]]`

## Validación Completa

### 1. Pyright debe pasar sin errores

```bash
pyright exercises/02_type_hinting.py
```

Salida esperada:
```
0 errors, 0 warnings, 0 informations
```

### 2. Tests deben pasar

```bash
pytest exercises/tests/test_02_type_hinting.py -v
```

Salida esperada:
```
======================== 31 passed in 0.20s ========================
```

(31 tests: 30 funcionales + 1 validación Pyright)

### 3. Ruff debe pasar

```bash
ruff check exercises/02_type_hinting.py
```

### 4. Formato correcto

```bash
ruff format exercises/02_type_hinting.py
```

## Solución de Problemas

### "ModuleNotFoundError: No module named 'exercises'"

Asegúrate de estar ejecutando pytest desde la carpeta `day_1`:

```bash
cd day_1
pytest exercises/tests/test_02_type_hinting.py -v
```

### "FAILED - AssertionError"

Lee el mensaje de error cuidadosamente. Pytest te mostrará:
- Qué test falló
- Qué valor esperaba
- Qué valor recibió

### Los tests pasan pero Pyright reporta errores

Verifica que:
- Los type hints sean correctos
- No haya variables sin tipo
- Los tipos de retorno sean correctos

## Próximos Pasos

Una vez completes todos los ejercicios:

1. Verifica que todos los tests pasen
2. Valida con Pyright
3. Formatea con Ruff
4. Revisa tu código con un compañero
5. Pasa al siguiente notebook

¡Buena suerte!
