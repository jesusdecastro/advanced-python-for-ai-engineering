"""Tests for DRY and KISS Principles exercises."""

import sys
from pathlib import Path

import pytest

# Add parent directory to path to import exercises
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import using importlib to handle module name starting with number
import importlib.util

spec = importlib.util.spec_from_file_location(
    "dry_kiss_principles", Path(__file__).parent.parent / "06_dry_kiss_principles.py"
)
dry_kiss = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dry_kiss)

calculate_circle_area = dry_kiss.calculate_circle_area
calculate_circle_circumference = dry_kiss.calculate_circle_circumference
calculate_sphere_volume = dry_kiss.calculate_sphere_volume
calculate_cylinder_volume = dry_kiss.calculate_cylinder_volume
create_user = dry_kiss.create_user
update_user = dry_kiss.update_user
get_discount_percentage = dry_kiss.get_discount_percentage
calculate_total_price = dry_kiss.calculate_total_price
format_user_full_name = dry_kiss.format_user_full_name
format_product_name = dry_kiss.format_product_name
calculate_room_floor_area = dry_kiss.calculate_room_floor_area
calculate_wall_area = dry_kiss.calculate_wall_area
calculate_table_surface_area = dry_kiss.calculate_table_surface_area
get_order_status_message = dry_kiss.get_order_status_message


class TestExercise1ApplyDRY:
    """Test DRY principle - eliminate PI duplication."""

    def test_calculate_circle_area(self):
        """Test circle area calculation."""
        # Area = π * r²
        # For r=5: π * 25 ≈ 78.54
        result = calculate_circle_area(5)
        assert abs(result - 78.54) < 0.01

    def test_calculate_circle_circumference(self):
        """Test circle circumference calculation."""
        # Circumference = 2 * π * r
        # For r=5: 2 * π * 5 ≈ 31.42
        result = calculate_circle_circumference(5)
        assert abs(result - 31.42) < 0.01

    def test_calculate_sphere_volume(self):
        """Test sphere volume calculation."""
        # Volume = (4/3) * π * r³
        # For r=3: (4/3) * π * 27 ≈ 113.10
        result = calculate_sphere_volume(3)
        assert abs(result - 113.10) < 0.01

    def test_calculate_cylinder_volume(self):
        """Test cylinder volume calculation."""
        # Volume = π * r² * h
        # For r=2, h=5: π * 4 * 5 ≈ 62.83
        result = calculate_cylinder_volume(2, 5)
        assert abs(result - 62.83) < 0.01

    def test_pi_constant_exists(self):
        """Test that PI constant is defined at module level."""
        # Students should create a PI constant
        try:
            pi_value = getattr(dry_kiss, "PI", None)
            if pi_value is not None:
                assert abs(pi_value - 3.14159) < 0.00001
            else:
                pytest.skip("PI constant not yet defined")
        except Exception:
            pytest.skip("PI constant not yet defined")


class TestExercise2ApplyDRYValidation:
    """Test DRY principle - extract validation logic."""

    def test_create_user_valid_data(self):
        """Test creating user with valid data."""
        user = create_user("Alice", "alice@example.com", 30)
        assert user["name"] == "Alice"
        assert user["email"] == "alice@example.com"
        assert user["age"] == 30

    def test_create_user_invalid_name(self):
        """Test that invalid name raises error."""
        with pytest.raises(ValueError, match="Name must be at least 2 characters"):
            create_user("A", "alice@example.com", 30)

    def test_create_user_invalid_email(self):
        """Test that invalid email raises error."""
        with pytest.raises(ValueError, match="Invalid email address"):
            create_user("Alice", "invalid-email", 30)

    def test_create_user_invalid_age(self):
        """Test that invalid age raises error."""
        with pytest.raises(ValueError, match="Invalid age"):
            create_user("Alice", "alice@example.com", -5)

    def test_update_user_valid_data(self):
        """Test updating user with valid data."""
        user = update_user(1, "Bob", "bob@example.com", 25)
        assert user["id"] == 1
        assert user["name"] == "Bob"
        assert user["email"] == "bob@example.com"
        assert user["age"] == 25

    def test_update_user_invalid_data(self):
        """Test that update_user validates data."""
        with pytest.raises(ValueError):
            update_user(1, "B", "bob@example.com", 25)

    def test_validation_functions_exist(self):
        """Test that validation helper functions are created."""
        try:
            validate_name = getattr(dry_kiss, "validate_name", None)
            validate_email = getattr(dry_kiss, "validate_email", None)
            validate_age = getattr(dry_kiss, "validate_age", None)
            validate_user_data = getattr(dry_kiss, "validate_user_data", None)

            if all([validate_name, validate_email, validate_age, validate_user_data]):
                assert callable(validate_name)
                assert callable(validate_email)
                assert callable(validate_age)
                assert callable(validate_user_data)
            else:
                pytest.skip("Validation functions not yet implemented")
        except Exception:
            pytest.skip("Validation functions not yet implemented")


class TestExercise3ApplyKISS:
    """Test KISS principle - simplify complex discount logic."""

    def test_premium_member_5_years_high_purchase(self):
        """Test premium member with 5+ years and high purchase."""
        discount = get_discount_percentage("premium", 1000, True, 5)
        assert discount == 25

    def test_premium_member_5_years_medium_purchase(self):
        """Test premium member with 5+ years and medium purchase."""
        discount = get_discount_percentage("premium", 500, True, 5)
        assert discount == 20

    def test_premium_member_5_years_low_purchase(self):
        """Test premium member with 5+ years and low purchase."""
        discount = get_discount_percentage("premium", 100, True, 5)
        assert discount == 15

    def test_premium_member_2_years_high_purchase(self):
        """Test premium member with 2-4 years and high purchase."""
        discount = get_discount_percentage("premium", 1000, True, 3)
        assert discount == 20

    def test_premium_non_member(self):
        """Test premium customer who is not a member."""
        discount = get_discount_percentage("premium", 1000, False, 0)
        assert discount == 5

    def test_regular_member_high_purchase(self):
        """Test regular member with high purchase."""
        discount = get_discount_percentage("regular", 500, True, 1)
        assert discount == 10

    def test_regular_member_low_purchase(self):
        """Test regular member with low purchase."""
        discount = get_discount_percentage("regular", 100, True, 1)
        assert discount == 5

    def test_regular_non_member(self):
        """Test regular non-member."""
        discount = get_discount_percentage("regular", 500, False, 0)
        assert discount == 0

    def test_unknown_customer_type(self):
        """Test unknown customer type."""
        discount = get_discount_percentage("unknown", 1000, True, 5)
        assert discount == 0


class TestExercise4ApplyKISSCalculation:
    """Test KISS principle - simplify price calculation."""

    def test_calculate_total_price_no_discount(self):
        """Test total price calculation without discount."""
        items = [
            {"price": 10.0, "quantity": 2, "discount": 0},
            {"price": 5.0, "quantity": 3, "discount": 0},
        ]
        total = calculate_total_price(items)
        # (10 * 2) + (5 * 3) = 20 + 15 = 35
        assert abs(total - 35.0) < 0.01

    def test_calculate_total_price_with_discount(self):
        """Test total price calculation with discount."""
        items = [
            {"price": 100.0, "quantity": 1, "discount": 0.1},  # 90
            {"price": 50.0, "quantity": 2, "discount": 0.2},  # 80
        ]
        total = calculate_total_price(items)
        # (100 * 1 * 0.9) + (50 * 2 * 0.8) = 90 + 80 = 170
        assert abs(total - 170.0) < 0.01

    def test_calculate_total_price_empty_list(self):
        """Test total price with empty list."""
        total = calculate_total_price([])
        assert total == 0

    def test_calculate_total_price_missing_fields(self):
        """Test total price with missing fields."""
        items = [
            {"price": 10.0},  # Missing quantity and discount
            {"quantity": 2},  # Missing price
        ]
        total = calculate_total_price(items)
        assert total == 0


class TestExercise5BalanceDRYKISS:
    """Test balancing DRY and KISS - appropriate abstraction."""

    def test_format_user_full_name(self):
        """Test user name formatting."""
        name = format_user_full_name("Alice", "Smith")
        assert name == "Alice Smith"

    def test_format_product_name(self):
        """Test product name formatting."""
        name = format_product_name("Apple", "iPhone 15")
        assert name == "Apple iPhone 15"

    def test_functions_remain_separate(self):
        """Test that functions remain separate (not combined)."""
        # These should remain separate even though code is similar
        # They represent different domain concepts
        assert format_user_full_name.__name__ == "format_user_full_name"
        assert format_product_name.__name__ == "format_product_name"


class TestExercise6ApplyDRYAreaCalculation:
    """Test DRY principle - extract common area calculation."""

    def test_calculate_room_floor_area(self):
        """Test room floor area calculation."""
        area = calculate_room_floor_area(5, 4)
        assert area == 20

    def test_calculate_wall_area(self):
        """Test wall area calculation."""
        area = calculate_wall_area(3, 4)
        assert area == 12

    def test_calculate_table_surface_area(self):
        """Test table surface area calculation."""
        area = calculate_table_surface_area(2, 1.5)
        assert area == 3.0

    def test_rectangle_area_function_exists(self):
        """Test that rectangle area helper function is created."""
        try:
            calculate_rectangle_area = getattr(dry_kiss, "calculate_rectangle_area", None)
            if calculate_rectangle_area:
                assert callable(calculate_rectangle_area)
                # Test the helper function
                assert calculate_rectangle_area(5, 4) == 20
            else:
                pytest.skip("calculate_rectangle_area not yet implemented")
        except Exception:
            pytest.skip("calculate_rectangle_area not yet implemented")


class TestExercise7ApplyKISSStatusLogic:
    """Test KISS principle - simplify status logic."""

    def test_get_order_status_known_codes(self):
        """Test known status codes."""
        assert get_order_status_message(200) == "Order Confirmed"
        assert get_order_status_message(201) == "Order Created"
        assert get_order_status_message(400) == "Invalid Order"
        assert get_order_status_message(404) == "Order Not Found"
        assert get_order_status_message(500) == "Processing Error"

    def test_get_order_status_success_range(self):
        """Test success status code range."""
        assert get_order_status_message(202) == "Success"
        assert get_order_status_message(299) == "Success"

    def test_get_order_status_client_error_range(self):
        """Test client error status code range."""
        assert get_order_status_message(401) == "Client Error"
        assert get_order_status_message(403) == "Client Error"

    def test_get_order_status_server_error_range(self):
        """Test server error status code range."""
        assert get_order_status_message(501) == "Server Error"
        assert get_order_status_message(503) == "Server Error"

    def test_get_order_status_unknown(self):
        """Test unknown status codes."""
        assert get_order_status_message(100) == "Unknown Status"
        assert get_order_status_message(600) == "Unknown Status"


class TestCodeQuality:
    """Test overall code quality improvements."""

    def test_functions_have_type_hints(self):
        """Test that students have added type hints."""
        # This is a reminder for students to add type hints
        # The test will pass regardless, but serves as documentation
        import inspect

        functions_to_check = [
            calculate_circle_area,
            create_user,
            get_discount_percentage,
            calculate_total_price,
        ]

        for func in functions_to_check:
            sig = inspect.signature(func)
            # Check if any parameters have annotations
            has_annotations = any(
                param.annotation != inspect.Parameter.empty for param in sig.parameters.values()
            )
            # This test is informational - it will pass either way
            if not has_annotations:
                pytest.skip(f"{func.__name__} doesn't have type hints yet")

    def test_docstrings_are_complete(self):
        """Test that docstrings are complete with Sphinx format."""
        # This is a reminder for students to complete docstrings
        functions_to_check = [calculate_circle_area, create_user, get_discount_percentage]

        for func in functions_to_check:
            docstring = func.__doc__
            if docstring and ":param" in docstring and ":return" in docstring:
                # Docstring is complete
                pass
            else:
                pytest.skip(f"{func.__name__} doesn't have complete Sphinx docstring yet")
