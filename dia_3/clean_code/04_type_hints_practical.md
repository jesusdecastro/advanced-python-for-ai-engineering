# Type Hints Prácticos

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Type Hints Básicos](#1-type-hints-básicos)
3. [Tipos Compuestos y Genéricos](#2-tipos-compuestos-y-genéricos)
4. [Optional y Union](#3-optional-y-union)
5. [Type Aliases y NewType](#4-type-aliases-y-newtype)
6. [Verificación Estática con mypy](#5-verificación-estática-con-mypy)
7. [Resumen](#resumen-de-principios)

---

## Introducción

Los type hints transforman Python de un lenguaje dinámicamente tipado a uno con tipado gradual opcional. Esta capacidad permite detectar errores antes de ejecutar el código, mejora la documentación, y facilita el mantenimiento en proyectos grandes.

**Referencia principal**: van Rossum, G., Lehtosalo, J., & Langa, Ł. (2014). PEP 484 – Type Hints. <https://peps.python.org/pep-0484/>

### Contexto: Por Qué Importa

**Problema real en Data/IA**:
Estás construyendo un pipeline de ML con múltiples funciones que procesan DataFrames. Una función espera columnas específicas, otra espera arrays NumPy, otra espera listas. Sin type hints, pasas un tipo incorrecto y el error aparece después de 2 horas de procesamiento. Con type hints, tu editor te avisa inmediatamente.

**Ejemplo concreto**:
Tienes una función `train_model(data, target)`. ¿`data` es un DataFrame, un array, una lista? ¿`target` es un string (nombre de columna) o un array (valores)? Sin type hints, tienes que leer el código o la documentación. Con type hints, tu editor te lo muestra mientras escribes.

**Consecuencias de NO usarlos**:
- **Errores en runtime**: Descubres problemas de tipos tarde, después de procesamiento costoso
- **Documentación implícita**: Tienes que leer código para saber qué tipos espera
- **Refactoring peligroso**: Cambiar tipos rompe código en lugares inesperados
- **Debugging lento**: Errores de tipo son difíciles de rastrear sin herramientas
- **Colaboración difícil**: Otros desarrolladores no saben qué tipos pasar

### Principio Fundamental

> "In the face of ambiguity, refuse the temptation to guess."
>
> — The Zen of Python

Los type hints eliminan la ambigüedad sobre qué tipos espera y retorna una función, haciendo el código más predecible y mantenible.

---

### El Concepto

**Definición técnica**:
Los type hints son anotaciones opcionales que especifican los tipos esperados de variables, parámetros de funciones, y valores de retorno. Python no los verifica en runtime, pero herramientas como mypy pueden verificarlos estáticamente.

**Cómo funciona internamente**:
1. **Anotaciones**: Python almacena type hints en `__annotations__`
2. **Sin verificación runtime**: Python ignora los hints durante ejecución
3. **Verificación estática**: Herramientas como mypy analizan el código sin ejecutarlo
4. **Inferencia de tipos**: mypy deduce tipos cuando no están explícitos

**Terminología clave**:
- **Type hint**: Anotación que especifica un tipo esperado
- **Static type checker**: Herramienta que verifica tipos sin ejecutar código (mypy, pyright)
- **Type inference**: Deducción automática de tipos por el checker
- **Generic types**: Tipos parametrizados como `List[int]`, `Dict[str, float]`
- **Type alias**: Nombre personalizado para un tipo complejo

---

## 1. Type Hints Básicos

### Por Qué Importa

Los type hints básicos cubren el 80% de los casos de uso y son fáciles de aprender. Empezar con estos tipos fundamentales te da beneficios inmediatos sin complejidad.

---

### Tipos Built-in

**Python 3.9+** permite usar tipos built-in directamente sin importar de `typing`.

```python
def process_numbers(numbers: list[int]) -> float:
    """
    Calculate average of numbers.
    
    :param numbers: List of integers
    :type numbers: list[int]
    :return: Average value
    :rtype: float
    """
    return sum(numbers) / len(numbers)


def format_user_data(name: str, age: int, active: bool) -> dict[str, str | int | bool]:
    """
    Format user data into dictionary.
    
    :param name: User name
    :type name: str
    :param age: User age
    :type age: int
    :param active: Whether user is active
    :type active: bool
    :return: Formatted user data
    :rtype: dict[str, str | int | bool]
    """
    return {
        "name": name,
        "age": age,
        "active": active,
    }
```

**Tipos básicos**:
- `int`: Enteros
- `float`: Números de punto flotante
- `str`: Cadenas de texto
- `bool`: Booleanos
- `list`: Listas
- `dict`: Diccionarios
- `set`: Conjuntos
- `tuple`: Tuplas

---

### Ejemplo Incorrecto: Sin Type Hints

```python
def train_model(data, target, test_size, random_state):
    """Train a model - sin type hints."""
    # ¿Qué tipos son estos parámetros?
    # ¿data es DataFrame, array, lista?
    # ¿target es string o array?
    # ¿test_size es float o int?
    X = data.drop(columns=[target])
    y = data[target]
    # ... resto del código
```

**Problemas**:

- **Ambigüedad**: No sabes qué tipos espera
- **Sin ayuda del editor**: No hay autocompletado inteligente
- **Errores tardíos**: Descubres problemas en runtime
- **Documentación pobre**: Tienes que leer el código

---

### Ejemplo Correcto: Con Type Hints

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_model(
    data: pd.DataFrame,
    target: str,
    test_size: float = 0.2,
    random_state: int = 42,
) -> RandomForestClassifier:
    """
    Train a Random Forest model.
    
    :param data: Training dataset
    :type data: pd.DataFrame
    :param target: Name of target column
    :type target: str
    :param test_size: Proportion of test set
    :type test_size: float
    :param random_state: Random seed
    :type random_state: int
    :return: Trained model
    :rtype: RandomForestClassifier
    """
    X = data.drop(columns=[target])
    y = data[target]
    # ... resto del código
    return model
```

**Ventajas**:

- **Claridad**: Tipos explícitos y obvios
- **Autocompletado**: Editor sugiere métodos correctos
- **Detección temprana**: mypy detecta errores antes de ejecutar
- **Documentación viva**: Los tipos son parte del código

---

## 2. Tipos Compuestos y Genéricos

### Por Qué Importa

Los tipos genéricos permiten especificar el contenido de colecciones, haciendo los type hints más precisos y útiles.

**Referencia**: PEP 585 – Type Hinting Generics In Standard Collections: <https://peps.python.org/pep-0585/>

---

### Listas, Diccionarios, y Tuplas

```python
from typing import Any

# Lista de enteros
def sum_numbers(numbers: list[int]) -> int:
    """Sum a list of integers."""
    return sum(numbers)


# Diccionario con tipos específicos
def get_user_scores(users: dict[str, float]) -> float:
    """
    Calculate average score from user dictionary.
    
    :param users: Dictionary mapping user names to scores
    :type users: dict[str, float]
    :return: Average score
    :rtype: float
    """
    return sum(users.values()) / len(users)


# Tupla con tipos fijos
def get_model_info() -> tuple[str, float, int]:
    """
    Get model information.
    
    :return: Tuple of (model_name, accuracy, num_features)
    :rtype: tuple[str, float, int]
    """
    return ("RandomForest", 0.85, 10)


# Tupla de longitud variable
def process_values(values: tuple[int, ...]) -> int:
    """
    Process variable number of integers.
    
    :param values: Tuple of integers
    :type values: tuple[int, ...]
    :return: Sum of values
    :rtype: int
    """
    return sum(values)
```

---

### Tipos Anidados

```python
# Lista de listas
def process_matrix(matrix: list[list[float]]) -> list[float]:
    """
    Calculate row sums of matrix.
    
    :param matrix: 2D matrix as list of lists
    :type matrix: list[list[float]]
    :return: List of row sums
    :rtype: list[float]
    """
    return [sum(row) for row in matrix]


# Diccionario complejo
def get_experiment_results() -> dict[str, dict[str, float]]:
    """
    Get experiment results.
    
    :return: Dictionary mapping experiment names to metric dictionaries
    :rtype: dict[str, dict[str, float]]
    """
    return {
        "experiment_1": {"accuracy": 0.85, "precision": 0.90},
        "experiment_2": {"accuracy": 0.88, "precision": 0.92},
    }


# Lista de tuplas
def get_coordinates() -> list[tuple[float, float]]:
    """
    Get list of (x, y) coordinates.
    
    :return: List of coordinate tuples
    :rtype: list[tuple[float, float]]
    """
    return [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)]
```

---

## 3. Optional y Union

### Por Qué Importa

Muchas funciones aceptan valores opcionales o múltiples tipos. `Optional` y `Union` permiten expresar estas situaciones de forma clara.

**Referencia**: PEP 604 – Allow writing union types as X | Y: <https://peps.python.org/pep-0604/>

---

### Optional: Valores que Pueden Ser None

**Python 3.10+** permite usar `Type | None` en vez de `Optional[Type]`.

```python
def find_user(user_id: int) -> dict[str, str] | None:
    """
    Find user by ID.
    
    :param user_id: User ID to search
    :type user_id: int
    :return: User data if found, None otherwise
    :rtype: dict[str, str] | None
    """
    # Buscar usuario...
    if user_found:
        return {"name": "John", "email": "john@example.com"}
    return None


def process_data(
    data: pd.DataFrame,
    output_path: str | None = None,
) -> pd.DataFrame:
    """
    Process data and optionally save to file.
    
    :param data: Input dataframe
    :type data: pd.DataFrame
    :param output_path: Optional path to save results
    :type output_path: str | None
    :return: Processed dataframe
    :rtype: pd.DataFrame
    """
    processed = data.dropna()
    
    if output_path is not None:
        processed.to_csv(output_path)
    
    return processed
```

---

### Union: Múltiples Tipos Posibles

**Python 3.10+** permite usar `Type1 | Type2` en vez de `Union[Type1, Type2]`.

```python
import numpy as np
import pandas as pd


def normalize_data(
    data: pd.DataFrame | np.ndarray | list[float],
) -> np.ndarray:
    """
    Normalize data from various input types.
    
    :param data: Input data in various formats
    :type data: pd.DataFrame | np.ndarray | list[float]
    :return: Normalized numpy array
    :rtype: np.ndarray
    """
    # Convert to numpy array
    if isinstance(data, pd.DataFrame):
        arr = data.values
    elif isinstance(data, list):
        arr = np.array(data)
    else:
        arr = data
    
    # Normalize
    return (arr - arr.mean()) / arr.std()


def get_config_value(key: str) -> str | int | float | bool:
    """
    Get configuration value of various types.
    
    :param key: Configuration key
    :type key: str
    :return: Configuration value
    :rtype: str | int | float | bool
    """
    config = {
        "model_name": "RandomForest",
        "n_estimators": 100,
        "learning_rate": 0.01,
        "verbose": True,
    }
    return config[key]
```

---

### Ejemplo Incorrecto: Ambigüedad con None

```python
def load_model(path):
    """Load model - ¿retorna None si falla?"""
    try:
        return joblib.load(path)
    except FileNotFoundError:
        return None  # ¿Esto es esperado o un error?
```

**Problemas**:

- **Ambigüedad**: No está claro si None es válido
- **Sin verificación**: mypy no puede ayudar
- **Errores silenciosos**: Código puede fallar después

---

### Ejemplo Correcto: Optional Explícito

```python
import joblib
from sklearn.ensemble import RandomForestClassifier


def load_model(path: str) -> RandomForestClassifier | None:
    """
    Load model from file.
    
    :param path: Path to model file
    :type path: str
    :return: Loaded model, or None if file not found
    :rtype: RandomForestClassifier | None
    """
    try:
        return joblib.load(path)
    except FileNotFoundError:
        return None


# Uso con verificación explícita
model = load_model("model.pkl")
if model is not None:
    predictions = model.predict(X_test)
else:
    print("Model not found")
```

**Ventajas**:

- **Claridad**: None es explícitamente parte del contrato
- **Verificación**: mypy verifica que manejes None
- **Sin sorpresas**: Comportamiento documentado

---

## 4. Type Aliases y NewType

### Por Qué Importa

Los type aliases simplifican tipos complejos y mejoran la legibilidad. `NewType` crea tipos distintos para prevenir errores sutiles.

**Referencia**: PEP 613 – Explicit Type Aliases: <https://peps.python.org/pep-0613/>

---

### Type Aliases

```python
from typing import TypeAlias

# Alias para tipo complejo
ModelConfig: TypeAlias = dict[str, int | float | str]
ExperimentResults: TypeAlias = dict[str, dict[str, float]]
Coordinates: TypeAlias = list[tuple[float, float]]


def train_with_config(config: ModelConfig) -> float:
    """
    Train model with configuration.
    
    :param config: Model configuration
    :type config: ModelConfig
    :return: Training accuracy
    :rtype: float
    """
    # Usar configuración...
    return 0.85


def compare_experiments(
    results: ExperimentResults,
) -> dict[str, float]:
    """
    Compare experiment results.
    
    :param results: Results from multiple experiments
    :type results: ExperimentResults
    :return: Best metrics from each experiment
    :rtype: dict[str, float]
    """
    return {
        name: max(metrics.values())
        for name, metrics in results.items()
    }
```

---

### NewType: Tipos Distintos

`NewType` crea un tipo distinto que mypy trata como diferente, previniendo mezclas accidentales.

```python
from typing import NewType

# Crear tipos distintos para IDs
UserId = NewType("UserId", int)
ModelId = NewType("ModelId", int)
ExperimentId = NewType("ExperimentId", int)


def get_user(user_id: UserId) -> dict[str, str]:
    """
    Get user by ID.
    
    :param user_id: User ID
    :type user_id: UserId
    :return: User data
    :rtype: dict[str, str]
    """
    # Buscar usuario...
    return {"name": "John"}


def get_model(model_id: ModelId) -> dict[str, str]:
    """
    Get model by ID.
    
    :param model_id: Model ID
    :type model_id: ModelId
    :return: Model data
    :rtype: dict[str, str]
    """
    # Buscar modelo...
    return {"name": "RandomForest"}


# Uso
user_id = UserId(123)
model_id = ModelId(456)

get_user(user_id)  # OK
get_model(model_id)  # OK

# mypy detecta error
get_user(model_id)  # Error: Expected UserId, got ModelId
get_model(user_id)  # Error: Expected ModelId, got UserId

# También detecta uso de int directo
get_user(123)  # Error: Expected UserId, got int
```

**Ventajas**:

- **Prevención de errores**: No puedes mezclar IDs accidentalmente
- **Documentación**: El tipo comunica el propósito
- **Sin overhead**: NewType no tiene costo en runtime

---

## 5. Verificación Estática con mypy

### Por Qué Importa

Los type hints solo son útiles si los verificas. mypy es el verificador estático estándar de Python que detecta errores de tipos antes de ejecutar el código.

**Referencia**: mypy Documentation: <https://mypy.readthedocs.io/>

---

### Instalación y Uso Básico

**Instalación**:
```bash
pip install mypy
```

**Uso básico**:
```bash
# Verificar un archivo
mypy script.py

# Verificar un directorio
mypy src/

# Verificar con configuración estricta
mypy --strict src/
```

---

### Configuración

**Archivo** `mypy.ini` o `pyproject.toml`:

```toml
[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_any_generics = true
disallow_subclassing_any = true
disallow_untyped_calls = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true

# Ignorar librerías sin stubs
[[tool.mypy.overrides]]
module = [
    "sklearn.*",
    "pandas.*",
]
ignore_missing_imports = true
```

---

### Ejemplo: Detección de Errores

```python
def calculate_average(numbers: list[int]) -> float:
    """Calculate average of numbers."""
    return sum(numbers) / len(numbers)


# mypy detecta estos errores:

# Error: Argument 1 has incompatible type "list[str]"; expected "list[int]"
calculate_average(["1", "2", "3"])

# Error: Argument 1 has incompatible type "str"; expected "list[int]"
calculate_average("123")

# Error: Incompatible return value type (got "int", expected "float")
def bad_function(x: int) -> float:
    return x  # Debería ser float(x)
```

---

### Integración con VS Code

**Configuración** (`.vscode/settings.json`):
```json
{
  "python.linting.mypyEnabled": true,
  "python.linting.enabled": true,
  "python.linting.mypyArgs": [
    "--config-file=mypy.ini"
  ]
}
```

**Extensión recomendada**:
- **Pylance**: Proporciona type checking en tiempo real

---

## Aprendizaje Clave

### Puntos Críticos a Recordar

1. **Usa type hints**: En todas las funciones públicas
2. **Python 3.10+**: Usa `Type | None` en vez de `Optional[Type]`
3. **Tipos genéricos**: Especifica contenido de colecciones (`list[int]`)
4. **Type aliases**: Simplifica tipos complejos repetidos
5. **NewType**: Previene mezclas accidentales de IDs
6. **Verifica con mypy**: Los hints solo ayudan si los verificas
7. **Configuración estricta**: Usa `--strict` para máxima seguridad

---

### Cómo Desarrollar Intuición

**Pregúntate**: "¿Qué tipo espera esta función?"
- Si no es obvio → Añade type hint
- Si es obvio → Añádelo igual (documentación)

**Pregúntate**: "¿Este parámetro puede ser None?"
- SÍ → Usa `Type | None`
- NO → Usa solo `Type`

**Pregúntate**: "¿Este tipo es complejo y se repite?"
- SÍ → Crea type alias
- NO → Usa el tipo directamente

**Pregúntate**: "¿Estos IDs se pueden mezclar accidentalmente?"
- SÍ → Usa NewType
- NO → Usa int directamente

---

### Cuándo Usar Type Hints

**Siempre usar en**:
- Funciones públicas
- Parámetros de funciones
- Valores de retorno
- Atributos de clase

**Opcional en**:
- Variables locales (mypy las infiere)
- Funciones privadas muy simples
- Scripts de un solo uso

**No necesario en**:
- Código legacy que no vas a mantener
- Prototipos rápidos (pero añádelos después)

---

## Resumen de Principios

Los type hints transforman Python en un lenguaje más seguro y mantenible:

1. **Claridad**: Tipos explícitos eliminan ambigüedad
2. **Detección temprana**: mypy encuentra errores antes de ejecutar
3. **Documentación viva**: Los tipos son parte del código
4. **Refactoring seguro**: Cambios de tipos se detectan automáticamente
5. **Mejor tooling**: Autocompletado y navegación mejorados
6. **Sin overhead**: No afectan performance en runtime

**Regla de oro**: Si una función es pública o compleja, debe tener type hints completos. Si mypy no puede verificar tu código, los hints no son suficientemente específicos.

---

## Referencias

1. van Rossum, G., Lehtosalo, J., & Langa, Ł. (2014). PEP 484 – Type Hints. <https://peps.python.org/pep-0484/>
2. PEP 585 – Type Hinting Generics In Standard Collections. <https://peps.python.org/pep-0585/>
3. PEP 604 – Allow writing union types as X | Y. <https://peps.python.org/pep-0604/>
4. PEP 613 – Explicit Type Aliases. <https://peps.python.org/pep-0613/>
5. mypy Documentation: <https://mypy.readthedocs.io/>
6. Python typing module: <https://docs.python.org/3/library/typing.html>

---

## Ejercicio Práctico Individual

Añade type hints completos a este código y verifica con mypy:

```python
def process_experiment_results(results, threshold):
    filtered = {}
    for name, metrics in results.items():
        if metrics["accuracy"] > threshold:
            filtered[name] = metrics
    return filtered

def calculate_metrics(predictions, labels):
    correct = sum(p == l for p, l in zip(predictions, labels))
    total = len(predictions)
    return correct / total
```

**Criterios de éxito**:
- [ ] Type hints en todos los parámetros
- [ ] Type hints en todos los retornos
- [ ] Tipos genéricos específicos (no `dict`, sino `dict[str, ...]`)
- [ ] mypy pasa sin errores con `--strict`
- [ ] Docstrings con tipos en formato Sphinx

---
