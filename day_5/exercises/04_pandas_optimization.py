"""
pandas Optimization Exercises - Day 5

This module contains exercises for practicing pandas optimization techniques,
including dtype optimization, categorical data, and vectorized operations.

Your task:
1. Optimize DataFrame dtypes to reduce memory usage
2. Convert appropriate columns to categorical dtype
3. Implement vectorized operations instead of loops
4. Measure and compare memory usage

Run the tests with: pytest tests/test_04_pandas_optimization.py
"""

import pandas as pd
import numpy as np


# Exercise 1: Optimize DataFrame dtypes
def optimize_dataframe_dtypes(df):
    """
    Optimize DataFrame dtypes to reduce memory usage.
    
    Convert integer columns to the smallest possible dtype (int8, int16, int32)
    based on the range of values. Convert float64 to float32 where appropriate.
    
    TODO: Add type hints for parameters and return value
    TODO: Complete the docstring with :param, :type, :return, :rtype
    
    Example:
        >>> df = pd.DataFrame({'age': [25, 30, 35], 'score': [85.5, 90.2, 78.8]})
        >>> optimized = optimize_dataframe_dtypes(df)
        >>> optimized['age'].dtype
        dtype('int8')
    """
    # TODO: Implement dtype optimization
    # Hint: Check min/max values and use np.iinfo() for integer ranges
    pass


# Exercise 2: Convert to categorical
def convert_to_categorical(df, threshold=0.5):
    """
    Convert object columns to categorical if they have low cardinality.
    
    A column should be converted to categorical if the ratio of unique values
    to total values is less than the threshold.
    
    TODO: Add type hints
    TODO: Complete the docstring
    
    Example:
        >>> df = pd.DataFrame({'country': ['USA', 'Canada', 'USA', 'Mexico']})
        >>> result = convert_to_categorical(df, threshold=0.5)
        >>> result['country'].dtype.name
        'category'
    """
    # TODO: Implement categorical conversion
    # Hint: Use nunique() and len() to calculate cardinality ratio
    pass


# Exercise 3: Vectorized price calculation
def calculate_final_prices(df):
    """
    Calculate final prices using vectorized operations.
    
    Given a DataFrame with 'price', 'quantity', and 'discount' columns,
    calculate the final price as: price * quantity * (1 - discount)
    
    TODO: Add type hints
    TODO: Complete the docstring
    
    Example:
        >>> df = pd.DataFrame({
        ...     'price': [100, 200],
        ...     'quantity': [2, 1],
        ...     'discount': [0.1, 0.2]
        ... })
        >>> result = calculate_final_prices(df)
        >>> result['final_price'].tolist()
        [180.0, 160.0]
    """
    # TODO: Implement vectorized calculation
    # Hint: Use pandas column operations, avoid loops
    pass


# Exercise 4: Memory usage comparison
def compare_memory_usage(df_original, df_optimized):
    """
    Compare memory usage between original and optimized DataFrames.
    
    Return a dictionary with 'original_mb', 'optimized_mb', and 'reduction_percent'.
    
    TODO: Add type hints
    TODO: Complete the docstring
    
    Example:
        >>> df1 = pd.DataFrame({'a': [1, 2, 3]})
        >>> df2 = pd.DataFrame({'a': pd.array([1, 2, 3], dtype='int8')})
        >>> result = compare_memory_usage(df1, df2)
        >>> 'reduction_percent' in result
        True
    """
    # TODO: Implement memory comparison
    # Hint: Use memory_usage(deep=True).sum() and convert to MB
    pass


# Exercise 5: Vectorized conditional operation
def categorize_scores(df, score_column='score'):
    """
    Categorize scores into 'low', 'medium', 'high' using vectorized operations.
    
    Rules:
    - score < 60: 'low'
    - 60 <= score < 80: 'medium'
    - score >= 80: 'high'
    
    TODO: Add type hints
    TODO: Complete the docstring
    
    Example:
        >>> df = pd.DataFrame({'score': [45, 70, 85, 92]})
        >>> result = categorize_scores(df)
        >>> result['category'].tolist()
        ['low', 'medium', 'high', 'high']
    """
    # TODO: Implement vectorized categorization
    # Hint: Use np.where() or pd.cut()
    pass
