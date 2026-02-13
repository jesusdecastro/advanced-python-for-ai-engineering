# Mocks: Aislar Dependencias Externas

## Contexto: Por Qué Importa

**Problema real en Data/IA**:

Tu función de negocio lee un fichero JSON, llama a una API, o consulta una base de datos. Quieres testear tu lógica, no la conexión a la BD ni la existencia del fichero. Los mocks reemplazan temporalmente esas dependencias externas por objetos falsos que tú controlas.

**Ejemplo concreto**:

Tienes una función que carga configuración desde un fichero JSON y valida que tenga las claves requeridas. Sin mocks, tu test depende de que el fichero exista en una ruta específica. Si otro dev ejecuta el test en su máquina, falla porque el fichero no está ahí.

**Consecuencias de NO usar mocks**:

- Tests que dependen de ficheros en rutas específicas — fallan en otros entornos
- Tests que llaman a APIs externas — fallan si hay rate limit, timeout, o está caída
- Costes reales en tests que llaman a APIs de pago (OpenAI, AWS)
- Tests lentos por I/O de red
- Tests no deterministas — el resultado puede cambiar

## El Concepto

### Definición técnica

Un **mock** es un objeto falso que simula el comportamiento de una dependencia externa (fichero, API, BD). Reemplaza temporalmente la dependencia real durante el test, permitiéndote controlar qué devuelve y verificar cómo se usó.

### Cómo funciona internamente

1. Usas `patch` para reemplazar temporalmente una función o clase
2. El mock intercepta las llamadas a esa función
3. Devuelve valores que tú controlas (con `return_value`)
4. Tu código bajo test ejecuta normalmente, pero usa el mock
5. Al terminar el test, `patch` restaura la función original

### Terminología clave

- **Mock**: Objeto falso que simula una dependencia
- **Patch**: Reemplazar temporalmente una función/clase por un mock
- **mock_open**: Mock especializado para simular lectura de ficheros
- **return_value**: Qué devuelve el mock cuando se llama
- **MagicMock**: Mock que acepta cualquier atributo o método

## Ejemplo Incorrecto

```python
# test que depende de un fichero real en disco
def test_load_config():
    """Este test FALLA si el fichero no existe."""
    config = load_pipeline_config("/home/dev/configs/pipeline.json")
    assert config["input_path"] == "/data/input"
    # ¿Y si otro dev tiene el fichero en otra ruta?
    # ¿Y si el contenido del fichero cambió?
    # ¿Y si ejecutas en CI donde no existe ese path?

# test que llama a una API real
def test_get_embeddings():
    """Este test FALLA si la API está caída, y CUESTA dinero."""
    result = get_embeddings("hello world", api_key="sk-real-key")
    assert len(result) == 1536
    # Coste: ~$0.0001 por llamada × 100 tests × 50 ejecuciones/día = 💸
    # Latencia: ~500ms por llamada × 100 tests = 50 segundos
```

**Problemas**:

- Depende de ficheros en rutas específicas — falla en otros entornos
- Depende de APIs externas — falla si hay rate limit, timeout, o está caída
- Costes reales en tests que llaman a APIs de pago
- Tests lentos por I/O de red
- Tests no deterministas — el resultado puede cambiar

## Ejemplo Correcto

```python
from unittest.mock import patch, mock_open
import pytest
import json

# --- Función bajo test ---

from pathlib import Path

def load_pipeline_config(config_path: str) -> dict:
    """Carga configuración del pipeline desde JSON."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")
    
    with open(path) as f:
        config = json.load(f)
    
    required_keys = {"input_path", "output_path", "transformations"}
    missing = required_keys - set(config.keys())
    if missing:
        raise ValueError(f"Missing required config keys: {missing}")
    
    return config

# --- Tests con mocks ---

def test_load_valid_config():
    """Verifica que un JSON válido se carga correctamente."""
    fake_json = json.dumps({
        "input_path": "/data/in",
        "output_path": "/data/out",
        "transformations": ["clean", "normalize"],
    })
    
    with patch("builtins.open", mock_open(read_data=fake_json)):
        with patch("pathlib.Path.exists", return_value=True):
            config = load_pipeline_config("any_path.json")
    
    assert config["input_path"] == "/data/in"
    assert "normalize" in config["transformations"]

def test_load_config_file_not_found():
    """Verifica que lanza FileNotFoundError si el fichero no existe."""
    with patch("pathlib.Path.exists", return_value=False):
        with pytest.raises(FileNotFoundError, match="Config not found"):
            load_pipeline_config("nonexistent.json")

def test_load_config_missing_required_keys():
    """Verifica que detecta claves faltantes en el JSON."""
    fake_json = json.dumps({"input_path": "/data/in"})  # Faltan 2 claves
    
    with patch("builtins.open", mock_open(read_data=fake_json)):
        with patch("pathlib.Path.exists", return_value=True):
            with pytest.raises(ValueError, match="Missing required config keys"):
                load_pipeline_config("incomplete.json")
```

**Ventajas**:

- Tests rápidos — no hacen I/O real
- Tests deterministas — siempre el mismo resultado
- Tests aislados — no dependen de ficheros, APIs ni infraestructura
- Testeamos nuestra lógica (validación de claves, manejo de errores), no la librería json
- Funcionan en cualquier entorno: local, CI, portátil de un nuevo dev

## Herramientas de Mock en Python

### 1. patch como context manager

```python
from unittest.mock import patch

# El más común — limpio y explícito
with patch("modulo.funcion", return_value="fake"):
    result = mi_codigo_que_llama_a_funcion()
```

### 2. patch como decorador

```python
@patch("modulo.funcion", return_value="fake")
def test_algo(mock_funcion):
    result = mi_codigo_que_llama_a_funcion()
    mock_funcion.assert_called_once()  # Verificar que se llamó
```

### 3. mock_open — simular lectura de ficheros

```python
from unittest.mock import mock_open

with patch("builtins.open", mock_open(read_data="contenido fake")):
    with open("cualquier_path.txt") as f:
        data = f.read()  # "contenido fake"
```

### 4. MagicMock — objeto que acepta cualquier atributo

```python
from unittest.mock import MagicMock

mock_client = MagicMock()
mock_client.get_embeddings.return_value = [0.1, 0.2, 0.3]
```

## Ejemplo: Mockear API Externa

```python
# Función que llama a API
def get_user_data(user_id: int) -> dict:
    """Obtiene datos de usuario desde API externa."""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()

# Test con mock
@patch("requests.get")
def test_get_user_data_success(mock_get):
    # Configurar el mock
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 1, "name": "Alice"}
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    
    # Ejecutar
    result = get_user_data(1)
    
    # Verificar
    assert result["name"] == "Alice"
    mock_get.assert_called_once_with("https://api.example.com/users/1")
```

## Regla de Oro del Mocking

> **Mockea lo que NO quieres testear, nunca tu propia lógica.**

**Mockear**: lectura de ficheros, llamadas a APIs, conexiones a BD, `datetime.now()`

**No mockear**: tus propias funciones de transformación, validación, o lógica de negocio

Si te encuentras mockeando tu propio código, es una señal de que tu código está demasiado acoplado y necesita refactorización.

## Aprendizaje Clave

**Puntos críticos a recordar**:

1. Los mocks aislan tu código de dependencias externas (I/O, APIs, BD)
2. Tests con mocks son rápidos, deterministas, y no dependen de infraestructura
3. Mockea lo externo, nunca tu propia lógica

**Cómo desarrollar intuición**:

- **Pregúntate**: "¿Este test depende de algo externo?"
  - Si SÍ (fichero, API, BD) → usa mock
  - Si NO (función pura) → no necesitas mock

**Cuándo usar / NO usar**:

- **Usar mocks cuando**:
  - Tu código lee ficheros o llama a APIs
  - Quieres testear manejo de errores (fichero no existe, API falla)
  - Necesitas tests rápidos y deterministas
  
- **NO usar mocks para**:
  - Funciones puras sin dependencias externas
  - Tu propia lógica de negocio
  - Tests de I/O donde quieres verificar el comportamiento real

**Referencia oficial**: [Python Documentation - unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

## Resumen

Los mocks reemplazan temporalmente dependencias externas (ficheros, APIs, BD) por objetos falsos que tú controlas. Permiten tests rápidos, deterministas, y aislados. Usa `patch` para reemplazar funciones, `mock_open` para ficheros, y `MagicMock` para objetos complejos. La regla de oro: mockea lo externo, nunca tu propia lógica.
