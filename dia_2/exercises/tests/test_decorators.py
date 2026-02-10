"""Tests for decorators exercises."""

from datetime import datetime
from pathlib import Path

import pytest

# Import from the installed package
from dia2_exercises.decorators import BankAccount, Date, validate_types


class TestBankAccount:
    """Tests for BankAccount class with @property."""

    def test_initial_balance(self):
        """Test account creation with initial balance."""
        account = BankAccount(100.0)
        assert account.balance == 100.0

    def test_balance_is_read_only(self):
        """Test that balance property is read-only."""
        account = BankAccount(100.0)
        with pytest.raises(AttributeError):
            account.balance = 200.0

    def test_deposit_increases_balance(self):
        """Test depositing money increases balance."""
        account = BankAccount(100.0)
        account.deposit(50.0)
        assert account.balance == 150.0

    def test_deposit_multiple_times(self):
        """Test multiple deposits."""
        account = BankAccount(100.0)
        account.deposit(25.0)
        account.deposit(75.0)
        assert account.balance == 200.0

    def test_withdraw_decreases_balance(self):
        """Test withdrawing money decreases balance."""
        account = BankAccount(100.0)
        account.withdraw(30.0)
        assert account.balance == 70.0

    def test_withdraw_exact_balance(self):
        """Test withdrawing exact balance."""
        account = BankAccount(100.0)
        account.withdraw(100.0)
        assert account.balance == 0.0

    def test_negative_initial_balance_raises_error(self):
        """Test that negative initial balance raises ValueError."""
        with pytest.raises(ValueError, match="negative"):
            BankAccount(-50.0)

    def test_negative_deposit_raises_error(self):
        """Test that negative deposit raises ValueError."""
        account = BankAccount(100.0)
        with pytest.raises(ValueError, match="positive"):
            account.deposit(-10.0)

    def test_negative_withdraw_raises_error(self):
        """Test that negative withdrawal raises ValueError."""
        account = BankAccount(100.0)
        with pytest.raises(ValueError, match="positive"):
            account.withdraw(-10.0)

    def test_insufficient_balance_raises_error(self):
        """Test that withdrawing more than balance raises ValueError."""
        account = BankAccount(100.0)
        with pytest.raises(ValueError, match="Insufficient"):
            account.withdraw(150.0)


class TestDate:
    """Tests for Date class with @classmethod factory methods."""

    def test_date_creation(self):
        """Test creating date with constructor."""
        date = Date(25, 12, 2024)
        assert date.day == 25
        assert date.month == 12
        assert date.year == 2024

    def test_from_string_creates_date(self):
        """Test creating date from string."""
        date = Date.from_string("15-08-2023")
        assert date.day == 15
        assert date.month == 8
        assert date.year == 2023

    def test_from_string_with_leading_zeros(self):
        """Test parsing string with leading zeros."""
        date = Date.from_string("05-03-2024")
        assert date.day == 5
        assert date.month == 3
        assert date.year == 2024

    def test_today_creates_current_date(self):
        """Test that today() creates date with current date."""
        date = Date.today()
        now = datetime.now()
        assert date.day == now.day
        assert date.month == now.month
        assert date.year == now.year

    def test_display_format(self):
        """Test date display format."""
        date = Date(25, 12, 2024)
        display = date.display()
        assert "25" in display
        assert "diciembre" in display.lower()
        assert "2024" in display

    def test_display_different_months(self):
        """Test display with different months."""
        date1 = Date(1, 1, 2024)
        date2 = Date(15, 6, 2024)

        display1 = date1.display()
        display2 = date2.display()

        assert "enero" in display1.lower()
        assert "junio" in display2.lower()


class TestValidateTypesDecorator:
    """Tests for custom @validate_types decorator."""

    def test_correct_types_pass(self):
        """Test that correct types pass validation."""

        @validate_types
        def add_numbers(a: int, b: int) -> int:
            return a + b

        result = add_numbers(5, 3)
        assert result == 8

    def test_incorrect_type_raises_error(self):
        """Test that incorrect types raise TypeError."""

        @validate_types
        def add_numbers(a: int, b: int) -> int:
            return a + b

        with pytest.raises(TypeError):
            add_numbers("5", 3)

    def test_multiple_incorrect_types(self):
        """Test validation with multiple incorrect types."""

        @validate_types
        def process(name: str, age: int, active: bool) -> str:
            return f"{name} is {age} years old"

        with pytest.raises(TypeError):
            process("Alice", "25", True)

    def test_string_type_validation(self):
        """Test string type validation."""

        @validate_types
        def greet(name: str) -> str:
            return f"Hello, {name}!"

        assert greet("Alice") == "Hello, Alice!"

        with pytest.raises(TypeError):
            greet(123)

    def test_preserves_function_metadata(self):
        """Test that decorator preserves function name and docstring."""

        @validate_types
        def my_function(x: int) -> int:
            """Multiply by two."""
            return x * 2

        assert my_function.__name__ == "my_function"
        assert "docstring" in my_function.__doc__

    def test_no_annotations_works(self):
        """Test that functions without annotations still work."""

        @validate_types
        def no_hints(a, b):
            return a + b

        # Should work without validation
        result = no_hints(5, 3)
        assert result == 8


class TestDecoratorIntegration:
    """Integration tests combining multiple decorator concepts."""

    def test_bank_account_workflow(self):
        """Test complete bank account workflow."""
        account = BankAccount(1000.0)

        # Multiple operations
        account.deposit(500.0)
        account.withdraw(200.0)
        account.deposit(100.0)
        account.withdraw(50.0)

        assert account.balance == 1350.0

    def test_date_factory_methods(self):
        """Test using different date factory methods."""
        # From string
        date1 = Date.from_string("01-01-2024")

        # Today
        date2 = Date.today()

        # Direct construction
        date3 = Date(31, 12, 2024)

        # All should have valid display
        assert len(date1.display()) > 0
        assert len(date2.display()) > 0
        assert len(date3.display()) > 0

    def test_decorated_function_with_property(self):
        """Test combining decorators with properties."""

        class Counter:
            def __init__(self):
                self._count = 0

            @property
            def count(self) -> int:
                return self._count

            @validate_types
            def increment(self, amount: int) -> None:
                self._count += amount

        counter = Counter()
        counter.increment(5)
        assert counter.count == 5

        with pytest.raises(TypeError):
            counter.increment("5")
