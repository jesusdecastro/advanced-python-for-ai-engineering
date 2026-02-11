"""
Logging Practice Exercises - Day 3.

Practice configuring and using logging effectively in data/AI applications.

Your task:
1. Configure logging appropriately
2. Add logging statements at correct levels
3. Add proper type hints to all functions
4. Complete the docstrings with :param, :type, :return, :rtype annotations
5. Ensure your code passes Ruff linting

Run the tests with: pytest tests/test_logging.py
"""

import logging
from pathlib import Path
from typing import Any, List, Dict, Callable

# TODO: Import time module for performance logging


# Exercise 1: Basic Logging Setup
# TODO: Implement function to configure logging
def setup_logging(log_level, log_file):
    """
    Configure logging with specified level and output file.
    
    TODO: Add :param, :type, :return, :rtype annotations
    
    Should configure:
        - Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        - Log format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        - Output to both file and console
    
    Example:
        >>> setup_logging('INFO', 'app.log')
    """
    pass


# Exercise 2: Logging in Data Loading
# TODO: Add type hints and implement with appropriate logging
def load_dataset(filepath):
    """
    Load dataset from file with logging at each step.
    
    TODO: Add :param, :type, :return, :rtype annotations
    
    Should log:
        - INFO: Starting to load dataset (include filepath)
        - INFO: Successfully loaded dataset (include number of records)
        - ERROR: If file doesn't exist
    
    Returns list of dictionaries representing the dataset.
    
    Example:
        >>> load_dataset('data.csv')
        [{'col1': 'val1'}, {'col1': 'val2'}]
    """
    pass


# TODO: Add type hints and implement with appropriate logging
def validate_dataset(data, required_columns):
    """
    Validate dataset has required columns with logging.
    
    TODO: Add :param, :type, :return, :rtype annotations
    
    Should log:
        - INFO: Starting validation
        - ERROR: If required columns are missing (list them)
        - INFO: Validation successful
    
    Returns True if valid, False otherwise.
    
    Example:
        >>> data = [{'name': 'Alice', 'age': 30}]
        >>> validate_dataset(data, ['name', 'age'])
        True
    """
    pass


# Exercise 3: Logging in Data Processing
# TODO: Add type hints and implement with appropriate logging
def preprocess_data(data):
    """
    Preprocess data with logging.
    
    TODO: Add :param, :type, :return, :rtype annotations
    
    Should:
        - Remove rows with missing values (log WARNING with count)
        - Normalize text fields to lowercase (log INFO about normalization)
        - Log INFO with summary: rows processed, rows removed
    
    Returns preprocessed data.
    
    Example:
        >>> data = [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': None}]
        >>> preprocess_data(data)
        [{'name': 'alice', 'age': '30'}]
    """
    pass


# Exercise 4: Error Logging
# TODO: Add type hints and implement with error logging
def safe_operation_with_logging(operation, *args, **kwargs):
    """
    Execute operation with error logging.
    
    TODO: Add :param, :type, :return, :rtype annotations
    
    Should log:
        - INFO: Operation starting (include operation name)
        - INFO: Operation completed successfully
        - ERROR: If operation fails (include exception details with exc_info=True)
    
    Returns result of operation or None if it fails.
    
    Example:
        >>> safe_operation_with_logging(lambda x: x * 2, 5)
        10
    """
    pass


# Exercise 5: Performance Logging
# TODO: Add type hints and implement with performance logging
def log_function_performance(func, *args, **kwargs):
    """
    Execute function and log its performance metrics.
    
    TODO: Add :param, :type, :return, :rtype annotations
    
    Should log:
        - INFO: Function execution starting (include function name)
        - INFO: Execution time in milliseconds
        - WARNING: If execution takes more than 1 second
    
    Returns the result of the function.
    
    Example:
        >>> log_function_performance(sum, [1, 2, 3, 4, 5])
        15
    """
    pass
