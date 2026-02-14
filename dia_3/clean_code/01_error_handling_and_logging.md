# Error Handling y Logging

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Excepciones Específicas vs Genéricas](#1-excepciones-específicas-vs-genéricas)
3. [Logging Efectivo](#2-logging-efectivo)
4. [Configuración de Logging](#3-configuración-de-logging)
5. [Contexto en Errores](#4-contexto-en-errores)
6. [Resumen](#resumen-de-principios)

---

## Introducción

El manejo de errores y logging son prácticas fundamentales que determinan si tu código es debuggeable en producción o una caja negra imposible de diagnosticar.

**Referencia principal**: Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 7: Error Handling.

### Contexto: Por Qué Importa

**Problema real en Data/IA**:
Estás entrenando un modelo con un dataset de 10 millones de registros. A las 3 AM (después de 6 horas de procesamiento) el script falla con "KeyError: 'age'". No sabes en qué registro falló, qué datos tenía, ni por qué. Tienes que empezar de cero.

**Ejemplo concreto**:
Tu función de preprocesamiento falla con "ValueError" pero no sabes:
- ¿En qué archivo falló?
- ¿Qué valor causó el error?
- ¿Cuántos registros procesó antes de fallar?
- ¿Fue un error puntual o sistemático?

**Consecuencias de NO usarlo**:
- **Debugging imposible**: Errores sin contexto, no sabes qué pasó
- **Tiempo perdido**: Reejecutar procesos largos desde cero
- **Datos perdidos**: No sabes qué registros se procesaron correctamente
- **Producción frágil**: Errores en producción sin forma de diagnosticar

### Principio Fundamental

> "Clean code is simple and direct. Clean code reads like well-written prose. Clean code never obscures the designer's intent but rather is full of crisp abstractions and straightforward lines of control."
>
> — Grady Booch

El manejo de errores es parte del código, no un añadido. Debe ser tan limpio y claro como el resto del código.

---

### El Concepto

**Definición técnica**:
El manejo de errores y logging son prácticas complementarias: el manejo de errores controla el flujo cuando algo sale mal, mientras que el logging registra información sobre la ejecución para debugging y monitoreo.

**Cómo funciona internamente**:
1. **Excepciones**: Python usa try/except para capturar y manejar errores
2. **Logging**: Módulo `logging` registra eventos con diferentes niveles de severidad
3. **Contexto**: Ambos deben proporcionar información suficiente para diagnosticar problemas

**Terminología clave**:
- **Exception**: Objeto que representa un error en tiempo de ejecución
- **Logging level**: Severidad del mensaje (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- **Stack trace**: Secuencia de llamadas que llevaron al error
- **Context**: Información adicional sobre el estado cuando ocurrió el error

---

## 1. Excepciones Específicas vs Genéricas

### Por Qué Importa

Capturar excepciones genéricas (`except Exception`) oculta errores y hace el debugging imposible. Las excepciones específicas te permiten manejar solo los errores que realmente puedes resolver.

---

### Ejemplo Incorrecto

```python
def load_model_config(config_path: str) -> dict:
    """Load model configuration - manejo genérico."""
    try:
        with open(config_path) as f:
            config = json.load(f)
        return config
    except Exception as e:  # ¡Demasiado genérico!
        print(f"Error: {e}")
        return {}
```

**Problemas**:

- Captura TODOS los errores (incluso KeyboardInterrupt)
- No distingue entre archivo no encontrado vs JSON inválido
- `print()` en vez de logging
- Retorna dict vacío silenciosamente (oculta el problema)

---

### Ejemplo Correcto

```python
import logging
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger(__name__)

def load_model_config(config_path: str) -> Dict[str, Any]:
    """
    Load model configuration from JSON file.
    
    :param config_path: Path to configuration file
    :type config_path: str
    :return: Configuration dictionary
    :rtype: Dict[str, Any]
    :raises FileNotFoundError: If config file doesn't exist
    :raises json.JSONDecodeError: If config file is not valid JSON
    :raises ValueError: If config file is empty
    """
    path = Path(config_path)
    
    # Check file exists
    if not path.exists():
        logger.error(f"Configuration file not found: {config_path}")
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    # Load and parse JSON
    try:
        with open(path) as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {config_path}: {e}")
        raise
    
    # Validate not empty
    if not config:
        logger.error(f"Configuration file is empty: {config_path}")
        raise ValueError(f"Config file is empty: {config_path}")
    
    logger.info(f"Successfully loaded config from {config_path}")
    return config
```

**Ventajas**:

- Excepciones específicas para cada tipo de error
- Logging con contexto claro
- No oculta errores (los propaga)
- Fácil de debuggear

---

## 2. Logging Efectivo

### Por Qué Importa

El logging es tu ventana al comportamiento del código en producción. Sin logging adecuado, los errores son imposibles de diagnosticar.

**Referencia**: Python Logging HOWTO: <https://docs.python.org/3/howto/logging.html>

---

### Niveles de Logging

```python
import logging

# DEBUG: Información detallada para diagnosticar problemas
logging.debug("Processing record 1523 with features: [0.5, 0.3, 0.8]")

# INFO: Confirmación de que las cosas funcionan como se espera
logging.info("Model training completed successfully in 45.2 seconds")

# WARNING: Algo inesperado pero no crítico
logging.warning("Missing 'age' field in 15 records, using default value")

# ERROR: Error que impide una operación específica
logging.error("Failed to save model checkpoint: disk full")

# CRITICAL: Error grave que puede detener la aplicación
logging.critical("Database connection lost, cannot continue")
```

---

### Ejemplo Incorrecto

```python
def process_dataset(data_path: str):
    """Process dataset - logging pobre."""
    print("Starting")  # No nivel, no contexto
    
    data = pd.read_csv(data_path)
    print(f"Loaded {len(data)} rows")  # print() en vez de logging
    
    # Procesa datos...
    cleaned = data.dropna()
    print("Cleaned")  # ¿Cuántos se eliminaron?
    
    return cleaned
```

**Problemas**:

- Usa `print()` en vez de logging
- Sin niveles de severidad
- Sin contexto útil
- No se puede controlar el output

---

### Ejemplo Correcto

```python
import logging
from pathlib import Path
import pandas as pd

logger = logging.getLogger(__name__)

def process_dataset(data_path: str) -> pd.DataFrame:
    """
    Process dataset with comprehensive logging.
    
    :param data_path: Path to CSV file
    :type data_path: str
    :return: Cleaned dataframe
    :rtype: pd.DataFrame
    :raises FileNotFoundError: If data file doesn't exist
    :raises pd.errors.EmptyDataError: If file is empty
    """
    logger.info(f"Starting dataset processing: {data_path}")
    
    # Load data
    try:
        data = pd.read_csv(data_path)
        logger.info(f"Loaded {len(data)} rows, {len(data.columns)} columns from {data_path}")
    except FileNotFoundError:
        logger.error(f"Data file not found: {data_path}")
        raise
    except pd.errors.EmptyDataError:
        logger.error(f"Data file is empty: {data_path}")
        raise
    
    # Clean data
    initial_rows = len(data)
    cleaned = data.dropna()
    removed_rows = initial_rows - len(cleaned)
    
    if removed_rows > 0:
        removal_pct = (removed_rows / initial_rows) * 100
        logger.warning(
            f"Removed {removed_rows} rows ({removal_pct:.1f}%) with missing values"
        )
    else:
        logger.info("No missing values found")
    
    logger.info(f"Processing complete: {len(cleaned)} rows remaining")
    return cleaned
```

**Ventajas**:

- Usa logging module con niveles apropiados
- Contexto rico (números, porcentajes, paths)
- Fácil de filtrar por nivel
- Se puede redirigir a archivos

---

## 3. Configuración de Logging

### Por Qué Importa

Una configuración adecuada de logging al inicio de tu aplicación asegura que todos los mensajes se registren consistentemente.

---

### Setup Básico para Scripts

```python
import logging
from pathlib import Path

def setup_logging(log_file: str = "pipeline.log", level: int = logging.INFO):
    """
    Configure logging for the application.
    
    :param log_file: Path to log file
    :type log_file: str
    :param level: Logging level
    :type level: int
    """
    # Create logs directory if needed
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # Also print to console
        ]
    )
    
    logging.info(f"Logging configured: level={logging.getLevelName(level)}, file={log_file}")

# Uso
if __name__ == "__main__":
    setup_logging("logs/training.log", level=logging.INFO)
    
    logger = logging.getLogger(__name__)
    logger.info("Starting training pipeline")
    # ... resto del código
```

---

### Setup Avanzado para Producción

```python
import logging
import logging.handlers
from pathlib import Path

def setup_production_logging(
    log_dir: str = "logs",
    level: int = logging.INFO,
    max_bytes: int = 10 * 1024 * 1024,  # 10MB
    backup_count: int = 5
):
    """
    Configure production-grade logging with rotation.
    
    :param log_dir: Directory for log files
    :type log_dir: str
    :param level: Logging level
    :type level: int
    :param max_bytes: Max size per log file
    :type max_bytes: int
    :param backup_count: Number of backup files to keep
    :type backup_count: int
    """
    # Create log directory
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    )
    simple_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # File handler with rotation
    file_handler = logging.handlers.RotatingFileHandler(
        f"{log_dir}/app.log",
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(simple_formatter)
    
    # Error file handler (only errors)
    error_handler = logging.handlers.RotatingFileHandler(
        f"{log_dir}/errors.log",
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(detailed_formatter)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(error_handler)
    
    logging.info("Production logging configured")
```

---

## 4. Contexto en Errores

### Por Qué Importa

Un error sin contexto es imposible de debuggear. Siempre incluye información sobre qué estabas procesando cuando falló.

---

### Ejemplo Incorrecto

```python
def train_model(data):
    """Train model - sin contexto en errores."""
    for i, row in data.iterrows():
        try:
            prediction = model.predict(row)
        except Exception as e:
            print(f"Error: {e}")  # ¿En qué fila? ¿Qué datos?
            continue
```

**Problemas**:

- No sabes en qué fila falló
- No sabes qué datos causaron el error
- Usa `print()` en vez de logging
- Captura excepciones genéricas

---

### Ejemplo Correcto

```python
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

def train_model(data: pd.DataFrame) -> List[float]:
    """
    Train model with detailed error context.
    
    :param data: Training data
    :type data: pd.DataFrame
    :return: List of predictions
    :rtype: List[float]
    """
    predictions = []
    errors = 0
    
    for idx, row in data.iterrows():
        try:
            prediction = model.predict(row)
            predictions.append(prediction)
        except ValueError as e:
            errors += 1
            logger.error(
                f"Prediction failed for row {idx}: {e}. "
                f"Row data: {row.to_dict()}"
            )
            predictions.append(None)
        except Exception as e:
            errors += 1
            logger.critical(
                f"Unexpected error at row {idx}: {type(e).__name__}: {e}. "
                f"Row data: {row.to_dict()}",
                exc_info=True  # Include full stack trace
            )
            raise
    
    if errors > 0:
        error_rate = (errors / len(data)) * 100
        logger.warning(f"Completed with {errors} errors ({error_rate:.1f}% error rate)")
    else:
        logger.info(f"Successfully processed all {len(data)} rows")
    
    return predictions
```

**Ventajas**:

- Incluye índice de fila donde falló
- Incluye datos de la fila problemática
- Distingue entre errores esperados y críticos
- Stack trace completo para errores inesperados

---

## Aprendizaje Clave

### Puntos Críticos a Recordar

1. **Excepciones específicas**: Captura solo los errores que puedes manejar
2. **Logging con contexto**: Incluye información que ayude a diagnosticar
3. **Niveles apropiados**: DEBUG para detalles, INFO para progreso, WARNING para problemas menores, ERROR para fallos
4. **No ocultes errores**: Si no puedes manejar un error, déjalo propagarse
5. **Configura logging**: Setup al inicio con formato consistente

---

### Cómo Desarrollar Intuición

**Pregúntate**: "Si este código falla a las 3 AM, ¿tendré suficiente información para debuggear?"
- NO → Añade más logging y contexto
- SÍ → Está bien

**Pregúntate**: "¿Puedo manejar este error de forma significativa?"
- SÍ → Captura la excepción específica y manéjala
- NO → Déjala propagarse (no uses `except Exception`)

**Pregúntate**: "¿Qué nivel de logging es apropiado?"
- Información de debugging detallada → DEBUG
- Progreso normal → INFO
- Algo raro pero no crítico → WARNING
- Operación falló → ERROR
- Sistema en peligro → CRITICAL

---

### Cuándo Usar Cada Nivel

**DEBUG cuando**:
- Valores de variables intermedias
- Flujo detallado de ejecución
- Solo útil durante desarrollo

**INFO cuando**:
- Inicio/fin de operaciones importantes
- Progreso de procesos largos
- Confirmación de éxito

**WARNING cuando**:
- Datos faltantes pero hay fallback
- Configuración subóptima
- Uso de valores por defecto

**ERROR cuando**:
- Operación falló pero el programa continúa
- Archivo no se pudo procesar
- Request a API falló

**CRITICAL cuando**:
- Sistema no puede continuar
- Pérdida de conexión crítica
- Corrupción de datos

---

## Resumen de Principios

El manejo de errores y logging efectivos son fundamentales en Data/IA:

1. **Usa excepciones específicas**: Captura solo lo que puedes manejar
2. **Logging con contexto**: Incluye información útil para debugging
3. **Niveles apropiados**: DEBUG, INFO, WARNING, ERROR, CRITICAL según severidad
4. **Configura al inicio**: Setup consistente con formato claro
5. **No ocultes errores**: Si no puedes manejar, propaga

**Regla de oro**: Si tu código falla en producción a las 3 AM, el logging debe tener suficiente información para que puedas diagnosticar el problema sin reejecutar.

---

## Referencias

1. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 7: Error Handling.
2. Python Logging HOWTO: <https://docs.python.org/3/howto/logging.html>
3. Python Logging Cookbook: <https://docs.python.org/3/howto/logging-cookbook.html>
4. PEP 282 – A Logging System: <https://peps.python.org/pep-0282/>
5. Effective Python: 90 Specific Ways to Write Better Python (2nd ed.). Brett Slatkin. Item 75: Use repr Strings for Debugging Output.

---

## Ejercicio Práctico Individual

Refactoriza el siguiente código para añadir manejo de errores apropiado y logging:

```python
def process_data_file(file_path):
    data = pd.read_csv(file_path)
    data = data.dropna()
    data['normalized'] = (data['value'] - data['value'].mean()) / data['value'].std()
    data.to_csv('output.csv')
    return len(data)
```

**Pistas**:
- ¿Qué puede fallar en cada paso?
- ¿Qué información necesitarías para debuggear?
- ¿Qué nivel de logging es apropiado para cada operación?

---

## 🏋️ Ejercicio Grupal: Añadir Error Handling y Logging a Pipeline

**Objetivo**: Aplicar principios de error handling y logging a un pipeline de ML real.

**Contexto**: Has heredado un script de entrenamiento que falla frecuentemente en producción, pero nadie sabe por qué. El equipo pierde horas reejecutando procesos y debuggeando sin información.

**Tiempo estimado**: 30-45 minutos

**Dinámica**:
1. **Análisis individual** (5 min): Identifica puntos de fallo
2. **Discusión en grupo** (10 min): Planifiquen estrategia de logging
3. **Refactorización colaborativa** (20 min): Añadan error handling y logging
4. **Presentación** (10 min): Compartan mejoras con otros grupos

---

### Código a Refactorizar

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_pipeline(data_path, model_path, test_size=0.2):
    # Load data
    data = pd.read_csv(data_path)
    
    # Prepare features
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    # Evaluate
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))
    
    # Save model
    joblib.dump(model, model_path)
    
    return {'train_acc': train_acc, 'test_acc': test_acc}

if __name__ == '__main__':
    result = train_pipeline('data.csv', 'model.pkl')
    print(result)
```

---

### Instrucciones para el Grupo

**Paso 1: Identificar Puntos de Fallo** (10 minutos)

Discutan y anoten:

1. ¿Qué puede fallar en cada paso?
2. ¿Qué información necesitarían para diagnosticar cada fallo?
3. ¿Qué errores son recuperables vs críticos?
4. ¿Qué nivel de logging es apropiado para cada operación?

**Paso 2: Diseñar Estrategia** (10 minutos)

Decidan en grupo:

1. ¿Qué excepciones específicas capturar?
2. ¿Qué información incluir en cada log?
3. ¿Cómo configurar el logging?
4. ¿Qué validaciones añadir?

**Paso 3: Refactorizar** (20 minutos)

Dividan el trabajo:

- **Persona 1**: Setup de logging y carga de datos
- **Persona 2**: Preparación de features y validación
- **Persona 3**: Entrenamiento y evaluación
- **Persona 4**: Guardado de modelo y función main

**Criterios de Éxito**:

- [ ] Logging configurado al inicio
- [ ] Excepciones específicas para cada tipo de error
- [ ] Contexto rico en cada log (números, paths, etc.)
- [ ] Niveles de logging apropiados
- [ ] Validaciones de datos
- [ ] Información suficiente para debuggear sin reejecutar
- [ ] No se ocultan errores críticos

---

### Pistas

**Para Carga de Datos**:
```python
# Capturar errores específicos
try:
    data = pd.read_csv(data_path)
    logger.info(f"Loaded {len(data)} rows from {data_path}")
except FileNotFoundError:
    logger.error(f"Data file not found: {data_path}")
    raise
except pd.errors.EmptyDataError:
    logger.error(f"Data file is empty: {data_path}")
    raise
```

**Para Validación**:
```python
# Validar antes de procesar
if 'target' not in data.columns:
    logger.error(f"Missing 'target' column. Available: {data.columns.tolist()}")
    raise ValueError("Target column not found")

if len(data) < 100:
    logger.warning(f"Small dataset: only {len(data)} rows")
```

**Para Entrenamiento**:
```python
# Log progreso y métricas
logger.info("Starting model training")
model.fit(X_train, y_train)
logger.info(f"Training complete: {len(X_train)} samples")

train_acc = accuracy_score(y_train, model.predict(X_train))
logger.info(f"Train accuracy: {train_acc:.4f}")
```

**Para Guardado**:
```python
# Manejar errores de escritura
try:
    joblib.dump(model, model_path)
    logger.info(f"Model saved to {model_path}")
except IOError as e:
    logger.error(f"Failed to save model: {e}")
    raise
```

---

### Preguntas para Reflexión

Después de refactorizar, discutan:

1. ¿Qué errores pueden diagnosticar ahora que antes no?
2. ¿Qué información de logging es más valiosa?
3. ¿Hay algún trade-off entre logging detallado y performance?
4. ¿Cómo cambiaría el logging para producción vs desarrollo?
5. ¿Qué errores deberían ser recuperables vs críticos?

---
