"""
Magic Methods Exercises - Day 2.

This module contains exercises to practice working with Python magic methods
(dunder methods), including __str__, __repr__, __eq__, __lt__, __len__,
__getitem__, __iter__, and __next__.

Your tasks:
1. Complete the Book class with __str__ and __repr__
2. Implement comparison methods for Student class
3. Create a Library container class with __len__, __getitem__, __contains__
4. Implement an EvenNumbers iterator with __iter__ and __next__

Run the tests with: pytest tests/test_06_magic_methods.py
"""

# TODO: Import necessary modules
# Hint: You'll need functools for @total_ordering


# Exercise 1: String Representation with __str__ and __repr__
# TODO: Complete the Book class
class Book:
    """
    Represent a book with title, author, and year.

    TODO: Add complete docstring with:
    :param title: Book title
    :type title: str
    :param author: Book author
    :type author: str
    :param year: Publication year
    :type year: int
    :ivar title: Stored book title
    :vartype title: str
    :ivar author: Stored book author
    :vartype author: str
    :ivar year: Stored publication year
    :vartype year: int
    """

    def __init__(self, title, author, year):
        # TODO: Add type hints to parameters
        # TODO: Initialize title, author, year attributes
        pass

    # TODO: Implement __str__ method
    def __str__(self):
        """
        Return user-friendly string representation.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Return format: "Title by Author (Year)"
        # Example: "1984 by George Orwell (1949)"
        pass

    # TODO: Implement __repr__ method
    def __repr__(self):
        """
        Return developer-friendly string representation.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Return format: "Book('Title', 'Author', Year)"
        # Example: "Book('1984', 'George Orwell', 1949)"
        # This should be evaluable (can recreate the object)
        pass


# Exercise 2: Comparison Methods with @total_ordering
# TODO: Add @total_ordering decorator
# TODO: Complete the Student class
class Student:
    """
    Represent a student with name and grade.

    TODO: Add complete docstring with:
    :param name: Student name
    :type name: str
    :param grade: Student grade (0-100)
    :type grade: float
    :ivar name: Stored student name
    :vartype name: str
    :ivar grade: Stored student grade
    :vartype grade: float
    """

    def __init__(self, name, grade):
        # TODO: Add type hints to parameters
        # TODO: Initialize name and grade attributes
        pass

    # TODO: Implement __eq__ method
    def __eq__(self, other):
        """
        Check equality based on name and grade.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :return, :rtype annotations
        """
        # TODO: Check if other is a Student instance
        # TODO: Return NotImplemented if not
        # TODO: Compare both name and grade
        pass

    # TODO: Implement __lt__ method
    def __lt__(self, other):
        """
        Compare students by grade for sorting.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :return, :rtype annotations
        """
        # TODO: Check if other is a Student instance
        # TODO: Return NotImplemented if not
        # TODO: Compare by grade (lower grade = less than)
        pass

    # TODO: Implement __repr__ method
    def __repr__(self):
        """
        Return string representation.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Return format: "Student('Name', Grade)"
        pass


# Exercise 3: Container Methods - __len__, __getitem__, __contains__
# TODO: Complete the Library class
class Library:
    """
    Represent a library that stores books.

    TODO: Add complete docstring with:
    :param name: Library name
    :type name: str
    :ivar name: Stored library name
    :vartype name: str
    :ivar books: List of books in library
    :vartype books: list
    """

    def __init__(self, name):
        # TODO: Add type hint to parameter
        # TODO: Initialize name attribute
        # TODO: Initialize empty books list
        pass

    def add_book(self, book):
        """
        Add a book to the library.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :return, :rtype annotations
        """
        # TODO: Append book to books list
        pass

    # TODO: Implement __len__ method
    def __len__(self):
        """
        Return number of books in library.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Return length of books list
        pass

    # TODO: Implement __getitem__ method
    def __getitem__(self, index):
        """
        Get book at index.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :return, :rtype annotations
        """
        # TODO: Return book at given index from books list
        pass

    # TODO: Implement __contains__ method
    def __contains__(self, book):
        """
        Check if book is in library.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :return, :rtype annotations
        """
        # TODO: Return True if book is in books list
        pass

    # TODO: Implement __repr__ method
    def __repr__(self):
        """
        Return string representation.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Return format: "Library('Name', X books)"
        pass


# Exercise 4: Iterator Protocol - __iter__ and __next__
# TODO: Complete the EvenNumbers class
class EvenNumbers:
    """
    Iterator that generates even numbers up to a maximum.

    TODO: Add complete docstring with:
    :param max_value: Maximum value (inclusive)
    :type max_value: int
    :ivar max_value: Stored maximum value
    :vartype max_value: int
    :ivar current: Current value in iteration
    :vartype current: int
    """

    def __init__(self, max_value):
        # TODO: Add type hint to parameter
        # TODO: Initialize max_value attribute
        # TODO: Initialize current to 0
        pass

    # TODO: Implement __iter__ method
    def __iter__(self):
        """
        Return the iterator object (self).

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Reset current to 0
        # TODO: Return self
        pass

    # TODO: Implement __next__ method
    def __next__(self):
        """
        Return the next even number.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        TODO: Add :raises StopIteration: When no more even numbers
        """
        # TODO: Check if current > max_value
        # TODO: If so, raise StopIteration
        # TODO: Store current value
        # TODO: Increment current by 2
        # TODO: Return stored value
        pass


# Bonus Exercise: Callable Object with __call__
# TODO: Complete the Multiplier class
class Multiplier:
    """
    Callable object that multiplies by a factor.

    TODO: Add complete docstring with:
    :param factor: Multiplication factor
    :type factor: float
    :ivar factor: Stored multiplication factor
    :vartype factor: float
    """

    def __init__(self, factor):
        # TODO: Add type hint to parameter
        # TODO: Initialize factor attribute
        pass

    # TODO: Implement __call__ method
    def __call__(self, value):
        """
        Multiply value by factor.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :return, :rtype annotations
        """
        # TODO: Return value * factor
        pass


# Bonus Exercise: Boolean Context with __bool__
# TODO: Complete the ShoppingCart class
class ShoppingCart:
    """
    Represent a shopping cart.

    TODO: Add complete docstring
    :ivar items: List of items in cart
    :vartype items: list
    """

    def __init__(self):
        # TODO: Initialize empty items list
        pass

    def add_item(self, item):
        """
        Add item to cart.

        TODO: Add parameter and return type annotations
        TODO: Add :param, :type, :return, :rtype annotations
        """
        # TODO: Append item to items list
        pass

    # TODO: Implement __bool__ method
    def __bool__(self):
        """
        Cart is truthy if it has items.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Return True if items list is not empty
        pass

    # TODO: Implement __len__ method
    def __len__(self):
        """
        Return number of items in cart.

        TODO: Add return type annotation
        TODO: Add :return, :rtype annotations
        """
        # TODO: Return length of items list
        pass
