"""
Decorators Exercises - Day 2.

This module contains exercises to practice working with Python decorators,
including @property, @staticmethod, @classmethod, and custom decorators.

Your tasks:
1. Complete the BankAccount class with @property
2. Implement the Date class with @classmethod factory methods
3. Create a custom @validate_types decorator

Run the tests with: pytest tests/test_03_decorators.py
"""

# TODO: Import necessary modules
# Hint: You'll need functools for wraps, datetime for Date class


# Exercise 1: BankAccount with @property
# TODO: Complete the BankAccount class
class BankAccount:
    """
    Bank account with balance management.

    TODO: Add complete docstring with:
    :param initial_balance: Starting balance
    :type initial_balance: float
    :ivar _balance: Private balance attribute
    :vartype _balance: float
    """

    def __init__(self, initial_balance):
        # TODO: Initialize _balance attribute
        # Hint: Validate that initial_balance is not negative
        pass

    # TODO: Add @property decorator
    def balance(self):
        """
        Get current balance (read-only property).

        TODO: Add return type annotation
        """
        pass

    def deposit(self, amount):
        """
        Deposit money into account.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :raises annotations
        """
        # TODO: Validate amount is positive
        # TODO: Add amount to balance
        pass

    def withdraw(self, amount):
        """
        Withdraw money from account.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :raises annotations
        """
        # TODO: Validate amount is positive
        # TODO: Validate sufficient balance
        # TODO: Subtract amount from balance
        pass


# Exercise 2: Date class with @classmethod
# TODO: Complete the Date class
class Date:
    """
    Date representation with factory methods.

    TODO: Add complete docstring with:
    :param day: Day of month
    :type day: int
    :param month: Month number (1-12)
    :type month: int
    :param year: Year
    :type year: int
    """

    def __init__(self, day, month, year):
        # TODO: Add type hints to parameters
        # TODO: Initialize day, month, year attributes
        pass

    # TODO: Add @classmethod decorator
    def from_string(self, date_string):
        """
        Create Date instance from string in DD-MM-YYYY format.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :return, :rtype annotations
        """
        # TODO: Parse date_string (format: "DD-MM-YYYY")
        # TODO: Extract day, month, year
        # TODO: Return new instance using cls(day, month, year)
        pass

    # TODO: Add @classmethod decorator
    def today(self):
        """
        Create Date instance with today's date.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Get current date using datetime
        # TODO: Return new instance with current day, month, year
        pass

    def display(self):
        """
        Display date in readable format.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Return formatted string like "25 de diciembre de 2024"
        # Hint: Create a month names dictionary
        pass


# Exercise 3: Custom decorator with type validation
# TODO: Implement the validate_types decorator
def validate_types(func):
    """
    Validate function arguments match their type hints.

    TODO: Add complete docstring with:
    :param func: Function to decorate
    :type func: callable
    :return: Wrapped function with type validation
    :rtype: callable
    :raises TypeError: When argument types don't match hints
    """

    # TODO: Add @wraps(func) decorator to preserve metadata
    def wrapper(*args, **kwargs):
        """
        Perform type validation.

        TODO: Add parameter and return type annotations
        """
        # TODO: Get function annotations using func.__annotations__
        # TODO: Get parameter names using func.__code__.co_varnames
        # TODO: For each argument, check if it matches the type hint
        # TODO: Raise TypeError if types don't match
        # TODO: Call and return original function
        pass

    return wrapper


# Bonus Exercise: Create a timing decorator
# TODO: Implement a decorator that measures execution time
def timing_decorator(func):
    """
    Measure and print function execution time.

    TODO: Add complete docstring
    TODO: Use functools.wraps
    TODO: Measure time before and after function call
    TODO: Print execution time
    """
    pass


# Bonus Exercise: Create a retry decorator with parameters
# TODO: Implement a decorator that retries failed function calls
def retry(max_attempts=3, delay=1.0):
    """
    Retry a function on failure.

    TODO: Add complete docstring with parameters
    TODO: Implement three-level decorator structure
    TODO: Catch exceptions and retry up to max_attempts
    TODO: Add delay between retries
    """
    pass
