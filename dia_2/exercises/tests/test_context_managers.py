"""Tests for context managers exercises."""

import time
from pathlib import Path

import pytest

# Import from the installed package
from dia2_exercises.context_managers import (
    ExecutionTimer,
    LoggingContext,
    SuppressException,
    temporary_file_writer,
)


class TestLoggingContext:
    """Tests for LoggingContext class."""

    def test_logging_context_enters_and_exits(self, capsys):
        """Test that context manager logs entry and exit."""
        with LoggingContext("test"):
            pass

        captured = capsys.readouterr()
        assert "Entering: test" in captured.out
        assert "Exiting: test" in captured.out

    def test_logging_context_with_code_execution(self, capsys):
        """Test context manager with code inside block."""
        with LoggingContext("operation"):
            print("Inside context")

        captured = capsys.readouterr()
        assert "Entering: operation" in captured.out
        assert "Inside context" in captured.out
        assert "Exiting: operation" in captured.out

    def test_logging_context_order(self, capsys):
        """Test that entry happens before exit."""
        with LoggingContext("order_test"):
            pass

        captured = capsys.readouterr()
        output = captured.out
        enter_pos = output.find("Entering")
        exit_pos = output.find("Exiting")
        assert enter_pos < exit_pos

    def test_logging_context_with_exception(self, capsys):
        """Test that exit is called even with exception."""
        with pytest.raises(ValueError):
            with LoggingContext("error_test"):
                raise ValueError("Test error")

        captured = capsys.readouterr()
        assert "Entering: error_test" in captured.out
        assert "Exiting: error_test" in captured.out

    def test_logging_context_returns_self(self):
        """Test that __enter__ returns self."""
        ctx = LoggingContext("test")
        with ctx as result:
            assert result is ctx


class TestExecutionTimer:
    """Tests for ExecutionTimer class."""

    def test_timer_measures_time(self):
        """Test that timer measures elapsed time."""
        with ExecutionTimer("test") as timer:
            time.sleep(0.1)

        assert timer.elapsed >= 0.1
        assert timer.elapsed < 0.2

    def test_timer_starts_at_zero(self):
        """Test that elapsed starts at zero."""
        timer = ExecutionTimer("test")
        assert timer.elapsed == 0.0

    def test_timer_with_no_delay(self):
        """Test timer with minimal execution time."""
        with ExecutionTimer("fast") as timer:
            pass

        assert timer.elapsed >= 0.0
        assert timer.elapsed < 0.01

    def test_timer_with_longer_delay(self):
        """Test timer with longer execution time."""
        with ExecutionTimer("slow") as timer:
            time.sleep(0.2)

        assert timer.elapsed >= 0.2
        assert timer.elapsed < 0.3

    def test_timer_name_stored(self):
        """Test that timer stores the operation name."""
        timer = ExecutionTimer("my_operation")
        assert timer.name == "my_operation"

    def test_timer_default_name(self):
        """Test timer with default name."""
        timer = ExecutionTimer()
        assert timer.name == "Operation"

    def test_timer_with_exception(self):
        """Test that timer records time even with exception."""
        with pytest.raises(ValueError):
            with ExecutionTimer("error_test") as timer:
                time.sleep(0.1)
                raise ValueError("Test error")

        assert timer.elapsed >= 0.1


class TestTemporaryFileWriter:
    """Tests for temporary_file_writer context manager."""

    def test_file_writer_creates_file(self, tmp_path):
        """Test that context manager creates and writes to file."""
        test_file = tmp_path / "test.txt"

        with temporary_file_writer(str(test_file)) as f:
            f.write("Hello, World!")

        assert test_file.exists()
        assert test_file.read_text() == "Hello, World!"

    def test_file_writer_closes_file(self, tmp_path):
        """Test that file is closed after context."""
        test_file = tmp_path / "test.txt"

        with temporary_file_writer(str(test_file)) as f:
            f.write("Test content")
            file_obj = f

        assert file_obj.closed

    def test_file_writer_multiple_writes(self, tmp_path):
        """Test writing multiple lines."""
        test_file = tmp_path / "test.txt"

        with temporary_file_writer(str(test_file)) as f:
            f.write("Line 1\n")
            f.write("Line 2\n")
            f.write("Line 3\n")

        content = test_file.read_text()
        assert "Line 1" in content
        assert "Line 2" in content
        assert "Line 3" in content

    def test_file_writer_closes_on_exception(self, tmp_path):
        """Test that file is closed even with exception."""
        test_file = tmp_path / "test.txt"

        with pytest.raises(ValueError):
            with temporary_file_writer(str(test_file)) as f:
                f.write("Before error")
                file_obj = f
                raise ValueError("Test error")

        assert file_obj.closed


class TestSuppressException:
    """Tests for SuppressException context manager."""

    def test_suppress_single_exception(self):
        """Test suppressing a single exception type."""
        with SuppressException(ValueError):
            raise ValueError("This should be suppressed")

        # If we reach here, exception was suppressed

    def test_suppress_does_not_affect_other_exceptions(self):
        """Test that other exceptions are not suppressed."""
        with pytest.raises(TypeError):
            with SuppressException(ValueError):
                raise TypeError("This should not be suppressed")

    def test_suppress_multiple_exception_types(self):
        """Test suppressing multiple exception types."""
        with SuppressException(ValueError, TypeError):
            raise ValueError("Suppressed")

        with SuppressException(ValueError, TypeError):
            raise TypeError("Also suppressed")

    def test_suppress_with_no_exception(self):
        """Test context manager when no exception occurs."""
        with SuppressException(ValueError):
            x = 1 + 1

        assert x == 2

    def test_suppress_subclass_exceptions(self):
        """Test that subclass exceptions are also suppressed."""

        class CustomError(ValueError):
            pass

        with SuppressException(ValueError):
            raise CustomError("Subclass should be suppressed")

    def test_suppress_does_not_suppress_unrelated(self):
        """Test that unrelated exceptions propagate."""
        with pytest.raises(RuntimeError):
            with SuppressException(ValueError, TypeError):
                raise RuntimeError("Not suppressed")


class TestContextManagerIntegration:
    """Integration tests combining multiple context manager concepts."""

    def test_nested_context_managers(self, capsys):
        """Test nesting multiple context managers."""
        with LoggingContext("outer"):
            with LoggingContext("inner"):
                print("Nested code")

        captured = capsys.readouterr()
        assert "Entering: outer" in captured.out
        assert "Entering: inner" in captured.out
        assert "Exiting: inner" in captured.out
        assert "Exiting: outer" in captured.out

    def test_timer_with_logging(self, capsys):
        """Test combining timer and logging."""
        with LoggingContext("timed_operation"):
            with ExecutionTimer("inner_timer") as timer:
                time.sleep(0.1)

        captured = capsys.readouterr()
        assert "Entering: timed_operation" in captured.out
        assert "Exiting: timed_operation" in captured.out
        assert timer.elapsed >= 0.1

    def test_suppress_with_timer(self):
        """Test suppressing exceptions while timing."""
        with SuppressException(ValueError):
            with ExecutionTimer("error_operation") as timer:
                time.sleep(0.05)
                raise ValueError("Suppressed error")

        # Timer should still have recorded time
        assert timer.elapsed >= 0.05

    def test_multiple_timers_sequential(self):
        """Test using multiple timers sequentially."""
        with ExecutionTimer("first") as timer1:
            time.sleep(0.05)

        with ExecutionTimer("second") as timer2:
            time.sleep(0.1)

        assert timer1.elapsed >= 0.05
        assert timer1.elapsed < 0.1
        assert timer2.elapsed >= 0.1

    def test_file_writer_with_exception_suppression(self, tmp_path):
        """Test file writing with exception suppression."""
        test_file = tmp_path / "test.txt"

        with SuppressException(ValueError):
            with temporary_file_writer(str(test_file)) as f:
                f.write("Content before error\n")
                raise ValueError("Suppressed")

        # File should exist and contain content
        assert test_file.exists()
        assert "Content before error" in test_file.read_text()
