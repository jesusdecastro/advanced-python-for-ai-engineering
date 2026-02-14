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



# Exercise 3: Custom Exception Classes
# TODO: Create custom exception class
class DataValidationError(Exception):
    """
    Custom exception for data validation errors.
    
    TODO: Add docstring explaining when to use this exception
    TODO: Add __init__ method that accepts message and optional data_info dict
    
    Example:
        >>> raise DataValidationError("Invalid data", {"row": 5, "column": "age"})
    """
    pass


# TODO: Create custom exception class
class ModelTrainingError(Exception):
    """
    Custom exception for model training errors.
    
    TODO: Add docstring
    TODO: Add __init__ method that accepts message, model_name, and optional error_details
    
    Example:
        >>> raise ModelTrainingError("Training failed", "RandomForest", {"epoch": 10})
    """
    pass


# TODO: Add type hints and implement with custom exceptions
def validate_training_data(data, required_columns):
    """
    Validate training data with custom exceptions.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should validate:
        - data is a list of dictionaries
        - data is not empty
        - all required_columns exist in all dictionaries
        - raise DataValidationError with details if validation fails
    
    Returns True if valid.
    
    Example:
        >>> data = [{'age': 30, 'income': 50000}]
        >>> validate_training_data(data, ['age', 'income'])
        True
    """
    pass


# Exercise 4: Context Managers for Error Handling
# TODO: Implement function using context manager
def safe_file_operation(filepath, operation):
    """
    Perform file operation with proper error handling.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should:
        - Use 'with' statement for file handling
        - Handle FileNotFoundError: raise with message "File not found: {filepath}"
        - Handle PermissionError: raise with message "Permission denied: {filepath}"
        - Handle IOError: raise with message "IO error reading: {filepath}"
        - operation is a callable that receives file object
    
    Returns result of operation.
    
    Example:
        >>> def read_first_line(f):
        ...     return f.readline().strip()
        >>> safe_file_operation('test.txt', read_first_line)
        'First line content'
    """
    pass


# Exercise 5: Exception Chaining
# TODO: Add type hints and implement with exception chaining
def load_and_process_config(config_path):
    """
    Load and process configuration with exception chaining.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should:
        - Try to load JSON from config_path
        - If FileNotFoundError, raise ValueError with "Config not found" and chain original
        - If JSONDecodeError, raise ValueError with "Invalid config format" and chain original
        - Process config (validate it has 'model' and 'params' keys)
        - If validation fails, raise ValueError with "Invalid config structure"
    
    Use 'raise ... from ...' for exception chaining.
    
    Returns processed config dict.
    
    Example:
        >>> load_and_process_config('config.json')
        {'model': 'rf', 'params': {'n_estimators': 100}}
    """
    pass


# Exercise 6: Finally Block Usage
# TODO: Add type hints and implement with finally block
def process_data_with_cleanup(data, temp_file_path):
    """
    Process data with guaranteed cleanup.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should:
        - Write data to temp_file_path
        - Process the data (simulate with some transformation)
        - Use finally block to ensure temp file is deleted
        - Return processed data
        - Temp file should be deleted even if processing fails
    
    Example:
        >>> data = [1, 2, 3, 4, 5]
        >>> process_data_with_cleanup(data, 'temp.txt')
        [2, 4, 6, 8, 10]
    """
    pass


# Exercise 7: Multiple Exception Types
# TODO: Add type hints and implement handling multiple exception types
def robust_data_loader(file_path, file_format):
    """
    Load data from file with robust error handling.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should handle:
        - FileNotFoundError: Return empty list with warning message
        - PermissionError: Raise with message "Cannot access file: {file_path}"
        - ValueError (for invalid format): Raise with message "Unsupported format: {file_format}"
        - Any other exception: Log error and re-raise
    
    Supported formats: 'csv', 'json'
    
    Returns list of data records.
    
    Example:
        >>> robust_data_loader('data.csv', 'csv')
        [{'col1': 'val1'}, {'col1': 'val2'}]
    """
    pass


# Exercise 8: Assertion vs Exception
# TODO: Implement function using both assertions and exceptions appropriately
def calculate_model_score(predictions, labels, model_type):
    """
    Calculate model score with appropriate error handling.
    
    TODO: Add :param, :type, :return, :rtype, :raises annotations
    
    Should:
        - Use exceptions for input validation (user-provided data)
        - Use assertions for internal invariants (things that should never happen)
        - Validate predictions and labels are lists
        - Validate they have same length (exception)
        - Validate model_type is in ['classification', 'regression']
        - Assert score is between 0 and 1 (internal invariant)
    
    Returns accuracy score (correct predictions / total).
    
    Example:
        >>> calculate_model_score([1, 0, 1], [1, 0, 1], 'classification')
        1.0
    """
    pass
