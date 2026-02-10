# Comentarios

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Los Comentarios No Compensan el Código Malo](#1-los-comentarios-no-compensan-el-código-malo)
3. [Explicarse en Código](#2-explicarse-en-código)
4. [Comentarios Buenos](#3-comentarios-buenos)
5. [Comentarios Malos](#4-comentarios-malos)
6. [Alternativas a los Comentarios](#5-alternativas-a-los-comentarios)
7. [Resumen](#resumen-de-principios)

---

## Introducción

Los comentarios son, en el mejor de los casos, un mal necesario. El uso apropiado de comentarios es compensar nuestro fracaso para expresarnos en código.

**Referencia principal**: Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 4: Comments.

### Principio Fundamental

> "Don't comment bad code—rewrite it."
>
> — Brian W. Kernighan & P. J. Plauger, *The Elements of Programming Style*

Los comentarios mienten. No siempre, y no intencionalmente, pero lo hacen. El código cambia y evoluciona. Los comentarios no siempre lo siguen.

---

## 1. Los Comentarios No Compensan el Código Malo

### Por Qué Importa

Una de las motivaciones más comunes para escribir comentarios es el código malo. No escribas comentarios para código malo—reescribe el código.

**Referencia**: Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.

---

### Ejemplo Incorrecto

```python
# Check to see if the employee is eligible for full benefits
if ((employee.flags & HOURLY_FLAG) and (employee.age > 65)):
    # Employee is eligible
    pass
```

**Problemas**:

- El comentario es necesario porque el código es críptico
- El código usa flags y operaciones bit a bit sin claridad

---

### Ejemplo Correcto

```python
def is_eligible_for_full_benefits(employee: Employee) -> bool:
    """Determine if employee qualifies for full benefits."""
    return employee.is_hourly_worker() and employee.age > 65

if is_eligible_for_full_benefits(employee):
    # Process benefits
    pass
```

**Ventajas**:

- El código se explica a sí mismo
- No se necesita comentario
- Más fácil de probar y mantener

---

## 2. Explicarse en Código

### Por Qué Importa

En muchos casos, es simplemente cuestión de crear una función que diga lo mismo que el comentario.

---

### Ejemplo Incorrecto

```python
# Check if user has admin privileges and is active
if user.role == 1 and user.status == 'A':
    grant_access()
```

---

### Ejemplo Correcto

```python
def is_active_admin(user: User) -> bool:
    """Check if user is an active administrator."""
    return user.is_admin() and user.is_active()

if is_active_admin(user):
    grant_access()
```

---

### Código Incorrecto

```python
# Check if model has been trained and has sufficient accuracy
if model is not None and hasattr(model, 'history') and model.evaluate(X_test, y_test)[1] > 0.85:
    deploy_model(model)
```

**Problemas**:

- Expresión compleja que requiere comentario
- Difícil de leer y entender de un vistazo
- Mezcla múltiples verificaciones en una línea

### Código Correcto

```python
def is_model_ready_for_deployment(
    model: keras.Model,
    X_test: np.ndarray,
    y_test: np.ndarray,
    minimum_accuracy: float = 0.85
) -> bool:
    """
    Verify if model meets deployment criteria.
    
    :param model: Trained model to evaluate
    :param X_test: Test features
    :param y_test: Test labels
    :param minimum_accuracy: Minimum required accuracy
    :return: True if model is ready for deployment
    """
    if model is None:
        return False
    
    if not hasattr(model, 'history'):
        return False
    
    _, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
    return test_accuracy > minimum_accuracy

if is_model_ready_for_deployment(model, X_test, y_test):
    deploy_model(model)
```

**Ventajas**:

- La función explica la intención sin necesidad de comentarios
- Cada verificación es clara y separada
- Fácil de probar y modificar
- Parámetros configurables

## 3. Comentarios Buenos

Algunos comentarios son necesarios o beneficiosos. Sin embargo, el único comentario verdaderamente bueno es el comentario que encuentras la manera de no escribir.

### 3.1 Comentarios Legales

```python
"""
Copyright (C) 2024 Company Name. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
```

### 3.2 Comentarios Informativos (Docstrings)

Los docstrings en Python son comentarios informativos esenciales que documentan la API pública.

```python
def train_test_split_stratified(
    X: np.ndarray,
    y: np.ndarray,
    test_size: float = 0.2,
    random_state: int = 42
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Split data into train and test sets with stratification.
    
    Ensures that the proportion of samples for each class is roughly
    the same in both training and test sets. This is particularly
    important for imbalanced datasets.
    
    :param X: Feature matrix of shape (n_samples, n_features)
    :param y: Target vector of shape (n_samples,)
    :param test_size: Proportion of dataset to include in test split
    :param random_state: Random seed for reproducibility
    :return: Tuple of (X_train, X_test, y_train, y_test)
    :raises ValueError: If test_size is not between 0 and 1
    
    Example:
        >>> X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        >>> y = np.array([0, 0, 1, 1])
        >>> X_train, X_test, y_train, y_test = train_test_split_stratified(X, y)
        >>> len(X_train), len(X_test)
        (3, 1)
    
    References:
        - Scikit-learn train_test_split documentation
        - Kohavi, R. (1995). A study of cross-validation and bootstrap
    """
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1")
    
    return train_test_split(X, y, test_size=test_size, 
                           stratify=y, random_state=random_state)
```

### 3.3 Explicación de Intención

A veces un comentario va más allá de simplemente información útil sobre la implementación y proporciona la intención detrás de una decisión.

```python
def calculate_learning_rate(epoch: int, initial_lr: float = 0.001) -> float:
    """
    Calculate learning rate with exponential decay.
    
    We use exponential decay rather than step decay because our
    experiments showed that it provides more stable convergence
    for this particular architecture. Step decay caused oscillations
    in the loss function after epoch 50.
    
    :param epoch: Current training epoch
    :param initial_lr: Initial learning rate
    :return: Decayed learning rate
    """
    decay_rate = 0.96
    decay_steps = 10
    return initial_lr * (decay_rate ** (epoch / decay_steps))
```

### 3.4 Clarificación

A veces es útil traducir el significado de algún argumento o valor de retorno oscuro a algo legible. En general, es mejor encontrar una manera de hacer que el argumento o valor de retorno sea claro por sí mismo, pero cuando es parte de una biblioteca estándar o código que no puedes alterar, un comentario clarificador puede ser útil.

```python
def preprocess_text_for_bert(text: str, max_length: int = 512) -> dict:
    """
    Preprocess text for BERT model input.
    
    :param text: Raw input text
    :param max_length: Maximum sequence length (BERT limit is 512 tokens)
    :return: Dictionary with input_ids, attention_mask, token_type_ids
    """
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    # BERT uses special tokens: [CLS] at start, [SEP] at end
    # max_length includes these special tokens, so actual text is max_length - 2
    encoded = tokenizer.encode_plus(
        text,
        add_special_tokens=True,  # Adds [CLS] and [SEP]
        max_length=max_length,
        padding='max_length',
        truncation=True,
        return_attention_mask=True,  # 1 for real tokens, 0 for padding
        return_token_type_ids=True,  # 0 for single sentence
        return_tensors='pt'
    )
    
    return encoded
```

### 3.5 Advertencia de Consecuencias

A veces es útil advertir a otros programadores sobre ciertas consecuencias.

```python
def load_entire_dataset_into_memory(file_path: str) -> pd.DataFrame:
    """
    Load complete dataset into memory.
    
    WARNING: This function loads the entire dataset into RAM.
    For the production dataset (>50GB), this will cause out-of-memory
    errors on most machines. Use load_dataset_in_chunks() instead
    for production data.
    
    This function should only be used for:
    - Development with sample data (<1GB)
    - Testing with mock data
    - Exploratory analysis on small subsets
    
    :param file_path: Path to dataset file
    :return: Complete dataset as DataFrame
    :raises MemoryError: If dataset is too large for available RAM
    """
    return pd.read_csv(file_path)


def train_model_without_validation(
    X_train: np.ndarray,
    y_train: np.ndarray
) -> keras.Model:
    """
    Train model without validation set.
    
    WARNING: This function trains without validation, which means:
    - No early stopping possible
    - High risk of overfitting
    - No way to monitor generalization during training
    
    Only use this for:
    - Quick prototyping
    - Hyperparameter search with cross-validation
    - When you have a separate validation pipeline
    
    For production training, use train_model_with_validation() instead.
    
    :param X_train: Training features
    :param y_train: Training labels
    :return: Trained model (potentially overfitted)
    """
    model = build_model()
    model.fit(X_train, y_train, epochs=100, verbose=0)
    return model
```

### 3.6 TODO Comments

Los comentarios TODO son trabajos que el programador piensa que deberían hacerse, pero por alguna razón no puede hacer en este momento.

```python
def calculate_model_confidence(
    predictions: np.ndarray,
    method: str = 'softmax'
) -> np.ndarray:
    """
    Calculate confidence scores for predictions.
    
    :param predictions: Model output logits
    :param method: Confidence calculation method
    :return: Confidence scores
    """
    if method == 'softmax':
        return softmax(predictions, axis=-1)
    elif method == 'sigmoid':
        return sigmoid(predictions)
    else:
        # TODO: Implement temperature scaling for better calibration
        # Temperature scaling has been shown to improve confidence calibration
        # See: Guo et al. (2017) "On Calibration of Modern Neural Networks"
        # Requires: validation set to tune temperature parameter
        raise NotImplementedError(f"Method {method} not yet implemented")
```

**Nota importante sobre TODOs**: Los TODOs no son una excusa para dejar código malo en el sistema. Escanea regularmente y elimina los TODOs que ya no necesitas.

## 4. Comentarios Malos

La mayoría de los comentarios caen en esta categoría. Generalmente son muletas o excusas para código pobre o justificaciones para decisiones insuficientes.

### 4.1 Comentarios Murmurantes

Si decides escribir un comentario, dedica el tiempo necesario para asegurarte de que sea el mejor comentario que puedas escribir.

```python
# Incorrecto: comentario vago y sin valor
def load_config():
    """Load config."""  # ¿Qué config? ¿De dónde? ¿Qué formato?
    # Load the config
    with open('config.json') as f:  # ¿Por qué JSON? ¿Qué contiene?
        config = json.load(f)
    return config

# Correcto: documentación clara y completa
def load_model_training_configuration(config_path: str = 'config.json') -> dict:
    """
    Load model training configuration from JSON file.
    
    Configuration must include:
    - learning_rate: float
    - batch_size: int
    - epochs: int
    - model_architecture: dict with layer specifications
    
    :param config_path: Path to JSON configuration file
    :return: Configuration dictionary
    :raises FileNotFoundError: If config file does not exist
    :raises json.JSONDecodeError: If config file is not valid JSON
    :raises KeyError: If required configuration keys are missing
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    required_keys = ['learning_rate', 'batch_size', 'epochs', 'model_architecture']
    missing_keys = [key for key in required_keys if key not in config]
    
    if missing_keys:
        raise KeyError(f"Missing required configuration keys: {missing_keys}")
    
    return config
```

### 4.2 Comentarios Redundantes

Un comentario es redundante si describe algo que ya se describe adecuadamente en el código mismo.

```python
# Incorrecto: comentarios redundantes
class ModelTrainer:
    """Class for training models."""  # Obvio por el nombre
    
    def __init__(self):
        """Constructor."""  # Completamente inútil
        self.model = None  # The model  # Redundante
        self.history = None  # The training history  # Redundante
    
    def train(self, X, y):
        """Train the model."""  # No añade información
        # Train the model on X and y
        self.model.fit(X, y)  # Fit the model  # Repite el código
        
    def get_model(self):
        """Get the model."""  # Obvio
        return self.model  # Return the model  # Redundante

# Correcto: documentación que añade valor
class NeuralNetworkTrainer:
    """
    Trainer for neural network models with automatic hyperparameter tuning.
    
    This trainer implements early stopping, learning rate scheduling,
    and model checkpointing. It automatically saves the best model
    based on validation loss.
    
    Attributes:
        model: Keras model instance
        training_history: Dictionary with training metrics per epoch
        best_model_path: Path where best model checkpoint is saved
    """
    
    def __init__(self, model_architecture: dict, checkpoint_dir: str = './checkpoints'):
        """
        Initialize trainer with model architecture.
        
        :param model_architecture: Dictionary specifying layer configuration
        :param checkpoint_dir: Directory for saving model checkpoints
        """
        self.model = self._build_model(model_architecture)
        self.training_history = {}
        self.checkpoint_dir = checkpoint_dir
        self.best_model_path = None
    
    def train_with_early_stopping(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        X_val: np.ndarray,
        y_val: np.ndarray,
        patience: int = 10
    ) -> dict:
        """
        Train model with early stopping based on validation loss.
        
        Training stops if validation loss does not improve for 'patience'
        consecutive epochs. The model with the best validation loss is
        automatically saved and restored at the end of training.
        
        :param X_train: Training features
        :param y_train: Training labels
        :param X_val: Validation features
        :param y_val: Validation labels
        :param patience: Number of epochs to wait before stopping
        :return: Dictionary with training history
        """
        early_stopping = EarlyStopping(
            monitor='val_loss',
            patience=patience,
            restore_best_weights=True
        )
        
        self.training_history = self.model.fit(
            X_train, y_train,
            validation_data=(X_val, y_val),
            callbacks=[early_stopping],
            verbose=0
        ).history
        
        return self.training_history
```

### 4.3 Comentarios Engañosos

A veces, con toda la mejor intención, un programador hace una declaración en sus comentarios que no es lo suficientemente precisa como para ser exacta.

```python
# Incorrecto: comentario engañoso
def process_batch(data: list) -> list:
    """
    Process all items in the batch.
    """
    # Actually only processes items where status == 'pending'
    # Comment is misleading!
    return [process_item(item) for item in data if item.status == 'pending']

# Correcto: comentario preciso
def process_pending_items_in_batch(data: list[dict]) -> list[dict]:
    """
    Process only items with 'pending' status from batch.
    
    Items with other statuses ('completed', 'failed', 'cancelled')
    are filtered out and not processed.
    
    :param data: List of item dictionaries with 'status' key
    :return: List of processed items (only those that were pending)
    """
    pending_items = [item for item in data if item.get('status') == 'pending']
    return [process_item(item) for item in pending_items]
```

### 4.4 Comentarios Mandatorios

Es simplemente tonto tener una regla que diga que cada función debe tener un docstring, o que cada variable debe tener un comentario. Los comentarios como estos solo saturan el código, propagan mentiras y prestan a confusión y desorganización general.

```python
# Incorrecto: docstrings inútiles por obligación
def add(a, b):
    """
    Add two numbers.
    
    :param a: first number
    :param b: second number
    :return: sum
    """
    return a + b

def subtract(a, b):
    """
    Subtract two numbers.
    
    :param a: first number
    :param b: second number
    :return: difference
    """
    return a - b

# Correcto: docstrings solo donde añaden valor
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def calculate_weighted_f1_score(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    class_weights: dict[int, float]
) -> float:
    """
    Calculate weighted F1 score for multi-class classification.
    
    The weighted F1 score accounts for class imbalance by weighting
    each class's F1 score by its support (number of true instances).
    This is particularly useful when classes are imbalanced and you
    want to give equal importance to all classes.
    
    :param y_true: Ground truth labels
    :param y_pred: Predicted labels
    :param class_weights: Dictionary mapping class labels to weights
    :return: Weighted F1 score between 0 and 1
    
    Example:
        >>> y_true = np.array([0, 0, 1, 1, 2, 2])
        >>> y_pred = np.array([0, 1, 1, 1, 2, 0])
        >>> weights = {0: 1.0, 1: 1.5, 2: 2.0}
        >>> calculate_weighted_f1_score(y_true, y_pred, weights)
        0.611
    
    References:
        - Scikit-learn f1_score documentation
        - Sokolova, M., & Lapalme, G. (2009). A systematic analysis
          of performance measures for classification tasks.
    """
    f1_per_class = f1_score(y_true, y_pred, average=None)
    weighted_f1 = sum(
        f1_per_class[cls] * weight 
        for cls, weight in class_weights.items()
    ) / sum(class_weights.values())
    return weighted_f1
```

### 4.5 Comentarios de Registro (Journal Comments)

A veces la gente añade un comentario al inicio de un módulo cada vez que lo editan. Estos comentarios se acumulan como un registro de cada cambio.

```python
# Incorrecto: registro manual de cambios
"""
Model training module.

Changes:
* 2024-01-15 - John: Added learning rate scheduling
* 2024-01-20 - Alice: Fixed bug in validation split
* 2024-02-01 - Bob: Added early stopping
* 2024-02-10 - John: Refactored data loading
* 2024-02-15 - Alice: Added model checkpointing
"""

# Correcto: usar control de versiones (Git)
"""
Model training module with advanced features.

This module provides neural network training with:
- Learning rate scheduling
- Early stopping
- Model checkpointing
- Automatic validation

For change history, see Git commit log.
"""
```

**Razonamiento**: Los sistemas de control de versiones (Git) son mucho mejores para rastrear cambios que los comentarios manuales. Los comentarios de registro se vuelven obsoletos, desordenados y difíciles de mantener.

### 4.6 Comentarios Ruidosos

A veces ves comentarios que no son más que ruido. Reafirman lo obvio y no proporcionan nueva información.

```python
# Incorrecto: comentarios ruidosos
class DataProcessor:
    def __init__(self):
        # Initialize variables
        self.data = None  # Data variable
        self.processed = False  # Processed flag
        self.errors = []  # Error list
    
    def load_data(self, path):
        # Load the data
        self.data = pd.read_csv(path)  # Read CSV file
        
    def process(self):
        # Process the data
        if self.data is not None:  # Check if data exists
            # Remove nulls
            self.data = self.data.dropna()  # Drop NA values
            # Set flag
            self.processed = True  # Mark as processed

# Correcto: código auto-explicativo sin ruido
class DataProcessor:
    """Processor for cleaning and transforming tabular data."""
    
    def __init__(self):
        self.data: Optional[pd.DataFrame] = None
        self.is_processed: bool = False
        self.processing_errors: list[str] = []
    
    def load_data_from_csv(self, file_path: str) -> None:
        """Load data from CSV file."""
        self.data = pd.read_csv(file_path)
        
    def remove_missing_values(self) -> None:
        """Remove rows with missing values from dataset."""
        if self.data is not None:
            self.data = self.data.dropna()
            self.is_processed = True
```

### 4.7 Código Comentado

Pocas prácticas son tan odiosas como comentar código. No hagas esto:

```python
# Incorrecto: código comentado
def train_model(X, y):
    # Old approach - too slow
    # model = RandomForestClassifier(n_estimators=1000)
    # model.fit(X, y)
    # return model
    
    # Previous version - didn't work well
    # model = LogisticRegression()
    # scaler = StandardScaler()
    # X_scaled = scaler.fit_transform(X)
    # model.fit(X_scaled, y)
    # return model
    
    # Current approach
    model = GradientBoostingClassifier()
    model.fit(X, y)
    return model

# Correcto: eliminar código viejo (Git lo guarda)
def train_gradient_boosting_model(
    X: np.ndarray,
    y: np.ndarray,
    n_estimators: int = 100
) -> GradientBoostingClassifier:
    """
    Train gradient boosting classifier.
    
    We chose gradient boosting over random forest and logistic
    regression based on cross-validation results showing 5%
    improvement in F1 score. See experiment logs in
    experiments/model_comparison_2024_02.ipynb
    
    :param X: Training features
    :param y: Training labels
    :param n_estimators: Number of boosting stages
    :return: Trained classifier
    """
    model = GradientBoostingClassifier(n_estimators=n_estimators)
    model.fit(X, y)
    return model
```

**Razonamiento**: Otros que vean el código comentado no tendrán el coraje de eliminarlo. Pensarán que está ahí por una razón y que es demasiado importante para eliminar. El código comentado se acumula como sedimento en el fondo de una botella de vino malo.

### 4.8 Comentarios de Posición

A veces los programadores les gusta marcar una posición particular en un archivo fuente.

```python
# Incorrecto: marcadores de posición ruidosos
################################################################################
# DATA LOADING FUNCTIONS
################################################################################

def load_training_data(path):
    pass

def load_test_data(path):
    pass

# ============================================================================
# PREPROCESSING FUNCTIONS
# ============================================================================

def normalize_features(data):
    pass

def encode_categories(data):
    pass

################################################################################
################################################################################
# MODEL TRAINING
################################################################################
################################################################################

def train_model(data):
    pass

# Correcto: organizar en módulos separados
# En data_loading.py
def load_training_data(path: str) -> pd.DataFrame:
    """Load training data from file."""
    pass

def load_test_data(path: str) -> pd.DataFrame:
    """Load test data from file."""
    pass

# En preprocessing.py
def normalize_features(data: pd.DataFrame) -> pd.DataFrame:
    """Normalize numerical features."""
    pass

def encode_categories(data: pd.DataFrame) -> pd.DataFrame:
    """Encode categorical variables."""
    pass

# En model_training.py
def train_model(data: pd.DataFrame) -> keras.Model:
    """Train neural network model."""
    pass
```

**Razonamiento**: Si necesitas marcadores de posición, probablemente tu archivo es demasiado largo. La solución es dividir el archivo en módulos más pequeños y cohesivos.

## 5. Alternativas a los Comentarios

### 5.1 Usar Nombres Descriptivos

```python
# Incorrecto: comentario explica código críptico
# Check if user has admin privileges and is active
if u.r == 1 and u.s == 'A':
    grant_access()

# Correcto: código auto-explicativo
if user.is_admin() and user.is_active():
    grant_access()
```

### 5.2 Extraer Funciones

```python
# Incorrecto: comentario describe bloque de código
def process_data(data):
    # Validate data format
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Data must be DataFrame")
    if len(data) == 0:
        raise ValueError("Data cannot be empty")
    if 'target' not in data.columns:
        raise ValueError("Data must have 'target' column")
    
    # Rest of processing
    pass

# Correcto: extraer validación a función
def validate_data_format(data: pd.DataFrame) -> None:
    """
    Validate data meets required format.
    
    :param data: DataFrame to validate
    :raises TypeError: If data is not a DataFrame
    :raises ValueError: If data is empty or missing required columns
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Data must be DataFrame")
    if len(data) == 0:
        raise ValueError("Data cannot be empty")
    if 'target' not in data.columns:
        raise ValueError("Data must have 'target' column")

def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Process validated data."""
    validate_data_format(data)
    # Rest of processing
    pass
```

### 5.3 Usar Type Hints

```python
# Incorrecto: comentario describe tipos
def train_model(X, y, config):
    """
    Train model.
    
    X: numpy array of features
    y: numpy array of labels
    config: dict with training configuration
    """
    pass

# Correcto: type hints reemplazan comentarios de tipo
def train_model(
    X: np.ndarray,
    y: np.ndarray,
    config: TrainingConfig
) -> keras.Model:
    """
    Train neural network model with specified configuration.
    
    :param X: Feature matrix of shape (n_samples, n_features)
    :param y: Label vector of shape (n_samples,)
    :param config: Training hyperparameters and settings
    :return: Trained Keras model
    """
    pass
```

### 5.4 Usar Constantes Nombradas

```python
# Incorrecto: comentario explica número mágico
def split_data(data):
    # Use 80% for training
    train_size = int(len(data) * 0.8)
    return data[:train_size], data[train_size:]

# Correcto: constante nombrada
TRAIN_TEST_SPLIT_RATIO = 0.8

def split_data_for_training(
    data: pd.DataFrame,
    train_ratio: float = TRAIN_TEST_SPLIT_RATIO
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split data into training and test sets.
    
    :param data: Complete dataset
    :param train_ratio: Proportion of data for training
    :return: Tuple of (training_data, test_data)
    """
    train_size = int(len(data) * train_ratio)
    return data[:train_size], data[train_size:]
```

## Resumen de Principios

1. **No comentes código malo, reescríbelo**: Los comentarios no compensan el código pobre
2. **Explícate en código**: Usa nombres descriptivos y funciones bien nombradas
3. **Comentarios buenos son raros**: La mayoría de los comentarios son innecesarios
4. **Docstrings añaden valor**: Documenta la API pública con información útil
5. **Evita comentarios redundantes**: No repitas lo que el código ya dice
6. **Elimina código comentado**: Usa control de versiones en su lugar
7. **Mantén comentarios actualizados**: Un comentario obsoleto es peor que ningún comentario

## Referencias

1. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 4: Comments.
2. Kernighan, B. W., & Plauger, P. J. (1978). *The Elements of Programming Style* (2nd ed.). McGraw-Hill.
3. Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.
4. PEP 257 – Docstring Conventions: <https://peps.python.org/pep-0257/>
5. PEP 484 – Type Hints: <https://peps.python.org/pep-0484/>
6. Google Python Style Guide - Comments: <https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>

## Ejercicio Práctico Individual

Refactoriza el siguiente código eliminando comentarios innecesarios y mejorando la claridad:

```python
# Model training script
def train(d, l, e=100, b=32):
    # Create model
    m = Sequential()
    # Add layers
    m.add(Dense(128, activation='relu'))  # First layer
    m.add(Dense(64, activation='relu'))   # Second layer
    m.add(Dense(1, activation='sigmoid')) # Output layer
    
    # Compile model
    m.compile(optimizer='adam', loss='binary_crossentropy')
    
    # Train model
    # Use 100 epochs and batch size 32
    m.fit(d, l, epochs=e, batch_size=b)
    
    # Return trained model
    return m
```

**Solución**: Aplicar principios de nombres significativos, type hints, y documentación apropiada sin comentarios redundantes.

---

## 🏋️ Ejercicio Grupal: Limpiar Comentarios en Código Real

**Objetivo**: Identificar y eliminar comentarios malos, reemplazándolos con código auto-explicativo.

**Contexto**: Has heredado un módulo de preprocesamiento de datos para un proyecto de NLP. El código está lleno de comentarios que más confunden que ayudan. El equipo necesita mantener este código pero nadie entiende qué hace realmente.

**Tiempo estimado**: 30-45 minutos

**Dinámica**:
1. **Análisis individual** (5 min): Lee el código y clasifica los comentarios
2. **Discusión en grupo** (10 min): Identifiquen tipos de comentarios malos
3. **Refactorización colaborativa** (20 min): Eliminen comentarios y mejoren código
4. **Presentación** (10 min): Compartan antes/después con otros grupos

---

### Código a Refactorizar

```python
"""
Text preprocessing module for NLP pipeline.

Author: John Doe
Date: 2023-01-15
Last modified: 2024-02-20 by Alice Smith
Changes:
- 2023-01-15: Initial version
- 2023-03-10: Added emoji removal
- 2023-06-15: Fixed bug in URL detection
- 2023-09-01: Added support for multiple languages
- 2024-01-10: Refactored tokenization
- 2024-02-20: Added lemmatization
"""

import re
import string
from typing import List
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import emoji

# Download required NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

class TextPreprocessor:
    """Class for preprocessing text."""  # Obvious comment
    
    def __init__(self, lang='english'):
        """Constructor."""  # Useless comment
        # Initialize the lemmatizer
        self.lem = WordNetLemmatizer()  # The lemmatizer
        # Set the language
        self.lang = lang  # Language parameter
        # Get stopwords for the language
        self.sw = set(stopwords.words(lang))  # Stopwords set
    
    def clean(self, txt):
        """Clean the text."""  # Doesn't explain what cleaning means
        # First, convert to lowercase
        txt = txt.lower()  # Make lowercase
        
        # Remove URLs - this regex matches http/https URLs
        # Pattern explanation: https?:// matches http:// or https://
        # [^\s]+ matches any non-whitespace characters
        txt = re.sub(r'https?://[^\s]+', '', txt)  # Remove URLs
        
        # Remove email addresses
        # Pattern: word characters, dots, hyphens @ word characters, dots
        txt = re.sub(r'\S+@\S+', '', txt)  # Remove emails
        
        # Remove mentions (Twitter style)
        txt = re.sub(r'@\w+', '', txt)  # Remove @mentions
        
        # Remove hashtags but keep the text
        # Example: #MachineLearning becomes MachineLearning
        txt = re.sub(r'#(\w+)', r'\1', txt)  # Remove # but keep text
        
        # Remove emojis - using emoji library
        txt = emoji.replace_emoji(txt, '')  # Remove emojis
        
        # Remove punctuation
        # string.punctuation contains !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        txt = txt.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
        
        # Remove extra whitespace
        txt = ' '.join(txt.split())  # Normalize whitespace
        
        # Return cleaned text
        return txt  # Return the result
    
    def tokenize(self, txt):
        """Tokenize text."""  # Obvious
        # Split on whitespace
        tokens = txt.split()  # Split into tokens
        # Return tokens
        return tokens  # Return the list
    
    def remove_stopwords(self, tokens):
        """Remove stopwords."""  # Obvious
        # Filter out stopwords
        # Keep only tokens that are not in stopwords set
        filtered = [t for t in tokens if t not in self.sw]  # Filter stopwords
        # Return filtered tokens
        return filtered  # Return result
    
    def lemmatize(self, tokens):
        """Lemmatize tokens."""  # Obvious
        # Apply lemmatization to each token
        # Lemmatization reduces words to their base form
        # Example: running -> run, better -> good
        lemmatized = [self.lem.lemmatize(t) for t in tokens]  # Lemmatize
        # Return lemmatized tokens
        return lemmatized  # Return result
    
    def process(self, txt, rm_sw=True, lem=True):
        """
        Process text through full pipeline.
        
        txt: input text
        rm_sw: whether to remove stopwords
        lem: whether to lemmatize
        """
        # Step 1: Clean the text
        txt = self.clean(txt)  # Clean
        
        # Step 2: Tokenize
        tokens = self.tokenize(txt)  # Tokenize
        
        # Step 3: Remove stopwords if flag is True
        if rm_sw:  # Check flag
            tokens = self.remove_stopwords(tokens)  # Remove stopwords
        
        # Step 4: Lemmatize if flag is True
        if lem:  # Check flag
            tokens = self.lemmatize(tokens)  # Lemmatize
        
        # Return processed tokens
        return tokens  # Return final result
    
    def process_batch(self, texts):
        """Process multiple texts."""  # Obvious
        # Initialize results list
        results = []  # Empty list for results
        
        # Loop through each text
        for txt in texts:  # Iterate over texts
            # Process the text
            processed = self.process(txt)  # Process each text
            # Add to results
            results.append(processed)  # Append to results
        
        # Return all results
        return results  # Return the list
    
    # TODO: Add support for custom stopwords
    # TODO: Add support for stemming as alternative to lemmatization
    # TODO: Optimize batch processing with multiprocessing
    # TODO: Add caching for repeated texts
    # TODO: Add support for more languages
    # TODO: Add spell checking
    # TODO: Add named entity recognition
    
    def get_stats(self, txt):
        """Get statistics about text."""
        # Count characters
        n_chars = len(txt)  # Character count
        
        # Count words
        n_words = len(txt.split())  # Word count
        
        # Count sentences - split on period, exclamation, question mark
        n_sents = len(re.findall(r'[.!?]+', txt))  # Sentence count
        
        # Calculate average word length
        # Sum of all word lengths divided by number of words
        words = txt.split()
        if len(words) > 0:  # Avoid division by zero
            avg_len = sum(len(w) for w in words) / len(words)  # Average word length
        else:
            avg_len = 0  # Default to 0 if no words
        
        # Return dictionary with stats
        return {
            'characters': n_chars,  # Total characters
            'words': n_words,  # Total words
            'sentences': n_sents,  # Total sentences
            'avg_word_length': avg_len  # Average word length
        }  # Return stats dict


# Helper function to clean HTML
def clean_html(txt):
    """Remove HTML tags."""  # Obvious
    # Use regex to remove HTML tags
    # Pattern: < followed by anything except >, then >
    txt = re.sub(r'<[^>]+>', '', txt)  # Remove HTML tags
    # Return cleaned text
    return txt  # Return result


################################################################################
# UTILITY FUNCTIONS
################################################################################

def load_texts(path):
    """Load texts from file."""  # Obvious
    # Open file in read mode
    with open(path, 'r', encoding='utf-8') as f:  # Open file
        # Read all lines
        texts = f.readlines()  # Read lines
    # Return texts
    return texts  # Return list


def save_processed(texts, path):
    """Save processed texts."""  # Obvious
    # Open file in write mode
    with open(path, 'w', encoding='utf-8') as f:  # Open file
        # Write each text on new line
        for txt in texts:  # Iterate texts
            # Join tokens with space and write
            f.write(' '.join(txt) + '\n')  # Write line


# Main execution
if __name__ == '__main__':
    # Create preprocessor instance
    prep = TextPreprocessor()  # Initialize preprocessor
    
    # Example text
    example = "Check out https://example.com! @user #NLP is amazing 😀"  # Test text
    
    # Process the text
    result = prep.process(example)  # Process
    
    # Print result
    print(result)  # Output
```

---

### Instrucciones para el Grupo

**Paso 1: Clasificar Comentarios** (10 minutos)

Identifiquen y clasifiquen cada comentario como:

1. **Comentario de Registro** (journal): Historial de cambios
2. **Comentario Redundante**: Repite lo que el código ya dice
3. **Comentario Ruidoso**: No añade información
4. **Comentario Mandatorio**: Docstring inútil por obligación
5. **Comentario de Posición**: Marcadores como `###########`
6. **TODO Acumulado**: TODOs que nunca se harán
7. **Comentario Bueno**: Realmente añade valor (si hay alguno)

**Paso 2: Planificar Mejoras** (10 minutos)

Para cada tipo de comentario malo, decidan:

1. **Eliminar**: ¿Se puede simplemente borrar?
2. **Reemplazar con código**: ¿Función con nombre descriptivo?
3. **Reemplazar con type hints**: ¿Los tipos explican mejor?
4. **Reemplazar con constantes**: ¿Números mágicos que necesitan nombre?
5. **Mejorar docstring**: ¿Necesita documentación real?

**Paso 3: Refactorizar** (20 minutos)

Dividan el trabajo:

- **Persona 1**: Limpiar `__init__` y métodos de limpieza
- **Persona 2**: Limpiar métodos de tokenización y stopwords
- **Persona 3**: Limpiar métodos de procesamiento y batch
- **Persona 4**: Limpiar funciones auxiliares y main

**Criterios de Éxito**:

- [ ] Cero comentarios redundantes
- [ ] Cero comentarios ruidosos
- [ ] Código auto-explicativo con nombres descriptivos
- [ ] Type hints en todas las funciones
- [ ] Docstrings útiles (no obvios)
- [ ] Constantes nombradas para valores mágicos
- [ ] Funciones extraídas donde sea necesario
- [ ] Eliminar historial de cambios (usar Git)

---

### Pistas

**Para Comentarios Redundantes**:
```python
# Antes
txt = txt.lower()  # Make lowercase

# Después
text = text.lower()
```

**Para Nombres Crípticos**:
```python
# Antes
self.lem = WordNetLemmatizer()  # The lemmatizer
self.sw = set(stopwords.words(lang))  # Stopwords set

# Después
self.lemmatizer = WordNetLemmatizer()
self.stopwords = set(stopwords.words(language))
```

**Para Comentarios que Explican Lógica**:
```python
# Antes
# Remove hashtags but keep the text
# Example: #MachineLearning becomes MachineLearning
txt = re.sub(r'#(\w+)', r'\1', txt)

# Después
def remove_hashtag_symbol_but_keep_text(text: str) -> str:
    """
    Remove # symbol from hashtags while preserving the text.
    
    Example:
        >>> remove_hashtag_symbol_but_keep_text("#MachineLearning")
        "MachineLearning"
    """
    return re.sub(r'#(\w+)', r'\1', text)
```

**Para Flag Arguments**:
```python
# Antes
def process(self, txt, rm_sw=True, lem=True):
    if rm_sw:
        tokens = self.remove_stopwords(tokens)
    if lem:
        tokens = self.lemmatize(tokens)

# Después
def process_with_stopword_removal(self, text: str) -> list[str]:
    """Process text including stopword removal."""
    pass

def process_with_lemmatization(self, text: str) -> list[str]:
    """Process text including lemmatization."""
    pass

def process_full_pipeline(self, text: str) -> list[str]:
    """Process text with all transformations."""
    pass
```

**Para Docstrings Obvios**:
```python
# Antes
def tokenize(self, txt):
    """Tokenize text."""
    return txt.split()

# Después
def tokenize_on_whitespace(self, text: str) -> list[str]:
    """
    Split text into tokens using whitespace as delimiter.
    
    :param text: Input text to tokenize
    :return: List of tokens
    
    Example:
        >>> tokenize_on_whitespace("hello world")
        ["hello", "world"]
    """
    return text.split()
```

---

### Preguntas para Reflexión

Después de refactorizar, discutan:

1. ¿Cuántos comentarios eliminaron vs cuántos mejoraron?
2. ¿El código es más claro sin los comentarios?
3. ¿Qué técnicas usaron para reemplazar comentarios?
4. ¿Encontraron algún comentario que SÍ añadía valor?
5. ¿Qué fue más difícil: eliminar comentarios o mejorar el código?
6. ¿Cómo manejarían los TODOs en un proyecto real?
