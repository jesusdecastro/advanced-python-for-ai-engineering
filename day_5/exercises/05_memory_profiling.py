"""
Memory Profiling Exercises - Day 5

This module contains exercises for practicing memory optimization techniques,
including dtype selection, generator usage, and memory-efficient data processing.

Your task:
1. Choose appropriate dtypes to minimize memory usage
2. Convert list comprehensions to generators
3. Implement chunked data processing
4. Measure and compare memory usage

Run the tests with: pytest tests/test_05_memory_profiling.py
"""

import numpy as np
import sys


# Exercise 1: Optimize array dtypes
def create_optimized_arrays(ages, scores, ids):
    """
    Create NumPy arrays with optimized dtypes.
    
    Given lists of ages (0-120), scores (0-100), and ids (0-1000000),
    create NumPy arrays with the smallest appropriate dtype for each.
    
    TODO: Add type hints
    TODO: Complete the docstring with :param, :type, :return, :rtype
    
    Example:
        >>> ages = [25, 30, 35]
        >>> scores = [85, 90, 78]
        >>> ids = [1001, 1002, 1003]
        >>> result = create_optimized_arrays(ages, scores, ids)
        >>> result['ages'].dtype
        dtype('int8')
    """
    # TODO: Create arrays with appropriate dtypes
    # Hint: ages fit in int8, scores fit in int8, ids need int32
    pass


# Exercise 2: Generator for squares
def squares_generator(n):
    """
    Generate squares of numbers from 0 to n-1 using a generator.
    
    This should yield values one at a time instead of creating a list.
    
    TODO: Add type hints
    TODO: Complete the docstring
    
    Example:
        >>> gen = squares_generator(5)
        >>> list(gen)
        [0, 1, 4, 9, 16]
    """
    # TODO: Implement generator
    # Hint: Use yield instead of return
    pass


# Exercise 3: Process data in chunks
def process_large_list_in_chunks(data, chunk_size=1000):
    """
    Process a large list in chunks to save memory.
    
    Calculate the sum of squares of all numbers, processing chunk_size
    elements at a time instead of creating a full list of squares.
    
    TODO: Add type hints
    TODO: Complete the docstring
    
    Example:
        >>> data = range(10000)
        >>> result = process_large_list_in_chunks(data, chunk_size=1000)
        >>> result == sum(x**2 for x in range(10000))
        True
    """
    # TODO: Implement chunked processing
    # Hint: Process data in slices of chunk_size
    pass


# Exercise 4: Memory-efficient filtering
def filter_large_dataset(data, threshold):
    """
    Filter a large dataset using a generator to save memory.
    
    Return a generator that yields only values greater than threshold.
    
    TODO: Add type hints
    TODO: Complete the docstring
    
    Example:
        >>> data = [1, 5, 3, 8, 2, 9, 4]
        >>> result = list(filter_large_dataset(data, 4))
        >>> result
        [5, 8, 9]
    """
    # TODO: Implement generator-based filtering
    # Hint: Use yield with a condition
    pass


# Exercise 5: Compare memory usage
def compare_list_vs_generator(n):
    """
    Compare memory usage of list comprehension vs generator expression.
    
    Return a dictionary with 'list_size' and 'generator_size' in bytes.
    
    TODO: Add type hints
    TODO: Complete the docstring
    
    Example:
        >>> result = compare_list_vs_generator(1000)
        >>> result['list_size'] > result['generator_size']
        True
    """
    # TODO: Create list and generator, measure sizes
    # Hint: Use sys.getsizeof()
    pass
