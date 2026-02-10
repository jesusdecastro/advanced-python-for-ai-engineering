"""
Tests for comprehensions exercises.

These tests validate the implementation of list, dict, and set comprehensions.
"""

import pytest
from dia2_exercises.comprehensions import (
    filter_even_numbers,
    square_numbers,
    create_name_dict,
)


def test_filter_even_numbers():
    """Test filtering even numbers using list comprehension."""
    # Test with mixed numbers
    result = filter_even_numbers([1, 2, 3, 4, 5, 6])
    assert result == [2, 4, 6]
    
    # Test with all odd numbers
    result = filter_even_numbers([1, 3, 5, 7])
    assert result == []
    
    # Test with all even numbers
    result = filter_even_numbers([2, 4, 6, 8])
    assert result == [2, 4, 6, 8]
    
    # Test with empty list
    result = filter_even_numbers([])
    assert result == []


def test_square_numbers():
    """Test squaring numbers using list comprehension."""
    # Test with positive numbers
    result = square_numbers([1, 2, 3, 4])
    assert result == [1, 4, 9, 16]
    
    # Test with negative numbers
    result = square_numbers([-2, -1, 0, 1, 2])
    assert result == [4, 1, 0, 1, 4]
    
    # Test with empty list
    result = square_numbers([])
    assert result == []


def test_create_name_dict():
    """Test creating dictionary from names using dict comprehension."""
    # Test with normal names
    names = ["Alice", "Bob", "Charlie"]
    result = create_name_dict(names)
    expected = {"Alice": 5, "Bob": 3, "Charlie": 7}
    assert result == expected
    
    # Test with empty list
    result = create_name_dict([])
    assert result == {}
    
    # Test with single name
    result = create_name_dict(["John"])
    assert result == {"John": 4}
