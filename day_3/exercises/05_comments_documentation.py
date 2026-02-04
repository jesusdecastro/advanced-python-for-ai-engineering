"""
Comments and Documentation Exercises - Day 3.

This module contains exercises focused on writing effective comments,
documentation, and docstrings. Students will learn when to comment,
how to write meaningful documentation, and best practices for code clarity.

Your task:
1. Add appropriate docstrings to functions and classes
2. Add meaningful comments where necessary
3. Remove or improve bad comments
4. Document complex logic appropriately

Run the tests with: pytest tests/test_05_comments_documentation.py
"""


# Exercise 1: Add Missing Docstring
# TODO: Add a complete Sphinx-format docstring to this function
def calculate_discount(price, discount_percent, is_member):
    if is_member:
        discount_percent += 5

    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount

    return final_price


# Exercise 2: Improve Bad Comments
# TODO: Remove obvious comments and add meaningful ones where needed
def process_user_data(user_data):
    # Get the name
    name = user_data.get("name")

    # Get the age
    age = user_data.get("age")

    # Check if age is valid
    if age < 0:
        raise ValueError("Age cannot be negative")

    # Calculate birth year
    from datetime import datetime

    current_year = datetime.now().year
    birth_year = current_year - age

    # Return result
    return {"name": name, "birth_year": birth_year}


# Exercise 3: Document Complex Logic
# TODO: Add comments explaining the algorithm and edge cases
def find_longest_palindrome(text):
    if not text:
        return ""

    longest = ""

    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring

    return longest


# Exercise 4: Complete Class Documentation
# TODO: Add class docstring and complete method docstrings
class DataValidator:
    def __init__(self, rules):
        self.rules = rules
        self.errors = []

    # TODO: Add docstring
    def validate(self, data):
        self.errors = []

        for field, rule in self.rules.items():
            if field not in data:
                self.errors.append(f"Missing required field: {field}")
                continue

            value = data[field]

            if "type" in rule and not isinstance(value, rule["type"]):
                self.errors.append(f"Invalid type for {field}: expected {rule['type'].__name__}")

            if "min" in rule and value < rule["min"]:
                self.errors.append(f"{field} is below minimum value {rule['min']}")

            if "max" in rule and value > rule["max"]:
                self.errors.append(f"{field} exceeds maximum value {rule['max']}")

        return len(self.errors) == 0

    # TODO: Add docstring
    def get_errors(self):
        return self.errors


# Exercise 5: Document API Function
# TODO: Add comprehensive docstring with examples
def fetch_and_cache(url, cache_duration=3600):
    import hashlib
    import json
    import time
    from pathlib import Path

    cache_dir = Path(".cache")
    cache_dir.mkdir(exist_ok=True)

    cache_key = hashlib.md5(url.encode()).hexdigest()
    cache_file = cache_dir / f"{cache_key}.json"

    if cache_file.exists():
        with open(cache_file, "r") as f:
            cached_data = json.load(f)

        if time.time() - cached_data["timestamp"] < cache_duration:
            return cached_data["data"]

    # Simulate fetching data
    data = {"url": url, "content": "Sample data"}

    with open(cache_file, "w") as f:
        json.dump({"timestamp": time.time(), "data": data}, f)

    return data


# Exercise 6: Self-Documenting Code
# TODO: Refactor this function to be more self-documenting
# Reduce the need for comments by using better variable names
def calc(d, r, t):
    # d is data list
    # r is rate
    # t is threshold

    # Filter data
    fd = [x for x in d if x > t]

    # Apply rate
    rd = [x * r for x in fd]

    # Get average
    if len(rd) == 0:
        return 0

    avg = sum(rd) / len(rd)

    return avg
