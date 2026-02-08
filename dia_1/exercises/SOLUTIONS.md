# Soluciones de Referencia - Type Hinting

Este archivo contiene soluciones de referencia para los ejercicios. **No lo consultes hasta que hayas intentado resolver los ejercicios por tu cuenta.**

## Ejercicio 1: `calculate_rectangle_area`

```python
def calculate_rectangle_area(width: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    :param width: Width of the rectangle
    :type width: float
    :param height: Height of the rectangle
    :type height: float
    :return: Area of the rectangle
    :rtype: float

    Example:
        >>> calculate_rectangle_area(5.0, 3.0)
        15.0
    """
    return width * height
```

---

## Ejercicio 2: `calculate_statistics`

```python
def calculate_statistics(numbers: list[float]) -> dict[str, float]:
    """
    Calculate statistics for a list of numbers.

    :param numbers: List of numeric values
    :type numbers: list[float]
    :return: Dictionary with keys 'sum', 'average', 'min', 'max'
    :rtype: dict[str, float]
    :raises ValueError: If the list is empty

    Example:
        >>> stats = calculate_statistics([1.0, 2.0, 3.0, 4.0, 5.0])
        >>> stats['average']
        3.0
    """
    if not numbers:
        raise ValueError("Cannot calculate statistics of empty list")

    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }
```

---

## Ejercicio 3: `process_value`

```python
def process_value(value: int | str) -> str:
    """
    Process a value that can be int or str.

    :param value: Value to process (int or str)
    :type value: int | str
    :return: Processed value as string
    :rtype: str

    Example:
        >>> process_value(42)
        'Processed: 42'
        >>> process_value('hello')
        'Processed: hello'
    """
    return f"Processed: {value}"
```

---

## Ejercicio 4: `find_user`

```python
def find_user(user_id: int) -> Optional[dict[str, str]]:
    """
    Find a user by ID, returning None if not found.

    :param user_id: User ID to search for
    :type user_id: int
    :return: User data or None if not found
    :rtype: Optional[dict[str, str]]

    Example:
        >>> find_user(1)
        {'id': '1', 'name': 'Alice'}
        >>> find_user(999) is None
        True
    """
    if user_id == 1:
        return {"id": "1", "name": "Alice"}
    return None
```

---

## Ejercicio 5: `DataProcessor` (Clase)

```python
class DataProcessor:
    """
    Process and analyze numerical data.

    :ivar name: Name of the processor
    :vartype name: str
    :ivar data: Stored data points
    :vartype data: list[float]
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the DataProcessor.

        :param name: Name of the processor
        :type name: str
        """
        self.name: str = name
        self.data: list[float] = []

    def add_data(self, data: list[float]) -> None:
        """
        Add data points to the processor.

        :param data: List of data points to add
        :type data: list[float]
        """
        self.data.extend(data)

    def get_average(self) -> Optional[float]:
        """
        Calculate the average of stored data.

        :return: Average value or None if no data
        :rtype: Optional[float]
        """
        if not self.data:
            return None
        return sum(self.data) / len(self.data)

    def get_data(self) -> list[float]:
        """
        Get all stored data.

        :return: List of data points
        :rtype: list[float]
        """
        return self.data.copy()
```

---

## Ejercicio 6: `validate_and_process` (Avanzado)

```python
def validate_and_process(
    value: int | str | float,
) -> tuple[bool, str | float | None]:
    """
    Validate and process a value, returning success status and result.

    :param value: Value to validate and process
    :type value: int | str | float
    :return: Tuple of (is_valid, result) where result is the processed value or None
    :rtype: tuple[bool, str | float | None]

    Example:
        >>> validate_and_process(42)
        (True, 42.0)
        >>> validate_and_process('hello')
        (True, 'hello')
        >>> validate_and_process(3.14)
        (True, 3.14)
    """
    if isinstance(value, int):
        return (True, float(value))
    elif isinstance(value, str):
        return (True, value)
    elif isinstance(value, float):
        return (True, value)
    else:
        return (False, None)
```

---

## Notas Importantes

- Estas soluciones son solo referencias. Tu implementación puede ser diferente pero debe pasar todos los tests.
- Asegúrate de que tu código tenga type hints completos y docstrings en formato Sphinx.
- Valida tu código con Pyright y formatea con Ruff.
- Si tu solución pasa todos los tests pero es diferente a la de referencia, ¡está bien! Lo importante es que funcione correctamente.

## Próximos Pasos

Una vez completes todos los ejercicios:

1. Verifica que todos los tests pasen
2. Valida con Pyright
3. Formatea con Ruff
4. Revisa tu código con un compañero
5. Pasa al siguiente notebook
