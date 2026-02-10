"""
Generators and Iterators Exercises - Day 2.

Practice creating generators with yield, using yield from, and processing data streams.
The functions below need to be implemented using generators.

Your task:
1. Implement each function as a generator using yield
2. Add proper type hints to all functions
3. Complete the docstrings with :param, :type, :yield, :rtype annotations
4. Ensure your code passes Ruff linting

Run the tests with: pytest tests/test_02_generators_iterators.py
"""

# TODO: Import necessary types from typing module
# Hint: You'll need Generator, Iterator, Iterable


# Exercise 1: Basic Generators with yield
# TODO: Add type hints and implement using yield
def fibonacci():
    """
    Generate Fibonacci sequence indefinitely.

    TODO: Add :yield and :rtype annotations

    Example:
        >>> fib_gen = fibonacci()
        >>> [next(fib_gen) for _ in range(10)]
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    pass


# TODO: Add type hints and implement using yield
def countdown(n):
    """
    Generate countdown from n to 1.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> list(countdown(5))
        [5, 4, 3, 2, 1]
    """
    pass


# TODO: Add type hints and implement using yield
def infinite_sequence(start):
    """
    Generate infinite sequence starting from start.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> gen = infinite_sequence(10)
        >>> [next(gen) for _ in range(5)]
        [10, 11, 12, 13, 14]
    """
    pass


# Exercise 2: Generators for Data Processing
# TODO: Add type hints and implement using yield
def chunk_data(data, chunk_size):
    """
    Split data into chunks of specified size.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> list(chunk_data([1, 2, 3, 4, 5], 2))
        [[1, 2], [3, 4], [5]]
    """
    pass


# TODO: Add type hints and implement using yield
def filter_even(numbers):
    """
    Filter only even numbers from an iterable.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> list(filter_even([1, 2, 3, 4, 5, 6]))
        [2, 4, 6]
    """
    pass


# TODO: Add type hints and implement using yield
def square_numbers(numbers):
    """
    Square each number from an iterable.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> list(square_numbers([1, 2, 3, 4]))
        [1, 4, 9, 16]
    """
    pass


# Exercise 3: yield from
# TODO: Add type hints and implement using yield from
def chain_iterables(*iterables):
    """
    Chain multiple iterables into a single generator.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> list(chain_iterables([1, 2], [3, 4], [5, 6]))
        [1, 2, 3, 4, 5, 6]
    """
    pass


# TODO: Add type hints and implement using yield from
def flatten_nested_list(nested_list):
    """
    Flatten a nested list (one level deep).

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> list(flatten_nested_list([[1, 2], [3, 4], [5]]))
        [1, 2, 3, 4, 5]
    """
    pass


# TODO: Add type hints and implement using yield from
def read_multiple_sources(sources):
    """
    Read data from multiple sources (lists) sequentially.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> sources = [['a', 'b'], ['c', 'd'], ['e']]
        >>> list(read_multiple_sources(sources))
        ['a', 'b', 'c', 'd', 'e']
    """
    pass


# Exercise 4: Streaming Data Processing
# TODO: Add type hints and implement using yield
def read_lines_stream(lines):
    """
    Stream lines one at a time (simulates file reading).

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> lines = ['line1', 'line2', 'line3']
        >>> list(read_lines_stream(lines))
        ['line1', 'line2', 'line3']
    """
    pass


# TODO: Add type hints and implement using yield
def process_csv_stream(csv_data):
    """
    Process CSV data stream and yield dictionaries.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> csv_data = [
        ...     ['name', 'age'],
        ...     ['Alice', '30'],
        ...     ['Bob', '25']
        ... ]
        >>> list(process_csv_stream(csv_data))
        [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
    """
    pass


# TODO: Add type hints and implement using yield
def running_average(numbers):
    """
    Calculate running average of numbers stream.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> list(running_average([10, 20, 30, 40]))
        [10.0, 15.0, 20.0, 25.0]
    """
    pass


# Exercise 5: Advanced Generator Patterns
# TODO: Add type hints and implement using yield
def take(iterable, n):
    """
    Take first n items from an iterable.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> list(take(range(100), 5))
        [0, 1, 2, 3, 4]
    """
    pass


# TODO: Add type hints and implement using yield
def drop(iterable, n):
    """
    Drop first n items from an iterable, yield the rest.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> list(drop(range(10), 5))
        [5, 6, 7, 8, 9]
    """
    pass


# TODO: Add type hints and implement using yield
def sliding_window(iterable, window_size):
    """
    Generate sliding windows of specified size.

    TODO: Add :param, :type, :yield, :rtype annotations

    Example:
        >>> list(sliding_window([1, 2, 3, 4, 5], 3))
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    """
    pass
