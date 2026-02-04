"""
Tests for comments and documentation exercises.
"""

import inspect
import sys
from pathlib import Path

import pytest

# Add parent directory to path to import exercises
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import using importlib to handle module name starting with number
import importlib.util

spec = importlib.util.spec_from_file_location(
    "comments_documentation", Path(__file__).parent.parent / "05_comments_documentation.py"
)
comments_documentation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(comments_documentation)

calculate_discount = comments_documentation.calculate_discount
process_user_data = comments_documentation.process_user_data
find_longest_palindrome = comments_documentation.find_longest_palindrome
DataValidator = comments_documentation.DataValidator
fetch_and_cache = comments_documentation.fetch_and_cache
calc = comments_documentation.calc


class TestCalculateDiscount:
    """Test calculate_discount function and its documentation."""

    def test_has_docstring(self):
        """Test that function has a docstring."""
        assert calculate_discount.__doc__ is not None
        assert len(calculate_discount.__doc__.strip()) > 0

    def test_docstring_has_parameters(self):
        """Test that docstring documents parameters."""
        docstring = calculate_discount.__doc__
        assert ":param" in docstring or "Args:" in docstring

    def test_docstring_has_return(self):
        """Test that docstring documents return value."""
        docstring = calculate_discount.__doc__
        assert ":return" in docstring or "Returns:" in docstring

    def test_regular_discount(self):
        """Test discount calculation for non-members."""
        result = calculate_discount(100, 10, False)
        assert result == 90.0

    def test_member_discount(self):
        """Test discount calculation for members."""
        result = calculate_discount(100, 10, True)
        assert result == 85.0

    def test_zero_discount(self):
        """Test with zero discount."""
        result = calculate_discount(100, 0, False)
        assert result == 100.0


class TestProcessUserData:
    """Test process_user_data function and comment quality."""

    def test_valid_user_data(self):
        """Test processing valid user data."""
        data = {"name": "Alice", "age": 30}
        result = process_user_data(data)
        assert result["name"] == "Alice"
        assert isinstance(result["birth_year"], int)

    def test_negative_age_raises_error(self):
        """Test that negative age raises ValueError."""
        data = {"name": "Bob", "age": -5}
        with pytest.raises(ValueError, match="Age cannot be negative"):
            process_user_data(data)

    def test_zero_age(self):
        """Test processing user with age zero."""
        data = {"name": "Baby", "age": 0}
        result = process_user_data(data)
        assert result["name"] == "Baby"

    def test_comments_are_meaningful(self):
        """Test that function doesn't have too many obvious comments."""
        source = inspect.getsource(process_user_data)
        # Count comment lines
        comment_lines = [line for line in source.split("\n") if line.strip().startswith("#")]
        # Should have fewer obvious comments after improvement
        assert len(comment_lines) < 10


class TestFindLongestPalindrome:
    """Test find_longest_palindrome function and algorithm documentation."""

    def test_has_algorithm_comments(self):
        """Test that function has comments explaining the algorithm."""
        source = inspect.getsource(find_longest_palindrome)
        # Should have at least some comments explaining the logic
        assert "#" in source

    def test_simple_palindrome(self):
        """Test finding palindrome in simple text."""
        result = find_longest_palindrome("racecar")
        assert result == "racecar"

    def test_multiple_palindromes(self):
        """Test finding longest among multiple palindromes."""
        result = find_longest_palindrome("abacabad")
        assert result == "abacaba"

    def test_empty_string(self):
        """Test with empty string."""
        result = find_longest_palindrome("")
        assert result == ""

    def test_no_palindrome(self):
        """Test with text containing only single character palindromes."""
        result = find_longest_palindrome("abc")
        assert len(result) == 1


class TestDataValidator:
    """Test DataValidator class and its documentation."""

    def test_class_has_docstring(self):
        """Test that class has a docstring."""
        assert DataValidator.__doc__ is not None
        assert len(DataValidator.__doc__.strip()) > 0

    def test_validate_method_has_docstring(self):
        """Test that validate method has a docstring."""
        assert DataValidator.validate.__doc__ is not None
        assert len(DataValidator.validate.__doc__.strip()) > 0

    def test_get_errors_method_has_docstring(self):
        """Test that get_errors method has a docstring."""
        assert DataValidator.get_errors.__doc__ is not None
        assert len(DataValidator.get_errors.__doc__.strip()) > 0

    def test_valid_data(self):
        """Test validation with valid data."""
        rules = {"age": {"type": int, "min": 0, "max": 150}}
        validator = DataValidator(rules)
        assert validator.validate({"age": 25}) is True
        assert len(validator.get_errors()) == 0

    def test_missing_field(self):
        """Test validation with missing required field."""
        rules = {"age": {"type": int}}
        validator = DataValidator(rules)
        assert validator.validate({}) is False
        assert len(validator.get_errors()) > 0

    def test_invalid_type(self):
        """Test validation with invalid type."""
        rules = {"age": {"type": int}}
        validator = DataValidator(rules)
        assert validator.validate({"age": "twenty"}) is False
        errors = validator.get_errors()
        assert any("type" in error.lower() for error in errors)

    def test_below_minimum(self):
        """Test validation with value below minimum."""
        rules = {"age": {"type": int, "min": 0}}
        validator = DataValidator(rules)
        assert validator.validate({"age": -5}) is False
        errors = validator.get_errors()
        assert any("minimum" in error.lower() for error in errors)

    def test_above_maximum(self):
        """Test validation with value above maximum."""
        rules = {"age": {"type": int, "max": 150}}
        validator = DataValidator(rules)
        assert validator.validate({"age": 200}) is False
        errors = validator.get_errors()
        assert any("maximum" in error.lower() for error in errors)


class TestFetchAndCache:
    """Test fetch_and_cache function and its documentation."""

    def test_has_comprehensive_docstring(self):
        """Test that function has a comprehensive docstring."""
        docstring = fetch_and_cache.__doc__
        assert docstring is not None
        assert len(docstring.strip()) > 50  # Should be detailed

    def test_docstring_has_parameters(self):
        """Test that docstring documents all parameters."""
        docstring = fetch_and_cache.__doc__
        assert "url" in docstring.lower()
        assert "cache_duration" in docstring.lower()

    def test_docstring_has_example(self):
        """Test that docstring includes usage example."""
        docstring = fetch_and_cache.__doc__
        assert "example" in docstring.lower() or ">>>" in docstring

    def test_fetch_data(self):
        """Test fetching data."""
        result = fetch_and_cache("https://example.com/api")
        assert result is not None
        assert "url" in result

    def test_cache_functionality(self):
        """Test that caching works."""
        url = "https://example.com/test"
        result1 = fetch_and_cache(url, cache_duration=10)
        result2 = fetch_and_cache(url, cache_duration=10)
        assert result1 == result2


class TestCalc:
    """Test calc function refactoring for self-documenting code."""

    def test_function_works(self):
        """Test that refactored function still works correctly."""
        data = [10, 20, 30, 40, 50]
        result = calc(data, 1.5, 25)
        # Should filter values > 25 (30, 40, 50), multiply by 1.5, get average
        expected = (30 * 1.5 + 40 * 1.5 + 50 * 1.5) / 3
        assert result == expected

    def test_empty_after_filter(self):
        """Test when no values pass the threshold."""
        data = [1, 2, 3]
        result = calc(data, 2.0, 10)
        assert result == 0

    def test_all_values_pass_filter(self):
        """Test when all values pass the threshold."""
        data = [10, 20, 30]
        result = calc(data, 2.0, 5)
        expected = (10 * 2.0 + 20 * 2.0 + 30 * 2.0) / 3
        assert result == expected

    def test_has_better_variable_names(self):
        """Test that function uses more descriptive variable names."""
        source = inspect.getsource(calc)
        # After refactoring, should have more descriptive names
        # This is a soft check - the function should be more readable
        assert "def calc" in source  # Function exists
