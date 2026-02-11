# Programación Defensiva

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Validación de Inputs](#1-validación-de-inputs)
3. [Guard Clauses](#2-guard-clauses)
4. [Verificación de Postcondiciones](#3-verificación-de-postcondiciones)
5. [Assertions vs Excepciones](#4-assertions-vs-excepciones)
6. [Patrones de Validación Reutilizables](#5-patrones-de-validación-reutilizables)
7. [Resumen](#resumen-de-principios)

---

## Introducción

La programación defensiva es una práctica de desarrollo que asume que todo puede fallar y prepara el código para manejar esos fallos de manera controlada. En lugar de confiar en que los inputs serán correctos, el código defensivo valida explícitamente todas las suposiciones y falla rápidamente cuando algo está mal.

**Referencia principal**: McConnell, S. (2004). *Code Complete* (2nd ed.). Microsoft Press. Chapter 8: Defensive Programming.

### Contexto: Por Qué Importa

**Problema real en Data/IA**:
Estás construyendo un pipeline de ML que procesa datos de múltiples fuentes externas. Los datos pueden venir con formatos incorrectos, valores nulos inesperados, o tipos de datos inconsistentes. Sin programación defensiva, tu pipeline falla en producción a las 3 AM, causando pérdida de datos y retrasos en entrenamientos críticos.

**Ejemplo concreto**:
Imagina que tu función recibe un DataFrame para entrenar un modelo. Asumes que todas las columnas numéricas están presentes y sin valores nulos. En desarrollo funciona perfecto. En producción, llega un CSV con una columna faltante y tu modelo explota con un error críptico. El cliente pierde confianza y tú pasas horas debuggeando.

**Consecuencias de NO usarlo**:
- **Fallos silenciosos**: Errores que no se detectan hasta que causan daño real
- **Debugging costoso**: Horas rastreando bugs que pudieron prevenirse con validaciones
- **Datos corruptos**: Resultados incorrectos que pasan desapercibidos
- **Pérdida de confianza**: Stakeholders dudan de la calidad de tu código
- **Incidentes en producción**: Sistemas caídos en horarios críticos
- **Tiempo perdido**: Reejecutar procesos largos desde cero

### Principio Fundamental

> "Defensive programming is a form of defensive design intended to ensure the continuing function of a piece of software under unforeseen circumstances."
>
> — Steve McConnell, Code Complete

El código defensivo no confía en nada: valida inputs, verifica precondiciones, y falla rápidamente cuando algo está mal.

---

### El Concepto

**Definición técnica**:
La programación defensiva es una práctica de desarrollo que asume que todo puede fallar y prepara el código para manejar esos fallos de manera controlada. Incluye validación de inputs, verificación de precondiciones, manejo explícito de casos edge, y fail-fast cuando algo está mal.

**Cómo funciona internamente**:
1. **Validación temprana**: Verificar inputs al inicio de la función
2. **Precondiciones explícitas**: Documentar y verificar lo que la función necesita
3. **Postcondiciones**: Verificar que el resultado es válido antes de retornar
4. **Invariantes**: Mantener el estado del sistema consistente
5. **Fail-fast**: Fallar inmediatamente cuando algo está mal, no propagar errores

**Terminología clave**:
- **Precondición**: Lo que debe ser verdad antes de ejecutar una función
- **Postcondición**: Lo que debe ser verdad después de ejecutar una función
- **Invariante**: Condición que siempre debe mantenerse verdadera
- **Fail-fast**: Principio de fallar inmediatamente ante errores
- **Guard clause**: Validación al inicio que retorna o lanza excepción temprano

---

## 1. Validación de Inputs

### Por Qué Importa

La validación de inputs es la primera línea de defensa contra errores. Verificar que los inputs son válidos antes de procesarlos previene errores costosos y facilita el debugging.

**Referencia**: Meyer, B. (1997). *Object-Oriented Software Construction* (2nd ed.). Prentice Hall. Chapter 11: Design by Contract.

---

### Ejemplo Incorrecto: Sin Validación

```python
def train_model(data, target_column):
    """Train model - asume que todo está bien."""
    # Asume que data es DataFrame
    # Asume que target_column existe
    # Asume que no hay valores nulos
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    model = RandomForestClassifier()
    model.fit(X, y)
    
    return model
```

**Problemas**:

- **No valida inputs**: ¿Qué pasa si `data` es None? ¿Si está vacío?
- **Asume estructura**: ¿Qué si `target_column` no existe en el DataFrame?
- **No verifica tipos**: ¿Qué si `data` no es un DataFrame?
- **Ignora valores nulos**: ¿Qué si hay NaN en los datos?
- **No valida resultado**: ¿El modelo se entrenó correctamente?
- **Falla tarde**: El error aparece en `fit()`, lejos del problema real

---

### Ejemplo Correcto: Validación Completa

```python
from typing import Any
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_model(
    data: pd.DataFrame,
    target_column: str,
    min_samples: int = 100,
) -> RandomForestClassifier:
    """
    Train a Random Forest model with defensive validation.
    
    :param data: Training dataset
    :type data: pd.DataFrame
    :param target_column: Name of target column
    :type target_column: str
    :param min_samples: Minimum required samples
    :type min_samples: int
    :return: Trained model
    :rtype: RandomForestClassifier
    :raises TypeError: If data is not a DataFrame
    :raises ValueError: If data is invalid or insufficient
    """
    # Validate types
    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            f"Expected DataFrame, got {type(data).__name__}"
        )
    
    # Validate not empty
    if data.empty:
        raise ValueError("Cannot train on empty DataFrame")
    
    # Validate target column exists
    if target_column not in data.columns:
        raise ValueError(
            f"Target column '{target_column}' not found. "
            f"Available columns: {list(data.columns)}"
        )
    
    # Validate sufficient samples
    if len(data) < min_samples:
        raise ValueError(
            f"Insufficient samples: {len(data)} < {min_samples}"
        )
    
    # Validate no nulls in target
    if data[target_column].isna().any():
        raise ValueError("Target column contains null values")
    
    # Prepare features
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    # Validate no nulls in features
    null_cols = X.columns[X.isna().any()].tolist()
    if null_cols:
        raise ValueError(
            f"Features contain null values in columns: {null_cols}"
        )
    
    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    
    # Postcondition: verify model trained
    if not hasattr(model, 'n_features_in_'):
        raise RuntimeError("Model failed to train properly")
    
    return model
```

**Ventajas**:

- **Falla rápido**: Detecta problemas antes de procesamiento costoso
- **Mensajes claros**: Errores específicos que facilitan debugging
- **Validación completa**: Verifica tipos, estructura, y calidad de datos
- **Documentación explícita**: Docstring lista todas las excepciones posibles
- **Postcondición**: Verifica que el resultado es válido
- **Mantenible**: Fácil agregar más validaciones

---

## 2. Guard Clauses

### Por Qué Importa

Las guard clauses son validaciones al inicio de una función que retornan o lanzan excepciones temprano. Esto evita anidamiento profundo y hace el código más legible.

---

### Ejemplo Incorrecto: Anidamiento Profundo

```python
def process_user_data(user_id, data):
    """Process user data - anidamiento profundo."""
    if user_id is not None:
        if user_id > 0:
            if data is not None:
                if len(data) > 0:
                    if 'email' in data:
                        # Lógica principal aquí
                        return process(data)
                    else:
                        raise ValueError("Email required")
                else:
                    raise ValueError("Data empty")
            else:
                raise ValueError("Data is None")
        else:
            raise ValueError("Invalid user_id")
    else:
        raise ValueError("user_id is None")
```

**Problemas**:

- **Anidamiento profundo**: Difícil de leer
- **Lógica principal oculta**: Está al final, anidada
- **Difícil de mantener**: Añadir validaciones aumenta anidamiento

---

### Ejemplo Correcto: Guard Clauses

```python
def process_user_data(
    user_id: int,
    data: dict[str, str],
) -> dict[str, str]:
    """
    Process user data with guard clauses.
    
    :param user_id: User ID
    :type user_id: int
    :param data: User data
    :type data: dict[str, str]
    :return: Processed data
    :rtype: dict[str, str]
    :raises ValueError: If validation fails
    """
    # Guard clauses - fail fast
    if user_id <= 0:
        raise ValueError(f"Invalid user_id: {user_id}")
    
    if not data:
        raise ValueError("Data cannot be empty")
    
    if 'email' not in data:
        raise ValueError("Email is required in data")
    
    # Main logic - not nested
    processed = {
        'user_id': user_id,
        'email': data['email'].lower(),
        'verified': True,
    }
    
    return processed
```

**Ventajas**:

- **Sin anidamiento**: Código plano y legible
- **Lógica principal visible**: Al final, sin anidamiento
- **Fácil de mantener**: Añadir validaciones es simple
- **Fail-fast**: Errores detectados inmediatamente

---

## 3. Verificación de Postcondiciones

### Por Qué Importa

Las postcondiciones verifican que el resultado de una función es válido antes de retornarlo. Esto previene que errores se propaguen silenciosamente.

---

### Ejemplo: Postcondiciones

```python
import pandas as pd
import numpy as np


def normalize_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize features with postcondition check.
    
    :param df: Input dataframe
    :type df: pd.DataFrame
    :return: Normalized dataframe
    :rtype: pd.DataFrame
    :raises RuntimeError: If normalization fails
    """
    # Precondition
    if df.empty:
        raise ValueError("Cannot normalize empty DataFrame")
    
    # Normalize
    result = (df - df.mean()) / df.std()
    
    # Postcondition: no NaN introduced
    if result.isna().any().any():
        raise RuntimeError(
            "Normalization introduced NaN values. "
            "Check for zero standard deviation."
        )
    
    # Postcondition: shape preserved
    if result.shape != df.shape:
        raise RuntimeError(
            f"Shape changed during normalization: "
            f"{df.shape} -> {result.shape}"
        )
    
    return result


def split_dataset(
    data: pd.DataFrame,
    train_ratio: float = 0.8,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split dataset with invariant checks.
    
    :param data: Input dataframe
    :type data: pd.DataFrame
    :param train_ratio: Proportion for training
    :type train_ratio: float
    :return: Tuple of (train, test) dataframes
    :rtype: tuple[pd.DataFrame, pd.DataFrame]
    :raises ValueError: If split is invalid
    """
    # Precondition
    if not 0 < train_ratio < 1:
        raise ValueError(
            f"train_ratio must be in (0, 1), got {train_ratio}"
        )
    
    n = len(data)
    split_idx = int(n * train_ratio)
    
    train = data.iloc[:split_idx]
    test = data.iloc[split_idx:]
    
    # Postcondition: no data loss
    if len(train) + len(test) != n:
        raise RuntimeError(
            f"Data loss in split: {len(train)} + {len(test)} != {n}"
        )
    
    # Postcondition: no overlap
    if set(train.index).intersection(test.index):
        raise RuntimeError("Overlap detected between train and test sets")
    
    # Postcondition: both non-empty
    if train.empty or test.empty:
        raise RuntimeError("Split resulted in empty train or test set")
    
    return train, test
```

**Ventajas**:

- **Detecta errores sutiles**: Problemas que pasarían desapercibidos
- **Documentación**: Postcondiciones documentan garantías
- **Debugging fácil**: Error aparece donde se origina
- **Confianza**: Sabes que el resultado es válido

---

## 4. Assertions vs Excepciones

### Por Qué Importa

Saber cuándo usar assertions vs excepciones es crucial. Las assertions son para invariantes que nunca deberían fallar, mientras que las excepciones son para errores recuperables.

**Referencia**: Python assert statement: <https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement>

---

### Cuándo Usar Cada Uno

**Usar Excepciones cuando**:
- Validar inputs de usuario
- Manejar errores de I/O
- Validar datos externos
- Errores que pueden ocurrir en producción

**Usar Assertions cuando**:
- Verificar invariantes internos
- Debugging durante desarrollo
- Condiciones que nunca deberían fallar
- Código que se puede desactivar con `-O`

---

### Ejemplo Incorrecto: Assertions para Validación

```python
def process_data(data):
    """Process data - MAL uso de assertions."""
    # MAL: assertions se pueden desactivar con -O
    assert data is not None, "Data cannot be None"
    assert len(data) > 0, "Data cannot be empty"
    
    # Procesar...
```

**Problema**: Las assertions se desactivan con `python -O`, dejando el código sin validación en producción.

---

### Ejemplo Correcto: Excepciones para Validación

```python
def process_data(data: list[int]) -> float:
    """
    Process data with proper validation.
    
    :param data: List of integers
    :type data: list[int]
    :return: Average value
    :rtype: float
    :raises ValueError: If data is invalid
    """
    # Excepciones para validación de inputs
    if data is None:
        raise ValueError("Data cannot be None")
    
    if len(data) == 0:
        raise ValueError("Data cannot be empty")
    
    # Procesar
    result = sum(data) / len(data)
    
    # Assertion para invariante interno
    assert result >= 0, "Average should be non-negative for positive inputs"
    
    return result
```

**Ventajas**:

- **Excepciones siempre activas**: No se desactivan en producción
- **Assertions para invariantes**: Verifican lógica interna
- **Claro**: Distinción entre errores externos e internos

---

## 5. Patrones de Validación Reutilizables

### Por Qué Importa

Crear validadores reutilizables reduce duplicación y asegura consistencia en las validaciones.

---

### Ejemplo: Clase Validadora

```python
from typing import Any
import pandas as pd
import numpy as np


class DataValidator:
    """Reusable validator for common data checks."""
    
    @staticmethod
    def require_dataframe(
        data: Any,
        name: str = "data",
    ) -> pd.DataFrame:
        """
        Ensure input is a DataFrame.
        
        :param data: Input to validate
        :type data: Any
        :param name: Name for error messages
        :type name: str
        :return: Validated dataframe
        :rtype: pd.DataFrame
        :raises TypeError: If not a DataFrame
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError(
                f"{name} must be DataFrame, got {type(data).__name__}"
            )
        return data
    
    @staticmethod
    def require_columns(
        df: pd.DataFrame,
        required: list[str],
        name: str = "DataFrame",
    ) -> None:
        """
        Ensure required columns exist.
        
        :param df: Dataframe to check
        :type df: pd.DataFrame
        :param required: Required column names
        :type required: list[str]
        :param name: Name for error messages
        :type name: str
        :raises ValueError: If columns are missing
        """
        missing = set(required) - set(df.columns)
        if missing:
            raise ValueError(
                f"{name} missing required columns: {missing}. "
                f"Available: {list(df.columns)}"
            )
    
    @staticmethod
    def require_no_nulls(
        df: pd.DataFrame,
        columns: list[str] | None = None,
    ) -> None:
        """
        Ensure no null values in specified columns.
        
        :param df: Dataframe to check
        :type df: pd.DataFrame
        :param columns: Columns to check (None = all)
        :type columns: list[str] | None
        :raises ValueError: If nulls are found
        """
        check_cols = columns or df.columns
        null_cols = [
            col for col in check_cols
            if df[col].isna().any()
        ]
        if null_cols:
            null_counts = {
                col: df[col].isna().sum()
                for col in null_cols
            }
            raise ValueError(
                f"Null values found: {null_counts}"
            )
    
    @staticmethod
    def require_numeric(
        df: pd.DataFrame,
        columns: list[str],
    ) -> None:
        """
        Ensure columns are numeric.
        
        :param df: Dataframe to check
        :type df: pd.DataFrame
        :param columns: Columns to check
        :type columns: list[str]
        :raises TypeError: If columns are not numeric
        """
        non_numeric = [
            col for col in columns
            if not pd.api.types.is_numeric_dtype(df[col])
        ]
        if non_numeric:
            raise TypeError(
                f"Columns must be numeric: {non_numeric}"
            )
    
    @staticmethod
    def require_positive(
        value: float | int,
        name: str = "value",
    ) -> None:
        """
        Ensure value is positive.
        
        :param value: Value to check
        :type value: float | int
        :param name: Name for error messages
        :type name: str
        :raises ValueError: If value is not positive
        """
        if value <= 0:
            raise ValueError(
                f"{name} must be positive, got {value}"
            )


# Uso
def train_model(
    data: pd.DataFrame,
    target: str,
    learning_rate: float = 0.01,
) -> RandomForestClassifier:
    """
    Train model with reusable validation.
    
    :param data: Training data
    :type data: pd.DataFrame
    :param target: Target column name
    :type target: str
    :param learning_rate: Learning rate
    :type learning_rate: float
    :return: Trained model
    :rtype: RandomForestClassifier
    """
    # Validaciones reutilizables
    DataValidator.require_dataframe(data, "training data")
    DataValidator.require_columns(data, [target])
    DataValidator.require_no_nulls(data, [target])
    DataValidator.require_positive(learning_rate, "learning_rate")
    
    # Training logic...
    model = RandomForestClassifier()
    # ...
    return model
```

**Ventajas**:

- **Reutilizable**: Validaciones consistentes en todo el código
- **Mantenible**: Cambiar validación en un solo lugar
- **Legible**: Código de validación claro y conciso
- **Testeable**: Validadores se pueden testear independientemente

---

## Aprendizaje Clave

### Puntos Críticos a Recordar

1. **Valida al inicio**: Guard clauses al principio de la función
2. **Falla rápido**: No dejes que errores se propaguen
3. **Mensajes útiles**: Errores que explican qué está mal y cómo arreglarlo
4. **Documenta excepciones**: Lista todas las excepciones en el docstring
5. **Verifica postcondiciones**: Asegura que el resultado es válido
6. **Excepciones vs assertions**: Excepciones para inputs, assertions para invariantes
7. **Validadores reutilizables**: Reduce duplicación

---

### Cómo Desarrollar Intuición

**Pregúntate**: "¿Qué puede salir mal con estos inputs?"
- Si hay múltiples formas de fallar → Agrega guard clauses
- Si el error sería confuso → Agrega mensaje descriptivo
- Si el fallo es costoso → Valida temprano

**Pregúntate**: "¿Este error puede ocurrir en producción?"
- SÍ → Usa excepción
- NO (solo bug interno) → Usa assertion

**Pregúntate**: "¿Puedo garantizar que el resultado es válido?"
- NO → Agrega postcondición
- SÍ → Está bien

---

### Cuándo Usar Programación Defensiva

**Siempre usar en**:
- Funciones públicas que otros usarán
- Procesamiento de datos externos
- Operaciones costosas (entrenamiento, I/O)
- Código en producción
- APIs y interfaces

**Opcional en**:
- Funciones privadas internas (usa assertions)
- Performance es crítico y ya validaste antes
- Prototipado rápido (pero agrégalo después)

---

## Resumen de Principios

La programación defensiva no es paranoia, es profesionalismo:

1. **Valida temprano**: Guard clauses al inicio
2. **Falla rápido**: No dejes que errores se propaguen
3. **Mensajes claros**: Facilita el debugging
4. **Documenta excepciones**: En el docstring
5. **Postcondiciones**: Verifica resultados
6. **Excepciones para inputs**: Assertions para invariantes
7. **Validadores reutilizables**: Consistencia y mantenibilidad

**Regla de oro**: Si una función es pública o procesa datos externos, debe validar todos sus inputs. Si algo puede fallar, debe fallar rápidamente con un mensaje claro.

---

## Referencias

1. McConnell, S. (2004). *Code Complete* (2nd ed.). Microsoft Press. Chapter 8: Defensive Programming.
2. Meyer, B. (1997). *Object-Oriented Software Construction* (2nd ed.). Prentice Hall. Chapter 11: Design by Contract.
3. Python assert statement: <https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement>
4. PEP 316 – Programming by Contract: <https://peps.python.org/pep-0316/>
5. Defensive Programming (Wikipedia): <https://en.wikipedia.org/wiki/Defensive_programming>

---

## Ejercicio Práctico Individual

Añade programación defensiva a este código:

```python
def calculate_model_metrics(y_true, y_pred, model_name):
    accuracy = (y_true == y_pred).sum() / len(y_true)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    
    return {
        'model': model_name,
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall
    }
```

**Criterios de éxito**:
- [ ] Type hints completos
- [ ] Validación de tipos
- [ ] Validación de arrays (vacíos, shape, NaN)
- [ ] Validación de model_name
- [ ] Manejo de excepciones en cálculo
- [ ] Postcondición: métricas en rango válido
- [ ] Docstring con excepciones documentadas

---
