"""
Type Hinting Exercises - Day 1

Add proper type hints to the functions and classes below.
The code is already implemented, but it's missing type hints.

Your task:
1. Add type hints to all function parameters
2. Add return type hints to all functions
3. Add type hints to class attributes
4. Update the docstrings with proper :type: and :rtype: annotations

Run the tests with: pytest tests/test_02_type_hinting.py
Validate type hints with: pyright exercises/02_type_hinting.py
"""

# TODO: Import necessary types from typing module
# Hint: You'll need Optional


# Exercise 1: Basic Type Hints
# TODO: Add type hints to parameters and return type
def calculate_rectangle_area(width, height):
    """
    Calculate the area of a rectangle.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> calculate_rectangle_area(5.0, 3.0)
        15.0
    """
    return width * height


# Exercise 2: Complex Types (List and Dict)
# TODO: Add type hints for list parameter and dict return type
def calculate_statistics(numbers):
    """
    Calculate statistics for a list of numbers.

    TODO: Add :param, :type, :return, :rtype, :raises annotations

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


# Exercise 3: Union Types
# TODO: Add union type hint (value can be int OR str)
def process_value(value):
    """
    Process a value that can be int or str.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> process_value(42)
        'Processed: 42'
        >>> process_value('hello')
        'Processed: hello'
    """
    return f"Processed: {value}"


# Exercise 4: Optional Types
# TODO: Add type hints (return type can be dict or None)
def find_user(user_id):
    """
    Find a user by ID, returning None if not found.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> find_user(1)
        {'id': '1', 'name': 'Alice'}
        >>> find_user(999) is None
        True
    """
    if user_id == 1:
        return {"id": "1", "name": "Alice"}
    return None


# Exercise 5: Class with Type Hints
# TODO: Add type hints to all methods and attributes
class DataProcessor:
    """
    Process and analyze numerical data.

    TODO: Add :ivar and :vartype annotations for name and data
    """

    def __init__(self, name):
        """
        Initialize the DataProcessor.

        TODO: Add :param, :type annotations
        """
        self.name = name
        self.data = []

    def add_data(self, data):
        """
        Add data points to the processor.

        TODO: Add :param, :type annotations
        """
        self.data.extend(data)

    def get_average(self):
        """
        Calculate the average of stored data.

        TODO: Add :return, :rtype annotations
        """
        if not self.data:
            return None
        return sum(self.data) / len(self.data)

    def get_data(self):
        """
        Get all stored data.

        TODO: Add :return, :rtype annotations
        """
        return self.data.copy()


# Exercise 6: Advanced - Function with Multiple Return Types
# TODO: Add type hints for union parameter and tuple return type
def validate_and_process(value):
    """
    Validate and process a value, returning success status and result.

    TODO: Add :param, :type, :return, :rtype annotations

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
