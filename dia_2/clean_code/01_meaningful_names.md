# Nombres Significativos

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Usar Nombres que Revelen Intención](#1-usar-nombres-que-revelen-intención)
3. [Evitar Desinformación](#2-evitar-desinformación)
4. [Hacer Distinciones Significativas](#3-hacer-distinciones-significativas)
5. [Usar Nombres Pronunciables](#4-usar-nombres-pronunciables)
6. [Usar Nombres Buscables](#5-usar-nombres-buscables)
7. [Evitar Codificaciones](#6-evitar-codificaciones)
8. [Evitar Mapeos Mentales](#7-evitar-mapeos-mentales)
9. [Resumen](#resumen-de-principios)

---

## Introducción

Los nombres son omnipresentes en el software. Nombramos variables, funciones, argumentos, clases y paquetes. Dado que hacemos tanto de esto, es mejor hacerlo bien.

**Referencia principal**: Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 2: Meaningful Names.

### Principio Fundamental

> "The name of a variable, function, or class, should answer all the big questions. It should tell you why it exists, what it does, and how it is used. If a name requires a comment, then the name does not reveal its intent."
>
> — Robert C. Martin, Clean Code

Un nombre bien elegido ahorra tiempo de lectura y reduce la carga cognitiva. En cualquier tipo de aplicación (web, datos, APIs, sistemas), nombres claros son críticos para mantener la comprensión del código.

---

## 1. Usar Nombres que Revelen Intención

### Por Qué Importa

El código se lee muchas más veces de las que se escribe. Un nombre que revela intención elimina la necesidad de comentarios explicativos y reduce el tiempo necesario para comprender el código.

---

### Ejemplo Incorrecto

```python
# Procesamiento de datos
d = []  # lista de datos
for i in data:
    if i[2] > 0.5:
        d.append(i)

# Procesamiento
p = Processor()
p.run(d)
```

**Problemas**:

- `d` no indica qué tipo de datos contiene
- `i` es genérico y no describe el elemento
- `i[2]` requiere conocimiento del esquema de datos
- `p` no indica qué tipo de procesador es
- Requiere comentarios para entender el propósito

---

### Ejemplo Correcto

```python
def filter_valid_transactions(
    transactions: list[dict],
    minimum_amount: float = 0.5
) -> list[dict]:
    """
    Filter transactions above minimum amount.
    
    :param transactions: List of transaction dictionaries
    :param minimum_amount: Minimum transaction amount to keep
    :return: Filtered list of valid transactions
    """
    valid_transactions = []
    for transaction in transactions:
        if transaction['amount'] > minimum_amount:
            valid_transactions.append(transaction)
    return valid_transactions

# Usage
filtered_data = filter_valid_transactions(raw_transactions)
payment_processor = PaymentProcessor()
payment_processor.process(filtered_data)
```

**Ventajas**:

- Cada nombre describe su propósito
- No se necesitan comentarios adicionales
- El flujo de datos es evidente
- Fácil de mantener y extender

---

### Ejemplos en Diferentes Contextos

#### Python Puro

```python
# Incorrecto
def calc(a, b, c):
    return a + b * c

# Correcto
def calculate_total_price(base_price: float, quantity: int, tax_rate: float) -> float:
    """Calculate total price including tax."""
    return base_price + (quantity * tax_rate)
```

#### Web API

```python
# Incorrecto
def get(id):
    r = db.query(id)
    return r

# Correcto
def fetch_user_profile(user_id: str) -> dict:
    """Retrieve user profile from database."""
    user_profile = database.query_user_by_id(user_id)
    return user_profile
```

#### Procesamiento de Datos

```python
# Incorrecto
df = pd.read_csv('data.csv')
df = df[df[2] > 100]

# Correcto
sales_data = pd.read_csv('sales_report.csv')
high_value_sales = sales_data[sales_data['amount'] > 100]
```

---

## 2. Evitar Desinformación

### Por Qué Importa

Los nombres que sugieren algo diferente de lo que realmente representan son peores que los nombres vagos. Crean expectativas falsas y pueden llevar a errores sutiles.

---

### Ejemplo Incorrecto

```python
# Incorrecto: 'list' en el nombre sugiere tipo list, pero es un dict
user_list = {
    'user_1': {'name': 'Alice', 'age': 30},
    'user_2': {'name': 'Bob', 'age': 25}
}

# Incorrecto: 'account' es singular pero contiene múltiples cuentas
account = ['acc_001', 'acc_002', 'acc_003']

# Incorrecto: sugiere que devuelve un objeto, pero devuelve un número
def calculate_user(user_data):
    return len(user_data['orders']) * user_data['avg_order_value']

# Incorrecto: 'O' (letra O) vs '0' (cero), 'l' (ele) vs '1' (uno)
O = 0  # Confuso
l = 1  # Confuso
```

**Problemas**:

- Expectativas incorrectas sobre tipos de datos
- Confusión entre singular y plural
- Nombres que se parecen visualmente pero son diferentes
- Funciones que no hacen lo que su nombre sugiere

---

### Ejemplo Correcto

```python
# Correcto: el nombre refleja el tipo real
user_registry = {
    'user_1': {'name': 'Alice', 'age': 30},
    'user_2': {'name': 'Bob', 'age': 25}
}

# Correcto: plural indica colección
account_ids = ['acc_001', 'acc_002', 'acc_003']

# Correcto: nombre describe lo que realmente devuelve
def calculate_user_lifetime_value(user_data: dict) -> float:
    """
    Calculate total value of user's orders.
    
    :param user_data: Dictionary with 'orders' and 'avg_order_value' keys
    :return: Lifetime value as float
    """
    return len(user_data['orders']) * user_data['avg_order_value']

# Correcto: nombres claros sin ambigüedad visual
zero_count = 0
line_number = 1
```

---

### Convenciones Específicas por Contexto

#### Python Puro

```python
# Aceptable: convenciones establecidas
i, j, k = 0, 0, 0  # Índices en loops simples
x, y = 10, 20      # Coordenadas

# Mejor: nombres descriptivos cuando el contexto no es obvio
row_index, column_index, depth_index = 0, 0, 0
x_coordinate, y_coordinate = 10, 20
```

#### Procesamiento de Datos

```python
# Aceptable: 'df' es convención común para DataFrames
df = pd.read_csv('data.csv')

# Mejor: nombre descriptivo del contenido
customer_orders = pd.read_csv('orders.csv')
product_inventory = pd.read_csv('inventory.csv')
```

#### Web APIs

```python
# Aceptable en contexto de HTTP
req = request.get_json()
res = {'status': 'ok'}

# Mejor: nombres completos
request_payload = request.get_json()
response_data = {'status': 'ok'}
```

---

## 3. Hacer Distinciones Significativas

### Por Qué Importa

Si los nombres deben ser diferentes, entonces también deben significar algo diferente. Las variaciones numéricas o palabras ruido no aportan información útil.

**Referencia**: Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.

---

### Ejemplo Incorrecto

```python
# Incorrecto: series numéricas sin significado
def process_data(data1, data2, data3):
    result1 = transform(data1)
    result2 = transform(data2)
    result3 = transform(data3)
    return result1, result2, result3

# Incorrecto: palabras ruido que no distinguen
class ProductInfo:
    pass

class ProductData:
    pass

# Incorrecto: variaciones sin significado real
def get_user_info(user_id):
    pass

def get_user_data(user_id):
    pass
```

---

### Ejemplo Correcto

```python
# Correcto: cada nombre indica propósito específico
def prepare_data_pipeline(
    raw_data: pd.DataFrame,
    validation_data: pd.DataFrame,
    test_data: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Prepare data for processing.
    
    :param raw_data: Unprocessed raw data
    :param validation_data: Validation set
    :param test_data: Hold-out test set
    :return: Tuple of processed datasets
    """
    processed_raw = clean_and_normalize(raw_data)
    processed_validation = clean_and_normalize(validation_data)
    processed_test = clean_and_normalize(test_data)
    return processed_raw, processed_validation, processed_test

# Correcto: clases con propósitos distintos
class UserConfiguration:
    """User settings and preferences."""
    pass

class UserStatistics:
    """Aggregated user activity metrics."""
    pass

# Correcto: funciones con propósitos específicos
def fetch_user_profile(user_id: str) -> dict:
    """Retrieve user profile from database."""
    pass

def calculate_user_metrics(user_id: str) -> dict:
    """Compute aggregated statistics for user."""
    pass
```

---

## 4. Usar Nombres Pronunciables

### Por Qué Importa

La programación es una actividad social. Necesitamos discutir el código con otros desarrolladores. Los nombres pronunciables facilitan la comunicación verbal.

---

### Ejemplo Incorrecto

```python
# Incorrecto: imposible de pronunciar
class DtaRcrd102:
    genymdhms = None  # generation date, year, month, day, hour, minute, second
    modymdhms = None  # modification date, year, month, day, hour, minute, second

# Incorrecto: abreviaciones crípticas
def proc_usr_rcrd(usrid):
    usrnm = get_nm(usrid)
    usraddr = get_addr(usrid)
    return {'nm': usrnm, 'addr': usraddr}
```

---

### Ejemplo Correcto

```python
# Correcto: pronunciable y claro
class CustomerRecord:
    """Record of customer information with timestamps."""
    
    def __init__(self):
        self.creation_timestamp: datetime = None
        self.modification_timestamp: datetime = None
        self.customer_id: str = None

# Correcto: nombres completos y descriptivos
def process_user_record(user_id: str) -> dict:
    """
    Process and retrieve user record information.
    
    :param user_id: Unique identifier for user
    :return: Dictionary with user name and address
    """
    user_name = fetch_user_name(user_id)
    user_address = fetch_user_address(user_id)
    return {
        'name': user_name,
        'address': user_address
    }
```

---

## 5. Usar Nombres Buscables

### Por Qué Importa

Los nombres de una sola letra y las constantes numéricas son difíciles de localizar en un cuerpo de texto. Es fácil buscar `MAX_RETRY_ATTEMPTS`, pero el número 3 podría aparecer en cientos de lugares.

**Referencia**: Hunt, A., & Thomas, D. (1999). *The Pragmatic Programmer*. Addison-Wesley.

---

### Ejemplo Incorrecto

```python
# Incorrecto: números mágicos y nombres de una letra
for i in range(7):
    s = s + (t[i] * 4)

# Incorrecto: constantes sin nombre
if response_time > 0.5:
    retry_request()

# Incorrecto: parámetros crípticos
def process(x, y, e=100, b=32, l=0.001):
    for i in range(e):
        for j in range(0, len(x), b):
            batch_x = x[j:j+b]
            batch_y = y[j:j+b]
            # processing logic
            pass
```

---

### Ejemplo Correcto

```python
# Correcto: constantes nombradas
DAYS_PER_WEEK = 7
HOURS_PER_DAY = 4

total_hours = 0
for day_index in range(DAYS_PER_WEEK):
    total_hours += (schedule[day_index] * HOURS_PER_DAY)

# Correcto: umbrales como constantes
MAXIMUM_RESPONSE_TIME_SECONDS = 0.5
MAXIMUM_RETRY_ATTEMPTS = 3

if response_time > MAXIMUM_RESPONSE_TIME_SECONDS:
    retry_request()

# Correcto: parámetros explícitos
DEFAULT_EPOCHS = 100
DEFAULT_BATCH_SIZE = 32
DEFAULT_LEARNING_RATE = 0.001

def process_training_data(
    features: np.ndarray,
    labels: np.ndarray,
    epochs: int = DEFAULT_EPOCHS,
    batch_size: int = DEFAULT_BATCH_SIZE,
    learning_rate: float = DEFAULT_LEARNING_RATE
) -> None:
    """Process training data with specified parameters."""
    for epoch_number in range(epochs):
        for batch_start in range(0, len(features), batch_size):
            batch_end = batch_start + batch_size
            feature_batch = features[batch_start:batch_end]
            label_batch = labels[batch_start:batch_end]
            # Processing logic here
            pass
```

---

### Configuración Centralizada

```python
# Excelente: configuración centralizada y buscable
@dataclass
class ApplicationConfig:
    """Configuration for application settings."""
    
    # API settings
    API_TIMEOUT_SECONDS: float = 30.0
    MAX_RETRY_ATTEMPTS: int = 3
    RETRY_DELAY_SECONDS: float = 1.0
    
    # Database settings
    CONNECTION_POOL_SIZE: int = 10
    QUERY_TIMEOUT_SECONDS: float = 5.0
    
    # Processing settings
    BATCH_SIZE: int = 100
    MAX_WORKERS: int = 4

# Usage
config = ApplicationConfig()
api_client = APIClient(timeout=config.API_TIMEOUT_SECONDS)
```

---

## 6. Evitar Codificaciones

### Por Qué Importa

Los nombres no deben incluir información de tipo o alcance. Los sistemas modernos de tipos y los IDEs hacen que estas codificaciones sean innecesarias.

---

### Notación Húngara (Obsoleta)

```python
# Incorrecto: notación húngara (obsoleta)
strName = "Alice"
iAge = 30
fSalary = 50000.0
lstEmployees = []
dictConfig = {}
```

---

### Código Correcto con Type Hints

```python
# Correcto: type hints modernos
name: str = "Alice"
age: int = 30
salary: float = 50000.0
employees: list[Employee] = []
configuration: dict[str, Any] = {}

# Excelente: nombres descriptivos con tipos claros
def calculate_total_cost(
    base_price: float,
    quantity: int,
    tax_rate: float = 0.21
) -> float:
    """
    Calculate total cost including tax.
    
    :param base_price: Base price per unit
    :param quantity: Number of units
    :param tax_rate: Tax rate as decimal
    :return: Total cost with tax
    """
    subtotal = base_price * quantity
    return subtotal * (1 + tax_rate)
```

---

## 7. Evitar Mapeos Mentales

### Por Qué Importa

Los lectores no deberían tener que traducir mentalmente tus nombres. Usa nombres del dominio del problema o del dominio de la solución.

---

### Ejemplo Incorrecto

```python
# Incorrecto: variables de una letra que requieren mapeo mental
for i in users:
    for j in i.orders:
        for k in j.items:
            process(k)

# Incorrecto: nombres genéricos
def foo(bar, baz):
    qux = bar * baz
    return qux / 2
```

---

### Ejemplo Correcto

```python
# Correcto: nombres explícitos
for user in users:
    for order in user.orders:
        for item in order.items:
            process_order_item(item)

# Correcto: nombres del dominio
def calculate_average_price(
    total_price: float,
    quantity: int
) -> float:
    """Calculate average price per unit."""
    return total_price / quantity
```

---

### Excepción: Convenciones Matemáticas

```python
# Aceptable: convenciones matemáticas establecidas
def euclidean_distance(p1: tuple, p2: tuple) -> float:
    """Calculate Euclidean distance between two points."""
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Aceptable en contexto de álgebra lineal
def matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Multiply two matrices: C = A @ B."""
    return A @ B
```

---

## Resumen de Principios

1. **Revelar Intención**: El nombre debe responder por qué existe, qué hace y cómo se usa
2. **Evitar Desinformación**: No sugerir algo diferente de lo que realmente es
3. **Distinciones Significativas**: Nombres diferentes deben significar cosas diferentes
4. **Pronunciable**: Facilita la comunicación verbal sobre el código
5. **Buscable**: Usa constantes nombradas en lugar de números mágicos
6. **Sin Codificaciones**: Los type hints modernos hacen innecesarias las notaciones húngaras
7. **Sin Mapeos Mentales**: El lector no debe traducir mentalmente tus nombres

---

## Referencias

1. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
2. Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.
3. Hunt, A., & Thomas, D. (1999). *The Pragmatic Programmer*. Addison-Wesley.
4. PEP 8 – Style Guide for Python Code: <https://peps.python.org/pep-0008/>
5. PEP 484 – Type Hints: <https://peps.python.org/pep-0484/>
6. Google Python Style Guide: <https://google.github.io/styleguide/pyguide.html>

---
