# Separación de Responsabilidades

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Las Tres Capas Fundamentales](#1-las-tres-capas-fundamentales)
3. [Capa de I/O: Input/Output](#2-capa-de-io-inputoutput)
4. [Capa de Lógica de Negocio](#3-capa-de-lógica-de-negocio)
5. [Capa de Presentación](#4-capa-de-presentación)
6. [Arquitectura en Capas](#5-arquitectura-en-capas)
7. [Resumen](#resumen-de-principios)

---

## Introducción

La separación de responsabilidades (Separation of Concerns) es un principio fundamental de diseño de software que establece que cada módulo o función debe tener una única responsabilidad bien definida. Este principio es especialmente crítico en proyectos de Data Science y ML donde el código tiende a mezclar I/O, transformaciones, y visualizaciones.

**Referencia principal**: Dijkstra, E. W. (1982). On the role of scientific thought. In *Selected writings on Computing: A Personal Perspective* (pp. 60-66). Springer.

### Contexto: Por Qué Importa

**Problema real en Data/IA**:
Tienes una función `train_model()` que lee CSV, limpia datos, entrena modelo, genera gráficos, y guarda resultados. Cuando quieres cambiar el formato de salida, tienes que modificar una función de 200 líneas y arriesgarte a romper el entrenamiento. Cuando quieres testear la lógica de limpieza, necesitas archivos CSV reales.

**Ejemplo concreto**:
Tu función hace TODO: carga datos desde CSV, valida columnas, transforma features, entrena modelo, evalúa métricas, genera visualizaciones, y guarda resultados en múltiples formatos. Cuando necesitas reusar solo la transformación en otro proyecto, tienes que copiar y adaptar código mezclado con I/O específico.

**Consecuencias de NO usarlo**:
- **Difícil de testear**: No puedes testear lógica sin archivos reales
- **Imposible de reusar**: Lógica mezclada con I/O específico
- **Mantenimiento costoso**: Cambiar una parte afecta todo
- **Trabajo en equipo difícil**: Conflictos constantes en la misma función
- **Debugging complejo**: Errores pueden estar en cualquier capa
- **Acoplamiento alto**: Cambios en formato de archivo rompen lógica de negocio

### Principio Fundamental

> "The separation of concerns is the key to managing complexity in software systems."
>
> — Edsger W. Dijkstra

Cada función debe hacer una cosa y hacerla bien. Mezclar responsabilidades crea código frágil y difícil de mantener.

---

### El Concepto

**Definición técnica**:
La separación de responsabilidades es un principio de diseño que establece que el código debe organizarse en módulos donde cada módulo tiene una responsabilidad específica y bien definida. En el contexto de Data/IA, esto significa separar I/O, lógica de negocio, y presentación.

**Cómo funciona internamente**:
1. **Identificar responsabilidades**: Determinar qué hace cada parte del código
2. **Agrupar por responsabilidad**: Código con la misma responsabilidad va junto
3. **Definir interfaces**: Establecer cómo se comunican las capas
4. **Minimizar dependencias**: Cada capa solo conoce lo necesario

**Terminología clave**:
- **Separation of Concerns (SoC)**: Principio de separar código por responsabilidades
- **Single Responsibility Principle (SRP)**: Cada módulo tiene una única razón para cambiar
- **Layered Architecture**: Organización del código en capas con responsabilidades específicas
- **Pure function**: Función sin efectos secundarios (sin I/O)
- **Side effect**: Operación que modifica estado externo (I/O, modificar variables globales)

---

## 1. Las Tres Capas Fundamentales

### Por Qué Importa

En proyectos de Data/IA, el código típicamente se organiza en tres capas principales. Entender estas capas y mantenerlas separadas es fundamental para código mantenible.

---

### Las Tres Capas

**1. Capa de I/O (Input/Output)**:
- Lectura y escritura de archivos
- Llamadas a APIs externas
- Acceso a bases de datos
- Carga de configuraciones

**2. Capa de Lógica de Negocio**:
- Transformaciones de datos
- Algoritmos y cálculos
- Validaciones de reglas de negocio
- Entrenamiento de modelos

**3. Capa de Presentación**:
- Formateo de output
- Generación de visualizaciones
- Creación de reportes
- Preparación de respuestas

---

### Ejemplo Incorrecto: Todo Mezclado

```python
def train_model(csv_path: str, output_dir: str) -> None:
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
