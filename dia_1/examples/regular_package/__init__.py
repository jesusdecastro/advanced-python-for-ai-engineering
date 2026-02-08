"""
Regular package with __init__.py.

This package demonstrates how __init__.py provides:
1. A clean public API
2. Direct access to functions and classes
3. Package metadata
4. Control over what gets exported
"""

# Import functions and classes to expose at package level
from .utils import greet, calculate_sum
from .models import User, Product

# Package metadata
__version__ = "1.0.0"
__author__ = "Python Course"

# Control what gets exported with 'from package import *'
__all__ = [
    'greet',
    'calculate_sum',
    'User',
    'Product',
]

# Package-level initialization (runs once on first import)
print(f"📦 Initializing regular_package v{__version__}")
