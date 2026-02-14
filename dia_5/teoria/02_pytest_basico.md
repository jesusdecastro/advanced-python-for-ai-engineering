# pytest Básico

## Contexto: Por Qué Importa

**Problema real en Data/IA**:

Tienes una función `normalize_whitespace` que limpia espacios en texto para NLP. Funciona con "hello  world" en tu notebook. Pero en producción recibe tabs, newlines, y espacios de distintos tipos (Unicode). Sin tests, no sabes si tu función maneja todos estos casos hasta que falla en producción.

**Ejemplo concreto**:

```python
def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())

# ¿Funciona con tabs? ¿Con newlines? ¿Con string vacío?
# ¿Con solo espacios? Sin tests, no lo sabes.
```

**Consecuencias de NO testear**:

- Descubres edge cases en producción, no en desarrollo
- Cada cambio puede romper casos que antes funcionaban
- No puedes refactorizar sin miedo
- Los nuevos miembros del equipo no saben qué comportamiento es correcto

## El Concepto

### Definición técnica

**pytest** es el framework de testing más usado en Python. Descubre automáticamente tus tests, ejecuta funciones que empiezan con `test_`, y reporta resultados de forma clara. No necesitas clases ni herencia — solo funciones con `assert`.

### Cómo funciona internamente

1. pytest busca ficheros `test_*.py` o `*_test.py`
2. Dentro de esos ficheros, busca funciones `def test_*()`
3. Ejecuta cada función de test en orden
4. Si un `assert` falla, captura el error y continúa con el siguiente test
5. Al final, muestra un resumen: cuántos pasaron, cuántos fallaron, y dónde

### Terminología clave

- **Test function**: Función que empieza con `test_` y contiene asserts
- **Test discovery**: Proceso automático de pytest para encontrar tests
- **Assertion**: Verificación con `assert` — si es False, el test falla
- **Patrón AAA**: Arrange (preparar), Act (ejecutar), Assert (verificar)
- **Test isolation**: Cada test es independiente — no comparten estado

## Instalación y Estructura

### Instalación

```bash
# Con uv (recomendado)
uv add --dev pytest pytest-cov

# Con pip
pip install pytest pytest-cov
```

### Estructura de proyecto

```
mi_proyecto/
├── pyproject.toml
├── src/
│   └── text_utils.py
└── tests/
    ├── __init__.py          # Vacío, pero necesario
    └── test_text_utils.py   # Prefijo test_ obligatorio
```

## Tu Primer Test

### Código bajo test

```python
# src/text_utils.py
def normalize_whitespace(text: str) -> str:
    """Reemplaza múltiples espacios por uno solo y hace strip."""
    return " ".join(text.split())
```

### Tests

```python
# tests/test_text_utils.py
from text_utils import normalize_whitespace

def test_normalize_removes_extra_spaces():
    # Arrange — preparar datos
    input_text = "hello   world"
    
    # Act — ejecutar código
    result = normalize_whitespace(input_text)
    
    # Assert — verificar resultado
    assert result == "hello world"

def test_normalize_strips_edges():
    assert normalize_whitespace("  hello  ") == "hello"

def test_normalize_empty_string():
    assert normalize_whitespace("") == ""

def test_normalize_tabs_and_newlines():
    assert normalize_whitespace("hello\t\nworld") == "hello world"
```

## Ejecución de Tests

### Comandos básicos

```bash
# Ejecutar todos los tests con output detallado
pytest tests/ -v

# Traceback compacto (útil cuando hay muchos fallos)
pytest tests/ -v --tb=short

# Solo listar tests sin ejecutarlos (dry-run)
pytest tests/ -v --co

# Ejecutar un test específico
pytest tests/test_text_utils.py::test_normalize_empty_string -v

# Con cobertura
pytest tests/ -v --cov=src --cov-report=term-missing
```

### Output de pytest

```
tests/test_text_utils.py::test_normalize_removes_extra_spaces PASSED  ←
tests/test_text_utils.py::test_normalize_strips_edges PASSED          ←
tests/test_text_utils.py::test_normalize_empty_string FAILED          ←
tests/test_text_utils.py::test_normalize_tabs ERROR                   ←
```

**Símbolos**:
- `.` / `PASSED`: el test pasó
- `F` / `FAILED`: el assert falló — tu código no hace lo esperado
- `E` / `ERROR`: excepción inesperada antes del assert — error en el test o en tu código

## El Patrón AAA

### Por Qué Importa

Sin estructura clara, los tests se vuelven difíciles de leer y mantener. El patrón AAA (Arrange, Act, Assert) es una convención que hace que cada test sea obvio: qué preparas, qué ejecutas, qué verificas.

### Estructura

```python
def test_example():
    # ARRANGE — preparar datos y estado
    input_data = "test input"
    expected_output = "expected result"
    
    # ACT — ejecutar el código bajo test
    result = my_function(input_data)
    
    # ASSERT — verificar el resultado
    assert result == expected_output
```

### Ejemplo Real

```python
def test_remove_accents_from_spanish_text():
    # ARRANGE
    text_with_accents = "café résumé"
    expected_clean_text = "cafe resume"
    
    # ACT
    result = remove_accents(text_with_accents)
    
    # ASSERT
    assert result == expected_clean_text
    assert "é" not in result
    assert "á" not in result
```

## Convenciones de pytest

### Nombres de ficheros y funciones

```python
# Correcto
# tests/test_text_utils.py
def test_normalize_whitespace():
    ...

def test_remove_accents():
    ...

# Incorrecto — pytest no los descubre
# tests/utils_test.py  (debe ser test_*.py)
def check_normalize():  # (debe ser test_*)
    ...
```

### Nombres descriptivos

```python
# Mal — no dice qué verifica
def test_normalize():
    assert normalize_whitespace("  hello  ") == "hello"

def test_normalize_2():
    assert normalize_whitespace("") == ""

# Bien — nombre describe el comportamiento
def test_normalize_strips_leading_and_trailing_spaces():
    assert normalize_whitespace("  hello  ") == "hello"

def test_normalize_handles_empty_string():
    assert normalize_whitespace("") == ""
```

## Ejemplo Incorrecto

```python
# Test sin estructura clara
def test_stuff():
    result = process_data("input", True, 42, None)
    assert result
    # ¿Qué verifica? ¿Por qué estos inputs?
    # ¿Qué debería ser result exactamente?

# Tests que dependen del orden
counter = 0

def test_increment():
    global counter
    counter += 1
    assert counter == 1

def test_increment_again():
    global counter  # ¡Depende del test anterior!
    counter += 1
    assert counter == 2  # Falla si se ejecuta solo
```

**Problemas**:

- Sin patrón AAA — difícil saber qué se está testeando
- Nombres genéricos — no describen el comportamiento
- Estado compartido — tests no son independientes
- Assert ambiguo — `assert result` no dice qué se espera

## Ejemplo Correcto

```python
def test_process_data_with_valid_input_returns_cleaned_dict():
    # ARRANGE
    raw_input = "  Hello World  "
    normalize = True
    max_length = 50
    default_value = None
    
    expected = {
        "text": "hello world",
        "length": 11,
        "truncated": False
    }
    
    # ACT
    result = process_data(raw_input, normalize, max_length, default_value)
    
    # ASSERT
    assert result == expected
    assert result["text"].islower()
    assert len(result["text"]) <= max_length

def test_process_data_with_empty_string_returns_default():
    # ARRANGE
    raw_input = ""
    default_value = "N/A"
    
    # ACT
    result = process_data(raw_input, False, 100, default_value)
    
    # ASSERT
    assert result["text"] == "N/A"
    assert result["length"] == 0
```

**Ventajas**:

- Patrón AAA claro — fácil de leer
- Nombres descriptivos — sabes qué verifica cada test
- Tests independientes — pueden ejecutarse en cualquier orden
- Asserts explícitos — verifican comportamiento específico

## Aprendizaje Clave

**Puntos críticos a recordar**:

1. pytest descubre automáticamente tests — solo sigue las convenciones de nombres
2. El patrón AAA hace que tus tests sean legibles y mantenibles
3. Cada test debe ser independiente — sin estado compartido

**Cómo desarrollar intuición**:

- **Pregúntate**: "¿Puedo leer este test y entender qué verifica sin ver el código?"
  - Si NO → mejora el nombre y la estructura AAA
  - Si SÍ → buen test

**Cuándo usar / NO usar**:

- **Usar pytest cuando**:
  - Escribes cualquier código Python que necesita tests
  - Quieres tests rápidos y fáciles de escribir
  - Necesitas descubrimiento automático de tests
  
- **NO usar pytest para**:
  - Tests de performance (usa pytest-benchmark)
  - Tests de carga (usa locust o similar)

**Referencia oficial**: [pytest Documentation - How to write and report assertions](https://docs.pytest.org/en/stable/how-to/assert.html)

## Resumen

pytest es el framework estándar para testing en Python. Sigue convenciones simples (`test_*.py`, `def test_*()`), usa `assert` nativo, y descubre tests automáticamente. El patrón AAA (Arrange, Act, Assert) estructura cada test de forma clara. Nombres descriptivos y tests independientes son esenciales para mantenibilidad.
