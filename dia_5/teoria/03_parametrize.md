# Parametrize: Testing con Tablas de Datos

## Contexto: Por Qué Importa

**Problema real en Data/IA**:

En data engineering y NLP, las funciones de transformación son el pan de cada día: limpiar texto, validar formatos, convertir tipos, normalizar valores. Cada una necesita testearse con muchos inputs diferentes — strings vacíos, Unicode, caracteres especiales, valores límite.

Sin `parametrize`, acabas con docenas de funciones de test casi idénticas que solo cambian el input y el expected. Es código duplicado que viola DRY y es tedioso de mantener.

**Ejemplo concreto**:

Tienes una función `remove_accents` que elimina acentos de texto. Necesitas testearla con: á, é, í, ó, ú, ñ, ü, texto sin acentos, string vacío, texto mixto. Sin `parametrize`, escribes 10 funciones casi idénticas.

**Consecuencias de NO usar parametrize**:

- Código duplicado — violación de DRY
- Difícil añadir casos nuevos — copiar/pegar función entera
- Difícil ver qué casos están cubiertos de un vistazo
- Si cambias la firma de la función, editas N tests

## El Concepto

### Definición técnica

`@pytest.mark.parametrize` es un decorador que ejecuta el mismo test con múltiples conjuntos de inputs. Defines una tabla de datos (inputs y expected outputs) y pytest ejecuta el test una vez por cada fila, reportando cada ejecución independientemente.

### Cómo funciona internamente

1. Defines una lista de tuplas con inputs y expected outputs
2. pytest genera un test independiente por cada tupla
3. Cada test se ejecuta aisladamente — si uno falla, los demás continúan
4. El output muestra exactamente qué caso falló

### Terminología clave

- **Parametrize**: Decorador que genera múltiples tests desde una tabla de datos
- **Test case**: Cada fila de la tabla — un conjunto de inputs/outputs
- **Test ID**: Identificador opcional para cada caso (mejora legibilidad del output)

## Ejemplo Incorrecto

```python
# Cinco funciones de test casi idénticas — solo cambia el input
def test_remove_accents_a():
    assert remove_accents("á") == "a"

def test_remove_accents_e():
    assert remove_accents("é") == "e"

def test_remove_accents_n():
    assert remove_accents("ñ") == "n"

def test_remove_accents_u_umlaut():
    assert remove_accents("ü") == "u"

def test_remove_accents_full_word():
    assert remove_accents("café") == "cafe"

def test_remove_accents_no_accents():
    assert remove_accents("hello") == "hello"

def test_remove_accents_empty():
    assert remove_accents("") == ""
```

**Problemas**:

- 7 funciones que hacen exactamente lo mismo con distinto input — violación de DRY
- Si cambias la firma de `remove_accents`, tienes que editar 7 funciones
- Añadir un caso nuevo requiere copiar/pegar otra función entera
- Difícil ver de un vistazo qué casos están cubiertos
- Los nombres de test son genéricos y no aportan contexto de negocio

## Ejemplo Correcto

```python
import pytest

@pytest.mark.parametrize("input_text, expected", [
    ("á", "a"),
    ("é", "e"),
    ("ñ", "n"),
    ("ü", "u"),
    ("café résumé", "cafe resume"),
    ("hello", "hello"),         # caso trivial — sin acentos
    ("", ""),                   # caso borde — vacío
    ("   ", "   "),             # caso borde — solo espacios
])
def test_remove_accents(input_text, expected):
    assert remove_accents(input_text) == expected
```

**Ventajas**:

- Una sola función, muchos casos — DRY
- Tabla visible: ves todos los inputs/outputs de un vistazo
- Cada caso se ejecuta independientemente — un fallo no oculta otros
- Añadir un caso es añadir una línea, no copiar una función
- pytest muestra exactamente qué caso falló

### Output de pytest

```
test_text.py::test_remove_accents[á-a] PASSED
test_text.py::test_remove_accents[é-e] PASSED
test_text.py::test_remove_accents[ñ-n] FAILED    ← ¿Tu función no maneja ñ?
test_text.py::test_remove_accents[ü-u] PASSED
```

## IDs Descriptivos

### Por Qué Importa

Los IDs por defecto de pytest son los valores de los parámetros. Para casos complejos, puedes añadir IDs descriptivos que mejoran la legibilidad del output.

### Ejemplo

```python
@pytest.mark.parametrize("input_text, expected", [
    pytest.param("$19.99", "1999", id="precio-con-simbolo"),
    pytest.param("hello world", "hello world", id="texto-limpio"),
    pytest.param("", "", id="vacio"),
    pytest.param("@#$%", "", id="solo-especiales"),
    pytest.param("café_2024", "caf_2024", id="mixto-unicode-numeros"),
])
def test_remove_special_chars(input_text, expected):
    assert remove_special_chars(input_text) == expected
```

### Output con IDs

```
test_text.py::test_remove_special_chars[precio-con-simbolo] PASSED
test_text.py::test_remove_special_chars[texto-limpio] PASSED
test_text.py::test_remove_special_chars[vacio] PASSED
test_text.py::test_remove_special_chars[solo-especiales] FAILED
```

## Múltiples Parámetros

### Ejemplo

```python
@pytest.mark.parametrize("text, max_length, expected", [
    ("hello", 10, "hello"),
    ("hello world", 5, "hello"),
    ("hello", 3, "hel"),
    ("", 10, ""),
])
def test_truncate_text(text, max_length, expected):
    assert truncate_text(text, max_length) == expected
```

## Casos de Uso Comunes

### Funciones de transformación

```python
@pytest.mark.parametrize("input_val, expected", [
    ("123", 123),
    ("0", 0),
    ("-42", -42),
    ("", None),
    ("abc", None),
])
def test_parse_int(input_val, expected):
    assert parse_int(input_val) == expected
```

### Validaciones

```python
@pytest.mark.parametrize("email, is_valid", [
    ("user@example.com", True),
    ("user.name@example.co.uk", True),
    ("user+tag@example.com", True),
    ("bad-email", False),
    ("@example.com", False),
    ("user@", False),
    ("", False),
])
def test_validate_email(email, is_valid):
    assert validate_email(email) == is_valid
```

### Parsers

```python
@pytest.mark.parametrize("log_line, expected", [
    ("2024-01-15 ERROR Database connection failed", 
     {"date": "2024-01-15", "level": "ERROR", "message": "Database connection failed"}),
    ("2024-01-15 INFO Started successfully", 
     {"date": "2024-01-15", "level": "INFO", "message": "Started successfully"}),
    ("", None),
    ("malformed log", None),
])
def test_parse_log_line(log_line, expected):
    assert parse_log_line(log_line) == expected
```

## Aprendizaje Clave

**Puntos críticos a recordar**:

1. `parametrize` elimina duplicación en tests con múltiples inputs
2. Cada caso se ejecuta independientemente — un fallo no oculta otros
3. La tabla de datos es visible — fácil ver qué casos están cubiertos

**Cómo desarrollar intuición**:

- **Pregúntate**: "¿Estoy copiando el mismo test cambiando solo el input?"
  - Si SÍ → usa `parametrize`
  - Si NO → tests separados están bien

**Cuándo usar / NO usar**:

- **Usar parametrize cuando**:
  - Testeas la misma función con muchos inputs distintos
  - Funciones de transformación, validaciones, parsers
  - Quieres ver todos los casos de un vistazo
  
- **NO usar parametrize cuando**:
  - Los tests verifican comportamientos diferentes
  - El setup (Arrange) es distinto para cada caso
  - Los asserts son diferentes

**Referencia oficial**: [pytest Documentation - Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)

## Resumen

`@pytest.mark.parametrize` te permite definir una tabla de inputs/outputs y ejecutar el mismo test con cada fila. Es esencial para funciones de transformación en data/NLP donde necesitas testear muchos casos. Elimina duplicación, mejora legibilidad, y cada caso se ejecuta independientemente.
