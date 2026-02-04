"""
Type Hints Advanced Exercises - Day 3

Practice using advanced type hints including generics, protocols, complex types,
and type narrowing. Learn to write type-safe, reusable code with proper annotations.

Your tasks:
1. Implement a generic Cache class with type parameters
2. Define a Serializable protocol and use it in functions
3. Use type narrowing to handle different result types

Run the tests with: pytest tests/test_03_type_hints_advanced.py
"""


# Exercise 1: Implement a Generic Cache
# TODO: Add proper type hints using TypeVar and Generic
# TODO: Complete the implementation with proper docstrings
class Cache:
    """
    Generic cache that stores key-value pairs.

    TODO: Make this class generic over K (key type) and V (value type)
    TODO: Add proper Sphinx docstrings with type information
    """

    def __init__(self):
        """
        Initialize empty cache.

        TODO: Add proper type hints to _storage
        """
        self._storage = {}

    def set(self, key, value):
        """
        Store a value in the cache.

        TODO: Add type hints for parameters
        TODO: Add :param, :type, :return, :rtype annotations
        """
        self._storage[key] = value

    def get(self, key):
        """
        Retrieve a value from the cache.

        TODO: Add type hints for parameters and return type
        TODO: Return None if key not found
        TODO: Add :param, :type, :return, :rtype annotations
        """
        return self._storage.get(key)

    def clear(self):
        """
        Clear all items from the cache.

        TODO: Add proper type hints
        TODO: Add :return, :rtype annotations
        """
        self._storage.clear()

    def has(self, key):
        """
        Check if key exists in cache.

        TODO: Add type hints for parameters and return type
        TODO: Add :param, :type, :return, :rtype annotations
        """
        return key in self._storage


# Exercise 2: Define a Serializable Protocol
# TODO: Define a Protocol that requires to_dict() and from_dict() methods
# TODO: Add proper type hints and docstrings
class Serializable:
    """
    TODO: Convert this to a Protocol
    TODO: Add proper docstring explaining the protocol
    """

    def to_dict(self):
        """
        Convert object to dictionary.

        TODO: Add proper return type hint
        TODO: Add :return, :rtype annotations
        """
        pass

    def from_dict(data):
        """
        Create object from dictionary.

        TODO: Add proper type hints for parameters and return
        TODO: Add :param, :type, :return, :rtype annotations
        TODO: Make this a @classmethod or @staticmethod
        """
        pass


# TODO: Implement a function that works with any Serializable object
def save_to_json(obj, filename):
    """
    Save a serializable object to JSON file.

    TODO: Add type hints using the Serializable protocol
    TODO: Add proper Sphinx docstring
    TODO: Implement the function (can use json.dumps for simplicity)

    :param obj: Object to serialize
    :type obj: Serializable
    :param filename: Path to save file
    :type filename: str
    :return: Success status
    :rtype: bool
    """
    pass


# TODO: Create a User class that implements the Serializable protocol
class User:
    """
    User class that can be serialized.

    TODO: Implement to_dict() and from_dict() methods
    TODO: Add proper type hints
    TODO: Add proper Sphinx docstrings
    """

    def __init__(self, name, age):
        """
        Initialize user.

        TODO: Add type hints for parameters
        TODO: Add :param, :type annotations
        """
        self.name = name
        self.age = age

    def to_dict(self):
        """
        Convert user to dictionary.

        TODO: Add return type hint
        TODO: Implement the method
        """
        pass

    def from_dict(data):
        """
        Create user from dictionary.

        TODO: Add type hints
        TODO: Make this a @classmethod
        TODO: Implement the method
        """
        pass


# Exercise 3: Type Narrowing with Validation
# TODO: Define a Result type that can be either success (dict) or error (str)
# Hint: Use Union or the | operator


def validate_email(email):
    """
    Validate email address.

    TODO: Add type hints for parameter and return
    TODO: Return dict with 'email' and 'valid' keys on success
    TODO: Return error message string on failure
    TODO: Add proper Sphinx docstring

    :param email: Email address to validate
    :type email: str
    :return: Success dict or error string
    :rtype: dict[str, str] | str
    """
    pass


def process_result(result):
    """
    Process validation result using type narrowing.

    TODO: Add type hints for parameter and return
    TODO: Use isinstance() to narrow the type
    TODO: Handle both success (dict) and error (str) cases
    TODO: Add proper Sphinx docstring

    :param result: Validation result
    :type result: dict[str, str] | str
    :return: Formatted message
    :rtype: str
    """
    pass


# Exercise 4: Generic Function with Constraints
# TODO: Create a TypeVar that only accepts int or float
# TODO: Implement a function that doubles numeric values
def double_value(value):
    """
    Double a numeric value.

    TODO: Add type hints using constrained TypeVar
    TODO: The function should work with int or float only
    TODO: Return type should match input type
    TODO: Add proper Sphinx docstring

    :param value: Numeric value to double
    :type value: int | float
    :return: Doubled value
    :rtype: int | float
    """
    pass


# Exercise 5: Protocol with Properties
# TODO: Define a Sized protocol that requires a size property
class Sized:
    """
    TODO: Convert this to a Protocol
    TODO: Require a size property that returns int
    """

    def size(self):
        """
        Get the size.

        TODO: Make this a @property
        TODO: Add return type hint
        """
        pass


# TODO: Implement a function that works with any Sized object
def print_size(obj):
    """
    Print the size of any sized object.

    TODO: Add type hints using the Sized protocol
    TODO: Add proper Sphinx docstring

    :param obj: Object with size property
    :type obj: Sized
    :return: None
    :rtype: None
    """
    pass


# TODO: Create a Buffer class that implements the Sized protocol
class Buffer:
    """
    Buffer with size property.

    TODO: Implement size property
    TODO: Add proper type hints
    """

    def __init__(self, data):
        """
        Initialize buffer with data.

        TODO: Add type hints
        """
        self.data = data

    def size(self):
        """
        Get buffer size.

        TODO: Make this a @property
        TODO: Return length of data
        TODO: Add return type hint
        """
        pass
