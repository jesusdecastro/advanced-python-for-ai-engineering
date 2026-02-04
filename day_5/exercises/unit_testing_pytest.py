"""
Unit Testing with pytest Exercises - Day 5

This module contains exercises for practicing pytest fundamentals including
writing tests, using fixtures, mocking, and measuring code coverage.

Your tasks:
1. Complete the test functions for email validation
2. Create fixtures for file management testing
3. Write tests with mocking for the weather service
4. Ensure all tests follow the AAA pattern

Run the tests with: pytest tests/test_01_unit_testing_pytest.py
Run with coverage: pytest --cov=exercises tests/test_01_unit_testing_pytest.py
"""

import re
import os
import requests
from typing import List


# Exercise 1: Email Validation
def validate_email(email):
    """
    Validate an email address.
    
    TODO: Add type hints
    TODO: Complete docstring with :param, :type, :return, :rtype
    
    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    if not email or not isinstance(email, str):
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


# Exercise 2: File Manager
class FileManager:
    """
    Manage files in a directory.
    
    TODO: Add type hints to all methods
    TODO: Complete docstrings
    """
    
    def __init__(self, base_dir):
        """
        Initialize the FileManager.
        
        TODO: Add parameter documentation
        """
        self.base_dir = base_dir
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
    
    def create_file(self, filename, content):
        """
        Create a file with content.
        
        TODO: Add parameter and return documentation
        """
        filepath = os.path.join(self.base_dir, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        return filepath
    
    def read_file(self, filename):
        """
        Read content from a file.
        
        TODO: Add parameter and return documentation
        """
        filepath = os.path.join(self.base_dir, filename)
        with open(filepath, 'r') as f:
            return f.read()
    
    def list_files(self):
        """
        List all files in the directory.
        
        TODO: Add return documentation
        """
        return [f for f in os.listdir(self.base_dir) 
                if os.path.isfile(os.path.join(self.base_dir, f))]
    
    def delete_file(self, filename):
        """
        Delete a file.
        
        TODO: Add parameter documentation
        """
        filepath = os.path.join(self.base_dir, filename)
        if os.path.exists(filepath):
            os.remove(filepath)


# Exercise 3: Weather Service with API calls
class WeatherService:
    """
    Service to fetch weather data from an external API.
    
    TODO: Add type hints
    TODO: Complete docstrings
    """
    
    def __init__(self, api_key):
        """
        Initialize the WeatherService.
        
        TODO: Add parameter documentation
        """
        self.api_key = api_key
        self.base_url = "https://api.weather.com/v1"
    
    def get_temperature(self, city):
        """
        Get current temperature for a city.
        
        TODO: Add parameter and return documentation
        TODO: Document exceptions
        """
        url = f"{self.base_url}/current"
        params = {"city": city, "api_key": self.api_key}
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        return data["temperature"]
    
    def get_forecast(self, city, days):
        """
        Get weather forecast for a city.
        
        TODO: Add parameter and return documentation
        TODO: Document exceptions
        """
        url = f"{self.base_url}/forecast"
        params = {"city": city, "days": days, "api_key": self.api_key}
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        return data["forecast"]


# Exercise 4: Shopping Cart (for fixture practice)
class ShoppingCart:
    """
    A shopping cart implementation for testing fixtures.
    
    TODO: Add type hints
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        """
        Add an item to the cart.
        
        TODO: Add parameter documentation
        """
        self.items.append({"name": name, "price": price, "quantity": quantity})
    
    def remove_item(self, name):
        """
        Remove an item from the cart by name.
        
        TODO: Add parameter documentation
        """
        self.items = [item for item in self.items if item["name"] != name]
    
    def total(self):
        """
        Calculate total cart value.
        
        TODO: Add return documentation
        """
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def item_count(self):
        """
        Get total number of items in cart.
        
        TODO: Add return documentation
        """
        return sum(item["quantity"] for item in self.items)
    
    def clear(self):
        """Clear all items from the cart."""
        self.items = []
