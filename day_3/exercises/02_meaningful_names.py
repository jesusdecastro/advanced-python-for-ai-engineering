"""
Meaningful Names Exercises - Day 3

Practice choosing descriptive names that reveal intention, avoid ambiguity,
and follow PEP 8 conventions. Learn to refactor cryptic names into clear,
self-documenting code.

Your tasks:
1. Refactor code with cryptic names to use descriptive names
2. Fix misleading names that contradict the actual data type or behavior
3. Apply PEP 8 naming conventions consistently
4. Improve function and class names to be more descriptive

Run the tests with: pytest tests/test_02_meaningful_names.py
"""


# Exercise 1: Refactor cryptic names to reveal intention
# TODO: Refactor this class to use meaningful names
class data:
    """
    TODO: Add proper docstring explaining what this class represents
    TODO: Rename class to follow PEP 8 (PascalCase)
    TODO: Rename attributes to reveal their purpose
    """

    def __init__(self):
        self.x = []
        self.y = 0

    def do_thing(self, a):
        """
        TODO: Add proper docstring with :param, :type, :return, :rtype
        TODO: Rename method and parameters to reveal intention
        """
        for i in a:
            if i > 0:
                self.x.append(i)
                self.y += 1
        return self.y


# TODO: Create refactored version with meaningful names
# Hint: This class appears to collect positive numbers
# Consider names like: PositiveNumberCollector, positive_numbers, count, etc.


# Exercise 2: Fix misleading names
# TODO: Fix the misleading name - this is a dict, not a list
user_list = {
    "john": {"age": 30, "email": "john@example.com"},
    "jane": {"age": 25, "email": "jane@example.com"},
}


# TODO: Rename to accurately reflect the data structure
# Hint: Consider names like user_registry, users_by_name, user_database


# TODO: Fix this function name - it does more than just "get"
def get_users(users):
    """
    TODO: Add proper docstring
    TODO: Rename function to accurately describe what it does
    """
    result = []
    for user in users:
        if user.get("active") and user.get("age", 0) >= 18:
            result.append({"name": user["name"].upper(), "email": user["email"]})
    return result


# TODO: Create refactored version with accurate name
# Hint: This function filters AND transforms users


# Exercise 3: Apply PEP 8 naming conventions
# TODO: Fix all naming convention violations in this code
MaxRetries = 3
UserName = "john"
default_timeout = 30


def CalculateTotal(Items):
    """
    TODO: Add proper docstring
    TODO: Fix function name (should be snake_case)
    TODO: Fix parameter name (should be snake_case)
    """
    Total = 0
    for Item in Items:
        Total += Item
    return Total


class shopping_cart:
    """
    TODO: Add proper docstring
    TODO: Fix class name (should be PascalCase)
    """

    def __init__(self):
        self.Items = []
        self.TotalPrice = 0

    def AddItem(self, item):
        """
        TODO: Add proper docstring
        TODO: Fix method name (should be snake_case)
        TODO: Fix attribute names (should be snake_case)
        """
        self.Items.append(item)
        self.TotalPrice += item.get("price", 0)


# TODO: Create refactored versions following PEP 8:
# - MAX_RETRIES (constant in UPPER_SNAKE_CASE)
# - user_name (variable in snake_case)
# - calculate_total (function in snake_case)
# - ShoppingCart (class in PascalCase)


# Exercise 4: Improve function names to use verb patterns
# TODO: Rename these functions to follow common verb patterns
def password(pwd):
    """
    TODO: Add proper docstring
    TODO: Rename to use verb pattern (e.g., is_valid_password, validate_password)
    """
    return len(pwd) >= 8


def admin(user_id):
    """
    TODO: Add proper docstring
    TODO: Rename to use boolean pattern (e.g., has_admin_privileges, is_admin)
    """
    # Simplified implementation
    return user_id == 1


def user_account(username, email):
    """
    TODO: Add proper docstring
    TODO: Rename to use creation pattern (e.g., create_user_account)
    """
    return {"username": username, "email": email, "created_at": "2024-01-01"}


# TODO: Create refactored versions with proper verb patterns


# Exercise 5: Improve class names to be specific nouns
# TODO: Rename these classes to be more specific
class Manager:
    """
    TODO: Add proper docstring
    TODO: Rename to be more specific (e.g., UserAuthenticator, UserRepository)
    """

    def __init__(self):
        self.users = {}

    def check(self, username, password):
        """
        TODO: Add proper docstring
        TODO: Rename method to be more descriptive
        """
        user = self.users.get(username)
        if not user:
            return False
        return user.get("password") == password


class Handler:
    """
    TODO: Add proper docstring
    TODO: Rename to be more specific (e.g., PaymentProcessor, DataTransformer)
    """

    def __init__(self):
        self.data = []

    def process(self, item):
        """
        TODO: Add proper docstring
        TODO: Rename method to be more descriptive
        """
        self.data.append(item)
        return len(self.data)


# TODO: Create refactored versions with specific class names


# Exercise 6: Add context to ambiguous names
# TODO: Add context to make these names clear
def send_message(name, street, city):
    """
    TODO: Add proper docstring
    TODO: Add context to parameters (e.g., customer_name, shipping_street)
    """
    message = f"Sending to {name} at {street}, {city}"
    return message


# TODO: Create refactored version with contextual names
# Hint: Is this a customer? A shipping address? A billing address?


# Exercise 7: Remove redundant context
# TODO: Remove redundant prefixes from this class
class User:
    """
    TODO: Add proper docstring
    TODO: Remove redundant 'user_' prefixes from attributes
    """

    def __init__(self):
        self.user_name = ""
        self.user_email = ""
        self.user_age = 0
        self.user_address = ""

    def get_user_info(self):
        """
        TODO: Add proper docstring
        TODO: Simplify method name (redundant 'user_')
        """
        return {"name": self.user_name, "email": self.user_email}


# TODO: Create refactored version without redundant context
