# Separación de Responsabilidades: Arquitectura en Capas

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Las Tres Capas en Data/IA](#las-tres-capas-en-dataia)
3. [Reglas de Dependencia](#reglas-de-dependencia-entre-capas)
4. [Patrones de Organización](#patrones-de-organización)
5. [Testing por Capas](#testing-por-capas)

---

## Introducción

Este documento se enfoca en **arquitectura en capas** para proyectos de Data/IA. Los conceptos de funciones pequeñas, hacer una cosa, y efectos secundarios ya están cubiertos en el Día 2 (Functions). Aquí nos centramos en cómo organizar el código en capas con responsabilidades claras.

**Referencia principal**: Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.

### Contexto: Por Qué Importa

**Problema real en Data/IA**:
Tu pipeline de ML mezcla lectura de CSV, transformaciones, entrenamiento, y visualizaciones en una función de 200 líneas. Cuando quieres cambiar el formato de salida, arriesgas romper el entrenamiento. Cuando quieres testear la lógica de limpieza, necesitas archivos CSV reales.

**Ejemplo concreto**:
Tienes `train_model()` que hace TODO: carga datos, valida, transforma, entrena, evalúa, genera gráficos, y guarda resultados. No puedes reusar solo la transformación en otro proyecto sin copiar código mezclado con I/O específico.

**Consecuencias de NO usarlo**:
- **Imposible testear lógica sin I/O**: Necesitas archivos reales para cada test
- **No reutilizable**: Lógica mezclada con I/O específico
- **Cambios riesgosos**: Modificar formato de archivo puede romper lógica de negocio
- **Debugging complejo**: Errores pueden estar en cualquier capa
- **Trabajo en equipo difícil**: Conflictos constantes en las mismas funciones

---

## Las Tres Capas en Data/IA

### El Concepto

En proyectos de Data/IA, el código se organiza en tres capas con responsabilidades específicas:

**1. Capa de I/O (Input/Output)**:
- Lectura/escritura de archivos (CSV, JSON, Parquet)
- Llamadas a APIs externas
- Acceso a bases de datos
- Carga de configuraciones

**2. Capa de Lógica de Negocio (Core)**:
- Transformaciones de datos (funciones puras)
- Algoritmos y cálculos
- Validaciones de reglas de negocio
- Entrenamiento de modelos

**3. Capa de Presentación**:
- Formateo de output
- Generación de visualizaciones
- Creación de reportes
- Logging de resultados

**Regla de oro**: La lógica de negocio NO debe depender de I/O ni presentación.

---

### Ejemplo Incorrecto: Todo Mezclado

```python
def train_model(csv_path: str, output_dir: str) -> None:
    """Train model - TODO mezclado."""
    # I/O mezclado con lógica
    data = pd.read_csv(csv_path)  # I/O
    
    if 'target' not in data.columns:  # Validación
        print("Error: missing target")  # Presentación
        return
    
    # Transformación
    data = data.dropna()
    data['normalized'] = (data['value'] - data['value'].mean()) / data['value'].std()
    
    # Entrenamiento
    X = data.drop('target', axis=1)
    y = data['target']
    model = RandomForestClassifier()
    model.fit(X, y)
    
    # Evaluación + Visualización + I/O mezclados
    accuracy = model.score(X, y)
    plt.figure()
    plt.plot(y, model.predict(X))
    plt.savefig(f"{output_dir}/predictions.png")  # I/O
    joblib.dump(model, f"{output_dir}/model.pkl")  # I/O
    print(f"Accuracy: {accuracy:.2f}")  # Presentación
```

**Problemas**:
- No puedes testear transformaciones sin archivos CSV
- No puedes reusar `normalize` en otro proyecto
- Cambiar formato de salida requiere modificar función de entrenamiento
- Imposible testear lógica de negocio aisladamente

---

### Ejemplo Correcto: Capas Separadas

```python
# ============================================
# CAPA 1: I/O (Adaptadores)
# ============================================

def load_training_data(csv_path: str) -> pd.DataFrame:
    """Load data from CSV. Pure I/O, no logic."""
    return pd.read_csv(csv_path)


def save_model(model: RandomForestClassifier, path: str) -> None:
    """Save model to disk. Pure I/O, no logic."""
    joblib.dump(model, path)


def save_plot(fig: plt.Figure, path: str) -> None:
    """Save plot to disk. Pure I/O, no logic."""
    fig.savefig(path)
    plt.close(fig)


# ============================================
# CAPA 2: LÓGICA DE NEGOCIO (Core)
# ============================================
# Funciones puras: sin I/O, fáciles de testear

def validate_training_data(data: pd.DataFrame) -> None:
    """Validate data structure. Pure function."""
    if 'target' not in data.columns:
        raise ValueError("Missing 'target' column")
    if data.empty:
        raise ValueError("Data is empty")


def normalize_features(data: pd.DataFrame) -> pd.DataFrame:
    """Normalize features. Pure function - testeable sin I/O."""
    cleaned = data.dropna().copy()
    cleaned['normalized'] = (
        (cleaned['value'] - cleaned['value'].mean()) / 
        cleaned['value'].std()
    )
    return cleaned


def train_random_forest(
    X: pd.DataFrame,
    y: pd.Series,
    n_estimators: int = 100,
) -> RandomForestClassifier:
    """Train model. Pure function - testeable sin I/O."""
    model = RandomForestClassifier(n_estimators=n_estimators)
    model.fit(X, y)
    return model


def calculate_accuracy(
    model: RandomForestClassifier,
    X: pd.DataFrame,
    y: pd.Series,
) -> float:
    """Calculate accuracy. Pure function."""
    return model.score(X, y)


# ============================================
# CAPA 3: PRESENTACIÓN
# ============================================

def create_prediction_plot(
    y_true: pd.Series,
    y_pred: np.ndarray,
) -> plt.Figure:
    """Create plot. Returns figure, no I/O."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(y_true, y_pred, alpha=0.5)
    ax.set_xlabel("True Values")
    ax.set_ylabel("Predictions")
    ax.set_title("Predictions vs True Values")
    return fig


def format_training_report(
    model_name: str,
    accuracy: float,
    n_samples: int,
) -> str:
    """Format report. Pure function, returns string."""
    return (
        f"Model: {model_name}\n"
        f"Accuracy: {accuracy:.2%}\n"
        f"Samples: {n_samples:,}"
    )


# ============================================
# ORQUESTADOR (Coordina las capas)
# ============================================

def train_model_pipeline(csv_path: str, output_dir: str) -> dict:
    """
    Orchestrate training pipeline.
    
    Coordina las tres capas pero no contiene lógica de negocio.
    """
    # Capa I/O
    data = load_training_data(csv_path)
    
    # Capa Lógica
    validate_training_data(data)
    processed = normalize_features(data)
    X = processed.drop('target', axis=1)
    y = processed['target']
    model = train_random_forest(X, y)
    accuracy = calculate_accuracy(model, X, y)
    
    # Capa Presentación
    predictions = model.predict(X)
    fig = create_prediction_plot(y, predictions)
    report = format_training_report("RandomForest", accuracy, len(data))
    
    # Capa I/O (salida)
    save_model(model, f"{output_dir}/model.pkl")
    save_plot(fig, f"{output_dir}/predictions.png")
    
    return {
        "accuracy": accuracy,
        "n_samples": len(data),
        "report": report,
    }
```

**Ventajas**:
- Lógica de negocio testeable sin I/O
- Funciones reutilizables en otros proyectos
- Cambiar formato de archivo no afecta lógica
- Fácil de mantener y extender
- Cada capa puede evolucionar independientemente

---

## Reglas de Dependencia entre Capas

### Principio de Dependencia

**Regla fundamental**: Las dependencias apuntan hacia adentro.

```
┌─────────────────────────────────────┐
│   Capa I/O (Adaptadores)            │
│   - load_data()                     │
│   - save_model()                    │
└──────────────┬──────────────────────┘
               │ depende de ↓
┌──────────────▼──────────────────────┐
│   Capa Lógica (Core)                │
│   - normalize_features()            │
│   - train_model()                   │
│   - calculate_metrics()             │
└──────────────┬──────────────────────┘
               │ NO depende de ↑
┌──────────────▼──────────────────────┐
│   Capa Presentación                 │
│   - format_report()                 │
│   - create_plot()                   │
└─────────────────────────────────────┘
```

**Reglas**:
1. **Core NO importa de I/O**: Lógica de negocio es independiente
2. **Core NO importa de Presentación**: Lógica no sabe cómo se presenta
3. **I/O puede importar de Core**: Para usar tipos y estructuras
4. **Presentación puede importar de Core**: Para formatear resultados

---

### Violación de Dependencia

```python
# MAL: Lógica de negocio depende de I/O
def normalize_features(csv_path: str) -> pd.DataFrame:
    """Lógica acoplada a formato de archivo."""
    data = pd.read_csv(csv_path)  # I/O en lógica
    return (data - data.mean()) / data.std()
```

**Problema**: No puedes testear sin archivo CSV. No puedes reusar con otros formatos.

---

### Dependencia Correcta

```python
# BIEN: Lógica pura, I/O separado
def normalize_features(data: pd.DataFrame) -> pd.DataFrame:
    """Lógica pura, testeable sin I/O."""
    return (data - data.mean()) / data.std()


# I/O en capa separada
def normalize_from_csv(csv_path: str) -> pd.DataFrame:
    """Adaptador que combina I/O + lógica."""
    data = pd.read_csv(csv_path)
    return normalize_features(data)
```

**Ventaja**: `normalize_features` es testeable, reutilizable, y no depende de formato de archivo.

---

## Patrones de Organización

### Estructura de Directorios

```
ml_project/
├── data/                    # Capa I/O
│   ├── loaders.py          # load_csv(), load_json()
│   ├── savers.py           # save_model(), save_metrics()
│   └── validators.py       # validate_file_exists()
│
├── core/                    # Capa Lógica (Core)
│   ├── preprocessing.py    # normalize(), clean_data()
│   ├── training.py         # train_model(), evaluate()
│   └── metrics.py          # calculate_accuracy(), f1_score()
│
├── presentation/            # Capa Presentación
│   ├── plots.py            # create_confusion_matrix()
│   ├── reports.py          # format_training_report()
│   └── formatters.py       # format_metrics()
│
└── pipelines/               # Orquestadores
    ├── training.py         # train_pipeline()
    └── inference.py        # predict_pipeline()
```

---

### Patrón: Repository

Encapsula acceso a datos detrás de una interfaz:

```python
# core/interfaces.py (Lógica define la interfaz)
from abc import ABC, abstractmethod

class DataRepository(ABC):
    """Interface para acceso a datos."""
    
    @abstractmethod
    def load_training_data(self) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def save_model(self, model: Any, name: str) -> None:
        pass


# data/csv_repository.py (I/O implementa la interfaz)
class CSVRepository(DataRepository):
    """Implementación con CSV."""
    
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
    
    def load_training_data(self) -> pd.DataFrame:
        return pd.read_csv(f"{self.data_dir}/train.csv")
    
    def save_model(self, model: Any, name: str) -> None:
        joblib.dump(model, f"{self.data_dir}/{name}.pkl")


# core/training.py (Lógica usa la interfaz)
def train_model(repo: DataRepository) -> RandomForestClassifier:
    """Lógica no sabe si datos vienen de CSV, DB, o API."""
    data = repo.load_training_data()
    # ... lógica de entrenamiento ...
    return model
```

**Ventaja**: Puedes cambiar de CSV a base de datos sin modificar lógica de negocio.

---

## Testing por Capas

### Capa I/O: Integration Tests

```python
def test_load_training_data():
    """Test con archivo real."""
    data = load_training_data("tests/fixtures/sample.csv")
    assert len(data) > 0
    assert 'target' in data.columns
```

### Capa Lógica: Unit Tests (Puros)

```python
def test_normalize_features():
    """Test sin I/O - datos en memoria."""
    data = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
    result = normalize_features(data)
    
    assert 'normalized' in result.columns
    assert abs(result['normalized'].mean()) < 0.01  # ~0
    assert abs(result['normalized'].std() - 1.0) < 0.01  # ~1
```

### Capa Presentación: Unit Tests

```python
def test_format_training_report():
    """Test sin I/O - solo formateo."""
    report = format_training_report("RF", 0.95, 1000)
    
    assert "RF" in report
    assert "95%" in report
    assert "1,000" in report
```

---

## Aprendizaje Clave

**Puntos críticos a recordar**:

1. **Lógica de negocio debe ser pura**: Sin I/O, sin efectos secundarios, fácil de testear
2. **Dependencias apuntan hacia adentro**: Core no depende de I/O ni Presentación
3. **Orquestador coordina capas**: Pipeline combina capas pero no contiene lógica
4. **Una función, una capa**: No mezcles I/O con lógica en la misma función

**Cómo desarrollar intuición**:

- **Pregúntate**: "¿Puedo testear esta función sin archivos reales?"
  - NO → Separa I/O de lógica
  - SÍ → Está bien diseñada

- **Pregúntate**: "¿Puedo reusar esta función en otro proyecto?"
  - NO → Probablemente está acoplada a I/O específico
  - SÍ → Buena separación de responsabilidades

**Cuándo usar**:
- **Siempre en proyectos de ML/Data**: Facilita testing y mantenimiento
- **Cuando el código crece**: Previene el caos
- **Trabajo en equipo**: Cada persona puede trabajar en una capa

**Cuándo NO preocuparse tanto**:
- **Scripts de exploración**: Notebooks experimentales pueden mezclar capas
- **Prototipos rápidos**: Primero valida la idea, luego refactoriza

**Referencia oficial**: Martin, R. C. (2017). *Clean Architecture*. Prentice Hall. Chapter 22: The Clean Architecture.

---

## Resumen

**Tres capas fundamentales**:
1. **I/O**: Lectura/escritura de datos externos
2. **Core**: Lógica de negocio pura (sin I/O)
3. **Presentación**: Formateo y visualización

**Regla de oro**: Core no depende de I/O ni Presentación.

**Beneficios**:
- Lógica testeable sin I/O
- Código reutilizable
- Mantenimiento más fácil
- Cambios menos riesgosos
    """Train model - TODO mezclado en una función."""
    # I/O mezclado con lógica
    data = pd.read_csv(csv_path)
    
    # Validación mezclada
    if 'target' not in data.columns:
        print("Error: missing target column")
        return
    
    # Transformación mezclada
    data = data.dropna()
    data['normalized'] = (data['value'] - data['value'].mean()) / data['value'].std()
    
    # Entrenamiento mezclado
    X = data.drop('target', axis=1)
    y = data['target']
    model = RandomForestClassifier()
    model.fit(X, y)
    
    # Evaluación mezclada
    accuracy = model.score(X, y)
    
    # Visualización mezclada
    plt.figure()
    plt.plot(y, model.predict(X))
    plt.savefig(f"{output_dir}/predictions.png")
    
    # Más I/O mezclado
    joblib.dump(model, f"{output_dir}/model.pkl")
    
    # Presentación mezclada
    print(f"Model trained with accuracy: {accuracy:.2f}")
```

**Problemas**:

- **No testeable**: Necesitas archivos reales para testear
- **No reutilizable**: No puedes usar solo la transformación
- **Frágil**: Cambiar formato de archivo afecta todo
- **Difícil de mantener**: 200 líneas haciendo todo
- **Acoplamiento alto**: Todas las capas mezcladas

---

### Ejemplo Correcto: Capas Separadas

```python
# ============================================
# CAPA 1: I/O
# ============================================

def load_training_data(csv_path: str) -> pd.DataFrame:
    """
    Load training data from CSV.
    
    :param csv_path: Path to CSV file
    :type csv_path: str
    :return: Raw dataframe
    :rtype: pd.DataFrame
    :raises FileNotFoundError: If file doesn't exist
    """
    return pd.read_csv(csv_path)


def save_model(model: RandomForestClassifier, output_path: str) -> None:
    """
    Save trained model to disk.
    
    :param model: Trained model
    :type model: RandomForestClassifier
    :param output_path: Path to save model
    :type output_path: str
    """
    joblib.dump(model, output_path)


# ============================================
# CAPA 2: BUSINESS LOGIC
# ============================================

def validate_training_data(data: pd.DataFrame) -> None:
    """
    Validate training data has required columns.
    
    :param data: Input dataframe
    :type data: pd.DataFrame
    :raises ValueError: If validation fails
    """
    if 'target' not in data.columns:
        raise ValueError("Missing 'target' column")
    
    if data.empty:
        raise ValueError("Data is empty")


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess data for training.
    
    Pure function - no I/O, easy to test.
    
    :param data: Raw dataframe
    :type data: pd.DataFrame
    :return: Preprocessed dataframe
    :rtype: pd.DataFrame
    """
    # Remove missing values
    cleaned = data.dropna()
    
    # Normalize
    cleaned = cleaned.copy()
    cleaned['normalized'] = (
        (cleaned['value'] - cleaned['value'].mean()) / 
        cleaned['value'].std()
    )
    
    return cleaned


def train_random_forest(
    X: pd.DataFrame,
    y: pd.Series,
    n_estimators: int = 100,
) -> RandomForestClassifier:
    """
    Train Random Forest model.
    
    Pure function - no I/O, easy to test.
    
    :param X: Features
    :type X: pd.DataFrame
    :param y: Target
    :type y: pd.Series
    :param n_estimators: Number of trees
    :type n_estimators: int
    :return: Trained model
    :rtype: RandomForestClassifier
    """
    model = RandomForestClassifier(n_estimators=n_estimators)
    model.fit(X, y)
    return model


def evaluate_model(
    model: RandomForestClassifier,
    X: pd.DataFrame,
    y: pd.Series,
) -> float:
    """
    Evaluate model accuracy.
    
    Pure function - no I/O, easy to test.
    
    :param model: Trained model
    :type model: RandomForestClassifier
    :param X: Features
    :type X: pd.DataFrame
    :param y: Target
    :type y: pd.Series
    :return: Accuracy score
    :rtype: float
    """
    return model.score(X, y)


# ============================================
# CAPA 3: PRESENTATION
# ============================================

def generate_prediction_plot(
    y_true: pd.Series,
    y_pred: np.ndarray,
    output_path: str,
) -> None:
    """
    Generate and save prediction plot.
    
    :param y_true: True values
    :type y_true: pd.Series
    :param y_pred: Predicted values
    :type y_pred: np.ndarray
    :param output_path: Path to save plot
    :type output_path: str
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(y_true, y_pred, alpha=0.5)
    plt.xlabel("True Values")
    plt.ylabel("Predictions")
    plt.title("Predictions vs True Values")
    plt.savefig(output_path)
    plt.close()


def format_training_report(
    model_name: str,
    accuracy: float,
    n_samples: int,
) -> str:
    """
    Format training report.
    
    :param model_name: Name of the model
    :type model_name: str
    :param accuracy: Model accuracy
    :type accuracy: float
    :param n_samples: Number of training samples
    :type n_samples: int
    :return: Formatted report
    :rtype: str
    """
    return f"""
Training Report
===============
Model: {model_name}
Samples: {n_samples}
Accuracy: {accuracy:.4f}
    """.strip()


# ============================================
# ORCHESTRATION
# ============================================

def train_model_pipeline(
    csv_path: str,
    output_dir: str,
) -> None:
    """
    Orchestrate training pipeline.
    
    Coordinates all layers but doesn't mix responsibilities.
    
    :param csv_path: Path to training data
    :type csv_path: str
    :param output_dir: Directory for outputs
    :type output_dir: str
    """
    # Layer 1: I/O
    data = load_training_data(csv_path)
    
    # Layer 2: Business Logic
    validate_training_data(data)
    processed = preprocess_data(data)
    
    X = processed.drop('target', axis=1)
    y = processed['target']
    
    model = train_random_forest(X, y)
    accuracy = evaluate_model(model, X, y)
    
    # Layer 1: I/O (save)
    save_model(model, f"{output_dir}/model.pkl")
    
    # Layer 3: Presentation
    predictions = model.predict(X)
    generate_prediction_plot(y, predictions, f"{output_dir}/predictions.png")
    
    report = format_training_report("RandomForest", accuracy, len(data))
    print(report)
```

**Ventajas**:

- **Testeable**: Cada función se puede testear independientemente
- **Reutilizable**: Lógica pura se puede usar en otros proyectos
- **Mantenible**: Cambios en una capa no afectan otras
- **Claro**: Cada función tiene una responsabilidad obvia
- **Colaboración fácil**: Diferentes personas pueden trabajar en diferentes capas

---

## 2. Capa de I/O: Input/Output

### Por Qué Importa

La capa de I/O maneja toda la interacción con el mundo externo. Separar esta capa permite cambiar formatos de archivo, fuentes de datos, o destinos de salida sin tocar la lógica de negocio.

---

### Responsabilidades de la Capa I/O

**Lectura**:
- Cargar datos desde archivos (CSV, JSON, Parquet)
- Consultar bases de datos
- Llamar APIs externas
- Leer configuraciones

**Escritura**:
- Guardar resultados en archivos
- Insertar en bases de datos
- Enviar a APIs
- Escribir logs

---

### Ejemplo: Funciones de I/O

```python
import json
from pathlib import Path
import pandas as pd


def load_csv_data(file_path: str) -> pd.DataFrame:
    """
    Load data from CSV file.
    
    :param file_path: Path to CSV file
    :type file_path: str
    :return: Loaded dataframe
    :rtype: pd.DataFrame
    :raises FileNotFoundError: If file doesn't exist
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return pd.read_csv(path)


def load_config(config_path: str) -> dict[str, any]:
    """
    Load configuration from JSON file.
    
    :param config_path: Path to config file
    :type config_path: str
    :return: Configuration dictionary
    :rtype: dict[str, any]
    :raises FileNotFoundError: If file doesn't exist
    :raises json.JSONDecodeError: If JSON is invalid
    """
    with open(config_path) as f:
        return json.load(f)


def save_results(
    results: dict[str, float],
    output_path: str,
) -> None:
    """
    Save results to JSON file.
    
    :param results: Results dictionary
    :type results: dict[str, float]
    :param output_path: Path to save results
    :type output_path: str
    """
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
```

---

## 3. Capa de Lógica de Negocio

### Por Qué Importa

La capa de lógica de negocio contiene las transformaciones, algoritmos, y reglas que definen qué hace tu aplicación. Esta capa debe ser pura (sin I/O) para ser fácilmente testeable y reutilizable.

---

### Características de Funciones Puras

**Una función pura**:
1. No tiene efectos secundarios (no modifica estado externo)
2. No hace I/O (no lee/escribe archivos)
3. Retorna el mismo output para el mismo input
4. Es fácil de testear (no necesita mocks)

---

### Ejemplo: Lógica Pura

```python
import pandas as pd
import numpy as np


def remove_outliers(
    data: pd.DataFrame,
    column: str,
    n_std: float = 3.0,
) -> pd.DataFrame:
    """
    Remove outliers from dataframe.
    
    Pure function - no I/O, deterministic, easy to test.
    
    :param data: Input dataframe
    :type data: pd.DataFrame
    :param column: Column to check for outliers
    :type column: str
    :param n_std: Number of standard deviations
    :type n_std: float
    :return: Dataframe without outliers
    :rtype: pd.DataFrame
    """
    mean = data[column].mean()
    std = data[column].std()
    
    lower_bound = mean - n_std * std
    upper_bound = mean + n_std * std
    
    return data[
        (data[column] >= lower_bound) & 
        (data[column] <= upper_bound)
    ]


def calculate_feature_importance(
    model: RandomForestClassifier,
    feature_names: list[str],
) -> dict[str, float]:
    """
    Calculate feature importance from model.
    
    Pure function - no I/O, easy to test.
    
    :param model: Trained model
    :type model: RandomForestClassifier
    :param feature_names: Names of features
    :type feature_names: list[str]
    :return: Dictionary mapping features to importance
    :rtype: dict[str, float]
    """
    importances = model.feature_importances_
    return dict(zip(feature_names, importances))


def split_train_test(
    data: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split data into train and test sets.
    
    Pure function - deterministic with random_state.
    
    :param data: Input dataframe
    :type data: pd.DataFrame
    :param test_size: Proportion of test set
    :type test_size: float
    :param random_state: Random seed
    :type random_state: int
    :return: Tuple of (train, test) dataframes
    :rtype: tuple[pd.DataFrame, pd.DataFrame]
    """
    n = len(data)
    n_test = int(n * test_size)
    
    shuffled = data.sample(frac=1, random_state=random_state)
    
    test = shuffled.iloc[:n_test]
    train = shuffled.iloc[n_test:]
    
    return train, test
```

---

## 4. Capa de Presentación

### Por Qué Importa

La capa de presentación maneja cómo se muestran los resultados al usuario. Separar esta capa permite cambiar formatos de output, generar diferentes visualizaciones, o adaptar reportes sin tocar la lógica de negocio.

---

### Responsabilidades de la Capa de Presentación

**Formateo**:
- Convertir datos a formato legible
- Generar reportes
- Preparar respuestas de API

**Visualización**:
- Crear gráficos
- Generar dashboards
- Exportar visualizaciones

---

### Ejemplo: Funciones de Presentación

```python
import matplotlib.pyplot as plt
import seaborn as sns


def format_metrics_table(metrics: dict[str, float]) -> str:
    """
    Format metrics as ASCII table.
    
    :param metrics: Dictionary of metrics
    :type metrics: dict[str, float]
    :return: Formatted table string
    :rtype: str
    """
    lines = ["Metric          | Value"]
    lines.append("-" * 30)
    
    for name, value in metrics.items():
        lines.append(f"{name:15} | {value:.4f}")
    
    return "\n".join(lines)


def plot_feature_importance(
    importance: dict[str, float],
    output_path: str,
    top_n: int = 10,
) -> None:
    """
    Plot feature importance bar chart.
    
    :param importance: Feature importance dictionary
    :type importance: dict[str, float]
    :param output_path: Path to save plot
    :type output_path: str
    :param top_n: Number of top features to show
    :type top_n: int
    """
    # Sort by importance
    sorted_features = sorted(
        importance.items(),
        key=lambda x: x[1],
        reverse=True
    )[:top_n]
    
    features, values = zip(*sorted_features)
    
    plt.figure(figsize=(10, 6))
    plt.barh(features, values)
    plt.xlabel("Importance")
    plt.title(f"Top {top_n} Feature Importance")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def generate_training_summary(
    model_name: str,
    train_metrics: dict[str, float],
    test_metrics: dict[str, float],
    training_time: float,
) -> str:
    """
    Generate comprehensive training summary.
    
    :param model_name: Name of the model
    :type model_name: str
    :param train_metrics: Training metrics
    :type train_metrics: dict[str, float]
    :param test_metrics: Test metrics
    :type test_metrics: dict[str, float]
    :param training_time: Time taken to train (seconds)
    :type training_time: float
    :return: Formatted summary
    :rtype: str
    """
    return f"""
{'='*50}
TRAINING SUMMARY
{'='*50}

Model: {model_name}
Training Time: {training_time:.2f}s

Training Metrics:
{format_metrics_table(train_metrics)}

Test Metrics:
{format_metrics_table(test_metrics)}

{'='*50}
    """.strip()
```

---

## 5. Arquitectura en Capas

### Por Qué Importa

Una arquitectura en capas bien definida facilita el mantenimiento, testing, y evolución del código. Cada capa tiene dependencias claras y responsabilidades específicas.

---

### Reglas de Dependencia

**Regla fundamental**: Las capas solo pueden depender de capas inferiores, nunca superiores.

```
┌─────────────────────────────┐
│   Presentation Layer        │  ← Depende de Business Logic
├─────────────────────────────┤
│   Business Logic Layer      │  ← Depende de I/O (solo para tipos)
├─────────────────────────────┤
│   I/O Layer                 │  ← No depende de otras capas
└─────────────────────────────┘
```

---

### Ejemplo: Proyecto Estructurado

```
project/
├── src/
│   ├── io/
│   │   ├── __init__.py
│   │   ├── data_loader.py      # Capa I/O
│   │   └── model_saver.py
│   │
│   ├── business/
│   │   ├── __init__.py
│   │   ├── preprocessing.py    # Lógica de negocio
│   │   ├── training.py
│   │   └── evaluation.py
│   │
│   ├── presentation/
│   │   ├── __init__.py
│   │   ├── formatters.py       # Presentación
│   │   └── visualizations.py
│   │
│   └── pipeline.py             # Orquestación
│
└── tests/
    ├── test_io.py
    ├── test_business.py
    └── test_presentation.py
```

---

## Aprendizaje Clave

### Puntos Críticos a Recordar

1. **Tres capas**: I/O, Business Logic, Presentation
2. **I/O separado**: Lectura/escritura en funciones dedicadas
3. **Lógica pura**: Sin I/O, fácil de testear
4. **Presentation separada**: Formateo y visualización aparte
5. **Dependencias claras**: Capas superiores dependen de inferiores
6. **Funciones pequeñas**: Cada función hace una cosa
7. **Orquestación**: Función coordinadora que usa todas las capas

---

### Cómo Desarrollar Intuición

**Pregúntate**: "¿Esta función hace más de una cosa?"
- SÍ → Separar en funciones más pequeñas
- NO → Está bien

**Pregúntate**: "¿Puedo testear esta lógica sin archivos/DB?"
- NO → Lógica mezclada con I/O, separar
- SÍ → Bien separada

**Pregúntate**: "¿Esta función tiene `pd.read_csv()` Y transformaciones?"
- SÍ → Separar I/O de lógica
- NO → Bien separada

**Pregúntate**: "¿Puedo reusar esta función en otro proyecto?"
- NO → Probablemente mezclada con I/O específico
- SÍ → Bien separada

---

### Cuándo Usar Cada Capa

**Capa I/O cuando**:
- Lees/escribes archivos
- Llamas APIs externas
- Accedes bases de datos
- Cargas configuraciones

**Capa Business Logic cuando**:
- Transformas datos
- Aplicas algoritmos
- Validas reglas de negocio
- Calculas métricas
- Entrenas modelos

**Capa Presentation cuando**:
- Formateas output para usuario
- Creas visualizaciones
- Generas reportes
- Preparas respuestas de API

---

## Resumen de Principios

La separación de responsabilidades hace tu código más mantenible, testeable y reutilizable:

1. **Separa I/O**: Lectura/escritura en funciones dedicadas
2. **Lógica pura**: Sin I/O, solo transformaciones
3. **Presentation aparte**: Formateo separado de lógica
4. **Testeable**: Cada capa se puede testear independientemente
5. **Reutilizable**: Lógica pura se puede usar en múltiples contextos
6. **Mantenible**: Cambios en una capa no afectan otras
7. **Colaboración**: Diferentes personas pueden trabajar en diferentes capas

**Regla de oro**: Si una función tiene `pd.read_csv()` Y lógica de negocio, sepárala en dos funciones. Si una función hace más de una cosa, sepárala.

---

## Referencias

1. Dijkstra, E. W. (1982). On the role of scientific thought. In *Selected writings on Computing: A Personal Perspective*. Springer.
2. Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.
3. Separation of Concerns: <https://en.wikipedia.org/wiki/Separation_of_concerns>
4. Single Responsibility Principle: <https://en.wikipedia.org/wiki/Single-responsibility_principle>
5. Clean Architecture Blog: <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>

---

## Ejercicio Práctico Individual

Refactoriza este código mezclado en tres capas separadas:

```python
def analyze_sales(csv_path: str, output_dir: str):
    # Load data
    data = pd.read_csv(csv_path)
    
    # Clean
    data = data.dropna()
    data['total'] = data['price'] * data['quantity']
    
    # Analyze
    monthly_sales = data.groupby('month')['total'].sum()
    
    # Visualize
    plt.figure()
    monthly_sales.plot(kind='bar')
    plt.savefig(f"{output_dir}/sales.png")
    
    # Report
    print(f"Total sales: ${monthly_sales.sum():.2f}")
    
    # Save
    monthly_sales.to_csv(f"{output_dir}/monthly_sales.csv")
```

**Criterios de éxito**:
- [ ] Funciones de I/O separadas (load, save)
- [ ] Lógica pura sin I/O (clean, analyze)
- [ ] Presentación separada (visualize, format)
- [ ] Función orquestadora que coordina
- [ ] Cada función testeable independientemente

---
