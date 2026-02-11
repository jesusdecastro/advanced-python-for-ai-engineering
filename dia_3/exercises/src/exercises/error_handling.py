"""
Error Handling Exercises - Day 3.

Practice proper exception handling, custom exceptions, and error recovery.

Your task:
1. Implement proper try-except blocks
2. Handle specific exceptions appropriately
3. Add proper type hints to all functions
4. Complete the docstrings with :param, :type, :return, :rtype, :raises annotations
5. Ensure your code passes Ruff linting

Run the tests with: pytest tests/test_error_handling.py
"""

from typing import Union, Optional, Dict, Any
import json

# TODO: Import Path from pathlib


# Exercise 1: Basic Exception Handling
# TODO: Add type hints and implement with exception handling
def divide_safely(a, b):
    """
    Divide two numbers with proper exception handling.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should handle:
        - ZeroDivisionError: Return None and don't raise
        - TypeError: If inputs are not numbers, raise TypeError with message
    
    Returns result of division or None if division by zero.
    
    Example:
        >>> divide_safely(10, 2)
        5.0
        >>> divide_safely(10, 0)
        None
    """
    pass


# TODO: Add type hints and implement with exception handling
def parse_config_file(filepath):
    """
    Parse a JSON config file with error handling.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should handle:
        - FileNotFoundError: Raise with message "Config file not found: {filepath}"
        - json.JSONDecodeError: Raise ValueError with message "Invalid JSON in config file"
    
    Returns parsed JSON as dictionary.
    
    Example:
        >>> parse_config_file('config.json')
        {'setting': 'value'}
    """
    pass


# Exercise 2: Multiple Exception Handling
# TODO: Add type hints and implement with multiple exception handling
def fetch_data_from_api(url, timeout):
    """
    Simulate fetching data from an API with error handling.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should validate:
        - Timeout must be positive: Raise ValueError "Timeout must be positive"
        - URL must start with http: Raise ValueError "Invalid URL"
    
    Returns dictionary with 'data' key if successful.
    
    Example:
        >>> fetch_data_from_api('https://api.example.com', 5)
        {'data': 'success'}
    """
    pass


# TODO: Add type hints and implement with exception handling
def process_user_input(user_input):
    """
    Process user input with validation and error handling.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should validate:
        - Input must be a string: Raise TypeError "Input must be a string"
        - Input cannot be empty or only whitespace: Raise ValueError "Input cannot be empty"
    
    Returns processed input (stripped and lowercased).
    
    Example:
        >>> process_user_input("  Hello World  ")
        'hello world'
    """
    pass
