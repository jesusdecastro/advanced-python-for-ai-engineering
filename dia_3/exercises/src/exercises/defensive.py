"""
Defensive Programming Exercises - Day 3.

Practice input validation, type hints, fail-fast, and eliminating magic numbers.

Your task:
1. Add comprehensive input validation
2. Use proper type hints (Union, Optional, etc.)
3. Implement fail-fast patterns
4. Use the provided constants (no magic numbers!)
5. Complete the docstrings with :param, :type, :return, :rtype, :raises annotations
6. Ensure your code passes Ruff linting

Run the tests with: pytest tests/test_defensive.py
"""

from typing import Union, Optional, List, Dict, Any


# Constants (Already defined - use these in your functions!)
MIN_AGE = 0
MAX_AGE = 150
MIN_HEIGHT = 0.5
MAX_HEIGHT = 2.5
MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 20
MIN_PASSWORD_LENGTH = 8
MIN_FEE_PERCENT = 0.0
MAX_FEE_PERCENT = 100.0
MIN_SCORE = 0
MAX_SCORE = 100


# Exercise 1: Input Validation with Type Hints
# TODO: Add proper type hints including Union
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index with input validation.
    
    BMI Formula: weight (kg) / height² (m²)
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should validate:
        - weight and height are numbers (int or float)
        - weight is positive (> 0)
        - height is positive (> 0)
        - height is in reasonable range (MIN_HEIGHT to MAX_HEIGHT)
    
    Should raise:
        - TypeError if inputs are not numbers
        - ValueError if inputs are not positive
        - ValueError if height is out of reasonable range
    
    Returns BMI rounded to 2 decimal places.
    
    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    pass


# TODO: Add proper type hints with Optional
def get_user_age(user_data):
    """
    Safely extract age from user data dictionary.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should validate:
        - user_data is a dictionary
        - 'age' key exists in dictionary
        - age value is an integer
        - age is in valid range (MIN_AGE to MAX_AGE)
    
    Should raise:
        - TypeError if user_data is not a dict
        - KeyError if 'age' key is missing
        - TypeError if age is not an integer
        - ValueError if age is out of range
    
    Returns the age if valid.
    
    Example:
        >>> get_user_age({'name': 'Alice', 'age': 30})
        30
    """
    pass


# Exercise 2: Fail Fast Pattern
# TODO: Add type hints and implement fail-fast validation
def process_transaction(amount, account_balance, transaction_fee_percent):
    """
    Process a financial transaction with fail-fast validation.
    
    Fee calculation: amount * (transaction_fee_percent / 100)
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should validate (fail fast - check in this order):
        1. All inputs are numbers
        2. amount is positive
        3. account_balance is non-negative
        4. transaction_fee_percent is between MIN_FEE_PERCENT and MAX_FEE_PERCENT
        5. account has sufficient balance (balance >= amount + fee)
    
    Should raise ValueError with specific message for each validation failure.
    
    Returns dictionary with: {'amount': X, 'fee': Y, 'total': Z, 'remaining_balance': W}
    
    Example:
        >>> process_transaction(100, 500, 2.5)
        {'amount': 100, 'fee': 2.5, 'total': 102.5, 'remaining_balance': 397.5}
    """
    pass


# Exercise 3: Type Hints with Union
# TODO: Add proper type hints with Union for multiple types
def parse_numeric_value(value):
    """
    Parse a numeric value that could be string, int, or float.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    Hint: Use Union[str, int, float] for the parameter type
    
    Should handle:
        - If value is already int or float, return as float
        - If value is string, try to convert to float
        - If conversion fails, raise ValueError with helpful message
        - If value is None or other type, raise TypeError
    
    Returns the value as a float.
    
    Example:
        >>> parse_numeric_value("42.5")
        42.5
        >>> parse_numeric_value(42)
        42.0
    """
    pass


# Exercise 4: Optional Return Type
# TODO: Add proper type hints with Optional for nullable return
def find_user_by_id(users, user_id):
    """
    Find user in list by ID, return None if not found.
    
    TODO: Add :param, :type, :return, :rtype annotations
    Hint: Return type should be Optional[Dict[str, Any]]
    
    Should validate:
        - users is a list
        - user_id is an integer
    
    Should raise:
        - TypeError if inputs are wrong type
    
    Returns user dict if found, None otherwise.
    
    Example:
        >>> users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        >>> find_user_by_id(users, 1)
        {'id': 1, 'name': 'Alice'}
        >>> find_user_by_id(users, 99)
        None
    """
    pass


# Exercise 5: Defensive Data Processing
# TODO: Add type hints and implement with defensive checks
def calculate_average_score(scores):
    """
    Calculate average score with defensive programming.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should validate:
        - scores is a list
        - scores is not empty
        - all items in scores are numbers (int or float)
        - all scores are between MIN_SCORE and MAX_SCORE
    
    Should raise appropriate errors for each validation failure.
    
    Returns average rounded to 2 decimal places.
    
    Example:
        >>> calculate_average_score([85, 90, 78, 92])
        86.25
    """
    pass


# Exercise 6: Comprehensive Validation
# TODO: Add type hints and implement with comprehensive validation
def normalize_dataset(data, feature_names):
    """
    Normalize dataset features with defensive validation.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should validate:
        - data is a list of dictionaries
        - data is not empty
        - feature_names is a list of strings
        - feature_names is not empty
        - all feature_names exist in all data dictionaries
        - all feature values are numeric
    
    Should raise appropriate errors for each validation failure.
    
    Normalize each feature to 0-1 range: (value - min) / (max - min)
    
    Returns normalized data (list of dicts).
    
    Example:
        >>> data = [{'age': 20, 'score': 50}, {'age': 40, 'score': 100}]
        >>> normalize_dataset(data, ['age', 'score'])
        [{'age': 0.0, 'score': 0.0}, {'age': 1.0, 'score': 1.0}]
    """
    pass
