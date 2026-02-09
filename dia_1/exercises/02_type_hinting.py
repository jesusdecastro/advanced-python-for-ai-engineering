"""
Type Hinting Exercises - Day 1

Add proper type hints to the functions and classes below.
The code is already implemented, but it's missing type hints.

Your task:
1. Add type hints to all function parameters
2. Add return type hints to all functions
3. Add type hints to class attributes
4. Ensure docstrings have proper :type: and :rtype: annotations

Run the tests with: pytest tests/test_02_type_hinting.py
Validate type hints with: pyright exercises/02_type_hinting.py

Note: You need to import the necessary types from the typing module.
"""

from typing import Dict, List, Optional, Tuple


# Exercise 1: Basic Type Hints
def calculate_rectangle_area(width, height):
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
    
    Tests to pass:
        - Basic calculation: 5.0 * 3.0 should return 15.0
        - Square: 4.0 * 4.0 should return 16.0
        - Decimal values: 2.5 * 4.0 should return 10.0
        - Small values: 0.5 * 0.5 should return 0.25
        - Large values: 1000.0 * 500.0 should return 500000.0
        - Must have type hints for width, height (float) and return type (float)
    """
    return width * height


# Exercise 2: Complex Types (List and Dict)
def calculate_statistics(numbers):
    """
    Calculate statistics for a list of numbers.

    :param numbers: List of numbers to analyze
    :type numbers: List[float]
    :return: Dictionary with sum, average, min, max
    :rtype: Dict[str, float]
    :raises ValueError: If the list is empty

    Example:
        >>> stats = calculate_statistics([1.0, 2.0, 3.0, 4.0, 5.0])
        >>> stats['average']
        3.0
    
    Tests to pass:
        - Basic statistics: [1.0, 2.0, 3.0, 4.0, 5.0] should return correct sum, average, min, max
        - Single value: [42.0] should return all stats equal to 42.0
        - Negative values: [-5.0, -2.0, 0.0, 2.0, 5.0] should handle correctly
        - Empty list: [] should raise ValueError
        - All same values: [7.0, 7.0, 7.0] should return correct stats
        - Must have type hints: List[float] parameter, Dict[str, float] return
    """
    if not numbers:
        raise ValueError("Cannot calculate statistics of empty list")

    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }


# Exercise 3: Union Types
def process_value(value):
    """
    Process a value that can be int or str.

    :param value: Value to process (can be int or str)
    :type value: int | str
    :return: Processed string
    :rtype: str

    Example:
        >>> process_value(42)
        'Processed: 42'
        >>> process_value('hello')
        'Processed: hello'
    
    Tests to pass:
        - Integer input: 42 should return 'Processed: 42'
        - String input: 'hello' should return 'Processed: hello'
        - Zero: 0 should return 'Processed: 0'
        - Negative integer: -10 should return 'Processed: -10'
        - Empty string: '' should return 'Processed: '
        - Must have union type hint: int | str for parameter
    """
    return f"Processed: {value}"


# Exercise 4: Optional Types
def find_user(user_id):
    """
    Find a user by ID, returning None if not found.

    :param user_id: ID of the user to find
    :type user_id: int
    :return: User dictionary if found, None otherwise
    :rtype: Optional[Dict[str, str]]

    Example:
        >>> find_user(1)
        {'id': '1', 'name': 'Alice'}
        >>> find_user(999) is None
        True
    
    Tests to pass:
        - Existing user: find_user(1) should return dict with 'id' and 'name'
        - Non-existent user: find_user(999) should return None
        - Return type must be dict when found
        - Dict must have 'id' and 'name' keys
        - Must have Optional[Dict[str, str]] return type hint
    """
    if user_id == 1:
        return {"id": "1", "name": "Alice"}
    return None


# Exercise 5: Class with Type Hints
class DataProcessor:
    """
    Process and analyze numerical data.

    :ivar name: Name of the processor
    :vartype name: str
    :ivar data: List of numerical data points
    :vartype data: List[float]
    
    Tests to pass:
        - Initialization: name should be stored, data should start empty
        - add_data: should extend data list with new values
        - get_average: should return correct average or None if empty
        - get_data: should return copy of data (not reference)
        - All methods must have proper type hints
    """

    def __init__(self, name):
        """
        Initialize the DataProcessor.

        :param name: Name of the processor
        :type name: str
        """
        self.name = name
        self.data = []

    def add_data(self, data):
        """
        Add data points to the processor.

        :param data: List of data points to add
        :type data: List[float]
        """
        self.data.extend(data)

    def get_average(self):
        """
        Calculate the average of stored data.

        :return: Average of data, or None if no data
        :rtype: Optional[float]
        """
        if not self.data:
            return None
        return sum(self.data) / len(self.data)

    def get_data(self):
        """
        Get all stored data.

        :return: Copy of the data list
        :rtype: List[float]
        """
        return self.data.copy()


# Exercise 6: Advanced - Function with Multiple Return Types
def validate_and_process(value):
    """
    Validate and process a value, returning success status and result.

    :param value: Value to validate and process (int, str, or float)
    :type value: int | str | float
    :return: Tuple of (success status, processed value or None)
    :rtype: Tuple[bool, int | str | float | None]

    Example:
        >>> validate_and_process(42)
        (True, 42.0)
        >>> validate_and_process('hello')
        (True, 'hello')
        >>> validate_and_process(3.14)
        (True, 3.14)
    
    Tests to pass:
        - Integer: 42 should return (True, 42.0) - converted to float
        - String: 'hello' should return (True, 'hello')
        - Float: 3.14 should return (True, 3.14)
        - Zero: 0 should return (True, 0.0)
        - Negative: -10 should return (True, -10.0)
        - Empty string: '' should return (True, '')
        - Return type must be tuple with bool and value
        - Must have proper union type hints for parameter and return
    """
    if isinstance(value, int):
        return (True, float(value))
    elif isinstance(value, str):
        return (True, value)
    elif isinstance(value, float):
        return (True, value)
    else:
        return (False, None)
