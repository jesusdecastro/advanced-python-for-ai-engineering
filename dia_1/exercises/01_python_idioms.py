"""
Exercises for Python Idioms - Day 1.

Complete the functions below to practice comprehensions, generators,
context managers, and decorators.
"""

from typing import Dict, List, Iterator, Any, Callable
import time


# ============================================================================
# EXERCISE 1: List Comprehensions
# ============================================================================

def square_evens(numbers: List[int]) -> List[int]:
    """
    Return a list of squares of even numbers only.
    
    Use list comprehension with filtering.
    
    :param numbers: List of integers
    :type numbers: List[int]
    :return: List of squares of even numbers
    :rtype: List[int]
    
    Example:
        >>> square_evens([1, 2, 3, 4, 5, 6])
        [4, 16, 36]
    
    Tests to pass:
        - Basic case: [1, 2, 3, 4, 5, 6] should return [4, 16, 36]
        - All odd numbers: [1, 3, 5, 7] should return empty list
        - All even numbers: [2, 4, 6] should return [4, 16, 36]
        - Empty list: [] should return empty list
    """
    # TODO: Implement using list comprehension
    pass


def transform_strings(words: List[str]) -> List[str]:
    """
    Transform list of strings to uppercase, only words longer than 3 chars.
    
    :param words: List of strings
    :type words: List[str]
    :return: List of uppercase strings (length > 3)
    :rtype: List[str]
    
    Example:
        >>> transform_strings(['hi', 'python', 'is', 'great'])
        ['PYTHON', 'GREAT']
    
    Tests to pass:
        - Basic case: ['hi', 'python', 'is', 'great'] should return ['PYTHON', 'GREAT']
        - All short words: ['hi', 'is', 'ok'] should return empty list
        - All long words: ['python', 'java', 'rust'] should return ['PYTHON', 'JAVA', 'RUST']
    """
    # TODO: Implement using list comprehension
    pass


# ============================================================================
# EXERCISE 2: Dict Comprehensions
# ============================================================================

def word_lengths(words: List[str]) -> Dict[str, int]:
    """
    Create a dictionary mapping words to their lengths.
    
    :param words: List of words
    :type words: List[str]
    :return: Dictionary of word -> length
    :rtype: Dict[str, int]
    
    Example:
        >>> word_lengths(['python', 'is', 'awesome'])
        {'python': 6, 'is': 2, 'awesome': 7}
    
    Tests to pass:
        - Basic case: ['python', 'is', 'awesome'] should return {'python': 6, 'is': 2, 'awesome': 7}
        - Empty list: [] should return empty dict
        - Single word: ['hello'] should return {'hello': 5}
    """
    # TODO: Implement using dict comprehension
    pass


def invert_dict(data: Dict[str, int]) -> Dict[int, str]:
    """
    Invert a dictionary (swap keys and values).
    
    :param data: Original dictionary
    :type data: Dict[str, int]
    :return: Inverted dictionary
    :rtype: Dict[int, str]
    
    Example:
        >>> invert_dict({'a': 1, 'b': 2, 'c': 3})
        {1: 'a', 2: 'b', 3: 'c'}
    
    Tests to pass:
        - Basic case: {'a': 1, 'b': 2, 'c': 3} should return {1: 'a', 2: 'b', 3: 'c'}
        - Empty dict: {} should return empty dict
    """
    # TODO: Implement using dict comprehension
    pass


def filter_dict_by_value(data: Dict[str, int], threshold: int) -> Dict[str, int]:
    """
    Filter dictionary to only include items where value > threshold.
    
    :param data: Original dictionary
    :type data: Dict[str, int]
    :param threshold: Minimum value to include
    :type threshold: int
    :return: Filtered dictionary
    :rtype: Dict[str, int]
    
    Example:
        >>> filter_dict_by_value({'a': 10, 'b': 5, 'c': 20}, 8)
        {'a': 10, 'c': 20}
    
    Tests to pass:
        - Basic case: {'a': 10, 'b': 5, 'c': 20} with threshold 8 should return {'a': 10, 'c': 20}
        - No values pass: {'a': 1, 'b': 2} with threshold 10 should return empty dict
        - All values pass: {'a': 10, 'b': 20} with threshold 5 should return {'a': 10, 'b': 20}
    """
    # TODO: Implement using dict comprehension
    pass


# ============================================================================
# EXERCISE 3: Generators
# ============================================================================

def countdown(n: int) -> Iterator[int]:
    """
    Generator that counts down from n to 1.
    
    :param n: Starting number
    :type n: int
    :yield: Numbers from n down to 1
    :rtype: Iterator[int]
    
    Example:
        >>> list(countdown(5))
        [5, 4, 3, 2, 1]
    
    Tests to pass:
        - Basic case: countdown(5) should yield [5, 4, 3, 2, 1]
        - Single number: countdown(1) should yield [1]
        - Zero: countdown(0) should yield nothing (empty)
        - Must return a generator (has __iter__ and __next__ methods)
    """
    # TODO: Implement using yield
    pass


def even_numbers(start: int, end: int) -> Iterator[int]:
    """
    Generator that yields even numbers in range [start, end).
    
    :param start: Start of range (inclusive)
    :type start: int
    :param end: End of range (exclusive)
    :type end: int
    :yield: Even numbers in range
    :rtype: Iterator[int]
    
    Example:
        >>> list(even_numbers(1, 10))
        [2, 4, 6, 8]
    
    Tests to pass:
        - Basic case: even_numbers(1, 10) should yield [2, 4, 6, 8]
        - Start with even: even_numbers(2, 8) should yield [2, 4, 6]
        - Empty range: even_numbers(5, 5) should yield nothing
    """
    # TODO: Implement using yield
    pass


def fibonacci_generator(n: int) -> Iterator[int]:
    """
    Generator that yields first n Fibonacci numbers.
    
    :param n: Number of Fibonacci numbers to generate
    :type n: int
    :yield: Fibonacci numbers
    :rtype: Iterator[int]
    
    Example:
        >>> list(fibonacci_generator(7))
        [0, 1, 1, 2, 3, 5, 8]
    
    Tests to pass:
        - Basic case: fibonacci_generator(7) should yield [0, 1, 1, 2, 3, 5, 8]
        - First two: fibonacci_generator(2) should yield [0, 1]
        - Zero: fibonacci_generator(0) should yield nothing
    """
    # TODO: Implement using yield
    pass


# ============================================================================
# EXERCISE 4: Context Managers
# ============================================================================

class Timer:
    """
    Context manager to measure execution time.
    
    Example:
        >>> with Timer() as t:
        ...     time.sleep(0.1)
        >>> t.elapsed > 0.1
        True
    
    Tests to pass:
        - Must measure elapsed time correctly (elapsed >= actual time)
        - Must set start and end times (both not None after use)
        - Must work even if exception occurs inside context
        - elapsed attribute must be set after exiting context
    """
    
    def __init__(self):
        """Initialize timer."""
        self.start = None
        self.end = None
        self.elapsed = None
    
    def __enter__(self):
        """Start timer when entering context."""
        # TODO: Implement __enter__
        # Hint: Record start time and return self
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop timer when exiting context."""
        # TODO: Implement __exit__
        # Hint: Record end time and calculate elapsed
        pass


class FileWriter:
    """
    Context manager for safe file writing.
    
    Ensures file is closed even if error occurs.
    
    Example:
        >>> with FileWriter('test.txt') as f:
        ...     f.write('Hello')
    
    Tests to pass:
        - Must create and write to file successfully
        - Must close file after exiting context (file.closed == True)
        - Must close file even if exception occurs inside context
        - The returned object from __enter__ must have a write() method
    """
    
    def __init__(self, filename: str):
        """
        Initialize file writer.
        
        :param filename: Path to file
        :type filename: str
        """
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        """Open file when entering context."""
        # TODO: Implement __enter__
        # Hint: Open file in write mode and return the file object
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close file when exiting context."""
        # TODO: Implement __exit__
        # Hint: Close the file if it's open
        pass


# ============================================================================
# EXERCISE 5: Decorators
# ============================================================================

def uppercase_decorator(func: Callable) -> Callable:
    """
    Decorator that converts function's string return value to uppercase.
    
    :param func: Function to decorate
    :type func: Callable
    :return: Decorated function
    :rtype: Callable
    
    Example:
        >>> @uppercase_decorator
        ... def greet(name):
        ...     return f"hello {name}"
        >>> greet("world")
        'HELLO WORLD'
    
    Tests to pass:
        - Basic case: function returning "hello world" should return "HELLO WORLD"
        - Already uppercase: function returning "LOUD" should return "LOUD"
        - Must preserve function arguments and calling behavior
    """
    # TODO: Implement decorator
    # Hint: Create wrapper function that calls original and converts result to uppercase
    pass


def repeat(times: int) -> Callable:
    """
    Decorator that repeats function execution n times.
    
    :param times: Number of times to repeat
    :type times: int
    :return: Decorator function
    :rtype: Callable
    
    Example:
        >>> @repeat(3)
        ... def say_hello():
        ...     print("Hello")
        >>> say_hello()
        Hello
        Hello
        Hello
    
    Tests to pass:
        - With times=3: function should execute 3 times
        - With times=1: function should execute 1 time
        - Must preserve function arguments
        - This is a decorator factory (returns a decorator)
    """
    # TODO: Implement decorator with parameter
    # Hint: This needs two levels of nesting (decorator factory pattern)
    pass


def validate_positive(func: Callable) -> Callable:
    """
    Decorator that validates all numeric arguments are positive.
    
    Raises ValueError if any argument is negative or zero.
    
    :param func: Function to decorate
    :type func: Callable
    :return: Decorated function
    :rtype: Callable
    :raises ValueError: If any argument is not positive
    
    Example:
        >>> @validate_positive
        ... def add(a, b):
        ...     return a + b
        >>> add(5, 3)
        8
        >>> add(-1, 3)
        Traceback (most recent call last):
        ...
        ValueError: All arguments must be positive
    
    Tests to pass:
        - Valid positive args: add(5, 3) should return 8
        - Negative arg: add(-1, 3) should raise ValueError with "positive" in message
        - Zero arg: multiply(0, 5) should raise ValueError with "positive" in message
        - Must check all numeric arguments (int and float)
    """
    # TODO: Implement decorator with validation
    # Hint: Check if arguments are numeric and > 0 before calling function
    pass


# ============================================================================
# EXERCISE 6: Combined Challenge
# ============================================================================

def process_sales_data(sales: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Process sales data using comprehensions.
    
    Calculate:
    - Total revenue per product (price * quantity)
    - Products with revenue > 1000
    - Total revenue across all products
    
    :param sales: List of sale dictionaries with 'product', 'price', 'quantity'
    :type sales: List[Dict[str, Any]]
    :return: Dictionary with 'revenues', 'high_revenue', 'total'
    :rtype: Dict[str, Any]
    
    Example:
        >>> sales = [
        ...     {'product': 'A', 'price': 100, 'quantity': 5},
        ...     {'product': 'B', 'price': 50, 'quantity': 10}
        ... ]
        >>> result = process_sales_data(sales)
        >>> result['total']
        1000
    
    Tests to pass:
        - Must return dict with keys: 'revenues', 'high_revenue', 'total'
        - 'revenues': dict mapping product -> revenue (price * quantity)
        - 'high_revenue': dict with only products where revenue > 1000
        - 'total': sum of all revenues
        - Empty sales list should return empty dicts and total=0
    """
    # TODO: Implement using comprehensions
    # Return dict with keys: 'revenues', 'high_revenue', 'total'
    pass


def batch_generator(items: List[Any], batch_size: int) -> Iterator[List[Any]]:
    """
    Generator that yields items in batches.
    
    :param items: List of items to batch
    :type items: List[Any]
    :param batch_size: Size of each batch
    :type batch_size: int
    :yield: Batches of items
    :rtype: Iterator[List[Any]]
    
    Example:
        >>> list(batch_generator([1, 2, 3, 4, 5], 2))
        [[1, 2], [3, 4], [5]]
    
    Tests to pass:
        - Basic case: [1,2,3,4,5] with batch_size=2 should yield [[1,2], [3,4], [5]]
        - Exact batches: [1,2,3,4] with batch_size=2 should yield [[1,2], [3,4]]
        - Single batch: [1,2,3] with batch_size=5 should yield [[1,2,3]]
        - Empty list: [] should yield nothing
        - Must return a generator (has __iter__ and __next__ methods)
    """
    # TODO: Implement generator that yields batches
    # Hint: Use slicing with range(0, len(items), batch_size)
    pass
