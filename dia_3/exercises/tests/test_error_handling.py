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



class TestCustomExceptions:
    """Test custom exception classes."""

    def test_data_validation_error_basic(self):
        """Should create DataValidationError with message."""
        from exercises.error_handling import DataValidationError
        
        with pytest.raises(DataValidationError, match="Invalid data"):
            raise DataValidationError("Invalid data")

    def test_data_validation_error_with_info(self):
        """Should create DataValidationError with data info."""
        from exercises.error_handling import DataValidationError
        
        try:
            raise DataValidationError("Invalid data", {"row": 5, "column": "age"})
        except DataValidationError as e:
            assert "Invalid data" in str(e)

    def test_model_training_error(self):
        """Should create ModelTrainingError."""
        from exercises.error_handling import ModelTrainingError
        
        with pytest.raises(ModelTrainingError, match="Training failed"):
            raise ModelTrainingError("Training failed", "RandomForest")


class TestValidateTrainingData:
    """Test validate_training_data function."""

    def test_validates_correct_data(self):
        """Should validate correct data."""
        from exercises.error_handling import validate_training_data
        
        data = [{'age': 30, 'income': 50000}, {'age': 25, 'income': 45000}]
        result = validate_training_data(data, ['age', 'income'])
        assert result is True

    def test_raises_for_non_list(self):
        """Should raise DataValidationError for non-list."""
        from exercises.error_handling import validate_training_data, DataValidationError
        
        with pytest.raises(DataValidationError):
            validate_training_data("not a list", ['age'])

    def test_raises_for_empty_data(self):
        """Should raise DataValidationError for empty data."""
        from exercises.error_handling import validate_training_data, DataValidationError
        
        with pytest.raises(DataValidationError):
            validate_training_data([], ['age'])

    def test_raises_for_missing_column(self):
        """Should raise DataValidationError for missing column."""
        from exercises.error_handling import validate_training_data, DataValidationError
        
        data = [{'age': 30}]
        with pytest.raises(DataValidationError, match="income"):
            validate_training_data(data, ['age', 'income'])


class TestSafeFileOperation:
    """Test safe_file_operation function."""

    def test_reads_file_successfully(self, tmp_path):
        """Should read file successfully."""
        from exercises.error_handling import safe_file_operation
        
        test_file = tmp_path / "test.txt"
        test_file.write_text("First line\nSecond line")
        
        def read_first(f):
            return f.readline().strip()
        
        result = safe_file_operation(str(test_file), read_first)
        assert result == "First line"

    def test_raises_for_nonexistent_file(self):
        """Should raise FileNotFoundError with message."""
        from exercises.error_handling import safe_file_operation
        
        def read_first(f):
            return f.readline()
        
        with pytest.raises(FileNotFoundError, match="File not found"):
            safe_file_operation("nonexistent.txt", read_first)


class TestLoadAndProcessConfig:
    """Test load_and_process_config function."""

    def test_loads_valid_config(self, tmp_path):
        """Should load and process valid config."""
        from exercises.error_handling import load_and_process_config
        
        config_file = tmp_path / "config.json"
        config_file.write_text('{"model": "rf", "params": {"n_estimators": 100}}')
        
        result = load_and_process_config(str(config_file))
        assert result['model'] == 'rf'
        assert 'params' in result

    def test_chains_exception_for_missing_file(self):
        """Should chain exception for missing file."""
        from exercises.error_handling import load_and_process_config
        
        with pytest.raises(ValueError, match="Config not found") as exc_info:
            load_and_process_config("nonexistent.json")
        
        # Check exception chaining
        assert exc_info.value.__cause__ is not None

    def test_chains_exception_for_invalid_json(self, tmp_path):
        """Should chain exception for invalid JSON."""
        from exercises.error_handling import load_and_process_config
        
        config_file = tmp_path / "bad.json"
        config_file.write_text("{invalid json}")
        
        with pytest.raises(ValueError, match="Invalid config format") as exc_info:
            load_and_process_config(str(config_file))
        
        assert exc_info.value.__cause__ is not None


class TestProcessDataWithCleanup:
    """Test process_data_with_cleanup function."""

    def test_processes_and_cleans_up(self, tmp_path):
        """Should process data and clean up temp file."""
        from exercises.error_handling import process_data_with_cleanup
        
        temp_file = tmp_path / "temp.txt"
        data = [1, 2, 3, 4, 5]
        
        result = process_data_with_cleanup(data, str(temp_file))
        
        assert result == [2, 4, 6, 8, 10]
        assert not temp_file.exists()  # File should be deleted

    def test_cleans_up_even_on_error(self, tmp_path):
        """Should clean up temp file even if processing fails."""
        from exercises.error_handling import process_data_with_cleanup
        
        temp_file = tmp_path / "temp.txt"
        
        # This should fail but still clean up
        try:
            process_data_with_cleanup(None, str(temp_file))
        except:
            pass
        
        # File should still be deleted
        assert not temp_file.exists()


class TestRobustDataLoader:
    """Test robust_data_loader function."""

    def test_loads_csv_data(self, tmp_path):
        """Should load CSV data."""
        from exercises.error_handling import robust_data_loader
        
        csv_file = tmp_path / "data.csv"
        csv_file.write_text("col1,col2\nval1,val2\nval3,val4")
        
        result = robust_data_loader(str(csv_file), 'csv')
        assert isinstance(result, list)
        assert len(result) > 0

    def test_returns_empty_for_missing_file(self):
        """Should return empty list for missing file."""
        from exercises.error_handling import robust_data_loader
        
        result = robust_data_loader("nonexistent.csv", 'csv')
        assert result == []

    def test_raises_for_unsupported_format(self, tmp_path):
        """Should raise ValueError for unsupported format."""
        from exercises.error_handling import robust_data_loader
        
        file = tmp_path / "data.xml"
        file.write_text("<data></data>")
        
        with pytest.raises(ValueError, match="Unsupported format"):
            robust_data_loader(str(file), 'xml')


class TestCalculateModelScore:
    """Test calculate_model_score function."""

    def test_calculates_perfect_score(self):
        """Should calculate perfect score."""
        from exercises.error_handling import calculate_model_score
        
        predictions = [1, 0, 1, 0]
        labels = [1, 0, 1, 0]
        score = calculate_model_score(predictions, labels, 'classification')
        
        assert score == 1.0

    def test_calculates_partial_score(self):
        """Should calculate partial score."""
        from exercises.error_handling import calculate_model_score
        
        predictions = [1, 0, 1, 0]
        labels = [1, 1, 1, 0]
        score = calculate_model_score(predictions, labels, 'classification')
        
        assert score == 0.75

    def test_raises_for_non_list(self):
        """Should raise exception for non-list inputs."""
        from exercises.error_handling import calculate_model_score
        
        with pytest.raises((TypeError, ValueError)):
            calculate_model_score("not a list", [1, 0], 'classification')

    def test_raises_for_length_mismatch(self):
        """Should raise exception for length mismatch."""
        from exercises.error_handling import calculate_model_score
        
        with pytest.raises(ValueError):
            calculate_model_score([1, 0], [1, 0, 1], 'classification')

    def test_raises_for_invalid_model_type(self):
        """Should raise exception for invalid model type."""
        from exercises.error_handling import calculate_model_score
        
        with pytest.raises(ValueError):
            calculate_model_score([1, 0], [1, 0], 'invalid_type')
