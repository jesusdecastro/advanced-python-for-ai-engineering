"""
Tests for Error Handling exercises.
"""

import json
import sys
from pathlib import Path

import pytest

# Add parent directory to path to import exercises
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import using importlib to handle module name starting with number
import importlib.util

spec = importlib.util.spec_from_file_location(
    "error_handling", Path(__file__).parent.parent / "04_error_handling.py"
)
error_handling = importlib.util.module_from_spec(spec)
spec.loader.exec_module(error_handling)

InvalidEmailError = error_handling.InvalidEmailError
validate_email = error_handling.validate_email
read_json_file = error_handling.read_json_file
InsufficientFundsError = error_handling.InsufficientFundsError
InvalidTransactionError = error_handling.InvalidTransactionError
transfer_money = error_handling.transfer_money
process_transaction = error_handling.process_transaction
DataProcessingError = error_handling.DataProcessingError
parse_config = error_handling.parse_config
process_user_data = error_handling.process_user_data
safe_divide = error_handling.safe_divide
get_user_age = error_handling.get_user_age


class TestExercise1EmailValidation:
    """Test email validation with custom exceptions."""

    def test_validate_email_valid_email(self):
        """Test that valid email returns True."""
        assert validate_email("user@example.com") is True
        assert validate_email("test.user@domain.co.uk") is True

    def test_validate_email_empty_raises_error(self):
        """Test that empty email raises InvalidEmailError."""
        with pytest.raises(InvalidEmailError):
            validate_email("")

    def test_validate_email_no_at_raises_error(self):
        """Test that email without @ raises InvalidEmailError."""
        with pytest.raises(InvalidEmailError):
            validate_email("userexample.com")

    def test_validate_email_no_dot_raises_error(self):
        """Test that email without . raises InvalidEmailError."""
        with pytest.raises(InvalidEmailError):
            validate_email("user@examplecom")

    def test_invalid_email_error_has_attributes(self):
        """Test that InvalidEmailError stores email and reason."""
        try:
            validate_email("")
        except InvalidEmailError as e:
            assert hasattr(e, "args")
            assert len(e.args) > 0


class TestExercise2SafeFileReading:
    """Test safe file reading with try/except/else/finally."""

    def test_read_json_file_not_found(self, capsys):
        """Test that missing file returns None and prints error."""
        result = read_json_file("nonexistent_file.json")

        assert result is None
        captured = capsys.readouterr()
        assert "File operation completed" in captured.out

    def test_read_json_file_valid_json(self, tmp_path, capsys):
        """Test that valid JSON file is parsed correctly."""
        # Create temporary JSON file
        test_file = tmp_path / "test.json"
        test_data = {"name": "Alice", "age": 30}
        test_file.write_text(json.dumps(test_data))

        result = read_json_file(str(test_file))

        assert result == test_data
        captured = capsys.readouterr()
        assert "File operation completed" in captured.out

    def test_read_json_file_invalid_json(self, tmp_path, capsys):
        """Test that invalid JSON returns None and prints error."""
        # Create temporary file with invalid JSON
        test_file = tmp_path / "invalid.json"
        test_file.write_text("{invalid json content")

        result = read_json_file(str(test_file))

        assert result is None
        captured = capsys.readouterr()
        assert "File operation completed" in captured.out


class TestExercise3BankingTransactions:
    """Test banking transaction system with custom exceptions."""

    def test_transfer_money_successful(self):
        """Test successful money transfer."""
        accounts = {"Alice": 1000.0, "Bob": 500.0}

        result = transfer_money(accounts, "Alice", "Bob", 200.0)

        assert result is True
        assert accounts["Alice"] == 800.0
        assert accounts["Bob"] == 700.0

    def test_transfer_money_insufficient_funds(self):
        """Test that insufficient funds raises InsufficientFundsError."""
        accounts = {"Alice": 100.0, "Bob": 500.0}

        with pytest.raises(InsufficientFundsError) as exc_info:
            transfer_money(accounts, "Alice", "Bob", 200.0)

        # Check that exception has required attributes
        assert exc_info.value.balance == 100.0
        assert exc_info.value.amount == 200.0
        assert exc_info.value.shortfall == 100.0

    def test_transfer_money_invalid_amount(self):
        """Test that negative amount raises InvalidTransactionError."""
        accounts = {"Alice": 1000.0, "Bob": 500.0}

        with pytest.raises(InvalidTransactionError):
            transfer_money(accounts, "Alice", "Bob", -50.0)

        with pytest.raises(InvalidTransactionError):
            transfer_money(accounts, "Alice", "Bob", 0.0)

    def test_transfer_money_account_not_found(self):
        """Test that missing account raises KeyError."""
        accounts = {"Alice": 1000.0}

        with pytest.raises(KeyError):
            transfer_money(accounts, "Alice", "Charlie", 100.0)

        with pytest.raises(KeyError):
            transfer_money(accounts, "Charlie", "Alice", 100.0)

    def test_process_transaction_successful(self, capsys):
        """Test successful transaction processing."""
        accounts = {"Alice": 1000.0, "Bob": 500.0}

        result = process_transaction(accounts, "Alice", "Bob", 200.0)

        assert result is True
        captured = capsys.readouterr()
        assert "success" in captured.out.lower() or "successful" in captured.out.lower()

    def test_process_transaction_handles_insufficient_funds(self, capsys):
        """Test that process_transaction handles InsufficientFundsError."""
        accounts = {"Alice": 100.0, "Bob": 500.0}

        result = process_transaction(accounts, "Alice", "Bob", 200.0)

        assert result is False
        captured = capsys.readouterr()
        # Should print error message
        assert len(captured.out) > 0

    def test_process_transaction_handles_invalid_amount(self, capsys):
        """Test that process_transaction handles InvalidTransactionError."""
        accounts = {"Alice": 1000.0, "Bob": 500.0}

        result = process_transaction(accounts, "Alice", "Bob", -50.0)

        assert result is False
        captured = capsys.readouterr()
        assert len(captured.out) > 0

    def test_process_transaction_handles_missing_account(self, capsys):
        """Test that process_transaction handles KeyError."""
        accounts = {"Alice": 1000.0}

        result = process_transaction(accounts, "Alice", "Charlie", 100.0)

        assert result is False
        captured = capsys.readouterr()
        assert "not found" in captured.out.lower() or "account" in captured.out.lower()


class TestExercise4ExceptionChaining:
    """Test exception chaining and re-raising."""

    def test_parse_config_valid_json(self):
        """Test that valid JSON is parsed correctly."""
        config_string = '{"host": "localhost", "port": 8080}'

        result = parse_config(config_string)

        assert result == {"host": "localhost", "port": 8080}

    def test_parse_config_invalid_json_raises_chained_exception(self):
        """Test that invalid JSON raises DataProcessingError with cause."""
        config_string = "{invalid json}"

        with pytest.raises(DataProcessingError) as exc_info:
            parse_config(config_string)

        # Check that the original exception is preserved
        assert exc_info.value.__cause__ is not None
        assert isinstance(exc_info.value.__cause__, json.JSONDecodeError)

    def test_process_user_data_valid_id(self):
        """Test that valid user ID is processed successfully."""
        result = process_user_data(42)

        assert isinstance(result, str)
        assert len(result) > 0

    def test_process_user_data_invalid_id_reraises(self, capsys):
        """Test that invalid user ID logs and re-raises ValueError."""
        with pytest.raises(ValueError):
            process_user_data(-5)

        # Should have logged the error
        captured = capsys.readouterr()
        assert len(captured.out) > 0


class TestExercise5MultipleExceptionHandling:
    """Test handling multiple exception types."""

    def test_safe_divide_normal_case(self):
        """Test normal division."""
        assert safe_divide(10.0, 2.0) == 5.0
        assert safe_divide(7.0, 2.0) == 3.5

    def test_safe_divide_zero_division(self, capsys):
        """Test that division by zero returns None."""
        result = safe_divide(10.0, 0.0)

        assert result is None
        captured = capsys.readouterr()
        assert len(captured.out) > 0

    def test_safe_divide_type_error(self, capsys):
        """Test that non-numeric values return None."""
        result = safe_divide("10", 2.0)

        assert result is None
        captured = capsys.readouterr()
        assert len(captured.out) > 0

    def test_get_user_age_valid_user(self):
        """Test getting age for valid user."""
        users = {
            "alice": {"age": 30, "email": "alice@example.com"},
            "bob": {"age": 25, "email": "bob@example.com"},
        }

        assert get_user_age(users, "alice") == 30
        assert get_user_age(users, "bob") == 25

    def test_get_user_age_user_not_found(self):
        """Test that missing user returns -1."""
        users = {"alice": {"age": 30}}

        result = get_user_age(users, "charlie")

        assert result == -1

    def test_get_user_age_invalid_users_dict(self):
        """Test that invalid users dict returns -1."""
        result = get_user_age(None, "alice")

        assert result == -1

        result = get_user_age("not a dict", "alice")

        assert result == -1


# Integration tests
class TestIntegration:
    """Integration tests combining multiple concepts."""

    def test_complete_banking_workflow(self, capsys):
        """Test complete banking workflow with multiple transactions."""
        accounts = {"Alice": 1000.0, "Bob": 500.0, "Charlie": 250.0}

        # Successful transfer
        assert process_transaction(accounts, "Alice", "Bob", 100.0) is True
        assert accounts["Alice"] == 900.0
        assert accounts["Bob"] == 600.0

        # Failed transfer - insufficient funds
        assert process_transaction(accounts, "Charlie", "Alice", 500.0) is False
        assert accounts["Charlie"] == 250.0  # Unchanged

        # Failed transfer - invalid amount
        assert process_transaction(accounts, "Bob", "Alice", -50.0) is False

        # Failed transfer - account not found
        assert process_transaction(accounts, "Alice", "David", 100.0) is False

    def test_exception_hierarchy(self):
        """Test that custom exceptions inherit from Exception."""
        assert issubclass(InvalidEmailError, Exception)
        assert issubclass(InsufficientFundsError, Exception)
        assert issubclass(InvalidTransactionError, Exception)
        assert issubclass(DataProcessingError, Exception)
