"""Tests for error handling exercises."""

import pytest
import json
from pathlib import Path
from exercises.error_handling import (
    divide_safely,
    parse_config_file,
    fetch_data_from_api,
    process_user_input,
)


class TestDivideSafely:
    """Test divide_safely function."""

    def test_divides_two_numbers(self):
        """Should divide two numbers correctly."""
        assert divide_safely(10, 2) == 5.0

    def test_returns_none_for_zero_division(self):
        """Should return None when dividing by zero."""
        result = divide_safely(10, 0)
        assert result is None

    def test_raises_type_error_for_non_numeric_input(self):
        """Should raise TypeError for non-numeric inputs."""
        with pytest.raises(TypeError):
            divide_safely("10", 2)
        
        with pytest.raises(TypeError):
            divide_safely(10, "2")

    def test_handles_negative_numbers(self):
        """Should handle negative numbers."""
        assert divide_safely(-10, 2) == -5.0
        assert divide_safely(10, -2) == -5.0

    def test_handles_floats(self):
        """Should handle float inputs."""
        assert divide_safely(10.5, 2.0) == 5.25


class TestParseConfigFile:
    """Test parse_config_file function."""

    def test_parses_valid_json_file(self, tmp_path):
        """Should parse valid JSON config file."""
        config_file = tmp_path / "config.json"
        config_file.write_text('{"setting": "value", "number": 42}')
        
        result = parse_config_file(str(config_file))
        assert result == {"setting": "value", "number": 42}

    def test_raises_error_for_nonexistent_file(self):
        """Should raise FileNotFoundError with message."""
        with pytest.raises(FileNotFoundError, match="Config file not found"):
            parse_config_file("nonexistent.json")

    def test_raises_error_for_invalid_json(self, tmp_path):
        """Should raise ValueError for invalid JSON."""
        config_file = tmp_path / "bad.json"
        config_file.write_text("{invalid json}")
        
        with pytest.raises(ValueError, match="Invalid JSON"):
            parse_config_file(str(config_file))


class TestFetchDataFromAPI:
    """Test fetch_data_from_api function."""

    def test_fetches_data_successfully(self):
        """Should return data for valid inputs."""
        result = fetch_data_from_api('https://api.example.com', 5)
        assert isinstance(result, dict)
        assert 'data' in result

    def test_raises_error_for_negative_timeout(self):
        """Should raise ValueError for negative timeout."""
        with pytest.raises(ValueError, match="Timeout must be positive"):
            fetch_data_from_api('https://api.example.com', -1)

    def test_raises_error_for_zero_timeout(self):
        """Should raise ValueError for zero timeout."""
        with pytest.raises(ValueError, match="Timeout must be positive"):
            fetch_data_from_api('https://api.example.com', 0)

    def test_raises_error_for_invalid_url(self):
        """Should raise ValueError for URL not starting with http."""
        with pytest.raises(ValueError, match="Invalid URL"):
            fetch_data_from_api('ftp://example.com', 5)
        
        with pytest.raises(ValueError, match="Invalid URL"):
            fetch_data_from_api('example.com', 5)


class TestProcessUserInput:
    """Test process_user_input function."""

    def test_processes_valid_input(self):
        """Should process valid input correctly."""
        result = process_user_input("  Hello World  ")
        assert result == "hello world"

    def test_raises_type_error_for_non_string(self):
        """Should raise TypeError for non-string input."""
        with pytest.raises(TypeError, match="Input must be a string"):
            process_user_input(123)
        
        with pytest.raises(TypeError, match="Input must be a string"):
            process_user_input(None)

    def test_raises_value_error_for_empty_string(self):
        """Should raise ValueError for empty string."""
        with pytest.raises(ValueError, match="Input cannot be empty"):
            process_user_input("")

    def test_raises_value_error_for_whitespace_only(self):
        """Should raise ValueError for whitespace-only string."""
        with pytest.raises(ValueError, match="Input cannot be empty"):
            process_user_input("   ")
        
        with pytest.raises(ValueError, match="Input cannot be empty"):
            process_user_input("\t\n")

    def test_strips_and_lowercases(self):
        """Should strip whitespace and convert to lowercase."""
        assert process_user_input("HELLO") == "hello"
        assert process_user_input("  MiXeD CaSe  ") == "mixed case"
