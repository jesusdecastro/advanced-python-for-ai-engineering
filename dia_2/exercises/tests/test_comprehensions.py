"""
Unit tests for comprehensions exercises.

These tests validate both functionality and proper use of comprehensions.

Run with: uv run pytest tests/test_comprehensions.py -v
"""

import subprocess
from pathlib import Path

import pytest

# Import from the installed package
from exercises.comprehensions import (
    create_number_to_cube_dict,
    extract_names_from_users,
    filter_dict_by_value,
    filter_even_numbers,
    flatten_matrix,
    get_squares,
    get_unique_characters,
    get_unique_numbers,
    get_word_lengths,
    invert_dictionary,
    uppercase_strings,
    word_frequency,
)


class TestTypeHintsWithPyright:
    """Test that Pyright validates the type hints correctly."""

    def test_pyright_passes(self) -> None:
        """Test that Pyright validation passes for the exercises file."""
        exercises_file = Path(__file__).parent.parent / "src" / "exercises" / "comprehensions.py"

        result = subprocess.run(
            ["pyright", str(exercises_file), "--outputjson"],
            capture_output=True,
            text=True,
        )

        # Pyright returns 0 if no errors
        if result.returncode != 0:
            pytest.fail(f"Pyright found type errors:\n{result.stdout}\n{result.stderr}")


class TestGetSquares:
    """Tests for get_squares function."""

    def test_basic_squares(self) -> None:
        """Test generating squares from 1 to 5."""
        assert get_squares(5) == [1, 4, 9, 16, 25]

    def test_single_square(self) -> None:
        """Test with n=1."""
        assert get_squares(1) == [1]

    def test_ten_squares(self) -> None:
        """Test generating first 10 squares."""
        expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        assert get_squares(10) == expected

    def test_zero_squares(self) -> None:
        """Test with n=0."""
        assert get_squares(0) == []

    def test_large_n(self) -> None:
        """Test with larger n."""
        result = get_squares(20)
        assert len(result) == 20
        assert result[0] == 1
        assert result[-1] == 400


class TestFilterEvenNumbers:
    """Tests for filter_even_numbers function."""

    def test_basic_filtering(self) -> None:
        """Test filtering even numbers."""
        assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_all_even(self) -> None:
        """Test with all even numbers."""
        assert filter_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]

    def test_all_odd(self) -> None:
        """Test with all odd numbers."""
        assert filter_even_numbers([1, 3, 5, 7]) == []

    def test_empty_list(self) -> None:
        """Test with empty list."""
        assert filter_even_numbers([]) == []

    def test_with_zero(self) -> None:
        """Test that zero is included (even)."""
        assert filter_even_numbers([0, 1, 2, 3]) == [0, 2]

    def test_negative_numbers(self) -> None:
        """Test with negative numbers."""
        assert filter_even_numbers([-4, -3, -2, -1, 0, 1, 2]) == [-4, -2, 0, 2]


class TestUppercaseStrings:
    """Tests for uppercase_strings function."""

    def test_basic_uppercase(self) -> None:
        """Test converting strings to uppercase."""
        assert uppercase_strings(["hello", "world"]) == ["HELLO", "WORLD"]

    def test_already_uppercase(self) -> None:
        """Test with already uppercase strings."""
        assert uppercase_strings(["HELLO", "WORLD"]) == ["HELLO", "WORLD"]

    def test_mixed_case(self) -> None:
        """Test with mixed case strings."""
        assert uppercase_strings(["HeLLo", "WoRLd"]) == ["HELLO", "WORLD"]

    def test_empty_list(self) -> None:
        """Test with empty list."""
        assert uppercase_strings([]) == []

    def test_empty_strings(self) -> None:
        """Test with empty strings."""
        assert uppercase_strings(["", ""]) == ["", ""]

    def test_with_numbers(self) -> None:
        """Test with strings containing numbers."""
        assert uppercase_strings(["hello123", "world456"]) == ["HELLO123", "WORLD456"]


class TestCreateNumberToCubeDict:
    """Tests for create_number_to_cube_dict function."""

    def test_basic_cubes(self) -> None:
        """Test creating cube dictionary."""
        assert create_number_to_cube_dict(3) == {1: 1, 2: 8, 3: 27}

    def test_single_number(self) -> None:
        """Test with n=1."""
        assert create_number_to_cube_dict(1) == {1: 1}

    def test_five_numbers(self) -> None:
        """Test with n=5."""
        expected = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        assert create_number_to_cube_dict(5) == expected

    def test_zero(self) -> None:
        """Test with n=0."""
        assert create_number_to_cube_dict(0) == {}

    def test_return_type(self) -> None:
        """Test that return type is dict."""
        result = create_number_to_cube_dict(3)
        assert isinstance(result, dict)


class TestInvertDictionary:
    """Tests for invert_dictionary function."""

    def test_basic_inversion(self) -> None:
        """Test inverting a dictionary."""
        assert invert_dictionary({"a": 1, "b": 2}) == {1: "a", 2: "b"}

    def test_single_item(self) -> None:
        """Test with single item."""
        assert invert_dictionary({"x": 10}) == {10: "x"}

    def test_empty_dict(self) -> None:
        """Test with empty dictionary."""
        assert invert_dictionary({}) == {}

    def test_string_values(self) -> None:
        """Test with string values."""
        assert invert_dictionary({"name": "Alice", "city": "NYC"}) == {
            "Alice": "name",
            "NYC": "city",
        }

    def test_numeric_keys(self) -> None:
        """Test with numeric keys."""
        assert invert_dictionary({1: "one", 2: "two"}) == {"one": 1, "two": 2}


class TestFilterDictByValue:
    """Tests for filter_dict_by_value function."""

    def test_basic_filtering(self) -> None:
        """Test filtering dictionary by value."""
        assert filter_dict_by_value({"a": 10, "b": 5, "c": 15}, 7) == {"a": 10, "c": 15}

    def test_no_items_pass(self) -> None:
        """Test when no items pass threshold."""
        assert filter_dict_by_value({"a": 1, "b": 2, "c": 3}, 10) == {}

    def test_all_items_pass(self) -> None:
        """Test when all items pass threshold."""
        result = filter_dict_by_value({"a": 10, "b": 20, "c": 30}, 5)
        assert result == {"a": 10, "b": 20, "c": 30}

    def test_empty_dict(self) -> None:
        """Test with empty dictionary."""
        assert filter_dict_by_value({}, 5) == {}

    def test_threshold_zero(self) -> None:
        """Test with threshold of zero."""
        result = filter_dict_by_value({"a": -5, "b": 0, "c": 5}, 0)
        assert result == {"c": 5}

    def test_equal_to_threshold(self) -> None:
        """Test that equal values are excluded."""
        result = filter_dict_by_value({"a": 10, "b": 5, "c": 5}, 5)
        assert result == {"a": 10}


class TestGetUniqueCharacters:
    """Tests for get_unique_characters function."""

    def test_basic_unique_chars(self) -> None:
        """Test extracting unique characters."""
        result = get_unique_characters("hello world")
        expected = {"h", "e", "l", "o", "w", "r", "d"}
        assert result == expected

    def test_no_duplicates(self) -> None:
        """Test with no duplicate characters."""
        result = get_unique_characters("abcd")
        assert result == {"a", "b", "c", "d"}

    def test_all_duplicates(self) -> None:
        """Test with all same character."""
        result = get_unique_characters("aaaa")
        assert result == {"a"}

    def test_empty_string(self) -> None:
        """Test with empty string."""
        assert get_unique_characters("") == set()

    def test_spaces_excluded(self) -> None:
        """Test that spaces are excluded."""
        result = get_unique_characters("a b c")
        assert result == {"a", "b", "c"}
        assert " " not in result

    def test_return_type(self) -> None:
        """Test that return type is set."""
        result = get_unique_characters("hello")
        assert isinstance(result, set)


class TestGetUniqueNumbers:
    """Tests for get_unique_numbers function."""

    def test_basic_unique_numbers(self) -> None:
        """Test getting unique numbers."""
        assert get_unique_numbers([1, 2, 2, 3, 3, 3, 4]) == {1, 2, 3, 4}

    def test_no_duplicates(self) -> None:
        """Test with no duplicates."""
        assert get_unique_numbers([1, 2, 3, 4]) == {1, 2, 3, 4}

    def test_all_same(self) -> None:
        """Test with all same number."""
        assert get_unique_numbers([5, 5, 5, 5]) == {5}

    def test_empty_list(self) -> None:
        """Test with empty list."""
        assert get_unique_numbers([]) == set()

    def test_negative_numbers(self) -> None:
        """Test with negative numbers."""
        assert get_unique_numbers([-1, -1, 0, 0, 1, 1]) == {-1, 0, 1}

    def test_return_type(self) -> None:
        """Test that return type is set."""
        result = get_unique_numbers([1, 2, 3])
        assert isinstance(result, set)


class TestGetWordLengths:
    """Tests for get_word_lengths function."""

    def test_basic_word_lengths(self) -> None:
        """Test getting unique word lengths."""
        assert get_word_lengths(["cat", "dog", "bird", "fish"]) == {3, 4}

    def test_all_same_length(self) -> None:
        """Test with all same length words."""
        assert get_word_lengths(["cat", "dog", "bat"]) == {3}

    def test_different_lengths(self) -> None:
        """Test with various lengths."""
        result = get_word_lengths(["a", "ab", "abc", "abcd"])
        assert result == {1, 2, 3, 4}

    def test_empty_list(self) -> None:
        """Test with empty list."""
        assert get_word_lengths([]) == set()

    def test_empty_strings(self) -> None:
        """Test with empty strings."""
        assert get_word_lengths(["", "", ""]) == {0}

    def test_return_type(self) -> None:
        """Test that return type is set."""
        result = get_word_lengths(["hello", "world"])
        assert isinstance(result, set)


class TestFlattenMatrix:
    """Tests for flatten_matrix function."""

    def test_basic_flatten(self) -> None:
        """Test flattening a 2D matrix."""
        assert flatten_matrix([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]

    def test_single_row(self) -> None:
        """Test with single row."""
        assert flatten_matrix([[1, 2, 3]]) == [1, 2, 3]

    def test_single_column(self) -> None:
        """Test with single column."""
        assert flatten_matrix([[1], [2], [3]]) == [1, 2, 3]

    def test_empty_matrix(self) -> None:
        """Test with empty matrix."""
        assert flatten_matrix([]) == []

    def test_empty_rows(self) -> None:
        """Test with empty rows."""
        assert flatten_matrix([[], [], []]) == []

    def test_mixed_row_lengths(self) -> None:
        """Test with different row lengths."""
        assert flatten_matrix([[1, 2], [3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]


class TestWordFrequency:
    """Tests for word_frequency function."""

    def test_basic_frequency(self) -> None:
        """Test word frequency counting."""
        words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
        expected = {"apple": 3, "banana": 2, "cherry": 1}
        assert word_frequency(words) == expected

    def test_all_unique(self) -> None:
        """Test with all unique words."""
        words = ["apple", "banana", "cherry"]
        expected = {"apple": 1, "banana": 1, "cherry": 1}
        assert word_frequency(words) == expected

    def test_all_same(self) -> None:
        """Test with all same word."""
        words = ["apple", "apple", "apple"]
        assert word_frequency(words) == {"apple": 3}

    def test_empty_list(self) -> None:
        """Test with empty list."""
        assert word_frequency([]) == {}

    def test_single_word(self) -> None:
        """Test with single word."""
        assert word_frequency(["apple"]) == {"apple": 1}

    def test_case_sensitive(self) -> None:
        """Test that counting is case-sensitive."""
        words = ["Apple", "apple", "APPLE"]
        result = word_frequency(words)
        assert result == {"Apple": 1, "apple": 1, "APPLE": 1}


class TestExtractNamesFromUsers:
    """Tests for extract_names_from_users function."""

    def test_basic_extraction(self) -> None:
        """Test extracting names from active users."""
        users = [
            {"name": "Alice", "active": True},
            {"name": "Bob", "active": False},
            {"name": "Charlie", "active": True},
        ]
        assert extract_names_from_users(users) == ["Alice", "Charlie"]

    def test_all_active(self) -> None:
        """Test with all active users."""
        users = [
            {"name": "Alice", "active": True},
            {"name": "Bob", "active": True},
        ]
        assert extract_names_from_users(users) == ["Alice", "Bob"]

    def test_none_active(self) -> None:
        """Test with no active users."""
        users = [
            {"name": "Alice", "active": False},
            {"name": "Bob", "active": False},
        ]
        assert extract_names_from_users(users) == []

    def test_empty_list(self) -> None:
        """Test with empty list."""
        assert extract_names_from_users([]) == []

    def test_single_active_user(self) -> None:
        """Test with single active user."""
        users = [{"name": "Alice", "active": True}]
        assert extract_names_from_users(users) == ["Alice"]

    def test_single_inactive_user(self) -> None:
        """Test with single inactive user."""
        users = [{"name": "Bob", "active": False}]
        assert extract_names_from_users(users) == []
