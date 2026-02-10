# Funciones

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Funciones Pequeñas](#1-funciones-pequeñas)
3. [Hacer Una Cosa](#2-hacer-una-cosa)
4. [Un Nivel de Abstracción](#3-un-nivel-de-abstracción-por-función)
5. [Argumentos de Función](#4-argumentos-de-función)
6. [Sin Efectos Secundarios](#5-sin-efectos-secundarios)
7. [Separación Comando-Consulta](#6-separación-comando-consulta)
8. [Preferir Excepciones](#7-preferir-excepciones-a-códigos-de-error)
9. [Resumen](#resumen-de-principios)

---

## Introducción

Las funciones son la primera línea de organización en cualquier programa. Escribir funciones bien diseñadas es fundamental para crear software mantenible y comprensible.

**Referencia principal**: Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 3: Functions.

### Principio Fundamental

> "Functions should do one thing. They should do it well. They should do it only."
>
> — Robert C. Martin, Clean Code

Una función bien diseñada es pequeña, hace una cosa, y la hace bien.

---

## 1. Funciones Pequeñas

### Por Qué Importa

Las funciones deben ser pequeñas. Cuanto más pequeña es una función, más fácil es entenderla, probarla y mantenerla.

**Regla práctica**: Si una función tiene más de 20 líneas, probablemente hace demasiado.

---

### Ejemplo Incorrecto

```python
def process_order(order_id, customer_id):
    # Fetch order
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM orders WHERE id = {order_id}")
    order = cursor.fetchone()
    conn.close()
    
    # Validate order
    if not order:
        raise ValueError("Order not found")
    if order['status'] != 'pending':
        raise ValueError("Order already processed")
    
    # Calculate total
    total = 0
    for item in order['items']:
        total += item['price'] * item['quantity']
    
    # Apply discount
    if total > 100:
        total *= 0.9
    
    # Update inventory
    for item in order['items']:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute(f"UPDATE inventory SET stock = stock - {item['quantity']} WHERE id = {item['id']}")
        conn.commit()
        conn.close()
    
    # Send email
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login('admin@company.com', 'password')
    message = f"Order {order_id} processed. Total: ${total}"
    smtp.sendmail('admin@company.com', customer['email'], message)
    smtp.quit()
    
    return total
```

**Problemas**:

- Hace al menos 6 cosas diferentes
- Imposible de probar sin base de datos y servidor SMTP
- Mezcla diferentes niveles de abstracción
- Difícil de reutilizar partes individuales

---

### Ejemplo Correcto

```python
def fetch_order_from_database(order_id: str) -> dict:
    """Retrieve order from database."""
    connection = database.connect()
    order = connection.query_order(order_id)
    connection.close()
    return order


def validate_order_status(order: dict) -> None:
    """Validate order can be processed."""
    if not order:
        raise ValueError("Order not found")
    if order['status'] != 'pending':
        raise ValueError("Order already processed")


def calculate_order_total(order: dict) -> float:
    """Calculate total price with discount."""
    subtotal = sum(item['price'] * item['quantity'] for item in order['items'])
    discount = 0.9 if subtotal > 100 else 1.0
    return subtotal * discount


def update_inventory_for_order(order: dict) -> None:
    """Decrease inventory stock for order items."""
    for item in order['items']:
        inventory.decrease_stock(item['id'], item['quantity'])


def send_order_confirmation_email(customer_email: str, order_id: str, total: float) -> None:
    """Send order confirmation to customer."""
    email_service.send(
        to=customer_email,
        subject=f"Order {order_id} Confirmed",
        body=f"Your order has been processed. Total: ${total:.2f}"
    )


def process_order(order_id: str, customer_id: str) -> float:
    """
    Process customer order: validate, calculate, update inventory, notify.
    
    :param order_id: Unique order identifier
    :param customer_id: Customer identifier
    :return: Order total amount
    """
    order = fetch_order_from_database(order_id)
    validate_order_status(order)
    
    total = calculate_order_total(order)
    update_inventory_for_order(order)
    
    customer = fetch_customer(customer_id)
    send_order_confirmation_email(customer['email'], order_id, total)
    
    return total
```

**Ventajas**:

- Cada función hace exactamente una cosa
- Fácil de probar con mocks
- Fácil de reutilizar componentes
- Código auto-documentado

---

## 2. Hacer Una Cosa

### Por Qué Importa

Una función debe hacer una cosa, hacerla bien, y ser lo único que haga. Si una función hace más de una cosa, es difícil de nombrar, probar y reutilizar.

---

### Ejemplo Incorrecto

```python
def process_user_data(user_id: str) -> dict:
    """Process user data and send notification."""
    # Fetch user
    user = database.get_user(user_id)
    
    # Validate
    if not user:
        raise ValueError("User not found")
    if user['age'] < 18:
        raise ValueError("User must be 18 or older")
    
    # Calculate score
    score = user['purchases'] * 10 + user['reviews'] * 5
    
    # Update database
    database.update_user_score(user_id, score)
    
    # Send email
    email_service.send(user['email'], f"Your new score is {score}")
    
    # Log activity
    logger.info(f"User {user_id} processed, score: {score}")
    
    return {'user_id': user_id, 'score': score}
```

**Problemas**:

- Hace 6 cosas: fetch, validate, calculate, update, notify, log
- Imposible de probar sin base de datos y email
- Viola el principio de responsabilidad única

---

### Ejemplo Correcto

```python
def fetch_user(user_id: str) -> dict:
    """Retrieve user from database."""
    user = database.get_user(user_id)
    if not user:
        raise ValueError(f"User {user_id} not found")
    return user


def validate_user_age(user: dict, minimum_age: int = 18) -> None:
    """Validate user meets age requirement."""
    if user['age'] < minimum_age:
        raise ValueError(f"User must be {minimum_age} or older")


def calculate_user_score(user: dict) -> int:
    """Calculate user engagement score."""
    PURCHASE_WEIGHT = 10
    REVIEW_WEIGHT = 5
    return user['purchases'] * PURCHASE_WEIGHT + user['reviews'] * REVIEW_WEIGHT


def update_user_score(user_id: str, score: int) -> None:
    """Update user score in database."""
    database.update_user_score(user_id, score)


def notify_user_score(user_email: str, score: int) -> None:
    """Send email notification about new score."""
    email_service.send(user_email, f"Your new score is {score}")


def log_user_processing(user_id: str, score: int) -> None:
    """Log user processing activity."""
    logger.info(f"User {user_id} processed, score: {score}")


def process_user_data(user_id: str) -> dict:
    """
    Process user: validate, calculate score, update, and notify.
    
    :param user_id: Unique user identifier
    :return: Dictionary with user_id and calculated score
    """
    user = fetch_user(user_id)
    validate_user_age(user)
    
    score = calculate_user_score(user)
    update_user_score(user_id, score)
    
    notify_user_score(user['email'], score)
    log_user_processing(user_id, score)
    
    return {'user_id': user_id, 'score': score}
```

---

## 3. Un Nivel de Abstracción por Función

### Por Qué Importa

Las declaraciones dentro de una función deben estar todas al mismo nivel de abstracción. Mezclar niveles es confuso.

**Referencia**: Fowler, M. (2018). *Refactoring*. "Compose Method: All operations in a method should be at the same level of abstraction."

---

### Ejemplo Incorrecto

```python
def generate_report(data_path: str) -> str:
    """Generate sales report."""
    # High-level: load data
    data = pd.read_csv(data_path)
    
    # Low-level: detailed cleaning
    data = data.dropna()
    data['amount_normalized'] = (data['amount'] - data['amount'].mean()) / data['amount'].std()
    data = pd.get_dummies(data, columns=['category'])
    
    # High-level: calculate
    total = data['amount'].sum()
    
    # Low-level: detailed formatting
    report = "Sales Report\n"
    report += "=" * 50 + "\n"
    report += f"Total Sales: ${total:,.2f}\n"
    report += f"Average: ${data['amount'].mean():,.2f}\n"
    
    return report
```

**Problemas**:

- Mezcla alto nivel (load, calculate) con bajo nivel (detalles de limpieza y formato)
- Difícil de seguir el flujo principal

---

### Ejemplo Correcto

```python
def load_sales_data(data_path: str) -> pd.DataFrame:
    """Load raw sales data from CSV."""
    return pd.read_csv(data_path)


def clean_sales_data(data: pd.DataFrame) -> pd.DataFrame:
    """Apply all cleaning transformations."""
    data_cleaned = remove_missing_values(data)
    data_normalized = normalize_amounts(data_cleaned)
    data_encoded = encode_categories(data_normalized)
    return data_encoded


def calculate_sales_metrics(data: pd.DataFrame) -> dict:
    """Calculate summary metrics."""
    return {
        'total': data['amount'].sum(),
        'average': data['amount'].mean(),
        'count': len(data)
    }


def format_sales_report(metrics: dict) -> str:
    """Format metrics into readable report."""
    return f"""
Sales Report
{'=' * 50}
Total Sales: ${metrics['total']:,.2f}
Average: ${metrics['average']:,.2f}
Transactions: {metrics['count']:,}
"""


def generate_report(data_path: str) -> str:
    """
    Generate sales report from data file.
    
    All operations at same level of abstraction.
    """
    raw_data = load_sales_data(data_path)
    clean_data = clean_sales_data(raw_data)
    metrics = calculate_sales_metrics(clean_data)
    report = format_sales_report(metrics)
    return report
```

---

## 4. Argumentos de Función

### Por Qué Importa

El número ideal de argumentos es cero. Después viene uno, seguido de dos. Tres argumentos deben evitarse cuando sea posible.

**Referencia**: Martin, R. C. (2008). *Clean Code*. "The ideal number of arguments for a function is zero."

---

### Ejemplo Incorrecto

```python
# Demasiados argumentos posicionales
def create_user(name, email, age, address, phone, city, country, postal_code, preferences):
    pass

# Flag arguments (indica que la función hace más de una cosa)
def process_data(data, is_training):
    if is_training:
        data = augment_data(data)
        data = shuffle_data(data)
    else:
        data = normalize_data(data)
    return data

# Output arguments (confuso)
def append_footer(report, footer_text):
    """Append footer to report."""
    report.append(footer_text)  # Modifica el argumento
    return None
```

---

### Ejemplo Correcto

```python
# Usar objetos de configuración
@dataclass
class UserProfile:
    """User profile information."""
    name: str
    email: str
    age: int
    address: str
    phone: str
    city: str
    country: str
    postal_code: str
    preferences: dict


def create_user(profile: UserProfile) -> User:
    """Create user from profile."""
    return User(profile)


# Separar funciones en lugar de usar flags
def process_training_data(data: np.ndarray) -> np.ndarray:
    """Process data for training (augmentation + shuffling)."""
    augmented = augment_data(data)
    shuffled = shuffle_data(augmented)
    return shuffled


def process_inference_data(data: np.ndarray) -> np.ndarray:
    """Process data for inference (normalization only)."""
    return normalize_data(data)


# Devolver nuevo valor en lugar de modificar argumento
def create_report_with_footer(report: list[str], footer: str) -> list[str]:
    """Create new report with footer appended."""
    return report + [footer]
```

---

## 5. Sin Efectos Secundarios

### Por Qué Importa

Los efectos secundarios son mentiras. Tu función promete hacer una cosa, pero también hace otras cosas ocultas.

---

### Ejemplo Incorrecto

```python
class UserAuthenticator:
    def __init__(self):
        self.session = None
        self.last_login = None
    
    def check_password(self, username: str, password: str) -> bool:
        """Check if password is valid."""
        user = database.find_user(username)
        if user and user.password == encrypt(password):
            # Side effect: modifies instance state
            self.session = Session(username)
            # Side effect: modifies global state
            self.last_login = datetime.now()
            # Side effect: writes to database
            database.update_last_login(username, self.last_login)
            return True
        return False
```

**Problemas**:

- La función hace más de lo que su nombre sugiere
- Efectos secundarios ocultos pueden causar bugs

---

### Ejemplo Correcto

```python
class UserAuthenticator:
    def __init__(self):
        self.session = None
        self.last_login = None
    
    def verify_password(self, username: str, password: str) -> bool:
        """Verify if password matches. Pure function with no side effects."""
        user = database.find_user(username)
        return user is not None and user.password == encrypt(password)
    
    def create_session(self, username: str) -> Session:
        """Create new session for user."""
        self.session = Session(username)
        return self.session
    
    def record_login_time(self, username: str) -> datetime:
        """Record and persist login time."""
        self.last_login = datetime.now()
        database.update_last_login(username, self.last_login)
        return self.last_login
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """Complete authentication process. Explicitly performs all steps."""
        if not self.verify_password(username, password):
            return False
        
        self.create_session(username)
        self.record_login_time(username)
        return True
```

---

## 6. Separación Comando-Consulta

### Por Qué Importa

Las funciones deben hacer algo o responder algo, pero no ambas cosas.

**Referencia**: Meyer, B. (1988). *Object-Oriented Software Construction*. "Command Query Separation."

---

### Ejemplo Incorrecto

```python
def set_and_check(obj: dict, attribute: str, value: Any) -> bool:
    """Set attribute and return True if it was changed."""
    if attribute in obj and obj[attribute] == value:
        return False  # No change needed
    obj[attribute] = value
    return True  # Changed

# Uso confuso
if set_and_check(user, 'status', 'active'):
    # ¿Qué significa True? ¿Se estableció? ¿Ya estaba establecido?
    print("Status changed")
```

---

### Ejemplo Correcto

```python
# Separar en comando y consulta
def set_attribute(obj: dict, attribute: str, value: Any) -> None:
    """Set attribute value. Command: modifies object state."""
    obj[attribute] = value


def attribute_was_changed(obj: dict, attribute: str, new_value: Any) -> bool:
    """Check if setting attribute would change its value. Query: no modification."""
    return attribute not in obj or obj[attribute] != new_value


# Uso claro
if attribute_was_changed(user, 'status', 'active'):
    set_attribute(user, 'status', 'active')
    print("Status changed")
```

---

## 7. Preferir Excepciones a Códigos de Error

### Por Qué Importa

Devolver códigos de error satura al llamador. Es mejor lanzar excepciones.

---

### Ejemplo Incorrecto

```python
ERROR_NONE = 0
ERROR_FILE_NOT_FOUND = 1
ERROR_INVALID_FORMAT = 2

def load_data(file_path: str) -> tuple[pd.DataFrame, int]:
    """Load data, return data and error code."""
    if not os.path.exists(file_path):
        return None, ERROR_FILE_NOT_FOUND
    
    try:
        data = pd.read_csv(file_path)
    except Exception:
        return None, ERROR_INVALID_FORMAT
    
    return data, ERROR_NONE

# Uso: anidamiento profundo
data, error = load_data('data.csv')
if error == ERROR_NONE:
    result, error2 = process(data)
    if error2 == ERROR_NONE:
        print("Success")
    else:
        print(f"Error: {error2}")
else:
    print(f"Error: {error}")
```

---

### Ejemplo Correcto

```python
class DataLoadingError(Exception):
    """Raised when data cannot be loaded."""
    pass

class InvalidDataFormatError(Exception):
    """Raised when data format is invalid."""
    pass


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from file.
    
    :param file_path: Path to data file
    :return: Loaded dataframe
    :raises DataLoadingError: If file does not exist
    :raises InvalidDataFormatError: If file format is invalid
    """
    if not os.path.exists(file_path):
        raise DataLoadingError(f"File not found: {file_path}")
    
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise InvalidDataFormatError(f"Invalid CSV format: {e}")


# Uso: flujo lineal
try:
    data = load_data('data.csv')
    result = process(data)
    print("Success")
except DataLoadingError as e:
    logger.error(f"Data loading failed: {e}")
except InvalidDataFormatError as e:
    logger.error(f"Invalid format: {e}")
```

---

## Resumen de Principios

1. **Funciones pequeñas**: Máximo 20 líneas, idealmente menos
2. **Hacer una cosa**: Una función, una responsabilidad
3. **Un nivel de abstracción**: No mezclar alto y bajo nivel
4. **Pocos argumentos**: Ideal 0-2, máximo 3
5. **Sin efectos secundarios**: Hacer solo lo que el nombre promete
6. **Separación comando-consulta**: Hacer o responder, no ambas
7. **Preferir excepciones**: Más limpio que códigos de error

---

## Referencias

1. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
2. Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.
3. Meyer, B. (1988). *Object-Oriented Software Construction*. Prentice Hall.
4. PEP 8 – Style Guide for Python Code: <https://peps.python.org/pep-0008/>

---

## Ejercicio Práctico

Refactoriza el siguiente código aplicando los principios de funciones limpias:

```python
def process(data_path, output_path):
    df = pd.read_csv(data_path)
    df = df.dropna()
    df['total'] = df['price'] * df['quantity']
    result = df.groupby('category')['total'].sum()
    result.to_csv(output_path)
    print(f"Processed {len(df)} rows")
    return result
```

**Pistas**:

- ¿Cuántas cosas hace esta función?
- ¿Están todas al mismo nivel de abstracción?
- ¿Tiene efectos secundarios?
- ¿Mezcla comando y consulta?
