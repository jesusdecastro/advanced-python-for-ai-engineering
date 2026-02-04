"""
Unit tests for type hinting exercises.

These tests validate both functionality AND type hints using Pyright.

Run with: pytest tests/test_02_type_hinting.py -v
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

# Import the module to test functionality
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Dynamically import module with numeric prefix
_module_path = Path(__file__).parent.parent / "02_type_hinting.py"
_spec = importlib.util.spec_from_file_location("type_hinting_exercises", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

DataProcessor = _module.DataProcessor
calculate_rectangle_area = _module.calculate_rectangle_area
calculate_statistics = _module.calculate_statistics
find_user = _module.find_user
process_value = _module.process_value
validate_and_process = _module.validate_and_process


class TestTypeHintsWithPyright:
    """Test that Pyright validates the type hints correctly."""

    def test_pyright_passes(self) -> None:
        """Test that Pyright validation passes for the exercises file."""
        exercises_file = Path(__file__).parent.parent / "02_type_hinting.py"

        result = subprocess.run(
            ["pyright", str(exercises_file), "--outputjson"],
            capture_output=True,
            text=True,
        )

        # Pyright returns 0 if no errors
        if result.returncode != 0:
            pytest.fail(f"Pyright found type errors:\n{result.stdout}\n{result.stderr}")


class TestCalculateRectangleArea:
    """Tests for calculate_rectangle_area function."""

    def test_basic_calculation(self) -> None:
        """Test basic rectangle area calculation."""
        assert calculate_rectangle_area(5.0, 3.0) == 15.0

    def test_square(self) -> None:
        """Test area of a square."""
        assert calculate_rectangle_area(4.0, 4.0) == 16.0

    def test_decimal_values(self) -> None:
        """Test with decimal values."""
        assert calculate_rectangle_area(2.5, 4.0) == 10.0

    def test_small_values(self) -> None:
        """Test with small values."""
        result = calculate_rectangle_area(0.5, 0.5)
        assert abs(result - 0.25) < 1e-9

    def test_large_values(self) -> None:
        """Test with large values."""
        assert calculate_rectangle_area(1000.0, 500.0) == 500000.0


class TestCalculateStatistics:
    """Tests for calculate_statistics function."""

    def test_basic_statistics(self) -> None:
        """Test basic statistics calculation."""
        stats = calculate_statistics([1.0, 2.0, 3.0, 4.0, 5.0])
        assert stats["sum"] == 15.0
        assert stats["average"] == 3.0
        assert stats["min"] == 1.0
        assert stats["max"] == 5.0

    def test_single_value(self) -> None:
        """Test with single value."""
        stats = calculate_statistics([42.0])
        assert stats["sum"] == 42.0
        assert stats["average"] == 42.0
        assert stats["min"] == 42.0
        assert stats["max"] == 42.0

    def test_negative_values(self) -> None:
        """Test with negative values."""
        stats = calculate_statistics([-5.0, -2.0, 0.0, 2.0, 5.0])
        assert stats["sum"] == 0.0
        assert stats["average"] == 0.0
        assert stats["min"] == -5.0
        assert stats["max"] == 5.0

    def test_empty_list_raises_error(self) -> None:
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError):
            calculate_statistics([])

    def test_all_same_values(self) -> None:
        """Test with all same values."""
        stats = calculate_statistics([7.0, 7.0, 7.0])
        assert stats["sum"] == 21.0
        assert stats["average"] == 7.0
        assert stats["min"] == 7.0
        assert stats["max"] == 7.0

    def test_decimal_average(self) -> None:
        """Test with decimal average."""
        stats = calculate_statistics([1.0, 2.0, 3.0])
        assert abs(stats["average"] - 2.0) < 1e-9


class TestProcessValue:
    """Tests for process_value function."""

    def test_process_integer(self) -> None:
        """Test processing integer value."""
        assert process_value(42) == "Processed: 42"

    def test_process_string(self) -> None:
        """Test processing string value."""
        assert process_value("hello") == "Processed: hello"

    def test_process_zero(self) -> None:
        """Test processing zero."""
        assert process_value(0) == "Processed: 0"

    def test_process_negative_integer(self) -> None:
        """Test processing negative integer."""
        assert process_value(-10) == "Processed: -10"

    def test_process_empty_string(self) -> None:
        """Test processing empty string."""
        assert process_value("") == "Processed: "

    def test_process_special_characters(self) -> None:
        """Test processing string with special characters."""
        assert process_value("@#$%") == "Processed: @#$%"


class TestFindUser:
    """Tests for find_user function."""

    def test_find_existing_user(self) -> None:
        """Test finding an existing user."""
        user = find_user(1)
        assert user is not None
        assert user["id"] == "1"
        assert user["name"] == "Alice"

    def test_find_nonexistent_user(self) -> None:
        """Test finding a non-existent user."""
        assert find_user(999) is None

    def test_find_user_returns_dict(self) -> None:
        """Test that find_user returns a dictionary."""
        user = find_user(1)
        assert isinstance(user, dict)

    def test_find_user_dict_keys(self) -> None:
        """Test that returned dictionary has correct keys."""
        user = find_user(1)
        assert user is not None
        assert "id" in user
        assert "name" in user

    def test_find_user_zero_id(self) -> None:
        """Test finding user with ID 0."""
        assert find_user(0) is None

    def test_find_user_negative_id(self) -> None:
        """Test finding user with negative ID."""
        assert find_user(-1) is None


class TestDataProcessor:
    """Tests for DataProcessor class."""

    def test_initialization(self) -> None:
        """Test DataProcessor initialization."""
        processor = DataProcessor("Temperature Sensor")
        assert processor.name == "Temperature Sensor"
        assert processor.get_data() == []

    def test_add_single_data_point(self) -> None:
        """Test adding a single data point."""
        processor = DataProcessor("Sensor")
        processor.add_data([20.5])
        assert processor.get_data() == [20.5]

    def test_add_multiple_data_points(self) -> None:
        """Test adding multiple data points."""
        processor = DataProcessor("Sensor")
        processor.add_data([20.5, 21.0, 19.8])
        assert processor.get_data() == [20.5, 21.0, 19.8]

    def test_add_data_multiple_times(self) -> None:
        """Test adding data multiple times."""
        processor = DataProcessor("Sensor")
        processor.add_data([20.5, 21.0])
        processor.add_data([19.8, 22.1])
        assert processor.get_data() == [20.5, 21.0, 19.8, 22.1]

    def test_get_average_with_data(self) -> None:
        """Test getting average with data."""
        processor = DataProcessor("Sensor")
        processor.add_data([20.0, 22.0, 24.0])
        assert processor.get_average() == 22.0

    def test_get_average_empty(self) -> None:
        """Test getting average with no data."""
        processor = DataProcessor("Sensor")
        assert processor.get_average() is None

    def test_get_average_single_value(self) -> None:
        """Test getting average with single value."""
        processor = DataProcessor("Sensor")
        processor.add_data([42.0])
        assert processor.get_average() == 42.0

    def test_get_data_returns_copy(self) -> None:
        """Test that get_data returns a copy, not reference."""
        processor = DataProcessor("Sensor")
        processor.add_data([1.0, 2.0, 3.0])
        data = processor.get_data()
        data.append(4.0)
        # Original data should not be modified
        assert processor.get_data() == [1.0, 2.0, 3.0]

    def test_processor_with_negative_values(self) -> None:
        """Test processor with negative values."""
        processor = DataProcessor("Sensor")
        processor.add_data([-5.0, 0.0, 5.0])
        assert processor.get_average() == 0.0


class TestValidateAndProcess:
    """Tests for validate_and_process function."""

    def test_process_integer(self) -> None:
        """Test processing integer."""
        is_valid, result = validate_and_process(42)
        assert is_valid is True
        assert result == 42.0
        assert isinstance(result, float)

    def test_process_string(self) -> None:
        """Test processing string."""
        is_valid, result = validate_and_process("hello")
        assert is_valid is True
        assert result == "hello"

    def test_process_float(self) -> None:
        """Test processing float."""
        is_valid, result = validate_and_process(3.14)
        assert is_valid is True
        assert result == 3.14

    def test_process_zero(self) -> None:
        """Test processing zero."""
        is_valid, result = validate_and_process(0)
        assert is_valid is True
        assert result == 0.0

    def test_process_negative_integer(self) -> None:
        """Test processing negative integer."""
        is_valid, result = validate_and_process(-10)
        assert is_valid is True
        assert result == -10.0

    def test_process_empty_string(self) -> None:
        """Test processing empty string."""
        is_valid, result = validate_and_process("")
        assert is_valid is True
        assert result == ""

    def test_return_type_is_tuple(self) -> None:
        """Test that return type is a tuple."""
        result = validate_and_process(42)
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_first_element_is_bool(self) -> None:
        """Test that first element is boolean."""
        is_valid, _ = validate_and_process(42)
        assert isinstance(is_valid, bool)
