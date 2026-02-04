"""
Tests for Meaningful Names exercises.
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import exercises
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import using importlib to handle module name starting with number
import importlib.util

spec = importlib.util.spec_from_file_location(
    "meaningful_names", Path(__file__).parent.parent / "02_meaningful_names.py"
)
meaningful_names = importlib.util.module_from_spec(spec)
spec.loader.exec_module(meaningful_names)


class TestExercise1RefactorCrypticNames:
    """Test refactoring of cryptic names to reveal intention."""

    def test_original_data_class_collects_positive_numbers(self):
        """Test that original class collects positive numbers."""
        collector = meaningful_names.data()
        result = collector.do_thing([1, -2, 3, -4, 5])

        assert result == 3  # Count of positive numbers
        assert collector.x == [1, 3, 5]  # Positive numbers collected
        assert collector.y == 3  # Count

    def test_original_data_class_ignores_negatives(self):
        """Test that original class ignores negative numbers."""
        collector = meaningful_names.data()
        result = collector.do_thing([-1, -2, -3])

        assert result == 0
        assert collector.x == []
        assert collector.y == 0

    def test_original_data_class_handles_empty_list(self):
        """Test that original class handles empty input."""
        collector = meaningful_names.data()
        result = collector.do_thing([])

        assert result == 0
        assert collector.x == []


class TestExercise2FixMisleadingNames:
    """Test fixing misleading names."""

    def test_user_list_is_actually_dict(self):
        """Test that user_list variable contains dict data."""
        user_data = meaningful_names.user_list

        assert isinstance(user_data, dict)
        assert "john" in user_data
        assert user_data["john"]["age"] == 30

    def test_get_users_filters_and_transforms(self):
        """Test that get_users function filters and transforms."""
        users = [
            {"name": "john", "email": "john@example.com", "active": True, "age": 25},
            {"name": "jane", "email": "jane@example.com", "active": False, "age": 30},
            {"name": "bob", "email": "bob@example.com", "active": True, "age": 17},
            {"name": "alice", "email": "alice@example.com", "active": True, "age": 22},
        ]

        result = meaningful_names.get_users(users)

        # Should only include active users >= 18
        assert len(result) == 2
        assert result[0]["name"] == "JOHN"  # Transformed to uppercase
        assert result[1]["name"] == "ALICE"

    def test_get_users_transforms_to_uppercase(self):
        """Test that get_users transforms names to uppercase."""
        users = [{"name": "test", "email": "test@example.com", "active": True, "age": 20}]

        result = meaningful_names.get_users(users)

        assert result[0]["name"] == "TEST"


class TestExercise3ApplyPEP8Conventions:
    """Test application of PEP 8 naming conventions."""

    def test_constants_exist(self):
        """Test that constants are defined."""
        assert hasattr(meaningful_names, "MaxRetries")
        assert meaningful_names.MaxRetries == 3

    def test_variables_exist(self):
        """Test that variables are defined."""
        assert hasattr(meaningful_names, "UserName")
        assert meaningful_names.UserName == "john"

    def test_calculate_total_function_works(self):
        """Test that CalculateTotal function calculates correctly."""
        result = meaningful_names.CalculateTotal([10, 20, 30])
        assert result == 60

    def test_calculate_total_handles_empty_list(self):
        """Test that CalculateTotal handles empty list."""
        result = meaningful_names.CalculateTotal([])
        assert result == 0

    def test_shopping_cart_class_works(self):
        """Test that shopping_cart class works correctly."""
        cart = meaningful_names.shopping_cart()

        cart.AddItem({"name": "item1", "price": 10})
        cart.AddItem({"name": "item2", "price": 20})

        assert len(cart.Items) == 2
        assert cart.TotalPrice == 30

    def test_shopping_cart_handles_missing_price(self):
        """Test that shopping_cart handles items without price."""
        cart = meaningful_names.shopping_cart()
        cart.AddItem({"name": "item1"})

        assert len(cart.Items) == 1
        assert cart.TotalPrice == 0


class TestExercise4ImproveFunctionNames:
    """Test improvement of function names with verb patterns."""

    def test_password_validates_length(self):
        """Test that password function validates length."""
        assert meaningful_names.password("12345678") is True
        assert meaningful_names.password("1234567") is False

    def test_password_handles_empty_string(self):
        """Test that password function handles empty string."""
        assert meaningful_names.password("") is False

    def test_admin_checks_user_id(self):
        """Test that admin function checks user ID."""
        assert meaningful_names.admin(1) is True
        assert meaningful_names.admin(2) is False

    def test_user_account_creates_account(self):
        """Test that user_account function creates account."""
        result = meaningful_names.user_account("john", "john@example.com")

        assert result["username"] == "john"
        assert result["email"] == "john@example.com"
        assert "created_at" in result


class TestExercise5ImproveClassNames:
    """Test improvement of class names to be specific nouns."""

    def test_manager_class_authenticates(self):
        """Test that Manager class can authenticate users."""
        manager = meaningful_names.Manager()
        manager.users = {"john": {"password": "secret123"}}

        assert manager.check("john", "secret123") is True
        assert manager.check("john", "wrong") is False
        assert manager.check("jane", "secret123") is False

    def test_handler_class_processes_items(self):
        """Test that Handler class processes items."""
        handler = meaningful_names.Handler()

        result1 = handler.process("item1")
        result2 = handler.process("item2")

        assert result1 == 1
        assert result2 == 2
        assert len(handler.data) == 2


class TestExercise6AddContextToAmbiguousNames:
    """Test adding context to ambiguous names."""

    def test_send_message_formats_correctly(self):
        """Test that send_message formats message correctly."""
        result = meaningful_names.send_message("John Doe", "123 Main St", "Springfield")

        assert "John Doe" in result
        assert "123 Main St" in result
        assert "Springfield" in result

    def test_send_message_handles_different_inputs(self):
        """Test that send_message handles various inputs."""
        result = meaningful_names.send_message("Jane Smith", "456 Oak Ave", "Portland")

        assert "Jane Smith" in result
        assert "456 Oak Ave" in result


class TestExercise7RemoveRedundantContext:
    """Test removal of redundant context from names."""

    def test_user_class_has_attributes(self):
        """Test that User class has all attributes."""
        user = meaningful_names.User()

        assert hasattr(user, "user_name")
        assert hasattr(user, "user_email")
        assert hasattr(user, "user_age")
        assert hasattr(user, "user_address")

    def test_user_get_info_returns_data(self):
        """Test that get_user_info returns user data."""
        user = meaningful_names.User()
        user.user_name = "John"
        user.user_email = "john@example.com"

        info = user.get_user_info()

        assert info["name"] == "John"
        assert info["email"] == "john@example.com"


# Additional tests for refactored versions (students will implement these)
class TestRefactoredVersions:
    """Tests for refactored versions with better names."""

    def test_refactored_functions_exist(self):
        """Test that students have created refactored versions."""
        # This test will pass once students implement refactored versions
        # Look for common refactored names
        refactored_names = [
            "PositiveNumberCollector",
            "user_registry",
            "filter_active_adult_users",
            "MAX_RETRIES",
            "calculate_total",
            "ShoppingCart",
            "is_valid_password",
            "has_admin_privileges",
            "create_user_account",
            "UserAuthenticator",
            "PaymentProcessor",
        ]

        found_any = False
        for name in refactored_names:
            if hasattr(meaningful_names, name):
                found_any = True
                break

        if not found_any:
            pytest.skip("Refactored versions not yet implemented")
        else:
            # At least one refactored version exists
            assert True
