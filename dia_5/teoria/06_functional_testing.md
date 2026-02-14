# Functional Testing: La Capa I/O con tmp_path

## Contexto: Por Qué Importa

**Problema real en Data/IA**:

Los unit tests con mocks verifican tu lógica aislada. Pero en data engineering, los bugs más peligrosos viven en la capa I/O: encodings rotos que corrompen caracteres Unicode, ficheros CSV con newlines inconsistentes, JSON con BOM invisible, paths con espacios o caracteres especiales.

Los mocks no detectan estos problemas porque simulan un mundo perfecto. Los functional tests usan ficheros reales en un directorio temporal, verificando que tu código funciona con I/O real de principio a fin.

**Ejemplo concreto**:

Tu función `process_csv_to_json` funciona perfectamente con mocks. En producción, recibe un CSV con caracteres Unicode (María, Zürich) y encoding UTF-8 con BOM. El JSON de salida tiene caracteres corruptos. Sin functional tests con ficheros reales, no detectas este bug hasta producción.

**Consecuencias de NO usar functional tests**:

- Bugs de encoding que corrompen datos Unicode
- Problemas con newlines inconsistentes (\\n vs \\r\\n)
- Paths con espacios o caracteres especiales que fallan
- JSON con BOM invisible que rompe parsers
- Ficheros que se crean pero están vacíos o corruptos

## El Concepto

### Definición técnica

Un **functional test** verifica un flujo completo de entrada → salida con I/O real. En vez de mockear ficheros, creas ficheros reales en un directorio temporal (`tmp_path`), ejecutas tu código, y verificas que el output es correcto.

### Cómo funciona internamente

1. pytest crea un directorio temporal único para cada test
2. Tu test crea ficheros reales en ese directorio
3. Ejecutas tu código que lee/escribe esos ficheros
4. Verificas que los ficheros de salida son correctos
5. pytest borra automáticamente el directorio al terminar

### Terminología clave

- **Functional test**: Test que verifica entrada → salida con I/O real
- **tmp_path**: Fixture de pytest que proporciona un directorio temporal
- **Pathlib.Path**: API moderna de Python para trabajar con paths
- **write_text() / read_text()**: Métodos convenientes para ficheros de texto

## Ejemplo Incorrecto

```python
import os

# Tests que crean ficheros en rutas fijas — contaminan el sistema
def test_csv_processing():
    """Test que deja basura en disco y falla en CI."""
    with open("/tmp/test_input.csv", "w") as f:
        f.write("name,age\\nAlice,30\\n")
    
    process_csv("/tmp/test_input.csv", "/tmp/test_output.json")
    
    with open("/tmp/test_output.json") as f:
        result = json.load(f)
    
    assert len(result) == 1
    
    # ¿Quién limpia /tmp/test_input.csv y /tmp/test_output.json?
    # ¿Qué pasa si dos tests usan el mismo nombre de fichero?
    # ¿Funciona en Windows donde /tmp no existe?
    os.remove("/tmp/test_input.csv")   # Si el test falla antes, no se limpia
    os.remove("/tmp/test_output.json")
```

**Problemas**:

- Ficheros en rutas fijas — conflictos entre tests y entre devs
- Limpieza manual — si el test falla, los ficheros quedan en disco
- No portable — `/tmp` no existe en Windows
- No aislado — un test puede leer restos del test anterior

## Ejemplo Correcto

```python
import csv
import json
import pytest

# --- Función bajo test ---

def process_csv_to_json(input_path: str, output_path: str) -> int:
    """Lee un CSV, lo convierte a lista de dicts y lo guarda como JSON."""
    with open(input_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = list(reader)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    
    return len(records)

# --- Functional tests con tmp_path ---

def test_csv_to_json_basic(tmp_path):
    """Conversión básica CSV → JSON con datos normales."""
    # ARRANGE: crear fichero CSV real en directorio temporal
    csv_file = tmp_path / "input.csv"
    csv_file.write_text("name,age,city\\nAlice,30,Madrid\\nBob,25,Barcelona\\n")
    
    json_file = tmp_path / "output.json"
    
    # ACT
    count = process_csv_to_json(str(csv_file), str(json_file))
    
    # ASSERT
    assert count == 2
    assert json_file.exists()
    
    result = json.loads(json_file.read_text())
    assert len(result) == 2
    assert result[0]["name"] == "Alice"
    assert result[1]["city"] == "Barcelona"

def test_csv_to_json_empty_file(tmp_path):
    """CSV con solo headers → JSON con lista vacía."""
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("name,age,city\\n")
    
    json_file = tmp_path / "output.json"
    count = process_csv_to_json(str(csv_file), str(json_file))
    
    assert count == 0
    result = json.loads(json_file.read_text())
    assert result == []

def test_csv_to_json_preserves_unicode(tmp_path):
    """CSV con caracteres Unicode → JSON los preserva correctamente."""
    csv_file = tmp_path / "unicode.csv"
    csv_file.write_text(
        "name,city\\nMaría,Logroño\\nRené,Zürich\\n",
        encoding="utf-8",
    )
    
    json_file = tmp_path / "output.json"
    process_csv_to_json(str(csv_file), str(json_file))
    
    result = json.loads(json_file.read_text(encoding="utf-8"))
    assert result[0]["name"] == "María"
    assert result[1]["city"] == "Zürich"
```

**Ventajas**:

- Cada test tiene su propio directorio temporal — aislamiento total
- pytest limpia automáticamente — sin ficheros huérfanos
- Ficheros reales detectan bugs de encoding, formato, y edge cases de I/O
- `pathlib.Path` con `write_text()` / `read_text()` es más legible que `open()`
- Funciona en cualquier SO (Linux, macOS, Windows)

## Cuándo Usar Functional Tests vs Mocks

| Escenario | Recomendación | Por Qué |
|-----------|---------------|---------|
| Función que transforma datos en memoria | Unit test (sin I/O) | No hay I/O que testear |
| Función que lee/escribe ficheros locales | Functional test con tmp_path | Detecta bugs de encoding, formato |
| Función que llama a API externa | Unit test con mock | No quieres depender de la API |
| Función que lee fichero y llama a API | Functional para fichero + mock para API | Lo mejor de ambos mundos |
| Pipeline completo local (CSV → proceso → CSV) | Functional test end-to-end | Verifica el flujo completo con I/O real |

## Fixture Reutilizable para Ficheros de Test

```python
# tests/conftest.py
import pytest

@pytest.fixture
def sample_csv_file(tmp_path):
    """Genera un CSV de ejemplo y devuelve su path."""
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(
        "id,name,score\\n"
        "1,Alice,95.5\\n"
        "2,Bob,87.3\\n"
        "3,Carol,92.1\\n"
    )
    return csv_file

@pytest.fixture
def sample_jsonl_file(tmp_path):
    """Genera un fichero JSONL de ejemplo y devuelve su path."""
    jsonl_file = tmp_path / "sample.jsonl"
    lines = [
        '{"timestamp": "2024-01-15T10:30:00", "severity": "INFO", "message": "Started"}',
        '{"timestamp": "2024-01-15T10:31:00", "severity": "ERROR", "message": "Failed"}',
        '{"timestamp": "2024-01-15T10:32:00", "severity": "WARNING", "message": "Slow"}',
    ]
    jsonl_file.write_text("\\n".join(lines) + "\\n")
    return jsonl_file

# En tus tests:
def test_process_csv(sample_csv_file, tmp_path):
    output = tmp_path / "output.json"
    process_csv(str(sample_csv_file), str(output))
    assert output.exists()
```

## Aprendizaje Clave

**Puntos críticos a recordar**:

1. Functional tests con `tmp_path` detectan bugs de I/O que los mocks ocultan
2. Cada test tiene su propio directorio temporal — aislamiento garantizado
3. pytest limpia automáticamente — sin ficheros huérfanos

**Cómo desarrollar intuición**:

- **Pregúntate**: "¿Este código lee o escribe ficheros?"
  - Si SÍ → functional test con `tmp_path`
  - Si NO → unit test (con o sin mock según dependencias)

**Cuándo usar / NO usar**:

- **Usar functional tests cuando**:
  - Tu código lee/escribe ficheros locales
  - Quieres verificar encodings, formatos, edge cases de I/O
  - Necesitas testear un flujo completo entrada → salida
  
- **NO usar functional tests para**:
  - Funciones puras sin I/O
  - Código que llama a APIs externas (usa mocks)
  - Tests que requieren infraestructura compleja (BD, S3)

**Referencia oficial**: [pytest Documentation - tmp_path fixture](https://docs.pytest.org/en/stable/how-to/tmp_path.html)

## Resumen

Los functional tests con `tmp_path` verifican que tu código funciona con I/O real, detectando bugs de encoding, formato, y edge cases que los mocks no pueden encontrar. Cada test tiene su propio directorio temporal que pytest limpia automáticamente. Usa functional tests para código que lee/escribe ficheros locales, y combínalos con mocks para dependencias externas (APIs, BD).
