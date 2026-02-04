"""
Abstract Base Classes Exercises - Day 4

Your task:
1. Create abstract base classes
2. Implement concrete classes that inherit from ABC

Run the tests with: pytest tests/test_05_abstract_base_classes.py
"""

from abc import ABC, abstractmethod


# Exercise: Create abstract base class
class DataProcessor(ABC):
    """Abstract base class for data processors."""
    
    @abstractmethod
    def process(self, data):
        """Process data."""
        pass
