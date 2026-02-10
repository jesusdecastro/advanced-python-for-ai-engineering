"""
Context Managers Exercises - Day 2.

This module contains exercises to practice working with Python context managers,
including the with statement, __enter__/__exit__ protocol, and contextlib.

Your tasks:
1. Complete the LoggingContext class with __enter__ and __exit__
2. Implement the ExecutionTimer context manager
3. Create a context manager using @contextmanager decorator
4. Implement an exception-handling context manager

Run the tests with: pytest tests/test_05_context_managers.py
"""

# TODO: Import necessary modules
# Hint: You'll need time for timing, contextlib for @contextmanager


# Exercise 1: Basic Context Manager with Class
# TODO: Complete the LoggingContext class
class LoggingContext:
    """
    Context manager that logs entry and exit of a code block.

    TODO: Add complete docstring with:
    :param name: Name of the context for logging
    :type name: str
    :ivar name: Stored context name
    :vartype name: str
    """

    def __init__(self, name):
        # TODO: Add type hint to parameter
        # TODO: Initialize name attribute
        pass

    # TODO: Implement __enter__ method
    def __enter__(self):
        """
        Enter the context and log entry message.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Print "Entering: {name}"
        # TODO: Return self
        pass

    # TODO: Implement __exit__ method
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context and log exit message.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :return, :rtype annotations
        """
        # TODO: Print "Exiting: {name}"
        # TODO: Return False to propagate exceptions
        pass


# Exercise 2: Timer Context Manager
# TODO: Complete the ExecutionTimer class
class ExecutionTimer:
    """
    Context manager that measures execution time of a code block.

    TODO: Add complete docstring with:
    :param name: Name of the operation being timed
    :type name: str
    :ivar name: Operation name
    :vartype name: str
    :ivar start_time: Start timestamp
    :vartype start_time: float
    :ivar elapsed: Elapsed time in seconds
    :vartype elapsed: float
    """

    def __init__(self, name="Operation"):
        # TODO: Add type hint to parameter
        # TODO: Initialize name attribute
        # TODO: Initialize start_time to None
        # TODO: Initialize elapsed to 0.0
        pass

    # TODO: Implement __enter__ method
    def __enter__(self):
        """
        Start the timer.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Record current time using time.time()
        # TODO: Return self
        pass

    # TODO: Implement __exit__ method
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Stop the timer and calculate elapsed time.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :return, :rtype annotations
        """
        # TODO: Calculate elapsed time (current time - start_time)
        # TODO: Store in self.elapsed
        # TODO: Return False
        pass


# Exercise 3: File Writer Context Manager with contextlib
# TODO: Implement temporary_file_writer using @contextmanager
def temporary_file_writer(filename):
    """
    Context manager that writes to a file and handles cleanup.

    TODO: Add @contextmanager decorator
    TODO: Add complete docstring with:
    :param filename: Path to file to write
    :type filename: str
    :yield: File object for writing
    :rtype: file object
    """
    # TODO: Open file in write mode
    # TODO: Yield the file object
    # TODO: In finally block, close the file
    # Hint: Use try/finally to ensure file is closed
    pass


# Exercise 4: Exception Suppressor Context Manager
# TODO: Complete the SuppressException class
class SuppressException:
    """
    Context manager that suppresses specific exception types.

    TODO: Add complete docstring with:
    :param exception_types: Exception types to suppress
    :type exception_types: tuple
    :ivar exception_types: Stored exception types
    :vartype exception_types: tuple
    """

    def __init__(self, *exception_types):
        # TODO: Store exception_types as tuple
        pass

    def __enter__(self):
        """
        Enter the context.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Return self
        pass

    # TODO: Implement __exit__ method
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit and suppress matching exceptions.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :return, :rtype annotations
        """
        # TODO: Check if exc_type is not None
        # TODO: Check if exc_type is a subclass of any exception_types
        # TODO: Return True to suppress, False otherwise
        pass


# Bonus Exercise: Temporary Attribute Context Manager
# TODO: Implement temporary_attribute using @contextmanager
def temporary_attribute(obj, attr, new_value):
    """
    Context manager that temporarily changes an object's attribute.

    TODO: Add @contextmanager decorator
    TODO: Add complete docstring with parameters
    TODO: Save old value
    TODO: Set new value
    TODO: Yield the object
    TODO: Restore old value in finally block
    """
    pass


# Bonus Exercise: Multiple Resource Manager
# TODO: Implement a context manager that manages multiple resources
class MultipleResources:
    """
    Context manager that manages multiple resources.

    TODO: Add complete docstring
    TODO: Accept list of context managers in __init__
    TODO: Enter all context managers in __enter__
    TODO: Exit all context managers in __exit__ (in reverse order)
    """

    pass
