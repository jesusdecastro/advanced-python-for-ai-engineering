"""
Classes and SRP Exercises - Day 4

This module contains exercises to practice the Single Responsibility Principle.

Your task:
1. Refactor the User class to follow SRP
2. Create separate classes for different responsibilities
3. Implement proper separation of concerns

Run the tests with: pytest tests/test_03_classes_srp.py
"""


# Exercise 1: Refactor User class to follow SRP
# TODO: This class has too many responsibilities - refactor it
class User:
    """
    User class with multiple responsibilities (VIOLATES SRP).
    
    TODO: Identify the different responsibilities
    TODO: Create separate classes for each responsibility
    TODO: Refactor this class to only handle user data
    """
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def validate_email(self):
        """Validate email format."""
        # TODO: Move to EmailValidator class
        pass
    
    def hash_password(self):
        """Hash the password."""
        # TODO: Move to PasswordHasher class
        pass
    
    def save_to_database(self):
        """Save user to database."""
        # TODO: Move to UserRepository class
        pass
    
    def send_welcome_email(self):
        """Send welcome email to user."""
        # TODO: Move to EmailService class
        pass


# Exercise 2: Create separate classes following SRP
# TODO: Create EmailValidator class
# TODO: Create PasswordHasher class
# TODO: Create UserRepository class
# TODO: Create EmailService class
