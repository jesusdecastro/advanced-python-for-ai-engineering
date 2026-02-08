"""
Tests for code quality tools exercises.
"""

import importlib.util
import sys
import tempfile
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Dynamically import module with numeric prefix
_module_path = Path(__file__).parent.parent / "05_code_quality_tools.py"
_spec = importlib.util.spec_from_file_location("code_quality_tools_exercises", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

calculate_total = _module.calculate_total
process_user_data = _module.process_user_data
analyze_data = _module.analyze_data
get_user_stats = _module.get_user_stats
merge_configs = _module.merge_configs
CodeAnalyzer = _module.CodeAnalyzer


class TestCalculateTotal:
    """Tests for calculate_total function."""

    def test_basic_calculation(self):
        """Test basic total calculation with tax."""
        items = [10.0, 20.0, 30.0]
        result = calculate_total(items)
        expected = 60.0 * 1.1  # 60 + 10% tax
        assert abs(result - expected) < 0.01

    def test_custom_tax_rate(self):
        """Test with custom tax rate."""
        items = [100.0]
        result = calculate_total(items, tax_rate=0.2)
        expected = 120.0  # 100 + 20% tax
        assert abs(result - expected) < 0.01

    def test_empty_list(self):
        """Test with empty list."""
        result = calculate_total([])
        assert result == 0.0

    def test_single_item(self):
        """Test with single item."""
        result = calculate_total([50.0], tax_rate=0.1)
        expected = 55.0
        assert abs(result - expected) < 0.01


class TestProcessUserData:
    """Tests for process_user_data function."""

    def test_basic_user_data(self):
        """Test processing basic user data."""
        result = process_user_data(1, "Alice", "alice@example.com", 30)

        assert result["id"] == 1
        assert result["name"] == "Alice"
        assert result["email"] == "alice@example.com"
        assert result["age"] == 30
        assert result["active"] is True

    def test_inactive_user(self):
        """Test processing inactive user."""
        result = process_user_data(2, "Bob", "bob@example.com", 25, is_active=False)

        assert result["active"] is False

    def test_return_type(self):
        """Test that function returns a dictionary."""
        result = process_user_data(1, "Test", "test@example.com", 20)
        assert isinstance(result, dict)

    def test_all_fields_present(self):
        """Test that all fields are present in result."""
        result = process_user_data(1, "Test", "test@example.com", 20)
        required_fields = ["id", "name", "email", "age", "active"]

        for field in required_fields:
            assert field in result


class TestAnalyzeData:
    """Tests for analyze_data function."""

    def test_filter_above_threshold(self):
        """Test filtering data above threshold."""
        data = [0.3, 0.6, 0.8, 0.4, 0.9]
        result = analyze_data(data, threshold=0.5)

        assert result == [0.6, 0.8, 0.9]

    def test_custom_threshold(self):
        """Test with custom threshold."""
        data = [1, 2, 3, 4, 5]
        result = analyze_data(data, threshold=3)

        assert result == [4, 5]

    def test_empty_data(self):
        """Test with empty data."""
        result = analyze_data([])
        assert result == []

    def test_no_items_above_threshold(self):
        """Test when no items exceed threshold."""
        data = [0.1, 0.2, 0.3]
        result = analyze_data(data, threshold=0.5)

        assert result == []

    def test_verbose_mode(self):
        """Test verbose mode doesn't affect results."""
        data = [0.6, 0.8]
        result = analyze_data(data, threshold=0.5, verbose=True)

        assert result == [0.6, 0.8]


class TestGetUserStats:
    """Tests for get_user_stats function."""

    def test_basic_statistics(self):
        """Test calculating basic user statistics."""
        users = [
            {"id": 1, "name": "Alice", "age": 30, "score": 85},
            {"id": 2, "name": "Bob", "age": 25, "score": 90},
            {"id": 3, "name": "Charlie", "age": 35, "score": 80},
        ]

        result = get_user_stats(users)

        assert result["total_users"] == 3
        assert abs(result["average_age"] - 30.0) < 0.01
        assert abs(result["average_score"] - 85.0) < 0.01

    def test_single_user(self):
        """Test with single user."""
        users = [{"id": 1, "name": "Alice", "age": 30, "score": 85}]

        result = get_user_stats(users)

        assert result["total_users"] == 1
        assert result["average_age"] == 30.0
        assert result["average_score"] == 85.0

    def test_empty_users(self):
        """Test with empty user list."""
        result = get_user_stats([])
        assert result is None

    def test_return_type(self):
        """Test that function returns correct type."""
        users = [{"id": 1, "name": "Alice", "age": 30, "score": 85}]
        result = get_user_stats(users)

        assert isinstance(result, dict)
        assert "total_users" in result
        assert "average_age" in result
        assert "average_score" in result


class TestMergeConfigs:
    """Tests for merge_configs function."""

    def test_merge_basic_configs(self):
        """Test merging basic configurations."""
        default = {"timeout": 30, "retries": 3, "verbose": False}
        user = {"timeout": 60}

        result = merge_configs(default, user)

        assert result["timeout"] == 60
        assert result["retries"] == 3
        assert result["verbose"] is False

    def test_merge_empty_user_config(self):
        """Test merging with empty user config."""
        default = {"timeout": 30, "retries": 3}
        user = {}

        result = merge_configs(default, user)

        assert result == default

    def test_merge_new_keys(self):
        """Test merging with new keys in user config."""
        default = {"timeout": 30}
        user = {"timeout": 60, "max_connections": 10}

        result = merge_configs(default, user)

        assert result["timeout"] == 60
        assert result["max_connections"] == 10

    def test_original_not_modified(self):
        """Test that original configs are not modified."""
        default = {"timeout": 30, "retries": 3}
        user = {"timeout": 60}

        result = merge_configs(default, user)

        # Original should not be modified
        assert default["timeout"] == 30
        assert result["timeout"] == 60


class TestCodeAnalyzer:
    """Tests for CodeAnalyzer class."""

    def test_initialization(self):
        """Test CodeAnalyzer initialization."""
        analyzer = CodeAnalyzer("test.py")

        assert analyzer.filename == "test.py"
        assert analyzer.lines == []
        assert analyzer.errors == []

    def test_load_file(self):
        """Test loading a file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write("line 1\n")
            f.write("line 2\n")
            f.write("line 3\n")
            temp_path = f.name

        try:
            analyzer = CodeAnalyzer(temp_path)
            analyzer.load_file()

            assert len(analyzer.lines) == 3
        finally:
            Path(temp_path).unlink()

    def test_count_lines(self):
        """Test counting lines."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write("line 1\n")
            f.write("line 2\n")
            temp_path = f.name

        try:
            analyzer = CodeAnalyzer(temp_path)
            analyzer.load_file()

            assert analyzer.count_lines() == 2
        finally:
            Path(temp_path).unlink()

    def test_find_long_lines(self):
        """Test finding long lines."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write("short\n")
            f.write("x" * 150 + "\n")  # Long line
            f.write("also short\n")
            temp_path = f.name

        try:
            analyzer = CodeAnalyzer(temp_path)
            analyzer.load_file()
            long_lines = analyzer.find_long_lines(max_length=100)

            assert len(long_lines) == 1
            assert long_lines[0][0] == 2  # Line number
            assert long_lines[0][1] > 100  # Line length
        finally:
            Path(temp_path).unlink()

    def test_get_report(self):
        """Test generating analysis report."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write("line 1\n")
            f.write("x" * 150 + "\n")
            temp_path = f.name

        try:
            analyzer = CodeAnalyzer(temp_path)
            analyzer.load_file()
            report = analyzer.get_report()

            assert "filename" in report
            assert "total_lines" in report
            assert "long_lines" in report
            assert "errors" in report
            assert report["total_lines"] == 2
            assert report["long_lines"] == 1
        finally:
            Path(temp_path).unlink()

    def test_empty_file(self):
        """Test analyzing empty file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            temp_path = f.name

        try:
            analyzer = CodeAnalyzer(temp_path)
            analyzer.load_file()

            assert analyzer.count_lines() == 0
            assert analyzer.find_long_lines() == []
        finally:
            Path(temp_path).unlink()
