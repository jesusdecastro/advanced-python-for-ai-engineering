"""
Inheritance vs Composition Exercises - Day 4

Your task:
1. Refactor inheritance hierarchies to use composition
2. Implement flexible designs using composition

Run the tests with: pytest tests/test_04_inheritance_vs_composition.py
"""


# Exercise: Refactor to use composition
class Engine:
    """Engine component."""
    
    def start(self):
        """Start the engine."""
        pass


class Car:
    """Car using composition."""
    
    def __init__(self):
        # TODO: Use composition instead of inheritance
        pass
