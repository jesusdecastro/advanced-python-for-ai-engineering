"""
Data models for regular package example.

This module is part of a regular package (with __init__.py).
"""


class User:
    """
    Simple user model.
    
    :param name: User's name
    :type name: str
    :param email: User's email
    :type email: str
    """
    
    def __init__(self, name: str, email: str):
        """Initialize user."""
        self.name = name
        self.email = email
    
    def __repr__(self) -> str:
        """String representation."""
        return f"User(name='{self.name}', email='{self.email}')"


class Product:
    """
    Simple product model.
    
    :param name: Product name
    :type name: str
    :param price: Product price
    :type price: float
    """
    
    def __init__(self, name: str, price: float):
        """Initialize product."""
        self.name = name
        self.price = price
    
    def __repr__(self) -> str:
        """String representation."""
        return f"Product(name='{self.name}', price=${self.price})"


class _InternalModel:
    """
    Internal model (not exported in __init__.py).
    
    This class is private to the package.
    """
    
    def __init__(self):
        """Initialize internal model."""
        self.data = "internal"
