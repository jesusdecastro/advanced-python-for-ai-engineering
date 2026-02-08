"""
Utility functions for regular package example.

This module is part of a regular package (with __init__.py).
"""


def greet(name: str) -> str:
    """
    Generate a greeting message.
    
    :param name: Name to greet
    :type name: str
    :return: Greeting message
    :rtype: str
    """
    return f"Hello, {name}!"


def calculate_sum(numbers: list[int]) -> int:
    """
    Calculate sum of numbers.
    
    :param numbers: List of integers
    :type numbers: list[int]
    :return: Sum of numbers
    :rtype: int
    """
    return sum(numbers)


def _internal_helper() -> str:
    """
    Internal helper function (not exported in __init__.py).
    
    :return: Helper message
    :rtype: str
    """
    return "This is an internal function"
