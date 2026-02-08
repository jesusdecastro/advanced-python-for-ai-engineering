"""
Code Quality Tools Exercises - Day 1

This module contains exercises for practicing with Ruff and Pyright.
Students will work with linting rules, code formatting, and type checking.

Your task:
1. Fix linting errors in provided code
2. Add type hints to functions
3. Configure Ruff rules
4. Understand and fix type checking errors

Run the tests with: pytest tests/test_05_code_quality_tools.py
"""

# TODO: Import necessary modules
# Hint: You'll need typing, pathlib, and re


# Exercise 1: Fix this function to pass Ruff linting
# TODO: Add type hints
def calculate_total(items, tax_rate=0.1):
    """
    Calculate total price including tax.

    TODO: Add complete Sphinx docstring
    """
    # TODO: Fix linting issues in this function
    total = 0
    for item in items:
        total = total + item
    tax = total * tax_rate
    final_total = total + tax
    return final_total


# Exercise 2: Add proper type hints
# TODO: Add type hints for all parameters and return value
def process_user_data(user_id, name, email, age, is_active=True):
    """
    Process user data and return formatted dictionary.

    TODO: Add complete Sphinx docstring with type annotations

    Example:
        >>> process_user_data(1, "Alice", "alice@example.com", 30)
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'age': 30, 'active': True}
    """
    # TODO: Add type hints to make this function type-safe
    return {"id": user_id, "name": name, "email": email, "age": age, "active": is_active}


# Exercise 3: Fix formatting issues
# TODO: Format this function properly (Ruff format style)
def analyze_data(data, threshold=0.5, verbose=False):
    """Analyze data and return results."""
    results = []
    for item in data:
        if item > threshold:
            if verbose:
                print(f"Item {item} exceeds threshold")
            results.append(item)
    return results


# Exercise 4: Add type hints for complex types
# TODO: Add proper type hints using List, Dict, Optional
def get_user_stats(users):
    """
    Calculate statistics for a list of users.

    TODO: Add complete Sphinx docstring

    Each user is a dict with: id, name, age, score
    Returns dict with: total_users, average_age, average_score
    """
    # TODO: Add type hints for nested structures
    if not users:
        return None

    total_users = len(users)
    total_age = sum(user["age"] for user in users)
    total_score = sum(user["score"] for user in users)

    return {
        "total_users": total_users,
        "average_age": total_age / total_users,
        "average_score": total_score / total_users,
    }


# Exercise 5: Fix type errors
# TODO: Add type hints and fix type inconsistencies
def merge_configs(default_config, user_config):
    """
    Merge user configuration with defaults.

    TODO: Add complete Sphinx docstring

    Example:
        >>> default = {"timeout": 30, "retries": 3}
        >>> user = {"timeout": 60}
        >>> merge_configs(default, user)
        {'timeout': 60, 'retries': 3}
    """
    # TODO: Add type hints
    # TODO: Fix potential type errors
    result = default_config.copy()
    result.update(user_config)
    return result


# Exercise 6: Create a class with proper type hints
# TODO: Add type hints to all methods
class CodeAnalyzer:
    """
    Analyze Python code for quality metrics.

    TODO: Add complete class docstring with :ivar annotations
    """

    # TODO: Add type hints to __init__
    def __init__(self, filename):
        """
        Initialize the analyzer.

        TODO: Add complete Sphinx docstring
        """
        self.filename = filename
        self.lines = []
        self.errors = []

    # TODO: Add type hints
    def load_file(self):
        """
        Load file content.

        TODO: Add complete Sphinx docstring
        """
        # TODO: Add proper error handling
        with open(self.filename) as f:
            self.lines = f.readlines()

    # TODO: Add type hints
    def count_lines(self):
        """
        Count total lines.

        TODO: Add complete Sphinx docstring
        """
        return len(self.lines)

    # TODO: Add type hints
    def find_long_lines(self, max_length=100):
        """
        Find lines exceeding max length.

        TODO: Add complete Sphinx docstring
        """
        long_lines = []
        for i, line in enumerate(self.lines, 1):
            if len(line) > max_length:
                long_lines.append((i, len(line)))
        return long_lines

    # TODO: Add type hints
    def get_report(self):
        """
        Generate analysis report.

        TODO: Add complete Sphinx docstring
        """
        return {
            "filename": self.filename,
            "total_lines": self.count_lines(),
            "long_lines": len(self.find_long_lines()),
            "errors": len(self.errors),
        }
