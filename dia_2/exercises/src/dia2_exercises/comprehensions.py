"""
Comprehensions Exercises - Day 2.

Practice list, dict, and set comprehensions.
The functions below need to be implemented using comprehensions.

Your task:
1. Implement each function using the appropriate comprehension type
2. Add proper type hints to all functions
3. Complete the docstrings with :param, :type, :return, :rtype annotations
4. Ensure your code passes Ruff linting

Run the tests with: pytest tests/test_01_comprehensions.py
"""

# TODO: Import necessary types from typing module
# Hint: You'll need List, Dict, Set


# Exercise 1: Basic List Comprehensions
# TODO: Add type hints and implement using list comprehension
def get_squares(n):
    """Generate a list of squares from 1 to n.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> get_squares(5)
        [1, 4, 9, 16, 25]
    """
    


# TODO: Add type hints and implement using list comprehension
def filter_even_numbers(numbers):
    """
    Filter only even numbers from a list.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    pass


# TODO: Add type hints and implement using list comprehension
def uppercase_strings(strings):
    """
    Convert all strings in a list to uppercase.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> uppercase_strings(['hello', 'world'])
        ['HELLO', 'WORLD']
    """
    pass


# Exercise 2: Dict Comprehensions
# TODO: Add type hints and implement using dict comprehension
def create_number_to_cube_dict(n):
    """
    Create a dictionary mapping numbers 1 to n to their cubes.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> create_number_to_cube_dict(3)
        {1: 1, 2: 8, 3: 27}
    """
    pass


# TODO: Add type hints and implement using dict comprehension
def invert_dictionary(original):
    """
    Invert a dictionary (swap keys and values).

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> invert_dictionary({'a': 1, 'b': 2})
        {1: 'a', 2: 'b'}
    """
    pass


# TODO: Add type hints and implement using dict comprehension
def filter_dict_by_value(data, threshold):
    """
    Filter dictionary to only include items where value > threshold.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> filter_dict_by_value({'a': 10, 'b': 5, 'c': 15}, 7)
        {'a': 10, 'c': 15}
    """
    pass


# Exercise 3: Set Comprehensions
# TODO: Add type hints and implement using set comprehension
def get_unique_characters(text):
    """
    Extract unique characters from a string (excluding spaces).

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> get_unique_characters('hello world')
        {'h', 'e', 'l', 'o', 'w', 'r', 'd'}
    """
    pass


# TODO: Add type hints and implement using set comprehension
def get_unique_numbers(numbers):
    """
    Get unique numbers from a list with duplicates.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> get_unique_numbers([1, 2, 2, 3, 3, 3, 4])
        {1, 2, 3, 4}
    """
    pass


# TODO: Add type hints and implement using set comprehension
def get_word_lengths(words):
    """
    Create a set of unique word lengths.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> get_word_lengths(['cat', 'dog', 'bird', 'fish'])
        {3, 4}
    """
    pass


# Exercise 4: Advanced Comprehensions
# TODO: Add type hints and implement using list comprehension
def flatten_matrix(matrix):
    """
    Flatten a 2D matrix into a 1D list.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> flatten_matrix([[1, 2], [3, 4], [5, 6]])
        [1, 2, 3, 4, 5, 6]
    """
    pass


# TODO: Add type hints and implement using dict comprehension
def word_frequency(words):
    """
    Create a dictionary with word frequencies.

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> word_frequency(['apple', 'banana', 'apple', 'cherry', 'banana', 'apple'])
        {'apple': 3, 'banana': 2, 'cherry': 1}
    """
    pass


# TODO: Add type hints and implement using list comprehension
def extract_names_from_users(users):
    """
    Extract names from a list of user dictionaries (only active users).

    TODO: Add :param, :type, :return, :rtype annotations

    Example:
        >>> users = [
        ...     {'name': 'Alice', 'active': True},
        ...     {'name': 'Bob', 'active': False},
        ...     {'name': 'Charlie', 'active': True}
        ... ]
        >>> extract_names_from_users(users)
        ['Alice', 'Charlie']
    """
    pass
