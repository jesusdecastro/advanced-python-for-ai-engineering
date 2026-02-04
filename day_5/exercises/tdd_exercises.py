"""
Test-Driven Development (TDD) Exercises - Day 5.

This module contains exercises for practicing Test-Driven Development.
You will implement functionality using the Red-Green-Refactor cycle.

Your tasks:
1. Implement ISBN-10 validator using TDD
2. Implement ShoppingCart with discount functionality using TDD
3. Implement TextAnalyzer using TDD

Remember the TDD cycle:
- RED: Write a failing test
- GREEN: Write minimal code to pass the test
- REFACTOR: Improve the code while keeping tests green

Run the tests with: pytest tests/test_02_tdd.py
"""


# Exercise 1: ISBN-10 Validator
def validate_isbn10(isbn):
    """
    Validate an ISBN-10 code.

    An ISBN-10 is valid if:
    - It has exactly 10 characters
    - First 9 characters are digits
    - Last character is a digit or 'X' (representing 10)
    - Checksum is valid: (d1*10 + d2*9 + ... + d10*1) % 11 == 0

    TODO: Add type hints
    TODO: Complete docstring with :param, :type, :return, :rtype

    Example:
        >>> validate_isbn10("0306406152")
        True
        >>> validate_isbn10("123456789X")
        False
    """
    # TODO: Implement using TDD
    # Start by writing tests first!
    pass


# Exercise 2: Shopping Cart with Discounts
class ShoppingCart:
    """
    Shopping cart with discount functionality.

    Supports:
    - Adding items with name, price, and quantity
    - Removing items
    - Calculating total
    - Applying discount codes (SAVE10 for 10%, SAVE20 for 20%)
    - Clearing cart

    TODO: Add type hints to all methods
    """

    def __init__(self):
        """Initialize an empty shopping cart."""
        # TODO: Implement using TDD
        pass

    def add_item(self, name, price, quantity=1):
        """
        Add an item to the cart.

        TODO: Add parameter documentation
        TODO: Implement using TDD
        """
        pass

    def remove_item(self, name):
        """
        Remove an item from the cart by name.

        TODO: Add parameter documentation
        TODO: Implement using TDD
        """
        pass

    def total(self):
        """
        Calculate total cart value before discount.

        TODO: Add return documentation
        TODO: Implement using TDD
        """
        pass

    def apply_discount(self, code):
        """
        Apply a discount code to the cart.

        Valid codes:
        - "SAVE10": 10% discount
        - "SAVE20": 20% discount

        TODO: Add parameter and return documentation
        TODO: Implement using TDD
        """
        pass

    def total_with_discount(self):
        """
        Calculate total cart value after discount.

        TODO: Add return documentation
        TODO: Implement using TDD
        """
        pass

    def clear(self):
        """
        Clear all items from the cart.

        TODO: Implement using TDD
        """
        pass


# Exercise 3: Text Analyzer
class TextAnalyzer:
    """
    Analyze text and calculate statistics.

    Provides:
    - Word count
    - Sentence count
    - Most frequent word
    - Average word length
    - Readability score (average words per sentence)

    TODO: Add type hints to all methods
    """

    def __init__(self, text):
        """
        Initialize the TextAnalyzer with text.

        TODO: Add parameter documentation
        TODO: Implement using TDD
        """
        pass

    def word_count(self):
        """
        Count the number of words in the text.

        TODO: Add return documentation
        TODO: Implement using TDD
        """
        pass

    def sentence_count(self):
        """
        Count the number of sentences in the text.

        Sentences end with '.', '!', or '?'

        TODO: Add return documentation
        TODO: Implement using TDD
        """
        pass

    def most_frequent_word(self):
        """
        Find the most frequently occurring word.

        Case-insensitive comparison.
        Ignores punctuation.

        TODO: Add return documentation
        TODO: Implement using TDD
        """
        pass

    def average_word_length(self):
        """
        Calculate the average length of words.

        TODO: Add return documentation
        TODO: Implement using TDD
        """
        pass

    def readability_score(self):
        """
        Calculate readability score as average words per sentence.

        TODO: Add return documentation
        TODO: Implement using TDD
        """
        pass
