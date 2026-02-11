"""Tests for logging practice exercises."""

import pytest
import logging
from pathlib import Path
from exercises.logging_practice import (
    setup_logging,
    load_dataset,
    validate_dataset,
    preprocess_data,
    safe_operation_with_logging,
    log_function_performance,
)


class TestSetupLogging:
    """Test setup_logging function."""

    def test_configures_logging_level(self, tmp_path):
        """Should configure logging with specified level."""
        log_file = tmp_path / "test.log"
        setup_logging('INFO', str(log_file))
        
        logger = logging.getLogger()
        assert logger.level == logging.INFO

    def test_creates_log_file(self, tmp_path):
        """Should create log file."""
        log_file = tmp_path / "test.log"
        setup_logging('DEBUG', str(log_file))
        
        # Log something to ensure file is created
        logging.info("Test message")
        assert log_file.exists()


class TestLoadDataset:
    """Test load_dataset function."""

    def test_loads_valid_dataset(self, tmp_path, caplog):
        """Should load dataset and log appropriately."""
        csv_file = tmp_path / "data.csv"
        csv_file.write_text("col1,col2\nval1,val2\nval3,val4")
        
        with caplog.at_level(logging.INFO):
            result = load_dataset(str(csv_file))
        
        assert len(result) == 2
        assert "Starting to load dataset" in caplog.text or "load" in caplog.text.lower()
        assert "Successfully loaded" in caplog.text or "success" in caplog.text.lower()

    def test_logs_error_for_missing_file(self, caplog):
        """Should log error when file doesn't exist."""
        with caplog.at_level(logging.ERROR):
            try:
                load_dataset("nonexistent.csv")
            except:
                pass
        
        assert "ERROR" in caplog.text


class TestValidateDataset:
    """Test validate_dataset function."""

    def test_validates_correct_dataset(self, caplog):
        """Should validate dataset with required columns."""
        data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        
        with caplog.at_level(logging.INFO):
            result = validate_dataset(data, ['name', 'age'])
        
        assert result is True
        assert "validation" in caplog.text.lower() or "INFO" in caplog.text

    def test_logs_error_for_missing_columns(self, caplog):
        """Should log error when required columns are missing."""
        data = [{'name': 'Alice'}]
        
        with caplog.at_level(logging.ERROR):
            result = validate_dataset(data, ['name', 'age'])
        
        assert result is False
        assert "ERROR" in caplog.text


class TestPreprocessData:
    """Test preprocess_data function."""

    def test_preprocesses_data_with_logging(self, caplog):
        """Should preprocess data and log steps."""
        data = [
            {'name': 'Alice', 'age': '30'},
            {'name': 'Bob', 'age': None},
            {'name': 'Charlie', 'age': '25'}
        ]
        
        with caplog.at_level(logging.INFO):
            result = preprocess_data(data)
        
        # Should remove row with None
        assert len(result) < len(data)
        # Should log processing steps
        assert "INFO" in caplog.text or "WARNING" in caplog.text

    def test_logs_warning_for_removed_rows(self, caplog):
        """Should log warning for removed rows."""
        data = [{'name': 'Alice', 'age': None}]
        
        with caplog.at_level(logging.WARNING):
            result = preprocess_data(data)
        
        assert "WARNING" in caplog.text or "removed" in caplog.text.lower()


class TestSafeOperationWithLogging:
    """Test safe_operation_with_logging function."""

    def test_logs_successful_operation(self, caplog):
        """Should log operation start and completion."""
        with caplog.at_level(logging.INFO):
            result = safe_operation_with_logging(lambda x: x * 2, 5)
        
        assert result == 10
        assert "INFO" in caplog.text

    def test_logs_error_on_failure(self, caplog):
        """Should log error when operation fails."""
        def failing_op():
            raise ValueError("Test error")
        
        with caplog.at_level(logging.ERROR):
            result = safe_operation_with_logging(failing_op)
        
        assert result is None
        assert "ERROR" in caplog.text


class TestLogFunctionPerformance:
    """Test log_function_performance function."""

    def test_logs_execution_time(self, caplog):
        """Should log function execution time."""
        with caplog.at_level(logging.INFO):
            result = log_function_performance(sum, [1, 2, 3, 4, 5])
        
        assert result == 15
        assert "INFO" in caplog.text or len(caplog.records) > 0

    def test_logs_warning_for_slow_execution(self, caplog):
        """Should log warning if execution is slow."""
        import time
        
        def slow_function():
            time.sleep(1.1)
            return "done"
        
        with caplog.at_level(logging.WARNING):
            result = log_function_performance(slow_function)
        
        assert "WARNING" in caplog.text
