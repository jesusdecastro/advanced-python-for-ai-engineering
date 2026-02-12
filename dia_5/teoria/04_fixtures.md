# Fixtures: Setup Reutilizable

## 🎯 Contexto: Por Qué Importa

**Problema real en Data/IA**:

Muchos tests necesitan los mismos datos de preparación: una lista de registros, un dataframe de ejemplo, una configuración válida, un directorio con ficheros. Sin fixtures, copias el mismo código de setup en cada test.

**Ejemplo concreto**:

Tienes 10 tests que procesan una lista de registros de usuarios. Cada test copia las mismas 20 líneas de setup. Cuando cambias la estructura de los datos, editas 10 tests.

**Consecuencias de NO usar fixtures**:

- Código duplicado en cada test
- Cambiar datos de test requiere editar N ficheros
- Difícil distinguir el setup del test real
- Riesgo de contaminación entre tests si usas variables globales

## 📚 El Concepto

### Definición técnica

Una **fixture** es una función decorada con `@pytest.fixture` que prepara datos o estado para tests. pytest la ejecuta automáticamente antes de cada test que la solicite (por nombre de parámetro), garantizando aislamiento.

### Cómo funciona internamente

1. Defines una función con `@pytest.fixture`
2. En tu test, añades un parámetro con el mismo nombre que la fixture
3. pytest detecta el parámetro, ejecuta la fixture, e inyecta el resultado
4. Cada test recibe una copia fresca (scope `function` por defecto)

### Terminología clave

- **Fixture**: Función de setup reutilizable
- **Scope**: Cuándo se ejecuta la fixture (`function`, `module`, `session`)
- **Dependency injection**: pytest inyecta fixtures por nombre de parámetro
- **Teardown**: Código de limpieza después del test (con `yield`)

## ❌ Ejemplo Incorrecto

```python
# El mismo setup copiado en cada test
def test_filter_valid_records():
    records = [
        {"name": "Alice", "age": 30, "email": "alice@test.com"},
        {"name": "Bob", "age": -5, "email": "bob@test.com"},
        {"name": "", "age": 25, "email": "invalid"},
        {"name": "Carol", "age": 45, "email": "carol@test.com"},
    ]
    result = filter_valid_records(records)
    assert len(result) == 2

def test_count_invalid_records():
    records = [
        {"name": "Alice", "age": 30, "email": "alice@test.com"},
        {"name": "Bob", "age": -5, "email": "bob@test.com"},
        {"name": "", "age": 25, "email": "invalid"},
        {"name": "Carol", "age": 45, "email": "carol@test.com"},
    ]
    result = count_invalid_records(records)
    assert result == 2
```

**Problemas**:

- Mismo bloque de datos copiado múltiples veces
- Si cambias la estructura, editas N sitios
- Difícil distinguir setup del test real
- Ruido visual

## ✅ Ejemplo Correcto

```python
import pytest

@pytest.fixture
def sample_records():
    """Registros de ejemplo con mezcla de válidos e inválidos."""
    return [
        {"name": "Alice", "age": 30, "email": "alice@test.com"},
        {"name": "Bob", "age": -5, "email": "bob@test.com"},
        {"name": "", "age": 25, "email": "invalid"},
        {"name": "Carol", "age": 45, "email": "carol@test.com"},
    ]

def test_filter_valid_records(sample_records):
    # sample_records se inyecta automáticamente
    result = filter_valid_records(sample_records)
    assert len(result) == 2

def test_count_invalid_records(sample_records):
    result = count_invalid_records(sample_records)
    assert result == 2

def test_extract_emails(sample_records):
    result = extract_emails(sample_records)
    assert "alice@test.com" in result
```

**Ventajas**:

- Datos definidos una vez, usados por muchos tests
- Cada test recibe una copia fresca (aislamiento)
- El test es solo Act + Assert — setup invisible
- Cambiar datos se hace en un solo lugar

## Scopes de Fixtures

### Function Scope (default)

```python
@pytest.fixture(scope="function")  # Default
def fresh_records():
    """Se ejecuta para CADA test."""
    return [...]
```

### Module Scope

```python
@pytest.fixture(scope="module")
def db_connection():
    """Se ejecuta UNA VEZ por fichero de test."""
    conn = create_connection()
    yield conn          # yield en vez de return → teardown después
    conn.close()        # Esto se ejecuta al acabar todos los tests del módulo
```

### Session Scope

```python
@pytest.fixture(scope="session")
def ml_model():
    """Se ejecuta UNA VEZ para toda la sesión de pytest."""
    return load_model("model.pkl")  # Costoso — solo lo haces una vez
```

## conftest.py: Fixtures Compartidas

### Por Qué Importa

Si múltiples ficheros de test necesitan las mismas fixtures, puedes definirlas en `conftest.py`. pytest lo descubre automáticamente y las hace disponibles para todos los tests.

### Ejemplo

```python
# tests/conftest.py
import pytest

@pytest.fixture
def sample_config():
    """Configuración base usable por cualquier test."""
    return {
        "input_path": "/data/input",
        "output_path": "/data/output",
        "batch_size": 32,
    }
```

```python
# tests/test_pipeline.py
def test_load_config(sample_config):
    # sample_config está disponible sin importar
    assert sample_config["batch_size"] == 32
```

### Reglas de conftest.py

- pytest lo descubre automáticamente — no hace falta importarlo
- Fixtures definidas aquí están disponibles para todos los tests del directorio y subdirectorios
- Puedes tener múltiples `conftest.py` a diferentes niveles del árbol

## Fixtures con Teardown

### Ejemplo

```python
@pytest.fixture
def temp_database():
    """Crea una BD temporal y la limpia después."""
    db = create_test_database()
    db.connect()
    
    yield db  # El test recibe db aquí
    
    # Teardown — se ejecuta después del test
    db.disconnect()
    db.delete()
```

## 💡 Aprendizaje Clave

**Puntos críticos a recordar**:

1. Fixtures eliminan duplicación de setup entre tests
2. Cada test recibe datos frescos (scope `function` por defecto)
3. `conftest.py` para fixtures compartidas entre ficheros

**Cómo desarrollar intuición**:

- **Pregúntate**: "¿Estoy copiando el mismo setup en múltiples tests?"
  - Si SÍ → crea una fixture
  - Si NO → setup inline está bien

**Cuándo usar / NO usar**:

- ✅ **Usar fixtures cuando**:
  - Múltiples tests necesitan los mismos datos
  - El setup es complejo o costoso
  - Quieres garantizar aislamiento entre tests
  
- ❌ **NO usar fixtures para**:
  - Setup trivial de una línea
  - Datos que solo usa un test

**Referencia oficial**: [pytest Documentation - Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

## Resumen

Las fixtures son funciones de setup reutilizables que pytest inyecta automáticamente en tests. Eliminan duplicación, garantizan aislamiento, y hacen que los tests sean más legibles. Usa `conftest.py` para fixtures compartidas entre ficheros.
