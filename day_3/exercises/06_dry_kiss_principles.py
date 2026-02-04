"""
DRY and KISS Principles Exercises - Day 3.

Practice applying DRY (Don't Repeat Yourself) and KISS (Keep It Simple, Stupid)
principles to write maintainable, clear code.

Your tasks:
1. Refactor duplicated code to follow DRY
2. Simplify overly complex code to follow KISS
3. Balance DRY and KISS to create appropriate abstractions

Run the tests with: pytest tests/test_06_dry_kiss_principles.py
"""


# Exercise 1: Apply DRY - Eliminate Duplication
# TODO: Extract the duplicated PI constant
# TODO: Add proper type hints to all functions
def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    TODO: Add proper Sphinx docstring with :param, :type, :return, :rtype
    TODO: Extract PI constant to avoid duplication
    """
    pi = 3.14159
    return pi * radius * radius


def calculate_circle_circumference(radius):
    """
    Calculate the circumference of a circle.

    TODO: Add proper Sphinx docstring
    TODO: Use extracted PI constant
    """
    pi = 3.14159  # Duplicated!
    return 2 * pi * radius


def calculate_sphere_volume(radius):
    """
    Calculate the volume of a sphere.

    TODO: Add proper Sphinx docstring
    TODO: Use extracted PI constant
    """
    pi = 3.14159  # Duplicated again!
    return (4 / 3) * pi * radius**3


def calculate_cylinder_volume(radius, height):
    """
    Calculate the volume of a cylinder.

    TODO: Add proper Sphinx docstring
    TODO: Use extracted PI constant
    """
    pi = 3.14159  # Still duplicated!
    return pi * radius * radius * height


# TODO: Create a constant at module level:
# PI = 3.14159265359
# Then refactor all functions above to use it


# Exercise 2: Apply DRY - Extract Validation Logic
# TODO: Extract duplicated validation logic into separate functions
def create_user(name, email, age):
    """
    Create a new user with validation.

    TODO: Add proper type hints and Sphinx docstring
    TODO: Extract validation logic to separate functions
    """
    # Validation logic (duplicated in update_user)
    if not name or len(name) < 2:
        raise ValueError("Name must be at least 2 characters")
    if not email or "@" not in email:
        raise ValueError("Invalid email address")
    if age < 0 or age > 150:
        raise ValueError("Invalid age")

    return {"name": name, "email": email, "age": age}


def update_user(user_id, name, email, age):
    """
    Update an existing user with validation.

    TODO: Add proper type hints and Sphinx docstring
    TODO: Use extracted validation functions
    """
    # Same validation logic duplicated!
    if not name or len(name) < 2:
        raise ValueError("Name must be at least 2 characters")
    if not email or "@" not in email:
        raise ValueError("Invalid email address")
    if age < 0 or age > 150:
        raise ValueError("Invalid age")

    return {"id": user_id, "name": name, "email": email, "age": age}


# TODO: Create these validation functions:
# def validate_name(name: str) -> None:
#     """Validate user name."""
#     if not name or len(name) < 2:
#         raise ValueError("Name must be at least 2 characters")
#
# def validate_email(email: str) -> None:
#     """Validate email address."""
#     if not email or "@" not in email:
#         raise ValueError("Invalid email address")
#
# def validate_age(age: int) -> None:
#     """Validate user age."""
#     if age < 0 or age > 150:
#         raise ValueError("Invalid age")
#
# def validate_user_data(name: str, email: str, age: int) -> None:
#     """Validate all user data."""
#     validate_name(name)
#     validate_email(email)
#     validate_age(age)


# Exercise 3: Apply KISS - Simplify Complex Code
# TODO: Simplify this overly complex function
def get_discount_percentage(customer_type, purchase_amount, is_member, years_as_member):
    """
    Calculate discount percentage based on multiple factors.

    TODO: Add proper type hints and Sphinx docstring
    TODO: Simplify the nested conditionals
    """
    discount = 0

    if customer_type == "premium":
        if is_member:
            if years_as_member >= 5:
                if purchase_amount >= 1000:
                    discount = 25
                elif purchase_amount >= 500:
                    discount = 20
                else:
                    discount = 15
            elif years_as_member >= 2:
                if purchase_amount >= 1000:
                    discount = 20
                elif purchase_amount >= 500:
                    discount = 15
                else:
                    discount = 10
            else:
                discount = 10
        else:
            discount = 5
    elif customer_type == "regular":
        if is_member:
            if purchase_amount >= 500:
                discount = 10
            else:
                discount = 5
        else:
            discount = 0
    else:
        discount = 0

    return discount


# TODO: Simplify by extracting helper functions or using a simpler structure


# Exercise 4: Apply KISS - Avoid Over-Engineering
# TODO: Simplify this overly complex implementation
def calculate_total_price(items):
    """
    Calculate total price of items.

    TODO: Add proper type hints and Sphinx docstring
    TODO: Replace complex reduce with simple loop
    """
    from functools import reduce

    # Overly complex - trying to be "clever"
    return reduce(
        lambda acc, item: acc
        + (item.get("price", 0) * item.get("quantity", 0) * (1 - item.get("discount", 0))),
        items,
        0,
    )


# TODO: Create a simpler version using a basic loop


# Exercise 5: Balance DRY and KISS
# TODO: Decide if these should be combined or kept separate
def format_user_full_name(first_name, last_name):
    """
    Format user's full name.

    TODO: Add proper type hints and Sphinx docstring
    TODO: Decide if this should be combined with format_product_name
    """
    return f"{first_name} {last_name}"


def format_product_name(brand, model):
    """
    Format product name.

    TODO: Add proper type hints and Sphinx docstring
    TODO: Decide if this should be combined with format_user_full_name
    """
    return f"{brand} {model}"


# TODO: Explain your decision in a comment:
# Should these be combined? Why or why not?
# Answer: [Your reasoning here]


# Exercise 6: Apply DRY - Extract Common Calculation
# TODO: Extract the common area calculation logic
def calculate_room_floor_area(length, width):
    """
    Calculate floor area of a room.

    TODO: Add proper type hints and Sphinx docstring
    TODO: Extract common rectangle area calculation
    """
    return length * width


def calculate_wall_area(height, width):
    """
    Calculate area of a wall.

    TODO: Add proper type hints and Sphinx docstring
    TODO: Use extracted rectangle area function
    """
    return height * width


def calculate_table_surface_area(length, width):
    """
    Calculate surface area of a table.

    TODO: Add proper type hints and Sphinx docstring
    TODO: Use extracted rectangle area function
    """
    return length * width


# TODO: Create a helper function:
# def calculate_rectangle_area(width: float, height: float) -> float:
#     """Calculate area of a rectangle."""
#     return width * height
#
# Then refactor the three functions above to use it


# Exercise 7: Apply KISS - Simplify Status Logic
# TODO: Simplify this complex status checking logic
def get_order_status_message(status_code):
    """
    Get human-readable status message for order.

    TODO: Add proper type hints and Sphinx docstring
    TODO: Simplify the nested conditionals
    """
    status_map = {
        200: "Order Confirmed",
        201: "Order Created",
        400: "Invalid Order",
        404: "Order Not Found",
        500: "Processing Error",
    }

    if status_code in status_map:
        return status_map[status_code]
    else:
        if status_code >= 200 and status_code < 300:
            return "Success"
        elif status_code >= 400 and status_code < 500:
            return "Client Error"
        elif status_code >= 500 and status_code < 600:
            return "Server Error"
        else:
            return "Unknown Status"


# TODO: Simplify by using .get() with default and cleaner logic
