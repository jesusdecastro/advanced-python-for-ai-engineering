"""
Objects vs Data Structures Exercises - Day 4

This module contains exercises to practice distinguishing between objects
and data structures, and implementing each appropriately.

Your task:
1. Complete the Temperature class with proper encapsulation
2. Create a Book dataclass for library data
3. Implement a Library class with book management behavior
4. Refactor the ShoppingCart to use proper encapsulation

Run the tests with: pytest tests/test_01_objects_vs_data_structures.py
"""

from dataclasses import dataclass


# Exercise 1: Temperature with Encapsulation
# TODO: Add proper encapsulation and validation
class Temperature:
    """
    Temperature class with validation and conversion methods.
    
    TODO: Complete the docstring with proper Sphinx format
    TODO: Add type hints to all methods
    TODO: Implement validation to prevent temperatures below absolute zero (-273.15°C)
    TODO: Add methods to convert to Fahrenheit and Kelvin
    """
    
    def __init__(self, celsius):
        # TODO: Add validation for absolute zero
        # TODO: Use private attribute (_celsius)
        pass
    
    def to_fahrenheit(self):
        """
        Convert temperature to Fahrenheit.
        
        TODO: Add complete docstring
        """
        pass
    
    def to_kelvin(self):
        """
        Convert temperature to Kelvin.
        
        TODO: Add complete docstring
        """
        pass
    
    def get_celsius(self):
        """
        Get temperature in Celsius.
        
        TODO: Add complete docstring
        """
        pass


# Exercise 2: Book Data Structure
# TODO: Create a dataclass for Book with proper type hints
# TODO: Include fields: isbn (str), title (str), author (str), year (int)
# TODO: Add proper Sphinx docstring


# Exercise 3: Library Object with Behavior
# TODO: Implement Library class with encapsulation
class Library:
    """
    Library management system.
    
    TODO: Complete the docstring
    TODO: Add type hints
    TODO: Implement methods: add_book, remove_book, find_by_isbn, find_by_author
    TODO: Use private attributes for internal book storage
    """
    
    def __init__(self):
        # TODO: Initialize private book storage
        pass
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        TODO: Add complete docstring with parameters and types
        """
        pass
    
    def remove_book(self, isbn):
        """
        Remove a book by ISBN.
        
        TODO: Add complete docstring
        TODO: Raise ValueError if book not found
        """
        pass
    
    def find_by_isbn(self, isbn):
        """
        Find a book by ISBN.
        
        TODO: Add complete docstring
        TODO: Return None if not found
        """
        pass
    
    def find_by_author(self, author):
        """
        Find all books by an author.
        
        TODO: Add complete docstring
        TODO: Return list of books
        """
        pass
    
    def get_book_count(self):
        """
        Get total number of books.
        
        TODO: Add complete docstring
        """
        pass


# Exercise 4: Shopping Cart with Encapsulation
# TODO: Refactor this class to use proper encapsulation
class ShoppingCart:
    """
    Shopping cart for e-commerce.
    
    TODO: Refactor to use private attributes
    TODO: Add validation in methods
    TODO: Add proper type hints
    """
    
    def __init__(self):
        self.items = []  # TODO: Make this private
        self.total = 0  # TODO: Calculate this dynamically, don't store it
    
    def add_item(self, name, price, quantity):
        """
        Add item to cart.
        
        TODO: Add validation (price > 0, quantity > 0)
        TODO: Add complete docstring
        """
        pass
    
    def remove_item(self, name):
        """
        Remove item from cart.
        
        TODO: Add complete docstring
        TODO: Raise ValueError if item not found
        """
        pass
    
    def get_total(self):
        """
        Calculate total cart value.
        
        TODO: Calculate from items, don't use stored total
        TODO: Add complete docstring
        """
        pass
    
    def get_item_count(self):
        """
        Get number of unique items in cart.
        
        TODO: Add complete docstring
        """
        pass
